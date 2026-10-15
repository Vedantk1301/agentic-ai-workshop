"""BLOCK 4: Why LangGraph. The same task as an explicit graph.

State = the shared information carried through the task (the "bag").
Nodes = steps (here, plain functions, no AI needed).
Edges = where to go next, decided by OUR routing code.

What this graph adds over 01 and 02:
  - missing budget -> ask the user and stop (don't call anything with a guess)
  - menu timeout   -> retry ONCE, then give an honest "unavailable" answer
  - verify         -> code double-checks every dish before we answer

Run:
  .venv\\Scripts\\python 03_langgraph_flow.py
  .venv\\Scripts\\python 03_langgraph_flow.py --scenario menu_flaky      (retry saves the day)
  .venv\\Scripts\\python 03_langgraph_flow.py --scenario menu_timeout    (retry, then give up honestly)
  .venv\\Scripts\\python 03_langgraph_flow.py --question "veg lunch, is it open?"   (asks for budget)
  .venv\\Scripts\\python 03_langgraph_flow.py --diagram                  (prints the graph as Mermaid)
"""

from __future__ import annotations

import argparse
import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph

from canteen import answers, console, data, rules, tools

QUESTION = "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."
MAX_MENU_ATTEMPTS = 2


class CanteenState(TypedDict, total=False):
    question: str
    constraints: dict
    attempts: int
    menu: dict | None
    menu_error: str | None
    hours: dict | None
    answer: str
    path: Annotated[list[str], operator.add]  # every node adds its name, so we can show the route


# ---------- nodes: each one does a single step and returns what it changed ----------

def read_request(state: CanteenState) -> dict:
    return {"constraints": rules.extract_constraints(state["question"]), "attempts": 0, "path": ["read_request"]}


def ask_for_budget(state: CanteenState) -> dict:
    return {"answer": rules.budget_question(), "path": ["ask_for_budget"]}


def search_menu(state: CanteenState) -> dict:
    c = state["constraints"]
    attempts = state.get("attempts", 0) + 1
    try:
        menu = tools.find_food(c["budget"], c["vegetarian"])
        return {"menu": menu, "menu_error": None, "attempts": attempts, "path": ["search_menu"]}
    except tools.MenuServiceError as exc:
        return {"menu": None, "menu_error": str(exc), "attempts": attempts, "path": [f"search_menu (failed, try {attempts})"]}


def check_hours(state: CanteenState) -> dict:
    return {"hours": tools.get_canteen_hours(), "path": ["check_hours"]}


def verify(state: CanteenState) -> dict:
    """Code checks the facts before we speak: every dish must really fit the request."""
    c = state["constraints"]
    real = {item["name"]: item for item in data.menu_records()}
    for dish in (state.get("menu") or {}).get("matches", []):
        record = real[dish["name"]]
        assert record["available"] and record["price"] <= c["budget"]
        assert record["vegetarian"] or not c["vegetarian"]
    return {"path": ["verify"]}


def answer(state: CanteenState) -> dict:
    c = state["constraints"]
    reply = answers.menu_sentence(c, state.get("menu"), state.get("menu_error"))
    if state.get("hours"):
        reply += " " + answers.hours_sentence(state["hours"])
    return {"answer": reply, "path": ["answer"]}


# ---------- edges: our code decides where to go next ----------

def after_reading(state: CanteenState) -> str:
    return "search_menu" if rules.valid_budget(state["constraints"]["budget"]) else "ask_for_budget"


def after_search(state: CanteenState) -> str:
    if state.get("menu_error") and state["attempts"] < MAX_MENU_ATTEMPTS:
        return "search_menu"  # bounded retry
    if state["constraints"]["wants_hours"]:
        return "check_hours"
    return "verify"


def build_graph():
    graph = StateGraph(CanteenState)
    for node in (read_request, ask_for_budget, search_menu, check_hours, verify, answer):
        graph.add_node(node.__name__, node)
    graph.add_edge(START, "read_request")
    graph.add_conditional_edges("read_request", after_reading, ["ask_for_budget", "search_menu"])
    graph.add_conditional_edges("search_menu", after_search, ["search_menu", "check_hours", "verify"])
    graph.add_edge("check_hours", "verify")
    graph.add_edge("verify", "answer")
    graph.add_edge("ask_for_budget", END)
    graph.add_edge("answer", END)
    return graph.compile()


def run(question: str) -> CanteenState:
    tools.reset_call_counter()
    return build_graph().invoke({"question": question})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", default="normal")
    parser.add_argument("--question", default=QUESTION)
    parser.add_argument("--diagram", action="store_true")
    args = parser.parse_args()
    console.setup(args.scenario)

    if args.diagram:
        print(build_graph().get_graph().draw_mermaid())
        return
    console.banner(f"LangGraph flow  (scenario: {args.scenario})")
    print(f"Question: {args.question}")
    result = run(args.question)
    print("\nROUTE:  " + "  ->  ".join(result["path"]))
    print(f"\nANSWER: {result['answer']}")


if __name__ == "__main__":
    main()
