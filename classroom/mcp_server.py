"""Local MCP server: the SAME two functions, exposed over stdio.

An MCP server has no model and makes no decisions. It only offers tools.
Any MCP client (a LangChain agent, LangGraph, CrewAI, Claude Desktop, Cursor)
can discover these tools and call them. You don't run this file yourself:
the client starts it as a child process (see mcp_connection.py).
"""
from mcp.server.fastmcp import FastMCP
from menu_tools import find_food, get_canteen_hours

server = FastMCP('Campus Canteen')   # the name clients see
server.tool()(find_food)             # register the existing function, unchanged
server.tool()(get_canteen_hours)

if __name__ == '__main__':
    # stdio = messages travel over standard input/output. So never add print() here:
    # printed text would corrupt the protocol messages.
    server.run(transport='stdio')
