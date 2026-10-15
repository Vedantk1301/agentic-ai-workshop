"""Execute the documented graph solution against the real example functions."""
import importlib.util
import re
import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize("scenario,question,expected_route,expected_calls", [
    ("after_hours", "veg lunch under Rs 80, is it open?", ["read_request", "check_hours", "closed_answer"], 0),
    ("normal", "veg lunch under Rs 80, is it open?", ["read_request", "check_hours", "search_menu", "verify", "answer"], 1),
    ("normal", "veg lunch please", ["read_request", "ask_for_budget"], 0),
])
def test_documented_closed_shortcut(scenario, question, expected_route, expected_calls, monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.setenv("SCENARIO", scenario)
    monkeypatch.setenv("DEMO_TIME", "12:30")
    spec = importlib.util.spec_from_file_location("exercise_graph", root / "03_langgraph_flow.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    solution = (root / "exercises/solutions.md").read_text(encoding="utf-8").split("## 3. Closed shortcut", 1)[1]
    code = re.search(r"```python\n(.*?)```", solution, re.S).group(1)
    exec(compile(code, "documented exercise 3", "exec"), vars(module))
    real_search, calls = module.tools.find_food, []

    def counted_search(*args, **kwargs):
        calls.append(args)
        return real_search(*args, **kwargs)

    monkeypatch.setattr(module.tools, "find_food", counted_search)
    result = module.run(question)
    assert result["path"] == expected_route
    assert len(calls) == expected_calls
    if scenario == "after_hours":
        assert "Closed now" in result["answer"] and "09:00" in result["answer"]
