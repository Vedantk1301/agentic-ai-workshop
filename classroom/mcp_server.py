"""Local MCP server: the SAME two functions, exposed over stdio."""
from mcp.server.fastmcp import FastMCP
from menu_tools import find_food, get_canteen_hours

server = FastMCP('Campus Canteen')
server.tool()(find_food)
server.tool()(get_canteen_hours)

if __name__ == '__main__':
    server.run(transport='stdio')
