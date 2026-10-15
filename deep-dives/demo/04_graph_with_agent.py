"""BLOCK 4 (part 2): Put the ReAct agent INSIDE a LangGraph graph.

The agent stays flexible (it picks tools), but the graph keeps control:
  read_request -> (no budget? ask) -> agent -> verify_recommendation -> answer

verify_recommendation is ordinary code. It checks every dish the agent recommends
against the REAL menu and the budget the student actually confirmed. A tool call can
be perfectly valid and still use the wrong budget, so we check, we don't assume.

Run:
  .venv\\Scripts\\python 04_graph_with_agent.py --offline
  .venv\\Scripts\\python 04_graph_with_agent.py --offline --inject-mistake fake_dish
  .venv\\Scripts\\python 04_graph_with_agent.py --offline --inject-mistake non_veg
  (drop --offline to use Gemini)

--inject-mistake simulates a model error FOR TEACHING. Say so on stage.
"""

from __future__ import annotations

import argparse
import json
import operator
from typing import Annotated, TypedDict

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langgraph.graph import END, START, StateGraph
from langgraph.errors import GraphRecursionError
from langchain_core.messages import ToolMessage
from pydantic import BaseModel, Field

from canteen import answers, console, data, lc_tools, models, rules

QUESTION = "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."

SYSTEM_PROMPT = """You are the Campus Canteen Assistant.
Use the tools for dishes, prices, stock and hours; never guess them.
Only recommend dishes that find_food returned, using their exact names.
If nothing matches or a tool fails, say so honestly. Keep the message short."""


class CanteenAnswer(BaseModel):
    """The agent's final answer, in a shape our code can check."""

    recommended_dishes: list[str] = Field(description="Exact dish names from find_food results. Empty if none.")
    message: str = Field(description="Short, friendly reply to the student.")


class State(TypedDict, total=False):
    question: str
    constraints: dict
    agent_answer: dict
    searched_budgets: list[int]
    menu: dict | None
    menu_query: dict | None
    menu_error: str | None
    hours: dict | None
    safe_menu: dict
    agent_error: str | None
    lookup_covers_request: bool
    problems: list[str]
    answer: str
    path: Annotated[list[str], operator.add]


def build_graph(offline: bool, inject_mistake: str | None = None):
    agent = create_agent(
        model=models.get_model(offline),
        tools=lc_tools.MENU_TOOLS,
        system_prompt=SYSTEM_PROMPT,
        response_format=ToolStrategy(CanteenAnswer),
    )

    def read_request(state: State) -> dict:
        return {"constraints": rules.extract_constraints(state["question"]), "path": ["read_request"]}

    def ask_for_budget(state: State) -> dict:
        return {"answer": rules.budget_question(), "path": ["ask_for_budget"]}

    def run_agent(state: State) -> dict:
        try:
            result = agent.invoke({"messages": [{"role": "user", "content": state["question"]}]}, config={"recursion_limit": 10})
        except GraphRecursionError:
            return {"agent_answer": {"recommended_dishes": [], "message": ""},
                    "searched_budgets": [], "menu": None, "menu_query": None, "menu_error": "agent step limit reached",
                    "hours": None, "agent_error": "The agent reached its step limit; I can't confirm a recommendation.",
                    "path": ["agent (step limit)"]}
        reply = result["structured_response"].model_dump()
        if inject_mistake == "fake_dish":  # simulated model error, for teaching only
            reply["recommended_dishes"].append("Paneer Tikka Wrap")
        if inject_mistake == "non_veg":
            reply["recommended_dishes"].append("Chicken roll")
        if inject_mistake == "free_text":
            reply["message"] = "Try the Paneer Tikka Wrap for Rs 60. Open until 22:00."
        # Capture the actual tool responses, not facts asserted by the model.
        # The latest lookup replaces older evidence, including when it fails.
        calls, budgets = {}, []
        menu, menu_query, hours = None, None, None
        menu_error = "no successful menu lookup"
        for msg in result["messages"]:
            for call in getattr(msg, "tool_calls", []):
                calls[call["id"]] = {"name": call["name"], "checked_args": None}
                if call["name"] == "find_food":
                    # Use the same schema as the tool: e.g. "80" becomes 80.
                    # Valid shape still does not prove the student's intent.
                    try:
                        checked = lc_tools.find_food.args_schema.model_validate(call["args"]).model_dump()
                    except (ValueError, TypeError):
                        continue
                    calls[call["id"]]["checked_args"] = checked
                    budgets.append(checked["max_price"])
            if not isinstance(msg, ToolMessage):
                continue
            call = calls.get(msg.tool_call_id, {})
            name = call.get("name")
            if name not in ("find_food", "get_canteen_hours"):
                continue
            try:
                record = json.loads(msg.content)
            except (ValueError, TypeError):
                record = {"status": "error", "error": "unreadable tool response"}
            if not isinstance(record, dict):
                record = {"status": "error", "error": "invalid tool response"}
            if name == "find_food":
                menu, menu_query = None, None
                if record.get("status") == "ok" and isinstance(record.get("matches"), list):
                    try:
                        # Successful tool filters describe what was actually
                        # searched. Keep them with the result, even when empty.
                        filters = record.get("filters", call.get("checked_args"))
                        menu_query = lc_tools.find_food.args_schema.model_validate(filters).model_dump()
                    except (ValueError, TypeError):
                        menu_error = "invalid menu lookup filters"
                    else:
                        menu, menu_error = record, None
                else:
                    menu_error = str(record.get("error", "menu unavailable"))
            else:
                required = ("now", "opens", "closes", "open_now")
                hours = record if all(k in record for k in required) and type(record["open_now"]) is bool else None
        return {"agent_answer": reply, "searched_budgets": budgets, "menu": menu, "menu_query": menu_query,
                "menu_error": menu_error, "hours": hours, "agent_error": None, "path": ["agent"]}

    def verify_recommendation(state: State) -> dict:
        c = state["constraints"]
        real = {item["name"].lower(): item for item in data.menu_records()}
        problems = []
        observed = {item["name"].lower() for item in (state.get("menu") or {}).get("matches", [])
                    if isinstance(item, dict) and isinstance(item.get("name"), str)}
        safe = []
        query = state.get("menu_query")
        covers_request = bool(query and query["max_price"] >= c["budget"]
                              and (c["vegetarian"] or not query["vegetarian"]))
        if state.get("menu") is not None and not state["menu"]["matches"] and not covers_request:
            problems.append("the empty lookup did not cover your full budget and dietary request")
        for budget in state.get("searched_budgets", []):
            if budget is not None and budget > c["budget"]:
                problems.append(f"the agent searched with Rs {budget}, but you said Rs {c['budget']}")
        for dish in state["agent_answer"]["recommended_dishes"]:
            record = real.get(dish.lower())
            if record is None:
                problems.append(f"'{dish}' is not on the menu")
            elif not record["available"]:
                problems.append(f"'{dish}' is out of stock")
            elif record["price"] > c["budget"]:
                problems.append(f"'{dish}' costs Rs {record['price']}, over your Rs {c['budget']}")
            elif c["vegetarian"] and not record["vegetarian"]:
                problems.append(f"'{dish}' is not vegetarian")
            elif dish.lower() not in observed:
                problems.append(f"'{dish}' was not returned by a successful menu lookup")
            elif not any(item["name"] == record["name"] for item in safe):
                safe.append({"name": record["name"], "price": record["price"]})
        return {"problems": problems, "safe_menu": {"matches": safe},
                "lookup_covers_request": covers_request, "path": ["verify_recommendation"]}

    def answer(state: State) -> dict:
        # Never forward the model's free-text message. A validated list does not
        # validate a separate paragraph. Render facts from checked records instead.
        if state.get("agent_error"):
            text = state["agent_error"]
        elif state.get("menu_error"):
            text = answers.menu_sentence(state["constraints"], None, state["menu_error"])
        elif not state["safe_menu"]["matches"] and not state["lookup_covers_request"]:
            text = "That lookup didn't cover your full request, so I couldn't confirm whether any food matches."
        elif not state["safe_menu"]["matches"] and (state.get("menu") or {}).get("matches"):
            text = "I couldn't confirm a valid recommendation from the agent."
        else:
            text = answers.menu_sentence(state["constraints"], state["safe_menu"], None)
        if state["constraints"]["wants_hours"]:
            text += " " + (answers.hours_sentence(state["hours"]) if state.get("hours")
                           else "I couldn't confirm the opening hours.")
        if state["problems"] and state["safe_menu"]["matches"]:
            text = "I double-checked the recommendation. " + text
        return {"answer": text, "path": ["answer (corrected)" if state["problems"] else "answer"]}

    graph = StateGraph(State)
    for node in (read_request, ask_for_budget, run_agent, verify_recommendation, answer):
        graph.add_node("agent" if node is run_agent else node.__name__, node)
    graph.add_edge(START, "read_request")
    graph.add_conditional_edges(
        "read_request",
        lambda s: "agent" if rules.valid_budget(s["constraints"]["budget"]) else "ask_for_budget",
        ["ask_for_budget", "agent"],
    )
    graph.add_edge("agent", "verify_recommendation")
    graph.add_edge("verify_recommendation", "answer")
    graph.add_edge("ask_for_budget", END)
    graph.add_edge("answer", END)
    return graph.compile()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", default="normal")
    parser.add_argument("--question", default=QUESTION)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--inject-mistake", choices=["fake_dish", "non_veg", "free_text"])
    args = parser.parse_args()
    console.setup(args.scenario)

    brain = "offline stand-in (not a real AI)" if args.offline else "Gemini"
    console.banner(f"Agent inside a graph  (brain: {brain}, scenario: {args.scenario})")
    if args.inject_mistake:
        print(f"NOTE: simulating a model mistake ({args.inject_mistake}) for teaching.")
    result = build_graph(args.offline, args.inject_mistake).invoke({"question": args.question})
    print("\nROUTE:  " + "  ->  ".join(result["path"]))
    if result.get("agent_answer"):
        print(f"MODEL PROPOSAL (untrusted): {result['agent_answer']}")
    for problem in result.get("problems", []):
        print(f"CODE CAUGHT:  {problem}")
    print(f"\nANSWER: {result['answer']}")


if __name__ == "__main__":
    main()
