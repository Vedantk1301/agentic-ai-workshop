# Build your first AI agent

A hands-on workshop for beginners at VIT Mumbai, 17 October 2026, 13:30-15:00 IST, Lab 05. You build a small canteen helper agent in about 30 lines of Python, give it a second tool, then see the same tools through MCP, LangGraph and CrewAI.

> ## 👉 Start here: [classroom/README.md](classroom/README.md)
>
> That page is the whole lesson: setup, then every step with copy-paste code, expected output and commands for **Windows** and **macOS / Linux**.

## Before class (10 minutes)

**1. Install Python 3.11 or newer** from [python.org](https://www.python.org/downloads/), plus an editor such as VS Code.

**2. Get the code.** Either:

- `git clone https://github.com/Vedantk1301/agentic-ai-workshop`
- or the green **Code** button on this page → **Download ZIP**, then extract it (no GitHub account or Git needed).

**3. Do Step 0 of [classroom/README.md](classroom/README.md).** It installs the packages, which is slow when the whole lab does it at once on the same Wi-Fi.

No API key is needed. Everything runs in offline mode, and a free Gemini key is optional ([docs/SETUP.md](docs/SETUP.md)).

## What's in here

| Folder | What it is |
| --- | --- |
| [classroom/](classroom/README.md) | **The lesson**, plus finished versions of every step in case you get stuck |
| [docs/](docs/) | Setup help, [troubleshooting](docs/TROUBLESHOOTING.md) and the take-home [prompting and project files guide](docs/PROMPTING_AND_PROJECT_FILES.md) |
| [slides/](slides/) | The curriculum, speaker script and run sheet |
| starter/, solutions/, deep-dives/ | Optional advanced material from an earlier edition |

<details>
<summary><b>For the instructor</b></summary>

CrewAI needs Python 3.11 to 3.13, so it is an instructor-only install. Students watch that demo.

Windows:

```powershell
.venv\Scripts\python -m pip install -r requirements-instructor.txt
.venv\Scripts\python classroom/crew.py --offline
```

macOS / Linux:

```sh
.venv/bin/python -m pip install -r requirements-instructor.txt
.venv/bin/python classroom/crew.py --offline
```

Verify the kit (Windows; use `.venv/bin/python` on macOS / Linux):

```powershell
.venv\Scripts\python tools/verify_workshop.py
.venv\Scripts\python -m pytest classroom/tests deep-dives/demo/tests -q -p no:cacheprovider
```

The full suite includes CrewAI; add `-k "not crew"` for the core suite. `--offline` means a labelled scripted model makes the decisions while the real framework and tool code runs. Offline checks don't prove the live model works or has quota. The menu and clock are fictional; no orders or payments happen.

</details>
