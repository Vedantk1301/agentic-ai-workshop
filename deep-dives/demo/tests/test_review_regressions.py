"""Review regressions: untrusted model output at the real graph boundary.

Most cases replace create_agent with a supplied transcript. The outer graph,
routing, validator and answer renderer execute normally. Actual agent/tool
integration is covered separately in test_agent_integration.py. No API/network.
"""
import importlib.util
import json
import sys
from pathlib import Path

import pytest
from langchain_core.messages import AIMessage, ToolMessage
from langgraph.errors import GraphRecursionError

ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    name = "review_" + filename.replace(".py", "")
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(autouse=True)
def normal_scenario(monkeypatch):
    monkeypatch.setenv("SCENARIO", "normal")
    monkeypatch.setenv("DEMO_TIME", "12:30")


def tool_trace(food, *, budget=80, vegetarian=True, hours=True):
    messages = [
        AIMessage(content="", tool_calls=[{
            "name": "find_food", "args": {"max_price": budget, "vegetarian": vegetarian}, "id": "food"
        }]),
        ToolMessage(content=json.dumps(food), tool_call_id="food"),
    ]
    if hours:
        messages += [
            AIMessage(content="", tool_calls=[{"name": "get_canteen_hours", "args": {}, "id": "hours"}]),
            ToolMessage(content=json.dumps({"now": "12:30", "opens": "09:00", "closes": "16:00", "open_now": True}), tool_call_id="hours"),
        ]
    return messages


def run_proposal(monkeypatch, dishes, text, messages):
    module = load("04_graph_with_agent.py")

    class ModelBoundary:
        def invoke(self, *args, **kwargs):
            return {"structured_response": module.CanteenAnswer(recommended_dishes=dishes, message=text),
                    "messages": messages}

    monkeypatch.setattr(module, "create_agent", lambda **kwargs: ModelBoundary())
    return module.build_graph(offline=True).invoke({"question": module.QUESTION})


FOOD = {"status": "ok", "matches": [{"name": "Veg sandwich", "price": 60}]}


def test_final_text_cannot_add_a_dish_not_in_the_verified_list(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"],
                          "Try the Paneer Tikka Wrap for Rs 60.",
                          tool_trace(FOOD))
    assert "Paneer Tikka Wrap" not in result["answer"]
    assert "Veg sandwich" in result["answer"]


def test_final_prices_and_hours_come_from_tool_records(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"],
                          "Veg sandwich costs Rs 1. Open until 22:00.",
                          tool_trace(FOOD))
    assert "Rs 60" in result["answer"] and "16:00" in result["answer"]
    assert "Rs 1." not in result["answer"] and "22:00" not in result["answer"]


def test_menu_failure_cannot_become_an_available_dish(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"], "Veg sandwich is in stock.",
                          tool_trace({"status": "error", "error": "menu unavailable"}))
    assert "Veg sandwich" not in result["answer"]
    assert "couldn't reach the menu" in result["answer"]


def test_no_menu_call_is_not_proof_of_stock(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"], "Veg sandwich is available.", [])
    assert "Veg sandwich" not in result["answer"]
    assert "can't recommend" in result["answer"]


def test_dish_must_have_been_returned_by_the_menu_tool(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"], "Veg sandwich is available.",
                          tool_trace({"status": "ok", "matches": []}))
    assert "Veg sandwich" not in result["answer"]
    assert result["problems"]


def test_successful_empty_lookup_is_not_called_a_service_error(monkeypatch):
    result = run_proposal(monkeypatch, [], "Made-up answer",
                          tool_trace({"status": "ok", "matches": []}))
    assert "Nothing vegetarian" in result["answer"]
    assert "couldn't reach the menu" not in result["answer"]


def test_missing_hours_does_not_become_a_claim_about_opening(monkeypatch):
    result = run_proposal(monkeypatch, ["Veg sandwich"], "The canteen is open until 22:00.",
                          tool_trace(FOOD, hours=False))
    assert "couldn't confirm the opening hours" in result["answer"]
    assert "22:00" not in result["answer"]


def test_wrong_tool_budget_cannot_authorise_an_over_budget_dish(monkeypatch):
    result = run_proposal(monkeypatch, ["Dosa"], "Get a dosa for Rs 90.",
                          tool_trace({"status": "ok", "matches": [{"name": "Dosa", "price": 90}]}, budget=100))
    assert "Dosa" not in result["answer"] and "dosa" not in result["answer"]
    assert any("over your Rs 80" in p for p in result["problems"])


def test_wrong_diet_argument_cannot_authorise_non_veg(monkeypatch):
    result = run_proposal(monkeypatch, ["Chicken roll"], "The chicken roll is vegetarian.",
                          tool_trace({"status": "ok", "matches": [{"name": "Chicken roll", "price": 75}]}, vegetarian=False))
    assert "Chicken roll" not in result["answer"]
    assert any("not vegetarian" in p for p in result["problems"])


def test_latest_failed_lookup_does_not_reuse_earlier_stock(monkeypatch):
    messages = tool_trace(FOOD)
    messages += [
        AIMessage(content="", tool_calls=[{"name": "find_food", "args": {"max_price": 80, "vegetarian": True}, "id": "refresh"}]),
        ToolMessage(content='{"status":"error","error":"refresh failed"}', tool_call_id="refresh"),
    ]
    result = run_proposal(monkeypatch, ["Veg sandwich"], "Veg sandwich is available.", messages)
    assert "Veg sandwich" not in result["answer"]


def test_exhausted_agent_stops_with_an_honest_answer(monkeypatch):
    module = load("04_graph_with_agent.py")

    class ExhaustedModel:
        def invoke(self, *args, **kwargs):
            raise GraphRecursionError("step limit")

    monkeypatch.setattr(module, "create_agent", lambda **kwargs: ExhaustedModel())
    result = module.build_graph(offline=True).invoke({"question": module.QUESTION})
    assert "step limit" in result["answer"].lower()
    assert "Veg sandwich" not in result["answer"]


@pytest.mark.parametrize("filename", ["01_tools_and_fixed_workflow.py", "03_langgraph_flow.py", "04_graph_with_agent.py"])
def test_zero_budget_asks_for_valid_input_instead_of_crashing(filename):
    module = load(filename)
    question = "vegetarian lunch under Rs 0"
    if filename.startswith("01"):
        answer = module.fixed_workflow(question, show_steps=False)
    elif filename.startswith("03"):
        answer = module.run(question)["answer"]
    else:
        answer = module.build_graph(offline=True).invoke({"question": question})["answer"]
    assert "positive" in answer.lower() and "budget" in answer.lower()


def test_free_text_mistake_demo_shows_a_proposal_but_never_sends_it():
    module = load("04_graph_with_agent.py")
    result = module.build_graph(offline=True, inject_mistake="free_text").invoke({"question": module.QUESTION})
    assert "Paneer Tikka Wrap" in result["agent_answer"]["message"]
    assert "Paneer Tikka Wrap" not in result["answer"]
    assert "Rs 60" in result["answer"]
