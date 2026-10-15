"""BLOCK 5: Multi-agent orchestration, shown as a team of roles.

Request: "Find lunch under Rs 80, and explain whether a prepaid coupon can be refunded."

  Coordinator    splits the job and combines the answers
  Menu adviser   only sees menu data (uses find_food)
  Policy adviser only sees the refund policy (uses get_refund_policy)

This is a plain-Python SIMULATION of the pattern, so it runs with no install and no
internet. In CrewAI, each role would be an Agent with a Task, run by a Crew with a
sequential or hierarchical process (see crewai_sketch.md, not run in class).

The question to end on: could ONE agent with two tools do this? Usually yes.
Use a team only for a reason: separate data, separate permissions, or truly
independent work. Every extra role adds calls, waiting time and failure points.

Run:
  .venv\\Scripts\\python 05_team_of_roles.py
  .venv\\Scripts\\python 05_team_of_roles.py --scenario policy_unavailable
"""

from __future__ import annotations

import argparse

from canteen import answers, console, tools

QUESTION = "Find lunch under Rs 80, and explain whether a prepaid coupon can be refunded."


def say(role: str, text: str) -> None:
    print(f"[{role:<15}] {text}")


def menu_adviser(budget: int) -> dict:
    say("MENU ADVISER", f"I only see menu data. Calling find_food(max_price={budget})")
    try:
        result = tools.find_food(budget, vegetarian=False)
        say("MENU ADVISER", f"Found: {result['matches']}")
        return {"ok": True, "result": result}
    except tools.MenuServiceError as exc:
        say("MENU ADVISER", f"Menu service failed: {exc}")
        return {"ok": False, "error": str(exc)}


def policy_adviser() -> dict:
    say("POLICY ADVISER", "I only see the policy. Calling get_refund_policy()")
    try:
        result = tools.get_refund_policy()
        say("POLICY ADVISER", f"Policy: {result['policy']}")
        return {"ok": True, "result": result}
    except tools.PolicyUnavailable as exc:
        say("POLICY ADVISER", f"Could not get the policy: {exc}")
        return {"ok": False, "error": str(exc)}


def coordinator(question: str, budget: int = 80) -> tuple[str, int]:
    handoffs = 0
    say("COORDINATOR", f"Request: {question}")
    say("COORDINATOR", "Splitting it: food -> Menu adviser, refund -> Policy adviser")
    menu = menu_adviser(budget)
    handoffs += 2  # task out, finding back
    policy = policy_adviser()
    handoffs += 2

    constraints = {"budget": budget, "vegetarian": False}
    reply = answers.menu_sentence(constraints, menu.get("result"), menu.get("error"))
    reply += " " + answers.policy_sentence(policy.get("result"), policy.get("error"))
    say("COORDINATOR", "Combining both findings. I don't add facts neither adviser gave me.")
    return reply, handoffs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", default="normal")
    args = parser.parse_args()
    console.setup(args.scenario)

    console.banner(f"A team of roles  (scenario: {args.scenario})")
    reply, handoffs = coordinator(QUESTION)
    print(f"\nANSWER: {reply}")
    print(f"\n-- 3 roles, {handoffs} handoffs, 2 tool calls. One agent with both tools would need 0 handoffs.")
    print("-- So why a team? Only for separate data, separate permissions, or truly independent work.")


if __name__ == "__main__":
    main()
