# Build your first AI agent

A guided VIT Mumbai workshop for beginners, 17 October 2026, 13:30-15:00 IST, Lab 05. Build a small canteen agent, add a tool, reuse the tools through MCP, then compare LangChain, LangGraph and CrewAI.

**Start with classroom/README.md.** Students write their application in a fresh folder; completed classroom files are checkpoints and instructor examples. The older starter/ and deep-dives/ material is optional advanced reference.

## Install before class

Install Python 3.11 and one editor. An AI coding editor is optional. Clone this repository or extract the supplied ZIP. While private, a GitHub link requires authorised access; the organiser can distribute the ZIP directly.

Windows PowerShell, repository root:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python classroom/check_setup.py
```

If the py launcher is unavailable, use python -m venv .venv after checking python --version is 3.11. For an existing valid workshop interpreter, use its full path rather than reinstalling Python.

macOS/Linux:

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python classroom/check_setup.py
```

Follow [the new-file lesson](classroom/README.md). start_here.py creates your_agent/ with data and setup/fallback support, without a finished agent. It refuses to overwrite a nonempty folder.

## Run the checkpoints

Windows, repository root:

```powershell
.venv\Scripts\python classroom/menu_tools.py
.venv\Scripts\python classroom/agent.py --offline
.venv\Scripts\python classroom/mcp_probe.py
.venv\Scripts\python classroom/mcp_agent.py --offline
.venv\Scripts\python classroom/graph.py --offline --at 17:00
```

Use .venv/bin/python on macOS/Linux. --offline means a labelled rule script supplies model decisions while real framework/tool code runs. MCP probe has no model at all. Remove --offline only after privately configuring and testing live Gemini; see [setup](docs/SETUP.md). Free-tier access and quota vary.

The presenter installs requirements-instructor.txt for the real CrewAI example:

```powershell
.venv\Scripts\python -m pip install -r requirements-instructor.txt
.venv\Scripts\python classroom/crew.py --offline
```

CrewAI is optional for students and has a heavier dependency set. The demo is an actual sequential crew; its offline model is scripted. A sequential handoff is different from a manager selecting workers and does not implement A2A automatically.

## Where to go

| Material | Purpose |
| --- | --- |
| [Classroom lesson](classroom/README.md) | Write a tool, build one agent, add hours and call MCP |
| [Slides](slides/Agentic%20AI%20in%20Practice.pdf) | Short explanations and activity prompts |
| [Speaker script](slides/Speaker%20Script.md) and [run sheet](slides/Live%20Run%20Sheet.md) | Exact slide/editor switches and commands |
| [Curriculum](slides/Curriculum.md) | Two-hour teaching sequence and scope |
| [Setup](docs/SETUP.md), [room guide](docs/ROOM_GUIDE.md) | Installation, access and large-room support |
| [Learning path](docs/LEARNING_PATH.md) | Manual loop, patterns, project habits and advanced material |
| classroom/saved_runs/ | Actual captured offline runs, labelled with their mode |

## Verify the kit

```powershell
.venv\Scripts\python tools/verify_workshop.py
.venv\Scripts\python -m pytest classroom/tests deep-dives/demo/tests -q -p no:cacheprovider
```

The full classroom suite includes CrewAI; install instructor requirements first. Use -k "not crew" for the core suite. Local tools and MCP work without keys. Offline checks do not establish live model availability or quota. The records and clock are fictional; no orders or payments occur.
