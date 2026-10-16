"""One useful graph branch; the open branch contains the familiar agent."""
import argparse
import asyncio
from typing import TypedDict

from langchain.agents import create_agent
from langgraph.graph import END, START, StateGraph

from mcp_connection import connected_tools
from workshop_runtime import banner, make_model, payload


class State(TypedDict, total=False):
    question: str
    hours: dict
    answer: str
    path: list[str]
    agent_messages: list


async def run(offline=False, at='12:30'):
    async with connected_tools() as tools:
        by_name = {tool.name: tool for tool in tools}
        lunch_agent = create_agent(make_model(offline), [by_name['find_food']],
                                  system_prompt='Find food using the tool. Respect budget and diet.')

        async def hours(state):
            result = await by_name['get_canteen_hours'].ainvoke({'at': at})
            return {'hours': payload(result), 'path': ['hours']}

        def choose(state):
            return 'agent' if state['hours']['open_now'] else 'closed'

        async def agent(state):
            result = await lunch_agent.ainvoke({'messages': [('user', state['question'])]}, {'recursion_limit': 10})
            return {'answer': str(result['messages'][-1].text),
                    'agent_messages': result['messages'], 'path': state['path'] + ['agent']}

        def closed(state):
            return {'answer': f"Canteen closed at mock time {state['hours']['now']}. No menu lookup needed.",
                    'path': state['path'] + ['closed']}

        flow = StateGraph(State)
        flow.add_node('hours', hours)
        flow.add_node('agent', agent)
        flow.add_node('closed', closed)
        flow.add_edge(START, 'hours')
        flow.add_conditional_edges('hours', choose, {'agent': 'agent', 'closed': 'closed'})
        flow.add_edge('agent', END)
        flow.add_edge('closed', END)
        return await flow.compile().ainvoke({'question': 'Find vegetarian lunch under Rs 80.'})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--at', default='12:30', help='Mock clock, HH:MM')
    args = parser.parse_args()
    banner(args.offline, 'MCP / stdio')
    result = asyncio.run(run(args.offline, args.at))
    print('ROUTE:', ' -> '.join(result['path']))
    print('ANSWER:', result['answer'])
