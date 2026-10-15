"""The fictional canteen: menu records, opening hours, refund policy and the mock clock.

Every demo uses these same records so the class compares designs, not data.
The demo time comes from DEMO_TIME (default 12:30), never the real clock,
so the canteen is "open" no matter when the workshop runs.

Scenarios (set with --scenario or the SCENARIO environment variable):
  normal              everything works
  sold_out            the veg sandwich sold out, so nothing veg under Rs 80 is in stock
  menu_timeout        the menu service never answers
  menu_flaky          the menu service fails once, then works (shows a retry)
  policy_unavailable  the refund-policy source is down
  after_hours         the clock reads 16:30, after closing
"""

from __future__ import annotations

import copy
import json
import os
from pathlib import Path

MENU = json.loads((Path(__file__).resolve().parents[1] / "data" / "menu.json").read_text(encoding="utf-8"))

OPENS = "09:00"
CLOSES = "16:00"

# Fictional policy text, written for this workshop.
REFUND_POLICY = (
    "Prepaid canteen coupons can be refunded at the counter within 7 days "
    "of purchase with your student ID. Used coupons cannot be refunded."
)

SCENARIOS = (
    "normal",
    "sold_out",
    "menu_timeout",
    "menu_flaky",
    "policy_unavailable",
    "after_hours",
)


def current_scenario() -> str:
    scenario = os.environ.get("SCENARIO", "normal").strip().lower()
    if scenario not in SCENARIOS:
        raise ValueError(f"Unknown scenario {scenario!r}. Choose one of: {', '.join(SCENARIOS)}")
    return scenario


def demo_time() -> str:
    """The mock clock. After-hours scenario overrides it to 16:30."""
    if current_scenario() == "after_hours":
        return "16:30"
    return os.environ.get("DEMO_TIME", "12:30")


def menu_records() -> list[dict]:
    """A fresh copy of the menu for the current scenario."""
    records = copy.deepcopy(MENU)
    if current_scenario() == "sold_out":
        for item in records:
            if item["name"] == "Veg sandwich":
                item["available"] = False
    return records
