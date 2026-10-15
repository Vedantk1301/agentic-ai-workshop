"""Five actual offline CLI checks. No API key, network or .env reads are required."""
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]

def run(script,*args):
    p=subprocess.run([sys.executable,'-B',str(ROOT/script),'--offline',*args],cwd=ROOT,
                     capture_output=True,text=True,encoding='utf-8',timeout=45)
    if p.returncode:
        raise RuntimeError(p.stdout+'\n'+p.stderr)
    return p.stdout

def require(condition,label):
    if not condition:raise AssertionError(label)
    print('PASS:',label,flush=True)

def main():
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
