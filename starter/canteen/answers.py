"""Turn tool results into an honest answer. Shared by the no-AI demos.

Rules it follows (the same ones we ask the AI to follow):
  - only recommend dishes the menu tool returned
  - "nothing matches" and "the service failed" get different answers
  - never state a refund rule we could not look up
"""

from __future__ import annotations


def _fmt_items(items: list[dict]) -> str:
    return ", ".join(f"{i['name']} (Rs {i['price']})" for i in items)


def menu_sentence(constraints: dict, menu_result: dict | None, menu_error: str | None) -> str:
    diet = "vegetarian " if constraints.get("vegetarian") else ""
    budget = constraints.get("budget")
    if menu_error:
        return f"Sorry, I couldn't reach the menu right now ({menu_error}), so I can't recommend a dish."
    if menu_result and menu_result["matches"]:
        return f"In stock {diet}options under Rs {budget}: {_fmt_items(menu_result['matches'])}."
    return (
        f"Nothing {diet}under Rs {budget} is in stock right now. "
        "Want me to check with a slightly higher budget?"
    )


def hours_sentence(hours: dict) -> str:
    if hours["open_now"]:
        return f"The canteen is open now (it's {hours['now']}) and closes at {hours['closes']}."
    return f"The canteen is closed right now (it's {hours['now']}). It opens at {hours['opens']}."


def policy_sentence(policy_result: dict | None, policy_error: str | None) -> str:
    if policy_error:
        return "I couldn't reach the refund policy, so I won't guess whether your coupon can be refunded."
    return f"Refund policy: {policy_result['policy']}"
