"""Behavioral checks for the build-first lesson; no API keys required."""
import asyncio
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

CLASSROOM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CLASSROOM))


def test_direct_menu_and_hours():
    tools = importlib.import_module('menu_tools')
    assert tools.find_food(80)['matches'] == [{'name': 'Veg sandwich', 'price': 60}]
    assert tools.find_food(30)['matches'] == []
    assert {r['name'] for r in tools.find_food(80, False)['matches']} == {'Chicken roll', 'Veg sandwich'}
    assert tools.get_canteen_hours()['open_now'] is True
    assert tools.get_canteen_hours('16:00')['open_now'] is False
    assert tools.get_canteen_hours('08:59')['open_now'] is False


@pytest.mark.parametrize('budget', [-1, True, 80.5, '80'])
def test_invalid_budgets_are_not_silently_accepted(budget):
    tools = importlib.import_module('menu_tools')
    with pytest.raises(ValueError):
        tools.find_food(budget)


def test_first_agent_calls_real_functions():
    agent = importlib.import_module('agent').build_agent(offline=True)
    result = agent.invoke({'messages': [('user', 'Find vegetarian lunch under Rs 80 and check opening hours.')]})
    names = [m.name for m in result['messages'] if m.type == 'tool']
    assert names == ['find_food', 'get_canteen_hours']
    answer = str(result['messages'][-1].content)
    assert 'Veg sandwich' in answer and '16:00' in answer


def test_manual_loop_refuses_unknown_tool():
    module = importlib.import_module('manual_loop')
    from langchain_core.messages import AIMessage

    class BadRequest:
        def bind_tools(self, tools):
            return self

        def invoke(self, messages):
            return AIMessage(content='', tool_calls=[{'name': 'delete_everything', 'args': {}, 'id': 'bad'}])

    with pytest.raises(ValueError, match='not allowed'):
        module.run_loop(BadRequest(), 'Find lunch', [], max_steps=2)


def test_manual_loop_stops_a_repeating_model():
    module = importlib.import_module('manual_loop')
    from langchain_core.messages import AIMessage
    from langchain_core.tools import tool

    @tool
    def ping() -> str:
        """Return a short response."""
        return 'pong'

    class Repeats:
        def bind_tools(self, tools):
            return self

        def invoke(self, messages):
            return AIMessage(content='', tool_calls=[{'name': 'ping', 'args': {}, 'id': str(len(messages))}])

    with pytest.raises(RuntimeError, match='limit'):
        module.run_loop(Repeats(), 'Keep going', [ping], max_steps=2)


def test_real_mcp_discovery_and_calls():
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    async def check():
        params = StdioServerParameters(command=sys.executable, args=[str(CLASSROOM / 'mcp_server.py')])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                names = {t.name for t in (await session.list_tools()).tools}
                assert names == {'find_food', 'get_canteen_hours'}
                result = await session.call_tool('find_food', {'max_price': 80, 'vegetarian': True})
                assert not result.isError
                payload = json.loads(result.content[0].text)
                assert payload == importlib.import_module('menu_tools').find_food(80)
                empty = await session.call_tool('find_food', {'max_price': 30})
                assert json.loads(empty.content[0].text)['matches'] == []
                invalid = await session.call_tool('find_food', {'max_price': -1})
                assert invalid.isError
    asyncio.run(check())


def test_agent_uses_mcp_results():
    result = asyncio.run(importlib.import_module('mcp_agent').run(offline=True))
    assert any(m.type == 'tool' and m.name == 'find_food' for m in result['messages'])
    assert 'Veg sandwich' in str(result['messages'][-1].content)


@pytest.mark.parametrize('at,route', [('12:30', ['hours', 'agent']), ('17:00', ['hours', 'closed'])])
def test_graph_routes_through_actual_mcp(at, route):
    result = asyncio.run(importlib.import_module('graph').run(offline=True, at=at))
    assert result['path'] == route
    if at == '17:00':
        assert 'closed' in result['answer'].lower()
        assert not result.get('agent_messages')
    else:
        assert 'Veg sandwich' in result['answer']


def test_real_crewai_handoff_uses_scout_context():
    result = importlib.import_module('crew').run(offline=True)
    assert result['roles'] == ['Menu scout', 'Lunch planner']
    assert 'Veg sandwich' in result['scout']
    assert 'Veg sandwich' in result['plan']
    assert '120' in result['plan']
    assert result['tool_names'] == ['find_food']


def test_crewai_cli_handles_a_legacy_windows_output_encoding():
    result = subprocess.run([sys.executable, str(CLASSROOM / 'crew.py'), '--offline'],
                            capture_output=True, encoding='utf-8', errors='replace', timeout=60,
                            env={**os.environ, 'PYTHONIOENCODING': 'cp1252'})
    assert result.returncode == 0, result.stderr
    assert 'codec can\'t encode' not in result.stdout
    assert 'SCOUT HANDOFF:' in result.stdout and 'Rs 120' in result.stdout


def test_live_crew_client_has_a_bounded_transport_without_making_a_request():
    module = importlib.import_module('crew')
    brain = module.make_live_brain('test-not-a-real-key', 'gemini-3.6-flash')
    try:
        options = brain.client._api_client._http_options
        assert options.timeout == 30000
        assert options.retry_options.attempts == 1
    finally:
        brain.client.close()


@pytest.mark.parametrize('ending_role', ['assistant', 'user'])
def test_live_crew_can_continue_after_a_tool_observation(ending_role):
    """Gemini rejects assistant-prefill requests after CrewAI's tool step."""
    from copy import deepcopy
    brain = importlib.import_module('crew').make_live_brain('test-not-a-real-key', 'gemini-3.5-flash-lite')
    messages = [
        {'role': 'system', 'content': 'Use the fictional menu.'},
        {'role': 'user', 'content': 'Find vegetarian lunch under Rs 75.'},
        {'role': ending_role, 'content': 'Observation: {"matches": [{"name": "Veg sandwich", "price": 60}]}'},
    ]
    original = deepcopy(messages)
    try:
        contents, instruction = brain._format_messages_for_gemini(messages)
        assert contents[-1].role == 'user'
        assert 'Veg sandwich' in '\n'.join(part.text or '' for item in contents for part in item.parts)
        assert instruction == 'Use the fictional menu.'
        assert messages == original
        if ending_role == 'user':
            assert len(contents) == 2  # No extra continuation on an ordinary request.
    finally:
        brain.client.close()
