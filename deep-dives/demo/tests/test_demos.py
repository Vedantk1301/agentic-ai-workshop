"""Checks every demo against the curriculum's scenario cards. Run: .venv\\Scripts\\python -m pytest -q"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

DEMO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DEMO))

from canteen import rules, tools  # noqa: E402

QUESTION = "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."


def load(filename: str):
    name = "demo_" + filename.replace(".py", "")
    spec = importlib.util.spec_from_file_location(name, DEMO / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module  # LangGraph reads type hints through the module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def scenario(monkeypatch):
    def set_scenario(name: str) -> None:
        monkeypatch.setenv("SCENARIO", name)
        tools.reset_call_counter()
    set_scenario("normal")
    return set_scenario


# ---- tools: code enforces price, vegetarian and stock ----

def test_veg_under_80_is_only_the_sandwich(scenario):
    assert tools.find_food(80, True)["matches"] == [{"name": "Veg sandwich", "price": 60}]


def test_non_veg_request_includes_chicken_roll_but_never_out_of_stock_poha(scenario):
    names = [m["name"] for m in tools.find_food(80, False)["matches"]]
    assert names == ["Veg sandwich", "Chicken roll"]


def test_sold_out_is_an_empty_success_not_an_error(scenario):
    scenario("sold_out")
    assert tools.find_food(80, True) == {
        "status": "ok",
        "filters": {"max_price": 80, "vegetarian": True, "in_stock_only": True},
        "matches": [],
    }


def test_timeout_is_a_failure(scenario):
    scenario("menu_timeout")
    with pytest.raises(tools.MenuServiceError):
        tools.find_food(80, True)


def test_mock_clock_open_at_lunch_closed_after_four(scenario):
    assert tools.get_canteen_hours()["open_now"] is True
    scenario("after_hours")
    assert tools.get_canteen_hours()["open_now"] is False


@pytest.mark.parametrize("text,budget", [
    ("veg lunch under Rs 80", 80), ("under 80 please", 80), ("₹75 max", 75), ("100 rupees", 100), ("veg lunch", None),
])
def test_budget_extraction(text, budget):
    assert rules.extract_budget(text) == budget


def test_non_veg_is_not_vegetarian():
    assert rules.wants_vegetarian("non-veg roll under 80") is False
    assert rules.wants_vegetarian("veg lunch") is True


# ---- 01 fixed workflow ----

def test_fixed_workflow_asks_for_missing_budget(scenario):
    wf = load("01_tools_and_fixed_workflow.py")
    assert "budget" in wf.fixed_workflow("veg lunch, is it open?", show_steps=False).lower()


# ---- 02 ReAct agent (offline stand-in) ----

def test_agent_asks_for_food_then_hours(scenario, capsys):
    agent = load("02_react_agent.py")
    summary = agent.run(QUESTION, offline=True, max_steps=10)
    out = capsys.readouterr().out
    assert out.index("find_food") < out.index("get_canteen_hours")
    assert summary["tool_calls"] == 2 and "Veg sandwich" in out


def test_agent_never_invents_a_dish_when_sold_out(scenario, capsys):
    scenario("sold_out")
    load("02_react_agent.py").run(QUESTION, offline=True, max_steps=10)
    answer = capsys.readouterr().out.split("[ANSWER]")[1]
    assert "Nothing vegetarian" in answer and "sandwich" not in answer.lower()


def test_step_limit_stops_the_agent(scenario, capsys):
    load("02_react_agent.py").run(QUESTION, offline=True, max_steps=2)
    assert "STOPPED" in capsys.readouterr().out


# ---- 03 LangGraph flow: the four scenario cards ----

@pytest.mark.parametrize("name,question,route,phrase", [
    ("normal", QUESTION, ["read_request", "search_menu", "check_hours", "verify", "answer"], "Veg sandwich"),
    ("normal", "veg lunch, is it open?", ["read_request", "ask_for_budget"], "budget"),
    ("sold_out", QUESTION, ["read_request", "search_menu", "check_hours", "verify", "answer"], "Nothing vegetarian"),
    ("menu_flaky", QUESTION, ["read_request", "search_menu (failed, try 1)", "search_menu", "check_hours", "verify", "answer"], "Veg sandwich"),
    ("menu_timeout", QUESTION, ["read_request", "search_menu (failed, try 1)", "search_menu (failed, try 2)", "check_hours", "verify", "answer"], "couldn't reach the menu"),
])
def test_graph_routes(scenario, name, question, route, phrase):
    scenario(name)
    result = load("03_langgraph_flow.py").run(question)
    assert result["path"] == route and phrase in result["answer"]


# ---- 04 agent inside a graph: code catches the model's mistake ----

@pytest.mark.parametrize("mistake,caught", [("fake_dish", "not on the menu"), ("non_veg", "not vegetarian")])
def test_verification_catches_injected_mistakes(scenario, mistake, caught):
    graph = load("04_graph_with_agent.py").build_graph(offline=True, inject_mistake=mistake)
    result = graph.invoke({"question": QUESTION})
    assert any(caught in p for p in result["problems"]) and "Veg sandwich" in result["answer"]


def test_clean_agent_answer_passes_verification(scenario):
    result = load("04_graph_with_agent.py").build_graph(offline=True).invoke({"question": QUESTION})
    assert result["problems"] == [] and result["agent_answer"]["recommended_dishes"] == ["Veg sandwich"]


# ---- 05 team of roles ----

def test_coordinator_never_guesses_a_refund_rule(scenario, capsys):
    scenario("policy_unavailable")
    reply, _ = load("05_team_of_roles.py").coordinator("Find lunch under Rs 80, and explain refunds.")
    assert "won't guess" in reply and "7 days" not in reply
