"""List and call the actual local MCP tools, without an LLM or API key.

This shows MCP on its own: discover tools, then call one. No AI involved.
    python classroom/mcp_probe.py
"""
import asyncio
from mcp_connection import connected_tools
from workshop_runtime import payload


async def main():
    # Starts mcp_server.py as a child process and asks it which tools it offers.
    async with connected_tools() as tools:
        print('DISCOVERED:', ', '.join(t.name for t in tools))
        food = next(t for t in tools if t.name == 'find_food')
        # Call the tool through MCP. The reply arrives as text; payload() turns it back into a dict.
        result = await food.ainvoke({'max_price': 80, 'vegetarian': True})
        print('MCP RESULT:', payload(result))


if __name__ == '__main__':
    asyncio.run(main())
