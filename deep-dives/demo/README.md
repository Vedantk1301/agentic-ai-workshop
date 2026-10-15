# Campus Canteen Assistant

Five small demos use one fictional menu. The current live class uses the [starter lesson](../../starter/README.md): one instruction file, one small change and one review task. The Classroom Follow Along in learning_lab preserves an older standalone folder layout for reference. Set up before class for laptop participation; paired/paper participation remains available. The other implementations support optional deeper practice.

| File | Purpose | Needs network/API? |
| --- | --- | --- |
| 01_tools_and_fixed_workflow.py | A tool and a fixed workflow | No |
| 02_react_agent.py | A model chooses its tools | Gemini, or --offline |
| 03_langgraph_flow.py | State, routing, clarification and bounded retries | No |
| 04_graph_with_agent.py | Agent inside a graph; final facts rendered in code | Gemini, or --offline |
| 05_team_of_roles.py | Plain-Python simulation of coordinator/adviser roles | No |

The source menu is data/menu.json: veg sandwich Rs 60 in stock; poha Rs 35 sold out; chicken roll Rs 75 in stock, not vegetarian; dosa Rs 90 in stock. Mock hours are 09:00–16:00 and the repeatable clock is 12:30. All records/policy are fictional.

## Fresh Windows setup

Install Python 3.11 and a text editor first. This dependency set was tested on Python 3.11. Open PowerShell in the extracted demo folder. Use your own extraction location.

~~~powershell
py -3.11 --version
py -3.11 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest -q -p no:cacheprovider
.venv\Scripts\python 01_tools_and_fixed_workflow.py
.venv\Scripts\python 04_graph_with_agent.py --offline --inject-mistake free_text
~~~

If the py launcher is unavailable but Python 3.11 is on PATH, check python --version, then use python -m venv .venv. Dependency installation needs internet once. Offline demos work after installation. No activation command or PowerShell execution-policy change is required.

## macOS/Linux equivalent

~~~sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q -p no:cacheprovider
.venv/bin/python 04_graph_with_agent.py --offline
~~~

Python 3.11 must already be installed. These equivalent commands are supplied for portability; this revision was executed on Windows, not macOS/Linux.

## Optional live Gemini

Use a separate workshop account and obtain a key from [Google AI Studio](https://aistudio.google.com/). Access and quotas depend on your model/account; a key does not guarantee free calls or enough quota.

Copy .env.example to .env only if you do not already have a configured file. Edit it privately and fill GOOGLE_API_KEY. Never put a key in Markdown, source control or a projected terminal.

~~~powershell
if (-not (Test-Path -LiteralPath .env)) { Copy-Item .env.example .env }
.venv\Scripts\python check_setup.py
.venv\Scripts\python 02_react_agent.py
.venv\Scripts\python 04_graph_with_agent.py
~~~

The setup check makes a real API call when a key is available. It lists model IDs before the call. If the model is unavailable, choose a suitable supported GEMINI_MODEL in .env. Then run both actual demos: a successful text call alone does not establish tool-calling/structured-output compatibility. Live Gemini was not exercised during the offline repair checks.

## Present or practise

~~~powershell
.venv\Scripts\python 01_tools_and_fixed_workflow.py --scenario sold_out
.venv\Scripts\python 01_tools_and_fixed_workflow.py --question "veg lunch under Rs 0"
.venv\Scripts\python 02_react_agent.py --offline --pause
.venv\Scripts\python 02_react_agent.py --offline --menu-only
.venv\Scripts\python 02_react_agent.py --offline --scenario sold_out
.venv\Scripts\python 03_langgraph_flow.py --scenario menu_flaky
.venv\Scripts\python 03_langgraph_flow.py --scenario menu_timeout
.venv\Scripts\python 03_langgraph_flow.py --question "veg lunch, is it open?"
.venv\Scripts\python 04_graph_with_agent.py --offline --inject-mistake fake_dish
.venv\Scripts\python 04_graph_with_agent.py --offline --inject-mistake free_text
.venv\Scripts\python 05_team_of_roles.py --scenario policy_unavailable
~~~

02's --pause reveals a completed trace one message at a time; it does not suspend execution. A live model may group or reorder tool requests. Predict from the actual trace rather than promise a fixed sequence.

--offline uses a rule-based stand-in, not a real AI. Say so. --inject-mistake deliberately changes a proposal for teaching. In 04, MODEL PROPOSAL is untrusted debug output; ANSWER is the checked result. The final answer never forwards the model's free-text paragraph.

## Scenarios and limits

normal; sold_out; menu_flaky; menu_timeout; policy_unavailable; after_hours. Missing or zero budget asks for valid input. A successful empty lookup differs from a failed lookup. 03 retries at most twice; 04 requires successful tool evidence and verifies the original constraints.

04 keeps the actual lookup filters with its result. An empty search under Rs 10 does not prove there is no lunch under Rs 80. The verifier uses schema-normalized arguments and checks query coverage before making a negative stock claim. Integration tests exercise the real agent and tools with altered offline model proposals.

This teaching project uses a small English parser and local fixtures. It does not provide general language validation, durable conversation resumption, orders or production access controls. Live-provider behavior requires separate checks.

## Learn the working method

[Guided lab](../learning_lab/AI%20Coding%20Lab.md) and [review exercise](../learning_lab/Review%20Exercise.md). docs/PROJECT.md defines the outcome/data; docs/REVIEW.md guides review. AGENTS.md holds shared coding instructions; CLAUDE.md and GEMINI.md import it for their clients. The ordinary Gemini API call in our demo does not automatically read those files.

Exercises/solutions are in exercises/; saved offline outputs are in saved_runs/. The student archive excludes .venv and .env. Each student creates their own environment and configures credentials only if choosing the live path.
