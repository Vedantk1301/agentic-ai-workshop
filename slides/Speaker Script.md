# Classroom speaker script

Trimmed 31-slide edition, 15 October 2026. Planned 120-minute slots, including a five-minute break and ten-minute Q&A. Rehearse with a timer. Use starter/README.md and docs/ROOM_GUIDE.md in the GitHub kit. Individual work is the default; sharing is optional. Follow the five common checkpoints. The 53-slide v3 deck is optional reference.

## Slide 1: VIT MUMBAI  ·  17 OCTOBER 2026

Slot 11:00:00–11:01:00 IST (60 seconds).

Welcome. Plan for a possible 100-200 students, with actual attendance still to be confirmed. Each student records a useful instruction, a small code change and its result, and a review finding. Use your own laptop where available; sharing is optional. Explain that we will work together through common checkpoints. The presenter leads from the front; helpers, if available, handle individual laptop issues.

## Slide 2: You have ₹80.
Attendance in 10 minutes.
You're hungry.

Slot 11:01:00–11:03:00 IST (120 seconds).

Ask which facts the assistant needs: budget, diet, stock and hours. Let everyone write a prediction first, then take two answers from different seating areas. Students can use their own laptop, share by taking turns, or record answers on paper. Do not assume everyone completed the earlier speaker setup.

## Slide 3: Overconfident AI recommends…

Slot 11:03:00–11:06:00 IST (180 seconds).

Introduce Canteen Bhaiya and Overconfident AI briefly. Give students thirty seconds to identify the nonexistent wrap, then sample answers. This is a constructed bad answer, not a measured Gemini failure. Point out the real sandwich, sold-out poha, non-vegetarian chicken and over-budget dosa.

## Slide 4: AI writes the order slip. Code makes the food.

Slot 11:06:00–11:10:00 IST (240 seconds).

Slowly trace model request, application execution and tool result. Use the order-slip analogy. A tool is ordinary code. A model can request a tool but does not directly run Python. Ask a student who actually reads the menu. If the answer is unclear, repeat this diagram instead of adding MCP terminology.

## Slide 5: Google AI Studio setup

Slot 11:10:00–11:14:00 IST (240 seconds).

Four-minute instructor demonstration, not simultaneous audience account creation. Open AI Studio and show API Keys using blank or masked configuration. New users may have a default project/key; otherwise show the creation route. Check free-tier/model access without promising eligibility or quota. Students continue with offline tasks and may configure live use privately outside the activity. No Cloud Console provisioning, billing upgrade or credit purchase. Sources: https://ai.google.dev/gemini-api/docs/api-key and https://ai.google.dev/gemini-api/docs/billing

## Slide 6: Connect the prepared Python demo

Slot 11:14:00–11:17:00 IST (180 seconds).

Show starter/.env.example with a blank key. Explain private .env configuration as GOOGLE_API_KEY and the separate GEMINI_MODEL setting. Do not type, reveal or distribute a real key. Demonstrate with prepared or masked configuration, not a room-wide setup pause. Run starter/check_setup.py and the actual live agent privately before class if showing Gemini. Coding-assistant sign-in and this application key are separate. AI Studio is 18+; unavailable accounts continue offline. Sources: https://ai.google.dev/gemini-api/docs/api-key and https://ai.google.dev/gemini-api/docs/available-regions

## Slide 7: Checkpoint 0: run the starter

Slot 11:17:00–11:20:00 IST (180 seconds).

Three-minute Checkpoint 0. Dependencies should already be installed. From the repository root run starter/agent.py --offline. Explicitly label the rule-based stand-in; the agent/tool plumbing still executes. Expected sandwich Rs 60 and closing time 16:00. Explain signals: 1 finger ready, 2 need help, 3 using saved trace. Helpers handle individual issues if available. Without helpers, address a repeated error briefly from the front and direct blocked students to deep-dives/demo/saved_runs/02_agent_lunch_and_hours_OFFLINE.txt, source and menu. Students record executed locally or read trace. Do not wait to inspect every laptop. Copy the supplied notes template or use paper.

## Slide 8: Give each file one job

Slot 11:20:00–11:23:00 IST (180 seconds).

Show these files inside starter/. Explain each reader and purpose. Tests are in deep-dives/demo/tests/ for later practice. Ask: where does stock belong? Where does the run command belong? Do not lecture on every folder or require everyone to create an empty repository.

## Slide 9: Markdown basics

Slot 11:23:00–11:26:00 IST (180 seconds).

Three minutes. Type a title, a Requirements heading and two bullets in a scratch Markdown note. Show preview. Each student writes one clear requirement. Mention the starter/workshop_notes.template.md for recording checkpoint evidence. Avoid Markdown extensions and front matter.

## Slide 10: Write the outcome before asking for code

Slot 11:26:00–11:29:00 IST (180 seconds).

The change is intentionally small. A first-year student can understand the budget change. A senior student should explain the evidence and failure cases. Read the three checks aloud. Do not expand this into a full new chatbot build.

## Slide 11: Useful instructions for an AI coder

Slot 11:29:00–11:32:00 IST (180 seconds).

Read the existing AGENTS.md. Demonstrate one shared instruction file in the active client. Current Antigravity supports workspace AGENTS.md and GEMINI.md; check loaded rules for the installed version. Mention CLAUDE.md for Claude Code and GEMINI.md for Gemini CLI in one sentence only. Do not install three clients. These files guide a coding assistant; the Python demo does not automatically read them. Source: https://www.antigravity.google/docs/rules

## Slide 12: Checkpoint 1: useful instructions

Slot 11:32:00–11:36:00 IST (240 seconds).

Four-minute Checkpoint 1. Each student writes five useful instruction lines in their own scratch note or on paper, then adds the best line to supplied starter/AGENTS.md without removing existing guidance. Sharing a laptop is optional; each student records their own line and a way to check it. Ask for progress signals and sample two answers from different seating areas. Do not walk to every laptop. Example: do not change menu records to make a test pass.

## Slide 13: Read one menu record

Slot 11:36:00–11:40:00 IST (240 seconds).

Four minutes. Open data/menu.json and read one record slowly. Name, integer rupee price, boolean vegetarian and stock. Explain true/false and double-quoted JSON strings. Ask why an instruction saying “always recommend sandwich” cannot establish stock. No JSON-schema lecture.

## Slide 14: Demo 1: a tool is just a function

Slot 11:40:00–11:44:00 IST (240 seconds).

Run part A of 01 once, or open its saved output. Read find_food(max_price=80, vegetarian=True). Ask which records are excluded and why. Stay on the small function and its return value. Do not explain package imports or all helper modules.

## Slide 15: ReAct: think, act, look, repeat

Slot 11:44:00–11:47:00 IST (180 seconds).

Explain ReAct as reasoning/action/observation using the lost-charger analogy. We can inspect tool requests and results; we are not displaying hidden reasoning. After every result the next request can depend on what was found. Keep to one loop and one example.

## Slide 16: Game: predict the next tool

Slot 11:47:00–11:52:00 IST (300 seconds).

Five-minute instructor demonstration. Run starter/agent.py --pause with Gemini only if privately tested beforehand; otherwise add --offline and explicitly disclose the rule-based stand-in. The pause reveals an already-completed trace. Ask the whole room for predictions before each reveal. Students do not make simultaneous live calls. A real model may group or reorder requests.

## Slide 17: Checkpoint 2: change and run

Slot 11:52:00–12:00:00 IST (480 seconds).

Eight-minute Checkpoint 2. First demonstrate copying starter/agent.py to starter/practice_agent.py and locating QUESTION. Everyone makes only the Rs 80 to Rs 30 change, manually or with an already configured coding assistant. Preserve MENU_ONLY_QUESTION, tools and data. Students run the copy with --offline and record the diff and observed result in their notes. Show the expected no-match result from the front. Use progress signals; helpers, if available, handle individual issues. Blocked students record a proposed edit and predicted output labelled not run, then continue. Optional sharing uses keyboard turns. Early finishers try sold_out or menu_timeout. Sample two explanations. Finish by 12:00.

## Slide 18: 5-minute break

Slot 12:00:00–12:05:00 IST (300 seconds).

Five-minute break, 12:00-12:05. Return at 12:05. Open docs/REVIEW.md and demo 04. Helpers may assist with unresolved setup during the break if available. The presenter does not promise to debug every laptop; blocked students continue with trace/source/paper after the break.

## Slide 19: Review the path to the user

Slot 12:05:00–12:08:00 IST (180 seconds).

Three minutes. Show the one-line budget diff first. Then introduce the review order: requirement, changed lines, input/tool values, failure, final text. A downloaded ZIP is not a Git repository. Use the editor comparison view. Git is optional and not a new installation topic.

## Slide 20: 24 tests passed. The answer was still wrong.

Slot 12:08:00–12:12:00 IST (240 seconds).

Four minutes. The original 24 tests passed, but the model message could still contain a fake dish. Only the recommended_dishes list was checked. Ask a student to point to the value actually returned to the user. More passing tests alone do not prove correctness.

## Slide 21: Checkpoint 3: review the answer

Slot 12:12:00–12:18:00 IST (360 seconds).

Six-minute Checkpoint 3. Open docs/REVIEW.md. Each student first identifies the unchecked return value, writes a correcting idea and one input/output check in their own note. Optional neighbour discussion follows. No Python or account is required. Ask for progress signals and sample two explanations. Demonstrate the worked answer afterward. A rule in AGENTS.md alone does not fix the unsafe return.

## Slide 22: Overconfident AI strikes again

Slot 12:18:00–12:22:00 IST (240 seconds).

Four minutes. Run deep-dives/demo/04_graph_with_agent.py --offline --inject-mistake fake_dish, then free_text only if time remains. The mistake is injected for teaching. The MODEL PROPOSAL is untrusted debug text; ANSWER uses checked records. Joke payoff: Canteen Bhaiya 1, Overconfident AI 0. Explain the checking idea, not the entire 200-line implementation.

## Slide 23: A check must match the claim

Slot 12:22:00–12:25:00 IST (180 seconds).

Three minutes. Ask what a successful empty lookup means, and how that differs from a source failure. A search under Rs 10 does not establish no food under Rs 80. These are extension questions if the room is comfortable. Everyone should at least explain why a failed lookup cannot prove stock.

## Slide 24: LangGraph is Google Maps for your agent

Slot 12:25:00–12:28:00 IST (180 seconds).

Three minutes. State is the bag of information, nodes are steps, edges are routes. Students need to read a route, not write LangGraph syntax today. A node can contain ordinary code or a model-driven loop. Ask where the original budget is kept.

## Slide 25: Our canteen graph

Slot 12:28:00–12:31:00 IST (180 seconds).

Three minutes. Follow one normal route and one failed lookup route. Missing/invalid budget asks and ends this run. A failed menu lookup has two attempts total: one retry, then honest unavailable information. No durable resumption is configured. An explicit graph can contain flexible agents. Ask which decision code should enforce.

## Slide 26: Demo 3: one graph, four routes

Slot 12:31:00–12:33:00 IST (120 seconds).

Two minutes. Use saved normal and timeout routes rather than another long live code tour. If behind, describe just one failure route. The full implementation and exercises remain in the take-home kit.

## Slide 27: Choose control before choosing a framework

Slot 12:33:00–12:36:00 IST (180 seconds).

Three-minute overview only. ReAct is a pattern, LangGraph orchestrates workflows and agents, and CrewAI provides crews and flows. They are not opposites on a deterministic-versus-autonomous scale. One model with two tools often handles lunch plus policy. Multi-agent setup and implementation are optional reference material. Sources: https://docs.langchain.com/oss/python/langgraph/overview and https://docs.crewai.com/en/concepts/crews and https://docs.crewai.com/en/concepts/flows

## Slide 28: Where would YOU give the AI freedom?

Slot 12:36:00–12:40:00 IST (240 seconds).

Four minutes. Give every student one minute to write where the model may choose and where code should check. Optional neighbour comparison follows; sample two answers from different seating areas. Use menu filtering, campus helper and a paid order as design questions. Extra jargon is not a better design. Finish by 12:40.

## Slide 29: Habits you can use in your next project

Slot 12:40:00–12:44:00 IST (240 seconds).

Four minutes. Connect each habit to the change students just made. Requirements before edits, shared instructions/data with distinct roles, narrow diff review, check the final answer and failures. Do not add RAG, deployment, payments, CI configuration or another provider setup. Ainaa recording moves to optional reference discussion after the workshop.

## Slide 30: Checkpoint 4: explain your result

Slot 12:44:00–12:50:00 IST (360 seconds).

Six-minute Checkpoint 4. Each student saves their own note: one useful instruction and how to check it, the budget diff and observed answer or clearly labelled unexecuted prediction, and one review finding/check. Ask for progress signals and sample explanations from different seating areas, including a beginner and a more experienced student where practical. Volunteers may spot-check within zones if available. No individual presenter approval queue. Use a collection channel only if already arranged by the coordinator. If many are unsure, recap model/tool/code and shorten extra framework discussion. Q&A begins at 12:50.

## Slide 31: Questions and your next small project

Slot 12:50:00–13:00:00 IST (600 seconds).

Ten-minute Q&A and close, ending 13:00. Share the GitHub repository URL. It contains the starter, solutions and deeper material. While private, only authorised accounts can access it. Challenge students to extend one small workflow and check a failure. Do not require all five demos as homework. If asked about an untested case, say what remains unknown and how you would check it. No invented demo URLs or product architecture claims.
