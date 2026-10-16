"""The complete first build: a model, ordinary tools and an agent loop.

Checkpoint for README Step 3 (two tools). Run from the repository root:
    python classroom/agent.py --offline
    python classroom/agent.py --offline --question "Find vegetarian lunch under Rs 30."
"""
from langchain.agents import create_agent
from langchain_core.tools import tool

from menu_tools import find_food, get_canteen_hours
from workshop_runtime import arguments, banner, make_model, show_messages


def build_agent(offline=False, with_hours=True):
    # Give the agent a list of allowed tools. It can only request these.
    tools = [tool(find_food)]
    if with_hours:
        tools.append(tool(get_canteen_hours))
    # Notice there is no if-statement deciding WHICH tool to call.
    # The model reads the question and the tool descriptions, then chooses.
    return create_agent(
        model=make_model(offline),
        tools=tools,
        system_prompt='Help with our fictional canteen. Use tools for menu and hours facts. '
                      'Respect the user budget and diet. Do not invent dishes. The default time is a fixture.',
    )


if __name__ == '__main__':
    args = arguments('One agent, two tools')  # reads --offline and --question from the command line
    banner(args.offline)
    agent = build_agent(args.offline)
    result = agent.invoke({'messages': [('user', args.question)]}, {'recursion_limit': 10})
    show_messages(result)
