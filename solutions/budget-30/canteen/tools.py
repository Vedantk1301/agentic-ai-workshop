"""The canteen tools as plain Python functions.

The lesson: these run in OUR code. The AI model can only ask for them.
Price, vegetarian and stock rules are enforced here, so the model cannot skip them.

An empty result and a failure are different things:
  {"status": "ok", "matches": []}            -> the lookup worked, nothing qualifies
  raise MenuServiceError / PolicyUnavailable  -> the lookup itself failed
"""

from __future__ import annotations

from canteen import data


class MenuServiceError(Exception):
    """The menu service did not answer (a timeout)."""


class PolicyUnavailable(Exception):
    """The refund-policy source could not be reached."""


_menu_calls = {"count": 0}


def reset_call_counter() -> None:
    _menu_calls["count"] = 0


def find_food(max_price: int, vegetarian: bool = False) -> dict:
    """Return in-stock dishes at or under max_price, optionally vegetarian only."""
    if not isinstance(max_price, int) or max_price <= 0:
        raise ValueError("max_price must be a positive whole number of rupees")

    _menu_calls["count"] += 1
    scenario = data.current_scenario()
    if scenario == "menu_timeout":
        raise MenuServiceError("menu service timed out")
    if scenario == "menu_flaky" and _menu_calls["count"] == 1:
        raise MenuServiceError("menu service timed out")

    matches = [
        item
        for item in data.menu_records()
        if item["available"]
        and item["price"] <= max_price
        and (item["vegetarian"] or not vegetarian)
    ]
    return {
        "status": "ok",
        "filters": {"max_price": max_price, "vegetarian": vegetarian, "in_stock_only": True},
        "matches": [{"name": m["name"], "price": m["price"]} for m in matches],
    }


def _minutes(hhmm: str) -> int:
    hours, minutes = hhmm.split(":")
    return int(hours) * 60 + int(minutes)


def get_canteen_hours() -> dict:
    """Opening hours and whether the canteen is open at the demo time."""
    now = data.demo_time()
    is_open = _minutes(data.OPENS) <= _minutes(now) < _minutes(data.CLOSES)
    return {"status": "ok", "opens": data.OPENS, "closes": data.CLOSES, "now": now, "open_now": is_open}


def get_refund_policy() -> dict:
    """The canteen's coupon refund policy (fictional)."""
    if data.current_scenario() == "policy_unavailable":
        raise PolicyUnavailable("refund-policy source unavailable")
    return {"status": "ok", "policy": data.REFUND_POLICY}
