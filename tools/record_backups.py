"""Capture actual scripted rehearsals. These are text outputs, not videos."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'classroom/saved_runs'
RUNS = {
    'tools': ['menu_tools.py'],
    'agent': ['agent.py', '--offline'],
    'agent-budget30': ['agent.py', '--offline', '--question', 'Find vegetarian lunch under Rs 30 and check hours.'],
    'mcp-probe': ['mcp_probe.py'],
    'mcp-agent': ['mcp_agent.py', '--offline'],
    'graph-open': ['graph.py', '--offline'],
    'graph-closed': ['graph.py', '--offline', '--at', '17:00'],
    'crew': ['crew.py', '--offline'],
    'manual-loop': ['manual_loop.py', '--offline'],
    'safety': ['safety_demo.py'],
}

if __name__ == '__main__':
    DEST.mkdir(parents=True, exist_ok=True)
    for name, args in RUNS.items():
        command = [sys.executable, str(ROOT / 'classroom' / args[0]), *args[1:]]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
                                errors='replace', timeout=90, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})
        if result.returncode:
            raise RuntimeError(f'{name} failed with exit {result.returncode}: {result.stderr[-1500:]}')
        text = ('# Actual captured local run\n# Mode: scripted brain or no model; not a live Gemini run.\n'
                '# Command: python classroom/' + ' '.join(args) + '\n\n' + result.stdout)
        (DEST / (name + '.txt')).write_text(text, encoding='utf-8')
        print('Captured:', name, flush=True)
