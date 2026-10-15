"""The same three tools, wrapped so a LangChain agent can request them.

The docstrings are what the model reads to decide which tool to ask for.
Errors come back as {"status": "error"} so the model OBSERVES the failure
instead of the program crashing. The model still cannot run anything itself.
"""

from __future__ import annotations

import json

from langchain_core.tools import tool

from canteen import tools


def _as_json(result: dict) -> str:
    return json.dumps(result, ensure_ascii=False)


@tool
def find_food(max_price: int, vegetarian: bool = False) -> str:
    """Find dishes that are IN STOCK right now at or under max_price rupees.

    Set vegetarian=True to return vegetarian dishes only.
    Returns status "ok" with a list of matches (the list can be empty),
    or status "error" if the menu service failed.
    """
    try:
        return _as_json(tools.find_food(max_price, vegetarian))
    except tools.MenuServiceError as exc:
        return _as_json({"status": "error", "error": str(exc)})
    except ValueError as exc:
        return _as_json({"status": "error", "error": f"invalid input: {exc}"})


@tool
def get_canteen_hours() -> str:
    """Get the canteen's opening hours and whether it is open right now."""
    return _as_json(tools.get_canteen_hours())


@tool
def get_refund_policy() -> str:
    """Get the canteen's refund policy for prepaid coupons."""
    try:
        return _as_json(tools.get_refund_policy())
    except tools.PolicyUnavailable as exc:
        return _as_json({"status": "error", "error": str(exc)})


MENU_TOOLS = [find_food, get_canteen_hours]
ALL_TOOLS = [find_food, get_canteen_hours, get_refund_policy]
