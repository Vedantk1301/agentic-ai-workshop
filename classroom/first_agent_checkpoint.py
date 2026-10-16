from langchain.agents import create_agent
from langchain_core.tools import tool
from menu_tools import find_food
from workshop_runtime import make_model, banner, show_messages

OFFLINE = True  # Scripted rehearsal. False uses your configured live Gemini.
banner(OFFLINE)
agent = create_agent(
    model=make_model(OFFLINE),
    tools=[tool(find_food)],
    system_prompt="Use the menu tool for facts. Respect budget and diet.",
)
result = agent.invoke(
    {"messages": [("user", "Find vegetarian lunch under Rs 80.")]},
    {"recursion_limit": 10},
)
show_messages(result)
