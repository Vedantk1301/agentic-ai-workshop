"""The new-file route must be usable outside the repository, including spaces."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def test_fresh_workspace_is_safe_and_has_only_support(tmp_path):
    destination = tmp_path / 'My first agent'
    result = subprocess.run([sys.executable, str(ROOT / 'tools/start_here.py'), str(destination)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (destination / 'data/menu.json').is_file()
    assert not (destination / 'menu_tools.py').exists()
    assert not (destination / 'my_agent.py').exists()
    assert not (destination / '.env').exists()
    repeated = subprocess.run([sys.executable, str(ROOT / 'tools/start_here.py'), str(destination)],
                              capture_output=True, text=True)
    assert repeated.returncode != 0
    assert 'overwrite' in repeated.stderr.lower()


def test_checkpoint_files_run_in_a_fresh_workspace(tmp_path):
    import shutil
    destination = tmp_path / 'Agent with spaces'
    result = subprocess.run([sys.executable, str(ROOT / 'tools/start_here.py'), str(destination)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    shutil.copy2(ROOT / 'classroom/menu_tools.py', destination / 'menu_tools.py')
    shutil.copy2(ROOT / 'classroom/first_agent_checkpoint.py', destination / 'my_agent.py')
    direct = subprocess.run([sys.executable, 'menu_tools.py'], cwd=destination, capture_output=True, text=True)
    assert direct.returncode == 0, direct.stderr
    assert 'Veg sandwich' in direct.stdout
    agent = subprocess.run([sys.executable, 'my_agent.py', '--offline'], cwd=destination,
                           capture_output=True, text=True, timeout=40)
    assert agent.returncode == 0, agent.stderr
    assert 'SCRIPTED' in agent.stdout and 'Veg sandwich' in agent.stdout
    assert 'get_canteen_hours' not in agent.stdout
    shutil.copy2(ROOT / 'classroom/agent.py', destination / 'my_agent.py')
    extended = subprocess.run([sys.executable, 'my_agent.py', '--offline'], cwd=destination,
                             capture_output=True, text=True, timeout=40)
    assert extended.returncode == 0, extended.stderr
    assert '16:00' in extended.stdout
    shutil.copy2(ROOT / 'classroom/mcp_server.py', destination / 'mcp_server.py')
    shutil.copy2(ROOT / 'classroom/mcp_probe.py', destination / 'probe.py')
    probe = subprocess.run([sys.executable, 'probe.py'], cwd=destination, capture_output=True,
                          text=True, timeout=40)
    assert probe.returncode == 0, probe.stderr
    assert 'find_food' in probe.stdout and 'Veg sandwich' in probe.stdout
