"""LangChain agent, same canteen, tools supplied by an actual MCP process."""
import asyncio
from langchain.agents import create_agent

from mcp_connection import connected_tools
from workshop_runtime import arguments, banner, make_model, show_messages

QUESTION = 'Find vegetarian lunch under Rs 80 and check opening hours.'


async def run(offline=False, question=QUESTION):
    async with connected_tools() as tools:
        agent = create_agent(make_model(offline), tools,
                             system_prompt='Use the tools for canteen facts. Respect budget and diet; do not invent dishes.')
        return await agent.ainvoke({'messages': [('user', question)]}, {'recursion_limit': 10})


if __name__ == '__main__':
    args = arguments('The same agent using MCP')
    banner(args.offline, 'MCP / stdio / local server process')
    show_messages(asyncio.run(run(args.offline, args.question)))
