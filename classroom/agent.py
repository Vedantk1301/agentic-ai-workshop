"""The complete first build: a model, ordinary tools and an agent loop."""
from langchain.agents import create_agent
from langchain_core.tools import tool

from menu_tools import find_food, get_canteen_hours
from workshop_runtime import arguments, banner, make_model, show_messages


def build_agent(offline=False, with_hours=True):
    tools = [tool(find_food)]
    if with_hours:
        tools.append(tool(get_canteen_hours))
    return create_agent(
        model=make_model(offline),
        tools=tools,
        system_prompt='Help with our fictional canteen. Use tools for menu and hours facts. '
                      'Respect the user budget and diet. Do not invent dishes. The default time is a fixture.',
    )


if __name__ == '__main__':
    args = arguments('One agent, two tools')
    banner(args.offline)
    agent = build_agent(args.offline)
    result = agent.invoke({'messages': [('user', args.question)]}, {'recursion_limit': 10})
    show_messages(result)
