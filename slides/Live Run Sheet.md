# Live run sheet

Switch between PowerPoint Presenter View and VS Code/terminal. The PPTX notes contain what to say, ask and demonstrate. The printed sheet below is a backup.

## Prepare the terminal

From the repository root on Vedant's machine:

```powershell
$py = 'C:\vedant-side\workshop\.venv-build-first\Scripts\python.exe'
& $py classroom/check_setup.py
& $py classroom/mcp_probe.py
```

For a student installation set $py to the absolute .venv/Scripts/python.exe in the extracted repository. Keep it absolute before changing to your_agent. Never project .env. Test real Gemini privately with classroom/check_setup.py --live before selecting live mode.

The new learner folder is created by tools/start_here.py. Build there; keep classroom reference files available for recovery. All --offline commands use scripted brains with real tools/frameworks. A saved text output is a backup, not a screen recording or a live model run.

## Slide and editor switches

| Slide | Time IST | Screen | Action |
| --- | --- | --- | --- |
| 1 | 11:00-11:01 | SLIDES | Have the new learner folder ready, with no menu_tools.py or my_agent.py. Open only the lesson and clean terminal; close private .env tabs. |
| 2 | 11:01-11:03 | SLIDES | Show a rehearsed short real run if available. Otherwise state clearly that the scripted preview is a rehearsal and the actual tool data is local. |
| 3 | 11:03-11:05 | SLIDES | Does the model magically know our current menu? |
| 4 | 11:05-11:08 | SLIDES | Use the menu on the next slide or the data file; no printed props are required. |
| 5 | 11:08-11:10 | SLIDES | Can the model request a function our app has not allowed? |
| 6 | 11:10-11:13 | SLIDES | Switch briefly to classroom/data/menu.json and point out the four fields. Return to the slide before typing. |
| 7 | 11:13-11:17 | EDITOR | In your new learner folder create menu_tools.py. Add imports/data loading, then find_food from classroom/README.md. Use the readable for loop. Run: & $py menu_tools.py |
| 8 | 11:17-11:20 | STUDENT ACTIVITY | Expect sandwich at 80 and an empty matches list at 30. Remove the temporary top-level print before importing the module. |
| 9 | 11:20-11:23 | SLIDES | Point to the name find_food and max_price=80 in a saved or rehearsed live trace. |
| 10 | 11:23-11:26 | SLIDES | Explain the five-line conceptual loop in the preparation guide. LangChain manages message bookkeeping in the student build. |
| 11 | 11:26-11:30 | EDITOR | Use the full 18-line first-agent checkpoint from classroom/README.md. Add imports, then agent creation, then invocation and show_messages. Run: & $py my_agent.py |
| 12 | 11:30-11:40 | STUDENT ACTIVITY | Use & $py my_agent.py in the learner folder. Have students point to MODEL REQUEST and RESULT. Explain the mode label. For live calls, observe actual behavior rather than expecting an exact sentence. |
| 13 | 11:40-11:45 | EDITOR + DISCUSSION | Try Rs 30. Distinguish an empty successful result from an error, without opening the advanced error-handling lab. |
| 14 | 11:45-11:48 | EDITOR | Add hours to menu_tools.py, update the import and tools list in my_agent.py. Show only these changes. |
| 15 | 11:48-11:55 | STUDENT ACTIVITY | Run my_agent.py again. Expect sandwich and mock closing 16:00. Take two short student explanations from different seating zones. |
| 16 | 11:55-12:00 | BREAK | Resume at 12:00. Bring up the MCP question, not installation steps. |
| 17 | 12:00-12:02 | SLIDES | What would be wasteful about rewriting the menu filter for every framework? |
| 18 | 12:02-12:05 | SLIDES | Point to menu_tools.py being imported by mcp_server.py. |
| 19 | 12:05-12:08 | EDITOR | Create the file in the learner folder. The supplied connection helper launches it through the current Python interpreter; no separate server window is needed. |
| 20 | 12:08-12:11 | EDITOR | From repository root: & $py classroom/mcp_probe.py, then & $py classroom/mcp_agent.py --offline. Remove --offline only for a privately rehearsed live run. |
| 21 | 12:11-12:15 | STUDENT ACTIVITY | Run probe.py in the learner folder, or use classroom/mcp_probe.py from repository root. See the two tool names and sandwich result. |
| 22 | 12:15-12:17 | SLIDES | Would a menu lookup help when the canteen is closed? |
| 23 | 12:17-12:20 | SLIDES | Where does the model choose its own actions here? |
| 24 | 12:20-12:23 | EDITOR | Open classroom/graph.py. Point to hours using MCP and agent containing create_agent. Explain choose without adding persistence or approval APIs. |
| 25 | 12:23-12:27 | EDITOR + DISCUSSION | Use & $py rather than python if using the prepared PowerShell interpreter variable. |
| 26 | 12:27-12:29 | SLIDES | Could one agent already do this? |
| 27 | 12:29-12:32 | EDITOR | Open classroom/crew.py. The presenter has already installed requirements-instructor.txt. Keep adapter compatibility details out of the beginner explanation. |
| 28 | 12:32-12:35 | EDITOR | Run & $py classroom/crew.py --offline. Point to SCOUT HANDOFF then PLANNER. |
| 29 | 12:35-12:37 | SLIDES | What would two lunch agents add besides latency? |
| 30 | 12:37-12:40 | SLIDES | Which is the simplest design that meets each requirement? |
| 31 | 12:40-12:42 | SLIDES | Skip this teaser if behind; do not introduce protocol messages or another server. |
| 32 | 12:42-12:44 | SLIDES | Where should a price change live? Where should a run command live? |
| 33 | 12:44-12:46 | STUDENT ACTIVITY | Use a plain Markdown file or paper if the coding client is unavailable. This is a two-minute introduction; the longer documentation lab is after class. |
| 34 | 12:46-12:49 | EDITOR | Open classroom/manual_loop.py and show the allowed lookup and step limit. Run classroom/safety_demo.py for a deliberately injected forbidden request. Label it as injected. |
| 35 | 12:49-12:50 | SLIDES | One minute. An AI coding editor is optional. The skill is making a small understandable change and observing its behavior, not accepting a whole generated project. Keep the long fake-wrap review after class. |
| 36 | 12:50-13:00 | Q&A | Close at 13:00. Do not add a surprise final installation or advanced topic. |

## Reference demo commands

From repository root:

```powershell
& $py classroom/menu_tools.py
& $py classroom/agent.py --offline
& $py classroom/mcp_probe.py
& $py classroom/mcp_agent.py --offline
& $py classroom/graph.py --offline
& $py classroom/graph.py --offline --at 17:00
& $py classroom/crew.py --offline
& $py classroom/safety_demo.py
```

Use the learner lesson for typing steps. The graph and crew are instructor demonstrations. If behind, skip A2A/orchestrator teasers, then shorten the crew demo; protect student build time, break and Q&A.
