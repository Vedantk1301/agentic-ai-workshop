"""Real CrewAI agents and sequential tasks, sharing the same MCP server."""
import argparse
import os
from pathlib import Path
import sys

# Rich emits Unicode event labels even when output is redirected on Windows.
if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')

# Keep this local demo free of telemetry and local state outside the project.
os.environ.setdefault('CREWAI_TELEMETRY_DISABLED', 'true')
os.environ.setdefault('OTEL_SDK_DISABLED', 'true')
os.environ.setdefault('CREWAI_TRACING_ENABLED', 'false')
os.environ.setdefault('CREWAI_STORAGE_DIR', str(Path(__file__).with_name('.crewai')))
# CrewAI 1.6.1 initializes its optional account store during import. In this
# standalone Windows demo, keep that process-local store in the ignored folder.
if sys.platform == 'win32':
    os.environ['LOCALAPPDATA'] = str(Path(__file__).with_name('.crewai').resolve())

from crewai import Agent, Crew, Process, Task
from crewai.mcp import MCPServerStdio
from crew_live import make_live_brain
from workshop_runtime import banner, configuration


def run(offline=False):
    if offline:
        from crew_brain import ScriptedCrewBrain
        scout_brain, planner_brain = ScriptedCrewBrain('scout'), ScriptedCrewBrain('planner')
    else:
        key, model = configuration()
        if not key:
            raise RuntimeError('Configure your private key or use --offline for a scripted rehearsal.')
        scout_brain = make_live_brain(key, model)
        planner_brain = make_live_brain(key, model)
    scout = Agent(role='Menu scout', goal='Get available vegetarian options within Rs 75 per person.',
                  backstory='You read the fictional canteen using its MCP tool.', llm=scout_brain,
                  allow_delegation=False, max_iter=4, max_retry_limit=0, verbose=False)
    # Native discovery prefixes tool names with full Windows command paths.
    # Keep a short model-facing alias; native tools retain their original MCP name.
    discovered = scout.get_mcp_tools([MCPServerStdio(command=sys.executable,
                         args=[str(Path(__file__).with_name('mcp_server.py').resolve())])])
    for discovered_tool in discovered:
        discovered_tool.name = discovered_tool.original_tool_name
    scout.tools = [t for t in discovered if t.name == 'find_food']
    planner = Agent(role='Lunch planner', goal='Propose lunch for two vegetarians within Rs 150 total.',
                    backstory='You use the menu scout findings and calculate the group total.',
                    llm=planner_brain, allow_delegation=False, max_iter=3, max_retry_limit=0, verbose=False)
    lookup = Task(description='Call find_food with max_price 75 and vegetarian true. Return its actual JSON result.',
                  expected_output='The actual menu result, including names and prices.', agent=scout)
    plan = Task(description='Use only the scout result. Choose one available item each for two vegetarians. '
                            'State the item, quantity, unit price and total within Rs 150. No ordering.',
                expected_output='A short group lunch proposal and total.', agent=planner, context=[lookup])
    team = Crew(agents=[scout, planner], tasks=[lookup, plan], process=Process.sequential,
                memory=False, cache=False, verbose=False, tracing=False)
    team.kickoff()
    return {'roles': [scout.role, planner.role], 'scout': lookup.output.raw, 'plan': plan.output.raw,
            'tool_names': [t.name for t in scout.tools]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--offline', action='store_true')
    args = parser.parse_args()
    banner(args.offline, 'real CrewAI tasks / MCP stdio tools')
    result = run(args.offline)
    print('SCOUT HANDOFF:', result['scout'])
    print('PLANNER:', result['plan'])
