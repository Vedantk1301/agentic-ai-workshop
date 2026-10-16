# Build your first canteen agent

Start here during class. You will create your own menu function and agent, then add a second tool. LangGraph and CrewAI are short instructor demonstrations after the build.

## 0. Prepare before class

Install Python 3.11 or newer and an editor. An AI coding editor is optional. The core dependency file includes local MCP support; CrewAI is an optional instructor installation.

**First, once:** create the `.venv` environment and install the packages. Skip this only if you already did it from the root README. Windows PowerShell, from the repository root:

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

On macOS/Linux use `python3 -m venv .venv` and `.venv/bin/python -m pip install -r requirements.txt`. If you later see "Cannot find path ...\.venv\Scripts\python.exe", this step was skipped.

**Then** set up your learner folder. Windows PowerShell, from the repository root:

```powershell
$py = (Resolve-Path .venv\Scripts\python.exe).Path
& $py classroom/check_setup.py
& $py tools/start_here.py
Set-Location your_agent
```

macOS/Linux, from the repository root:

```sh
PY="$(pwd)/.venv/bin/python"
"$PY" classroom/check_setup.py
"$PY" tools/start_here.py
cd your_agent
```

### What each file in your_agent/ does

| File | Who writes it | Job |
| --- | --- | --- |
| data/menu.json | provided | The four fictional menu records. Facts live here, not in the model. |
| workshop_runtime.py | provided | Builds the model (scripted or live Gemini) and prints each step of a run. |
| offline_brain.py | provided | The scripted stand-in used when OFFLINE=True. Not real AI. |
| mcp_connection.py | provided | Starts your mcp_server.py and connects to it (Step 4). |
| menu_tools.py | you, Step 1 | Your tools: plain Python functions. |
| my_agent.py | you, Step 2 | Your agent: model + tools + instructions + loop. |

When the slides say `python my_agent.py`, use your workshop Python: `& $py my_agent.py` on Windows or `"$PY" my_agent.py` on macOS/Linux.

If your learner folder was already created, skip tools/start_here.py and continue at Step 1; the script refuses to overwrite existing work. The new folder contains data/menu.json, configuration support, a local MCP connection helper and a labelled scripted model for rehearsal. It contains no completed menu function or agent. Checkpoints in classroom/ are recovery options, not files you must copy before trying.

## 1. Run a normal function

Create menu_tools.py in your_agent. First load the tiny fictional menu:

```python
import json
from datetime import datetime
from pathlib import Path

MENU = json.loads((Path(__file__).parent / "data" / "menu.json").read_text(encoding="utf-8"))
```

Add this function below it. Read the loop: skip unavailable or over-budget food, apply the diet rule, then return the matching records. The two input checks reject invalid types and negative budgets.

```python
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

Run it:

```powershell
& $py menu_tools.py
```

On macOS/Linux use "$PY" menu_tools.py. Expect status ok and Veg sandwich at Rs 60. Try 30: the tool successfully returns an empty list. We have written ordinary Python; no model is involved yet.

Why `if __name__ == "__main__":`? Python sets `__name__` to `"__main__"` only for the file you run directly. So the test print runs when you run `menu_tools.py`, but stays silent when `my_agent.py` (Step 2) or `mcp_server.py` (Step 4) imports it. That matters for MCP: any stray print there would corrupt the protocol messages. Keep the block at the bottom of the file.

**Try this (one minute each):** change the line inside the `if` block to `print(find_food(80, vegetarian=False))` and the Chicken roll appears next to the Veg sandwich. (`False` means "vegetarian not required", so veg dishes still show; it does not mean non-veg only.) Try `find_food(-5)` and the input check refuses it with a clear error. Open data/menu.json, set Poha to `"available": true`, run `find_food(40)`, then change it back.

## 2. Create the first agent in a new file

Create my_agent.py. Add the imports and OFFLINE setting first, then create_agent, then the invocation. Run after the complete block is in place.

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

```powershell
& $py my_agent.py
```

Expect a request to find_food, its actual returned result, and an answer mentioning the sandwich. OFFLINE=True uses a simple rule script; it is not a real AI. The LangChain agent and actual Python tool still run. If you have privately configured and checked live Gemini access, set OFFLINE=False. See docs/SETUP.md. Do not share keys.

Point to the tool name and arguments. The model requests a call; the application executes the function and sends the result back. The model can request another action or finish. LangChain manages that loop and its messages. The optional manual_loop.py shows the same plumbing explicitly after class.

How to read the output:

| Line | Meaning |
| --- | --- |
| `YOU:` | Your question, sent to the model. |
| `MODEL REQUEST:` | The model asks for a tool by name, with arguments. It does not run anything. |
| `RESULT find_food:` | Your Python ran the function and this is the real data it returned. |
| `ANSWER:` | The model's final reply, written from those results. |

**Try this:** ask "Find non-vegetarian lunch under Rs 80." and check the arguments in MODEL REQUEST. With a live model, also try replacing find_food's docstring with something vague, such as `"""Does a thing."""`, and ask again: with a poor description, the model has a harder time knowing when to use the tool. (Deleting the docstring entirely stops the program at `tool(find_food)` with "Function must have a docstring": LangChain refuses to register a tool the model can't understand. Put it back afterwards.)

## 3. Add a new ability

Add this function to menu_tools.py, **above** the `if __name__ == "__main__":` block (functions first, the test block stays last):

```python
def get_canteen_hours(at: str = '12:30') -> dict:
    """Read fictional hours at a mock time. Default 12:30; not a live clock."""
    now = datetime.strptime(at, '%H:%M').time()
    opens = datetime.strptime('09:00', '%H:%M').time()
    closes = datetime.strptime('16:00', '%H:%M').time()
    return {'opens': '09:00', 'closes': '16:00', 'now': at,
            'open_now': opens <= now < closes, 'mock_clock': True}
```

In my_agent.py, change the import and tool list, then ask for both facts:

```python
from menu_tools import find_food, get_canteen_hours

# Inside create_agent:
tools=[tool(find_food), tool(get_canteen_hours)],

# In the user message:
"Find vegetarian lunch under Rs 80 and check opening hours."
```

The snippet above shows replacements in different locations, not a second complete program. Run my_agent.py again. Expect actual food and hours results; default mock time is 12:30 and closing time 16:00. A live model can choose a different call order. Explain what the second tool added.

**Try this:**

- Change the budget to Rs 30. The correct answer is "nothing available"; check that it doesn't invent a dish.
- With a live model, ask only "Is the canteen open?" and see which tool it chooses. A live model calls only the hours tool; the OFFLINE scripted brain checks the menu first anyway, because it follows fixed rules. That difference is exactly what "the model decides" means.
- Ask for **non-vegetarian** lunch. The tool can only say `vegetarian=True` (veg only) or `False` (anything), so it returns both dishes and the model has to filter in its answer. That's a tool-design gap: a better tool would take `diet="veg" | "non-veg" | "any"`. Good tools make the model's job easy; try adding that as an extension.

## 4. MCP: the same tools, plugged in a standard way

**In class:** just watch this part; the instructor runs it on screen. **After class, or if you finish early:** build it yourself below.

**What MCP is, in one paragraph.** Your `find_food` only works inside your own Python program. MCP (Model Context Protocol) is a standard "plug" for tools: you put your functions behind a small **MCP server**, and any MCP-aware app (a LangChain agent, LangGraph, CrewAI, Claude Desktop, Cursor) can discover and call them, without you rewriting them. The server has no model and makes no decisions. It only offers tools.

### 4a. See it work (no new files, about one minute)

Stay in `your_agent/`. These run the ready-made versions in `classroom/`:

```powershell
& $py ../classroom/mcp_probe.py
```

Expect `DISCOVERED: find_food, get_canteen_hours` and then `MCP RESULT:` with the Veg sandwich. That's a real MCP call with no AI involved: the client asked the server which tools it has, then called one.

```powershell
& $py ../classroom/mcp_agent.py --offline
```

Expect the same answer as your own agent. **The tools didn't change; only how they're connected.**

### 4b. Build your own server (optional)

In `your_agent/`, create **two** files. You never start the server yourself: `mcp_connection.py` (already in your folder) launches it in the background whenever a client needs it.

**File 1: `mcp_server.py`**, the server. It registers your existing functions, unchanged:

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

Keep the file name exactly `mcp_server.py`, and never add `print` to it: the server talks to clients through standard output, and a stray print would corrupt the messages.

**File 2: `probe.py`**, a tiny client that starts your server, lists its tools and calls one:

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

Run it:

```powershell
& $py probe.py
```

Expect `['find_food', 'get_canteen_hours']` and then the sandwich record. Lines starting with `INFO` are the server's own logs; ignore them.

To connect an *agent* to your server, look at `classroom/mcp_agent.py`: it is your Step 2 agent, except the tools come from `connected_tools()` instead of `tool(find_food)`.

## 5. Watch two framework variations

**In class: the instructor runs these.** You can run them too, from `your_agent/`:

```powershell
& $py ../classroom/graph.py --offline
```

```powershell
& $py ../classroom/graph.py --offline --at 17:00
```

**LangGraph, a workflow:** the graph checks the hours first, and **code** decides the route. At 12:30 it runs the lunch agent; at 17:00 it takes the "closed" route and never calls the model. Vocabulary: *state* is the information carried along, a *node* is a step, an *edge* is which step comes next.

**CrewAI, two agents:** the instructor also runs `classroom/crew.py --offline`. A "menu scout" agent finds options through the same MCP server and hands them to a "lunch planner" agent, which proposes 2 × Veg sandwich = Rs 120. CrewAI is an instructor-only install (`requirements-instructor.txt`) and needs Python 3.11 to 3.13. Ask yourself: did this small job really need two agents?

## 6. Keep your project understandable

Write a short README.md with the purpose and run command. Write an instruction file supported by your coding client, using a title and clear rules:

```markdown
# Canteen project rules
- Use data/menu.json for menu facts.
- Explain each proposed change before editing.
- Run the changed behavior and report what was actually tested.
- Keep API keys out of code and commits.
```

AGENTS.md, CLAUDE.md and GEMINI.md support differs by client. Ordinary Markdown is not automatically loaded or enforced. A runtime tool allowlist, argument validation and a loop limit are code boundaries. The optional manual_loop.py demonstrates them.

## Choose one extension afterward

Add a tool that returns the canteen location; change the graph's closed response; or compare a one-agent group lunch proposal with the two-agent version. Change one thing, explain what should happen, run it and inspect the result. Use docs/LEARNING_PATH.md for optional depth.

**Take-home:** [docs/PROMPTING_AND_PROJECT_FILES.md](../docs/PROMPTING_AND_PROJECT_FILES.md) shows how to write a better system prompt, clear tool descriptions, and README and AGENTS.md files that both people and coding agents can use.

If setup fails, use a checkpoint or saved_runs recording with its mode label. Record whether you ran your code, copied a checkpoint or read a saved output. These are useful recovery routes with different evidence.
