"""Plain rules that read a request. No AI involved.

Used by the fixed workflow and the LangGraph flow to pull out the budget and
diet from a sentence like "veg lunch under Rs 80, is the canteen open?".
Simple on purpose: a fixed workflow trades flexibility for predictability.
"""

from __future__ import annotations

import re


def valid_budget(value: int | None) -> bool:
    """Missing or zero budgets need clarification before any lookup."""
    return type(value) is int and value > 0


def budget_question() -> str:
    return "What's your budget? Please give a positive whole number of rupees."

_BUDGET_PATTERNS = (
    r"(?:rs\.?|₹|inr)\s*(\d+)",
    r"(\d+)\s*(?:rs|rupees|₹)",
    r"(?:under|below|within|budget(?: of)?|max)\s*(?:rs\.?|₹)?\s*(\d+)",
)


def extract_budget(text: str) -> int | None:
    lowered = text.lower()
    for pattern in _BUDGET_PATTERNS:
        match = re.search(pattern, lowered)
        if match:
            return int(match.group(1))
    return None


def wants_vegetarian(text: str) -> bool:
    lowered = text.lower().replace("-", " ")
    if "non veg" in lowered or "nonveg" in lowered:
        return False
    return bool(re.search(r"\bveg(etarian)?\b", lowered))


def extract_constraints(text: str) -> dict:
    lowered = text.lower()
    return {
        "budget": extract_budget(text),
        "vegetarian": wants_vegetarian(text),
        "wants_hours": any(word in lowered for word in ("open", "closed", "hours", "timing")),
        "wants_refund": any(word in lowered for word in ("refund", "coupon")),
    }
