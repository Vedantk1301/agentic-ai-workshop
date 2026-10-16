"""Prepared local-process connection. No remote hosting required."""
from contextlib import asynccontextmanager
from pathlib import Path
import sys

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools

SERVER_PATH = Path(__file__).with_name('mcp_server.py').resolve()


@asynccontextmanager
async def connected_tools():
    client = MultiServerMCPClient({'canteen': {
        'transport': 'stdio', 'command': sys.executable, 'args': [str(SERVER_PATH)],
    }})
    async with client.session('canteen') as session:
        yield await load_mcp_tools(session)
