"""Create a learner folder with setup support, data and no completed agent."""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'classroom'


def create(destination):
    destination = Path(destination).resolve()
    if destination.exists() and any(destination.iterdir()):
        raise ValueError('Refusing to overwrite a nonempty learner folder. Choose a new folder.')
    destination.mkdir(parents=True, exist_ok=True)
    for name in ['workshop_runtime.py', 'offline_brain.py', 'mcp_connection.py', '.env.example']:
        shutil.copy2(SOURCE / name, destination / name)
    shutil.copytree(SOURCE / 'data', destination / 'data', dirs_exist_ok=True)
    (destination / 'README.md').write_text(
        '# Your first agent\n\nStart with classroom/README.md in the downloaded kit. '
        'Create menu_tools.py, then my_agent.py yourself. The provided files supply configuration, '
        'a labelled scripted fallback, a local MCP connection and fictional data. '
        'They do not contain your completed agent.\n', encoding='utf-8')
    print('Created:', destination)
    print('Next: create menu_tools.py in this folder and follow classroom/README.md.')


if __name__ == '__main__':
    try:
        create(sys.argv[1] if len(sys.argv) > 1 else ROOT / 'your_agent')
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
