"""BLOCK 2: Tools and a fixed workflow. There is no AI anywhere in this file.

Part A runs the menu tool directly, so students see a tool is just a function.
Part B is a fixed workflow: OUR code decides every step, in a fixed order.

Run (PowerShell, inside the demo folder):
  .venv\\Scripts\\python 01_tools_and_fixed_workflow.py
  .venv\\Scripts\\python 01_tools_and_fixed_workflow.py --scenario sold_out
  .venv\\Scripts\\python 01_tools_and_fixed_workflow.py --question "veg lunch please, is it open?"
"""

from __future__ import annotations

import argparse
import json

from canteen import answers, console, rules, tools

QUESTION = "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."


def part_a_tool_directly() -> None:
    console.banner("PART A: the menu tool, called directly (no AI)")
    print("find_food(max_price=80, vegetarian=True) returns:")
    try:
        print(json.dumps(tools.find_food(80, True), indent=2))
    except tools.MenuServiceError as exc:
        print(f"FAILED: {exc}   (a failure, which is different from 'no matches')")
    tools.reset_call_counter()


def fixed_workflow(question: str, show_steps: bool = True) -> str:
    """Read -> validate -> search menu -> check hours -> answer. Code decides every step."""

    def step(text: str) -> None:
        if show_steps:
            print(f"  {text}")

    constraints = rules.extract_constraints(question)
    step(f"1. read request      -> {constraints}")

    if not rules.valid_budget(constraints["budget"]):
        step("2. validate          -> missing or invalid budget, so ask instead of guessing")
        return rules.budget_question()
    step(f"2. validate          -> budget Rs {constraints['budget']}, vegetarian={constraints['vegetarian']}")

    try:
        menu = tools.find_food(constraints["budget"], constraints["vegetarian"])
        step(f"3. search menu       -> {len(menu['matches'])} match(es): {menu['matches']}")
        reply = answers.menu_sentence(constraints, menu, None)
    except tools.MenuServiceError as exc:
        step(f"3. search menu       -> FAILED: {exc}")
        reply = answers.menu_sentence(constraints, None, str(exc))

    hours = tools.get_canteen_hours()
    step(f"4. check hours       -> open_now={hours['open_now']} at {hours['now']}")
    reply += " " + answers.hours_sentence(hours)

    step("5. present answer")
    return reply


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", default="normal")
    parser.add_argument("--question", default=QUESTION)
    args = parser.parse_args()
    console.setup(args.scenario)

    part_a_tool_directly()
    console.banner(f"PART B: fixed workflow  (scenario: {args.scenario})")
    print(f"Question: {args.question}\n")
    print(f"\nANSWER: {fixed_workflow(args.question)}")


if __name__ == "__main__":
    main()
