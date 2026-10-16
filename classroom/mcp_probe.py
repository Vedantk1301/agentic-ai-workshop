"""List and call the actual local MCP tools, without an LLM or API key."""
import asyncio
from mcp_connection import connected_tools


async def main():
    async with connected_tools() as tools:
        print('DISCOVERED:', ', '.join(t.name for t in tools))
        food = next(t for t in tools if t.name == 'find_food')
        print('MCP RESULT:', await food.ainvoke({'max_price': 80, 'vegetarian': True}))


if __name__ == '__main__':
    asyncio.run(main())
