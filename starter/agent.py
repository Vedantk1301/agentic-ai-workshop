"""A ReAct-style canteen agent with LangChain.

The model requests tools; application code executes them. The --offline option
uses a clearly labelled rule-based stand-in, not a real AI.

Run from the repository root using its .venv:
  .venv\Scripts\python starter/agent.py --offline
  .venv\Scripts\python starter/agent.py --offline --menu-only
  .venv\Scripts\python starter/agent.py --offline --scenario sold_out
  .venv\Scripts\python solutions/budget-30/agent.py --offline

Drop --offline only after privately configuring and testing live Gemini.
"""

from __future__ import annotations

import argparse
import time

from langchain.agents import create_agent
from langgraph.errors import GraphRecursionError

from canteen import console, lc_tools, models
from canteen.trace import print_trace

QUESTION = "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."
MENU_ONLY_QUESTION = "What vegetarian food can I get under Rs 80?"

SYSTEM_PROMPT = """You are the Campus Canteen Assistant.
- Use the tools for anything about dishes, prices, stock or opening hours. Never guess them.
- Only recommend dishes the find_food tool returned. Never invent a dish or a price.
- If nothing matches, say so plainly and offer to try a different budget.
- If a tool returns an error, say that information is unavailable right now.
- Vegetarian is not an allergen guarantee.
Keep answers short and friendly."""


def build_agent(offline: bool, tools=lc_tools.MENU_TOOLS):
    """The whole agent: a model, the tools it may request, and instructions."""
    return create_agent(model=models.get_model(offline), tools=tools, system_prompt=SYSTEM_PROMPT)


def run(question: str, offline: bool, max_steps: int, pause: bool = False, tools=lc_tools.MENU_TOOLS) -> dict:
    agent = build_agent(offline, tools)
    started = time.perf_counter()
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": question}]},
            config={"recursion_limit": max_steps},  # the step limit: stop instead of looping forever
        )
    except GraphRecursionError:
        print(f"\nSTOPPED: hit the step limit of {max_steps}. A stuck agent stops; it doesn't loop forever.")
        return {}
    return print_trace(result["messages"], time.perf_counter() - started, pause=pause) | {"result": result}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--scenario", default="normal")
    parser.add_argument("--question")
    parser.add_argument("--menu-only", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--pause", action="store_true", help="reveal the completed trace one step at a time (execution finishes first)")
    parser.add_argument("--max-steps", type=int, default=10)
    args = parser.parse_args()
    console.setup(args.scenario)

    question = args.question or (MENU_ONLY_QUESTION if args.menu_only else QUESTION)
    brain = "offline stand-in (not a real AI)" if args.offline else "Gemini"
    console.banner(f"ReAct-style agent  (brain: {brain}, scenario: {args.scenario})")
    run(question, args.offline, args.max_steps, pause=args.pause)


if __name__ == "__main__":
    main()
