# Build your first AI agent

A canteen helper that finds lunch within your budget, checks whether the canteen is open, and shows you every step it took. About 30 lines of your own Python.

| Step | What you do | When |
| --- | --- | --- |
| [0. Set up](#0-set-up-once) | Create the Python environment and your folder | Once, before class |
| [1. A tool](#1-a-tool-is-just-a-function) | Write a plain Python function | In class |
| [2. An agent](#2-give-the-tool-to-an-ai-model) | Hand that function to an AI model | In class |
| [3. Your turn](#3-your-turn-add-a-second-ability) | Give the agent a second ability | In class |
| [4. MCP](#4-mcp-the-same-tools-through-a-standard-plug) | See tools shared through a standard plug | Watch |
| [5. LangGraph and CrewAI](#5-langgraph-and-crewai) | See a workflow and a two-agent team | Watch |
| [6. Next steps](#6-after-class) | Tidy your project and keep building | After class |

> **Copy, don't type.** Every code block below is a complete file or a complete change. Copy it, paste it, then read the explanation under it.
>
> **Two commands for everything.** Use the **Windows** one in PowerShell (VS Code's default terminal on Windows), or the **macOS / Linux** one in Terminal.

---

## 0. Set up once

### 0a. Create the environment

Open a terminal **in the repository folder** (`agentic-ai-workshop`). Check you have Python 3.11 or newer:

Windows:

```powershell
py --version
```

macOS / Linux:

```sh
python3 --version
```

Create a private environment called `.venv` and install the packages. This takes two to three minutes, so do it before class if you can.

Windows:

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

macOS / Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

> **No need to "activate" anything.** We call the environment's Python directly through a shortcut (next step), which also avoids PowerShell permission errors.

### 0b. Make a `$py` shortcut and create your folder

`$py` (Windows) or `$PY` (macOS / Linux) is a shortcut that always means "the Python inside `.venv`". Every command in this guide uses it.

Windows:

```powershell
$py = (Resolve-Path .venv\Scripts\python.exe).Path
& $py classroom/check_setup.py
& $py tools/start_here.py
Set-Location your_agent
```

macOS / Linux:

```sh
PY="$(pwd)/.venv/bin/python"
"$PY" classroom/check_setup.py
"$PY" tools/start_here.py
cd your_agent
```

You should see a list of library versions, `Local menu and mock hours: OK`, and `Created: ...your_agent`. Your terminal is now **inside `your_agent/`**. Stay there for the whole workshop.

> **Opened a new terminal later?** The shortcut only lives in the terminal where you made it. From inside `your_agent/`, make it again:
>
> Windows: `$py = (Resolve-Path ..\.venv\Scripts\python.exe).Path`
>
> macOS / Linux: `PY="$(cd .. && pwd)/.venv/bin/python"`

### What's in `your_agent/`

| File | Who writes it | Its job |
| --- | --- | --- |
| `data/menu.json` | provided | The four fictional menu items. Facts live here, not in the model. |
| `workshop_runtime.py` | provided | Builds the model (scripted or live Gemini) and prints every step of a run. |
| `offline_brain.py` | provided | The scripted stand-in used when `OFFLINE = True`. Not real AI. |
| `mcp_connection.py` | provided | Starts an MCP server and connects to it (Step 4). |
| `menu_tools.py` | **you**, Step 1 | Your tools: plain Python functions. |
| `my_agent.py` | **you**, Step 2 | Your agent: model + tools + instructions + loop. |

Finished versions of every step live in `classroom/`. They're there to rescue you if you're stuck, not to copy before trying.

---

## 1. A tool is just a function

Create **`menu_tools.py`** in `your_agent/` and paste this whole file:

```python
import json
from datetime import datetime
from pathlib import Path

MENU = json.loads((Path(__file__).parent / "data" / "menu.json").read_text(encoding="utf-8"))


def find_food(max_price: int, vegetarian: bool = True) -> dict:
    """Find available food within a per-person rupee budget. True means vegetarian only."""
    if type(max_price) is not int or max_price < 0:
        raise ValueError('max_price must be a nonnegative whole number')
    if type(vegetarian) is not bool:
        raise ValueError('vegetarian must be true or false')
    matches = []
    for dish in MENU:
        if not dish['available'] or dish['price'] > max_price:
            continue
        if vegetarian and not dish['vegetarian']:
            continue
        matches.append({'name': dish['name'], 'price': dish['price']})
    return {'status': 'ok', 'matches': matches}


if __name__ == "__main__":
    # Runs only when you run this file directly, never when my_agent.py imports it.
    print(find_food(80))
```

Run it.

Windows:

```powershell
& $py menu_tools.py
```

macOS / Linux:

```sh
"$PY" menu_tools.py
```

You should see:

```text
{'status': 'ok', 'matches': [{'name': 'Veg sandwich', 'price': 60}]}
```

**What's happening.** No AI yet, just ordinary Python:

- `MENU` loads the four dishes from `data/menu.json`.
- The two `raise ValueError` lines refuse bad input, such as a negative budget. A tool should protect itself.
- The two `continue` lines are the rules: skip anything sold out or over budget, and skip non-veg if you asked for veg.
- It returns plain data, not a sentence. The model will write the sentence later.
- `if __name__ == "__main__":` runs the test print only when you run this file directly. When `my_agent.py` imports it later, it stays silent. Keep that block at the bottom.

> **Try this (one minute each)**
>
> - Change the print to `find_food(30)`. You get `'matches': []`. That's a correct answer ("I checked, nothing fits"), not an error.
> - Try `find_food(80, vegetarian=False)`. The Chicken roll appears next to the sandwich, because `False` means "veg not required", not "non-veg only".
> - Try `find_food(-5)`. The input check stops it with a clear message.

---

## 2. Give the tool to an AI model

Create **`my_agent.py`** in `your_agent/` and paste this whole file:

```python
from langchain.agents import create_agent
from langchain_core.tools import tool
from menu_tools import find_food
from workshop_runtime import make_model, banner, show_messages

OFFLINE = True  # Scripted rehearsal. False uses your configured live Gemini.
banner(OFFLINE)
agent = create_agent(
    model=make_model(OFFLINE),
    tools=[tool(find_food)],
    system_prompt="Use the menu tool for facts. Respect budget and diet.",
)
result = agent.invoke(
    {"messages": [("user", "Find vegetarian lunch under Rs 80.")]},
    {"recursion_limit": 10},
)
show_messages(result)
```

Run it.

Windows:

```powershell
& $py my_agent.py
```

macOS / Linux:

```sh
"$PY" my_agent.py
```

You should see:

```text
BRAIN: SCRIPTED REHEARSAL (not a real AI)
TOOLS: local functions
YOU: Find vegetarian lunch under Rs 80.
MODEL REQUEST: find_food {'max_price': 80, 'vegetarian': True}
RESULT find_food: {"status": "ok", "matches": [{"name": "Veg sandwich", "price": 60}]}
ANSWER: Veg sandwich (Rs 60)
```

**How to read it.**

| Line | Meaning |
| --- | --- |
| `YOU:` | Your question, sent to the model. |
| `MODEL REQUEST:` | The model **asks** for a tool by name, with arguments. It runs nothing itself. |
| `RESULT find_food:` | **Your Python** ran the function. This is the real data. |
| `ANSWER:` | The model's reply, written from those results. |

**The model asks. Your code does.** That's the most important idea of the workshop.

**What's happening.**

- `create_agent` builds the think, act, observe loop for you.
- `tool(find_food)` wraps your function. The model sees its name, its arguments and its **docstring**, so the docstring is a prompt: it tells the model when to use the tool.
- `system_prompt` is the agent's job description. Also a prompt.
- `recursion_limit` is a safety stop so the loop can't run forever.
- `OFFLINE = True` uses a **scripted brain**: LangChain and your tool run for real, but the decisions are pre-written, so it works without an API key. It is not real AI. To use live Gemini, add your own key (see `docs/SETUP.md`) and set `OFFLINE = False`.

> **Try this**
>
> - Ask `"Find non-vegetarian lunch under Rs 80."` and look at the arguments in `MODEL REQUEST`.
> - With a live model, run the same question with `OFFLINE = True` and then `False`. Same tool, same data, but the live model writes its own sentence.

---

## 3. Your turn: add a second ability

Three small changes. You will **not** write any `if` statement that decides when to call the new tool. You just give the model another tool.

**Change 1.** In `menu_tools.py`, paste this function **above** the `if __name__ == "__main__":` block:

```python
def get_canteen_hours(at: str = '12:30') -> dict:
    """Read fictional hours at a mock time. Default 12:30; not a live clock."""
    now = datetime.strptime(at, '%H:%M').time()
    opens = datetime.strptime('09:00', '%H:%M').time()
    closes = datetime.strptime('16:00', '%H:%M').time()
    return {'opens': '09:00', 'closes': '16:00', 'now': at,
            'open_now': opens <= now < closes, 'mock_clock': True}
```

**Changes 2 and 3.** In `my_agent.py`, replace these three lines (they are in different places in the file):

```python
from menu_tools import find_food, get_canteen_hours

tools=[tool(find_food), tool(get_canteen_hours)],

{"messages": [("user", "Find vegetarian lunch under Rs 80 and check opening hours.")]},
```

Run it again (same command as Step 2). You should now see **two** `MODEL REQUEST` lines and an answer like:

```text
ANSWER: Veg sandwich (Rs 60) Canteen open at mock time 12:30; closes 16:00.
```

> **Try this**
>
> - Change the budget to Rs 30. The right answer is "nothing available". Check it doesn't invent a dish.
> - With a live model, ask only `"Is the canteen open?"`. It calls **only** the hours tool. The offline script checks the menu first anyway, because it follows fixed rules. That difference is exactly what "the model decides" means.
> - Ask for non-veg lunch. The tool only knows `vegetarian=True` (veg only) or `False` (anything), so the model has to filter in its answer. A better tool would take `diet="veg"`, `"non-veg"` or `"any"`. Good tools make the model's job easy.

Stuck? The finished version is `classroom/agent.py`.

---

## 4. MCP: the same tools through a standard plug

**In class, just watch.** The instructor runs this on screen.

Your `find_food` only works inside your own program. **MCP** (Model Context Protocol) is a standard plug for tools, like USB-C. You put your functions behind a small **MCP server**, and any MCP-aware app (LangChain, LangGraph, CrewAI, Claude Desktop, Cursor) can discover and call them without rewriting them. The server has no model and makes no decisions; it only offers tools.

To run the ready-made demos yourself, stay in `your_agent/`.

Windows:

```powershell
& $py ../classroom/mcp_probe.py
& $py ../classroom/mcp_agent.py --offline
```

macOS / Linux:

```sh
"$PY" ../classroom/mcp_probe.py
"$PY" ../classroom/mcp_agent.py --offline
```

The first prints `DISCOVERED: find_food, get_canteen_hours` and a real tool result, with no AI involved. The second is your agent again, with its tools arriving through MCP. **The tools didn't change; only how they're connected.**

<details>
<summary><b>After class: build your own MCP server (optional)</b></summary>

In `your_agent/`, create two files. You never start the server yourself; `mcp_connection.py` launches it in the background when a client needs it.

**`mcp_server.py`**, the server. It registers your existing functions, unchanged:

```python
"""Local MCP server: the SAME two functions, exposed over stdio."""
from mcp.server.fastmcp import FastMCP
from menu_tools import find_food, get_canteen_hours

server = FastMCP('Campus Canteen')
server.tool()(find_food)
server.tool()(get_canteen_hours)

if __name__ == '__main__':
    server.run(transport='stdio')
```

Keep the name exactly `mcp_server.py`, and never add `print` to it: the server talks through standard output, and a stray print corrupts the messages.

**`probe.py`**, a tiny client that starts your server, lists its tools and calls one:

```python
import asyncio
from mcp_connection import connected_tools
from workshop_runtime import payload

async def main():
    async with connected_tools() as tools:          # starts mcp_server.py for you
        print([t.name for t in tools])               # the tools the server offers
        food = next(t for t in tools if t.name == "find_food")
        result = await food.ainvoke({"max_price": 80, "vegetarian": True})
        print(payload(result))                       # MCP replies as text; payload() turns it into a dict

asyncio.run(main())
```

Run it with `& $py probe.py` (Windows) or `"$PY" probe.py` (macOS / Linux). Expect `['find_food', 'get_canteen_hours']` and the sandwich record. Lines starting with `INFO` are the server's logs; ignore them.

To connect an agent to your server, read `classroom/mcp_agent.py`: it's your Step 2 agent, with tools from `connected_tools()` instead of `tool(find_food)`.

</details>

---

## 5. LangGraph and CrewAI

**In class, just watch.** These show the same canteen built two other ways.

### LangGraph: a workflow where code picks the route

Windows:

```powershell
& $py ../classroom/graph.py --offline
& $py ../classroom/graph.py --offline --at 17:00
```

macOS / Linux:

```sh
"$PY" ../classroom/graph.py --offline
"$PY" ../classroom/graph.py --offline --at 17:00
```

At 12:30 you get `ROUTE: hours -> agent`; at 17:00, `ROUTE: hours -> closed`, and the model is never called. Three words explain LangGraph:

| Word | Meaning | In our graph |
| --- | --- | --- |
| **State** | The information carried from step to step | the question, the hours, the answer |
| **Node** | One step, a plain Python function | `hours`, `agent`, `closed` |
| **Edge** | Which step comes next | `START → hours`, then a code check: open → `agent`, closed → `closed` |

"Is it open?" is a fixed rule, so **code** decides it. The agent sits *inside* the graph for the part that needs judgement. Read `classroom/graph.py`; the comments mark state, nodes and edges.

### CrewAI: two agents with a handoff

The instructor runs `classroom/crew.py`. CrewAI is an instructor-only install (`requirements-instructor.txt`, Python 3.11 to 3.13), so students just watch.

| Word | Meaning | In our crew |
| --- | --- | --- |
| **Agent** | A role with a goal and its own tools | "Menu scout" (uses `find_food`) and "Lunch planner" |
| **Task** | One job given to one agent | find options; plan lunch for two within Rs 150 |
| **Crew** | The team that runs the tasks in order | the scout's result is handed to the planner |

The planner proposes 2 × Veg sandwich = Rs 120. Ask yourself: did this small job really need two agents?

---

## 6. After class

**Keep your project understandable.** Add a short `README.md` (what it does, how to run it) and an `AGENTS.md` that coding assistants read:

```markdown
# Canteen project rules
- Use data/menu.json for menu facts.
- Explain each proposed change before editing.
- Run the changed behavior and report what was actually tested.
- Keep API keys out of code and commits.
```

**Keep building.** Pick one:

- Give the agent a `diet` argument (`veg`, `non-veg`, `any`) or a tool that returns the canteen's location.
- Swap `data/menu.json` for your hostel mess menu or your timetable.
- Read `classroom/manual_loop.py`: the whole agent loop in about 20 lines, with no framework hiding it.

**Take-home guide:** [docs/PROMPTING_AND_PROJECT_FILES.md](../docs/PROMPTING_AND_PROJECT_FILES.md) covers writing good system prompts, tool descriptions, and README and AGENTS.md files.

---

## Stuck?

| You see | Do this |
| --- | --- |
| `Cannot find path ...\.venv\Scripts\python.exe` | Step 0a was skipped. Create the environment, then redo Step 0b. |
| `The expression after '&' ... was not valid` | `$py` isn't set in this terminal. See "Opened a new terminal later?" in Step 0b. |
| `can't open file ...your_agent\classroom\...` | Add `../` in front: `../classroom/name.py`. |
| `No module named 'menu_tools'` | Run the command from inside `your_agent/`, where `menu_tools.py` lives. |
| `No Gemini key found` | Set `OFFLINE = True` in `my_agent.py`, or add your own key (`docs/SETUP.md`). |
| `CrewAI is not installed in this Python` | Expected for students. Watch the instructor's demo instead. |
| Anything else | Open the finished version in `classroom/` and compare, or ask a volunteer. More fixes are in `docs/TROUBLESHOOTING.md`. |
