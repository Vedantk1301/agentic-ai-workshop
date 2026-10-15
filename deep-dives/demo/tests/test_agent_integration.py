"""Use real create_agent and real tools; replace only the offline model's proposal."""
from canteen import models
from test_review_regressions import load


def run_changed_argument(monkeypatch, *, max_price=80, vegetarian=True, question=None, scenario="normal"):
    monkeypatch.setenv("SCENARIO", scenario)
    monkeypatch.setenv("DEMO_TIME", "12:30")
    module = load("04_graph_with_agent.py")

    class ChangedArguments(models.OfflineStandIn):
        def _next(self, messages):
            reply = super()._next(messages)
            for call in reply.tool_calls:
                if call["name"] == "find_food":
                    call["args"].update(max_price=max_price, vegetarian=vegetarian)
            return reply

    monkeypatch.setattr(module.models, "get_model", lambda offline: ChangedArguments())
    return module.build_graph(offline=True).invoke({"question": question or module.QUESTION})


def test_narrow_empty_lookup_cannot_claim_no_food_within_full_budget(monkeypatch):
    result = run_changed_argument(monkeypatch, max_price=10)
    assert result["menu"]["filters"]["max_price"] == 10
    assert result["menu"]["matches"] == []
    assert "Nothing vegetarian under Rs 80" not in result["answer"]
    assert "couldn't confirm" in result["answer"].lower()
    assert result["problems"]


def test_tool_coerced_numeric_string_is_checked_without_crashing(monkeypatch):
    result = run_changed_argument(monkeypatch, max_price="80")
    assert result["menu"]["filters"]["max_price"] == 80
    assert result["searched_budgets"] == [80]
    assert "Veg sandwich" in result["answer"] and "Rs 60" in result["answer"]
    assert result["problems"] == []


def test_narrower_diet_lookup_cannot_claim_no_food_for_an_unrestricted_request(monkeypatch):
    # Force only the sandwich out of stock; the chicken roll is still available.
    result = run_changed_argument(monkeypatch, vegetarian=True, question="lunch under Rs 80", scenario="sold_out")
    assert result["menu"]["matches"] == []
    assert "Nothing under Rs 80" not in result["answer"]
    assert "couldn't confirm" in result["answer"].lower()
    assert result["problems"]
