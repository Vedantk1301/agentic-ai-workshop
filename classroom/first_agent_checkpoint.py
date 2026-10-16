"""Checkpoint for README Step 2: the first agent, with one tool.

If your own my_agent.py is stuck, compare it with this file line by line.
"""
from langchain.agents import create_agent          # builds the think-act-observe loop for us
from langchain_core.tools import tool               # wraps a Python function so a model can request it
from menu_tools import find_food                    # our ordinary function from Step 1
from workshop_runtime import make_model, banner, show_messages  # provided helpers: model setup and printing

OFFLINE = True  # Scripted rehearsal. False uses your configured live Gemini.
banner(OFFLINE)  # prints whether this run is scripted or live, so nobody is misled

agent = create_agent(
    model=make_model(OFFLINE),        # the "brain": scripted rules offline, Gemini when live
    tools=[tool(find_food)],          # the only tool this agent may request
    system_prompt="Use the menu tool for facts. Respect budget and diet.",  # the job description
)

result = agent.invoke(
    {"messages": [("user", "Find vegetarian lunch under Rs 80.")]},  # the user's goal
    {"recursion_limit": 10},          # safety stop: the loop may not run forever
)

# Print every step: the question, each tool request, each real result, the final answer.
show_messages(result)
