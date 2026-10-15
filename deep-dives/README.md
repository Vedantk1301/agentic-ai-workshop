# Optional implementations and deeper study

Finish the [starter](../starter/README.md) first. This folder preserves the complete workshop examples. It is intentionally broader than the live session.

| Example | What problem it addresses | What to inspect |
| --- | --- | --- |
| 01 fixed workflow | A known, simple order of work | Functions, original constraints and failed lookups |
| 02 ReAct-style agent | Flexible selection among allowed tools | Tool requests, observations and step limits |
| 03 graph | Explicit routes, state and bounded retries | Missing input and timeout paths |
| 04 agent within graph | Unsupported model output reaching a user | Actual tool evidence, query coverage and final text |
| 05 role team | Coordinating menu and policy responsibilities | Whether a team is justified; honest unavailable policy |

Run from the repository root with the root environment:

```powershell
.venv\Scripts\python deep-dives/demo/03_langgraph_flow.py --scenario menu_flaky
.venv\Scripts\python deep-dives/demo/04_graph_with_agent.py --offline --inject-mistake fake_dish
.venv\Scripts\python deep-dives/demo/04_graph_with_agent.py --offline --inject-mistake free_text
.venv\Scripts\python deep-dives/demo/05_team_of_roles.py --scenario policy_unavailable
```

Use .venv/bin/python on macOS/Linux. Demos 01/03/05 need no model; 02/04 support --offline or optional configured Gemini. Injected mistakes are simulated. Demo 05 is plain Python, not a live CrewAI deployment.

Continue with [the guided lab](learning_lab/AI%20Coding%20Lab.md), [exercises and solutions](demo/exercises/README.md), [study guide](guides/Agentic%20AI%20Study%20Guide.md), [practice and answers](guides/Practice%20and%20Answer%20Key.md) or [full reference slides](Full%20Reference%20Deck.pdf).

The preserved lab uses paths relative to this older demo/ layout. When following it literally, enter deep-dives/demo; the shared root interpreter is ../../.venv/Scripts/python on Windows or ../../.venv/bin/python on macOS/Linux. Alternatively use the root commands above. Its old timetable/reference slides are superseded by the current 31-slide classroom deck.

The preserved Classroom Follow Along and review PDF describe an older lesson layout. Use starter/README.md for the current individual-work lesson, five room checkpoints and optional sharing. Instructor guidance is in [ROOM_GUIDE](../docs/ROOM_GUIDE.md).
