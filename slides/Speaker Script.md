# Build first workshop speaker script

36 slides. 120 minutes including break and Q&A. Use the live run sheet for exact commands. Rehearse; planned timings are not a measured delivery time.

## Slide 1: Build your first AI agent

Slot 11:00:00–11:01:30 IST (90 seconds).

SAY
We will build a small program that uses AI to choose tools. By the end you should understand one working loop and know why you might choose a graph or a team.

DO / SCREEN
Have the new learner folder ready, with no menu_tools.py or my_agent.py. Open only the lesson and clean terminal; close private .env tabs.

ASK
Who has used a chatbot? Who has written a Python function?

FALLBACK
Sharing and checkpoint files are available. Do not turn the introduction into installation support.

SOURCES


## Slide 2: You have Rs 80 and ten minutes

Slot 11:01:30–11:03:30 IST (120 seconds).

SAY
Use a familiar deadline: the next lecture starts soon and you need lunch. Ask what information matters before saying any framework names.

DO / SCREEN
Show a rehearsed short real run if available. Otherwise state clearly that the scripted preview is a rehearsal and the actual tool data is local.

ASK
Budget? Diet? Availability? Opening hours?

FALLBACK
Use classroom/saved_runs/agent.txt. Read its SCRIPTED label aloud.

SOURCES


## Slide 3: What makes this an agent?

Slot 11:03:30–11:05:30 IST (120 seconds).

SAY
The agent is the whole program: model, instructions, permitted tools and the loop around them. A model response alone is not Python execution.

DO / SCREEN


ASK
Does the model magically know our current menu?

FALLBACK


SOURCES
https://docs.langchain.com/oss/python/langchain/agents

## Slide 4: Act out the tool call

Slot 11:05:30–11:08:30 IST (180 seconds).

SAY
Ask three volunteers to play the user, model and menu tool. Keep the whole role-play to two minutes. The tool holder has the four fictional records. The model must ask for them before recommending food.

DO / SCREEN
Use the menu on the next slide or the data file; no printed props are required.

ASK
Who actually looked at the menu?

FALLBACK
Play all three roles from the front if volunteers are slow.

SOURCES


## Slide 5: Give each part one job

Slot 11:08:30–11:10:00 IST (90 seconds).

SAY
Name each part only after the role-play. Point from user to model to application function, and then back with the result. Do not add MCP or multi-agent terminology yet.

DO / SCREEN


ASK
Can the model request a function our app has not allowed?

FALLBACK


SOURCES


## Slide 6: Our entire canteen menu

Slot 11:10:00–11:13:00 IST (180 seconds).

SAY
Four records are enough. Only the sandwich qualifies. The hours fixture is 09:00-16:00 and mock time is 12:30. These are fictional teaching records.

DO / SCREEN
Switch briefly to classroom/data/menu.json and point out the four fields. Return to the slide before typing.

ASK
Why does the cheaper poha not qualify?

FALLBACK


SOURCES


## Slide 7: A tool starts as a function

Slot 11:13:00–11:17:00 IST (240 seconds).

SAY
Explain function, argument and return value just in time. This slide is an outline with an ellipsis, not the runnable solution. Use the full small function in the lesson.

DO / SCREEN
In your new learner folder create menu_tools.py. Add imports/data loading, then find_food from classroom/README.md. Use the readable for loop. Run: & $py menu_tools.py

ASK
Which values go in? What comes back?

FALLBACK
Open classroom/menu_tools.py as the labelled completed checkpoint.

SOURCES


## Slide 8: Your turn: run the tool

Slot 11:17:00–11:20:00 IST (180 seconds).

SAY
Give students three minutes to run it. Show the slide while they type. Ask for ready/help/checkpoint signals. Do not inspect every laptop.

DO / SCREEN
Expect sandwich at 80 and an empty matches list at 30. Remove the temporary top-level print before importing the module.

ASK
Is an empty result the same as a failed lookup?

FALLBACK
Copy classroom/menu_tools.py into the learner folder, or read its saved result and label what happened.

SOURCES


## Slide 9: Let the model request the function

Slot 11:20:00–11:23:00 IST (180 seconds).

SAY
The description tells the model when the function is relevant. A tool request has a name and arguments. The library routes an allowed request to Python and returns the actual result.

DO / SCREEN
Point to the name find_food and max_price=80 in a saved or rehearsed live trace.

ASK
Who reads the JSON file?

FALLBACK


SOURCES
https://docs.langchain.com/oss/python/langchain/agents

## Slide 10: The ReAct-style loop

Slot 11:23:00–11:26:00 IST (180 seconds).

SAY
Explain ReAct as reasoning and acting in a loop. We inspect tool actions and results, not private chain-of-thought. Our tool-calling agent illustrates this pattern; we are not reproducing every detail of the original paper.

DO / SCREEN
Explain the five-line conceptual loop in the preparation guide. LangChain manages message bookkeeping in the student build.

ASK
What should happen when the agent has enough information?

FALLBACK


SOURCES
https://arxiv.org/abs/2210.03629

## Slide 11: Build with LangChain

Slot 11:26:00–11:30:00 IST (240 seconds).

SAY
Write this in a new my_agent.py. Explain model, tools and instruction. make_model is supplied configuration/fallback support; create_agent is the framework loop. OFFLINE=True is scripted rehearsal; False requires a privately configured tested live model.

DO / SCREEN
Use the full 18-line first-agent checkpoint from classroom/README.md. Add imports, then agent creation, then invocation and show_messages. Run: & $py my_agent.py

ASK
Where did we give the model permission to request find_food?

FALLBACK
Use classroom/first_agent_checkpoint.py after the menu tool exists.

SOURCES


## Slide 12: Build and run your first agent

Slot 11:30:00–11:40:00 IST (600 seconds).

SAY
Protect these ten minutes. Let students type and run the small file. Stay on this slide. Volunteers handle individual setup; explain repeated mistakes from the front.

DO / SCREEN
Use & $py my_agent.py in the learner folder. Have students point to MODEL REQUEST and RESULT. Explain the mode label. For live calls, observe actual behavior rather than expecting an exact sentence.

ASK
What did you write, and what did LangChain handle?

FALLBACK
Run & $py classroom/agent.py --offline from repository root, or use the saved output. Label checkpoint use accurately.

SOURCES


## Slide 13: What happened in that run?

Slot 11:40:00–11:45:00 IST (300 seconds).

SAY
Give about two minutes for a budget/question variation and three minutes for discussion. Explain what repeats and what finishes. A normal model can choose a different order or not need a tool for a greeting.

DO / SCREEN
Try Rs 30. Distinguish an empty successful result from an error, without opening the advanced error-handling lab.

ASK
Could it answer opening hours with only this tool?

FALLBACK
Use the saved agent-budget30.txt result.

SOURCES


## Slide 14: Add one new ability

Slot 11:45:00–11:48:00 IST (180 seconds).

SAY
Write the full hours function from the lesson. This slide is an outline. We use a mock clock so everyone can reproduce the same case; it is not live campus data.

DO / SCREEN
Add hours to menu_tools.py, update the import and tools list in my_agent.py. Show only these changes.

ASK
What should we ask so the program needs both tools?

FALLBACK


SOURCES


## Slide 15: Your agent now has two tools

Slot 11:48:00–11:55:00 IST (420 seconds).

SAY
Give students seven minutes. In a real model run the tool order may vary; what matters is that menu/hours claims have the relevant results. Scripted rehearsal follows a known sequence.

DO / SCREEN
Run my_agent.py again. Expect sandwich and mock closing 16:00. Take two short student explanations from different seating zones.

ASK
Which part did you add? Which question now works?

FALLBACK
The completed classroom/agent.py is the two-tool checkpoint.

SOURCES


## Slide 16: Five-minute break

Slot 11:55:00–12:00:00 IST (300 seconds).

SAY
Stop for the full five-minute break. Let volunteers help setup during the pause without making it another lecture.

DO / SCREEN
Resume at 12:00. Bring up the MCP question, not installation steps.

ASK


FALLBACK


SOURCES


## Slide 17: Can another app use our tools?

Slot 12:00:00–12:02:30 IST (150 seconds).

SAY
Motivate the boundary after the function works. A common MCP server exposes tools; it does not provide a model or make the system autonomous.

DO / SCREEN


ASK
What would be wasteful about rewriting the menu filter for every framework?

FALLBACK


SOURCES
https://modelcontextprotocol.io/docs/learn/architecture

## Slide 18: Same data, same tool service

Slot 12:02:30–12:05:30 IST (180 seconds).

SAY
Each example starts a local stdio instance of the same server program. We are not deploying a central campus server. The functions remain ordinary Python.

DO / SCREEN
Point to menu_tools.py being imported by mcp_server.py.

ASK
Does MCP replace the model?

FALLBACK


SOURCES
https://github.com/langchain-ai/langchain-mcp-adapters
https://docs.crewai.com/en/mcp/overview

## Slide 19: Expose our functions through MCP

Slot 12:05:30–12:08:30 IST (180 seconds).

SAY
Write mcp_server.py. Explain registration as making the functions discoverable to a client. No need to teach async internals or every transport.

DO / SCREEN
Create the file in the learner folder. The supplied connection helper launches it through the current Python interpreter; no separate server window is needed.

ASK


FALLBACK


SOURCES
https://github.com/modelcontextprotocol/python-sdk

## Slide 20: Discover, call, then connect an agent

Slot 12:08:30–12:11:30 IST (180 seconds).

SAY
First list tools and call find_food directly through MCP; that does not need a model. Then show classroom/mcp_agent.py. connected_tools owns a local connection and closes it after use.

DO / SCREEN
From repository root: & $py classroom/mcp_probe.py, then & $py classroom/mcp_agent.py --offline. Remove --offline only for a privately rehearsed live run.

ASK
Which part moved into another process?

FALLBACK


SOURCES
https://github.com/langchain-ai/langchain-mcp-adapters

## Slide 21: Try one real MCP call

Slot 12:11:30–12:15:00 IST (210 seconds).

SAY
Give students three and a half minutes for the probe from the lesson where setup permits. The local MCP call is real even without an LLM key.

DO / SCREEN
Run probe.py in the learner folder, or use classroom/mcp_probe.py from repository root. See the two tool names and sandwich result.

ASK
What stayed the same?

FALLBACK
Keep the direct-function agent and watch the instructor MCP call; complete local setup after class.

SOURCES


## Slide 22: What if the canteen is closed?

Slot 12:15:00–12:17:00 IST (120 seconds).

SAY
Use a concrete requirement before introducing graph vocabulary. The earlier agent chooses tools; this outer workflow guarantees an hours step first.

DO / SCREEN


ASK
Would a menu lookup help when the canteen is closed?

FALLBACK


SOURCES
https://docs.langchain.com/oss/python/langgraph/overview

## Slide 23: One branch around an agent

Slot 12:17:00–12:20:00 IST (180 seconds).

SAY
Read the route together. State holds hours, question and answer. A node is an ordinary function that updates that information. An edge chooses the next step. The open node contains the familiar agent.

DO / SCREEN


ASK
Where does the model choose its own actions here?

FALLBACK


SOURCES
https://docs.langchain.com/oss/python/langgraph/overview

## Slide 24: Wire the small graph

Slot 12:20:00–12:23:00 IST (180 seconds).

SAY
This is an instructor demonstration. Students can read the three functions and wiring. Do not require the room to type the whole graph.

DO / SCREEN
Open classroom/graph.py. Point to hours using MCP and agent containing create_agent. Explain choose without adding persistence or approval APIs.

ASK


FALLBACK


SOURCES


## Slide 25: Predict both routes, then run

Slot 12:23:00–12:27:00 IST (240 seconds).

SAY
Ask for predictions before each run. Both calls use the same actual MCP server. The offline brain is scripted. The closed route does not invoke the lunch agent.

DO / SCREEN
Use & $py rather than python if using the prepared PowerShell interpreter variable.

ASK
What would you change to add an approval step later?

FALLBACK
Use saved_runs/graph-open.txt and graph-closed.txt.

SOURCES


## Slide 26: Could two agents share the job?

Slot 12:27:00–12:29:30 IST (150 seconds).

SAY
Use a group lunch for two vegetarians within Rs 150. Scout gathers options under Rs 75 per person. Planner proposes quantities and a total. This is a deliberately small example of a handoff, not proof that two agents improve lunch search.

DO / SCREEN


ASK
Could one agent already do this?

FALLBACK


SOURCES
https://docs.crewai.com/en/concepts/processes

## Slide 27: A real CrewAI handoff

Slot 12:29:30–12:32:30 IST (180 seconds).

SAY
This excerpt is an outline; open the runnable file. Show Agent, Task and Crew objects. Only the scout has the menu tool, discovered through the same MCP program. This is sequential, not a manager dynamically choosing workers.

DO / SCREEN
Open classroom/crew.py. The presenter has already installed requirements-instructor.txt. Keep adapter compatibility details out of the beginner explanation.

ASK


FALLBACK


SOURCES
https://docs.crewai.com/en/concepts/processes

## Slide 28: Run the scout and planner

Slot 12:32:30–12:35:30 IST (180 seconds).

SAY
Read the SCRIPTED label if using offline. The actual CrewAI orchestration, MCP lookup and task context run. A live Gemini run requires separate private rehearsal. Do not call this a benchmark or autonomous AI when scripted.

DO / SCREEN
Run & $py classroom/crew.py --offline. Point to SCOUT HANDOFF then PLANNER.

ASK


FALLBACK
Use saved_runs/crew.txt; do not install CrewAI during class.

SOURCES


## Slide 29: When does a team earn its cost?

Slot 12:35:30–12:37:00 IST (90 seconds).

SAY
Briefly sketch a coordinator choosing a menu or facilities specialist. That is a different optional pattern from the sequential crew we ran. Keep its implementation for later.

DO / SCREEN


ASK
What would two lunch agents add besides latency?

FALLBACK


SOURCES


## Slide 30: Choose for the job

Slot 12:37:00–12:40:00 IST (180 seconds).

SAY
Give three quick scenarios: one menu question, an action needing approval, and research followed by writing. Students choose and give one reason. CrewAI also has flows; LangGraph can host multiple agents.

DO / SCREEN


ASK
Which is the simplest design that meets each requirement?

FALLBACK


SOURCES
https://docs.langchain.com/oss/python/langgraph/overview
https://docs.crewai.com/en/concepts/flows

## Slide 31: MCP and A2A connect different things

Slot 12:40:00–12:42:00 IST (120 seconds).

SAY
Spend at most one minute on A2A and the remaining minute recapping categories. ReAct and handoffs are patterns; LangChain, LangGraph, CrewAI are frameworks; MCP/A2A are protocols.

DO / SCREEN
Skip this teaser if behind; do not introduce protocol messages or another server.

ASK


FALLBACK


SOURCES
https://a2a-protocol.org/latest/topics/a2a-and-mcp/

## Slide 32: Give the files clear jobs

Slot 12:42:00–12:44:00 IST (120 seconds).

SAY
Now that the program works, the folders have a purpose. Show the small project. Mention CLAUDE.md/GEMINI.md as other client conventions. Arbitrary Markdown is not automatically loaded or enforced.

DO / SCREEN


ASK
Where should a price change live? Where should a run command live?

FALLBACK


SOURCES


## Slide 33: Write a useful project instruction

Slot 12:44:00–12:46:00 IST (120 seconds).

SAY
Write these together, then ask each student for one useful instruction in a note or supported project file. Explain the difference between guidance and runtime enforcement.

DO / SCREEN
Use a plain Markdown file or paper if the coding client is unavailable. This is a two-minute introduction; the longer documentation lab is after class.

ASK


FALLBACK


SOURCES


## Slide 34: Keep control of allowed actions

Slot 12:46:00–12:49:00 IST (180 seconds).

SAY
Use one narrow safety example after the agent makes sense. A model request cannot execute an unregistered function through our loop. Avoid a new long threat-model lecture.

DO / SCREEN
Open classroom/manual_loop.py and show the allowed lookup and step limit. Run classroom/safety_demo.py for a deliberately injected forbidden request. Label it as injected.

ASK
Would writing "be safe" in a prompt replace this check?

FALLBACK
Read the seven-line boundary example and the expected refusal.

SOURCES


## Slide 35: Review one small AI-assisted change

Slot 12:49:00–12:50:00 IST (60 seconds).

SAY
One minute. An AI coding editor is optional. The skill is making a small understandable change and observing its behavior, not accepting a whole generated project. Keep the long fake-wrap review after class.

DO / SCREEN


ASK


FALLBACK


SOURCES


## Slide 36: What will you build next?

Slot 12:50:00–13:00:00 IST (600 seconds).

SAY
Reserve the last ten minutes for questions. Invite a short explanation of one tool call or framework choice. Direct students to classroom/README.md and docs/LEARNING_PATH.md. The repository stays private until explicitly released; distribute the ZIP through the organiser.

DO / SCREEN
Close at 13:00. Do not add a surprise final installation or advanced topic.

ASK
What can your agent now do that it could not do at the beginning?

FALLBACK


SOURCES
