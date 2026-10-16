"""Current classroom and previous reference CLI checks, without an API key."""
import argparse
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]

def run(script,*args,offline=True):
    flags=['--offline'] if offline else []
    p=subprocess.run([sys.executable,'-B',str(ROOT/script),*flags,*args],cwd=ROOT,
                     capture_output=True,text=True,encoding='utf-8',timeout=45)
    if p.returncode:
        raise RuntimeError(p.stdout+'\n'+p.stderr)
    return p.stdout

def require(condition,label):
    if not condition:raise AssertionError(label)
    print('PASS:',label,flush=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--with-crew',action='store_true')
    args=parser.parse_args()
    require('Veg sandwich' in run('classroom/menu_tools.py',offline=False),'new lesson: ordinary menu function')
    require('16:00' in run('classroom/agent.py'),'new lesson: model loop with two tools')
    require('Veg sandwich' in run('classroom/mcp_probe.py',offline=False),'new lesson: actual MCP discovery and call')
    require('Veg sandwich' in run('classroom/mcp_agent.py'),'new lesson: MCP agent')
    require('hours -> closed' in run('classroom/graph.py','--at','17:00'),'new lesson: graph closed branch')
    if args.with_crew:
        require('Rs 120' in run('classroom/crew.py'),'new lesson: real CrewAI handoff with scripted brains')
    original=run('starter/agent.py')
    require('Veg sandwich' in original and '16:00' in original,'starter: Rs80 finds sandwich and hours')
    worked=run('solutions/budget-30/agent.py')
    require('Nothing vegetarian under Rs 30' in worked and '16:00' in worked,'solution: Rs30 has no match; hours unchanged')
    sold=run('starter/agent.py','--scenario','sold_out')
    require('Nothing vegetarian under Rs 80' in sold,'sold out: successful empty lookup')
    failed=run('starter/agent.py','--scenario','menu_timeout')
    require("couldn't reach the menu" in failed,'timeout: report unavailable information')
    guarded=run('deep-dives/demo/04_graph_with_agent.py','--inject-mistake','free_text')
    answer=guarded.rsplit('ANSWER:',1)[-1]
    require('MODEL PROPOSAL' in guarded and 'Paneer Tikka Wrap' in guarded
            and 'Paneer Tikka Wrap' not in answer and '22:00' not in answer
            and 'Rs 60' in answer and '16:00' in answer,'graph: invented message does not reach final answer')

if __name__=='__main__':main()
