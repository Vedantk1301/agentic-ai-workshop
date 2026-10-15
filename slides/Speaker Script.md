# Classroom speaker script

Trimmed 31-slide edition, 15 October 2026. Planned 120-minute slots, including a five-minute break and ten-minute Q&A. Rehearse with a timer. Use Classroom Follow Along.md for student tasks. The 53-slide v3 deck is optional reference.

## Slide 1: VIT MUMBAI  ·  17 OCTOBER 2026

Slot 11:00:00–11:01:00 IST (60 seconds).

Welcome. Today each pair will write useful project instructions, change one request in a prepared program, and review an incorrect answer. We are following one canteen example. You do not need to learn every framework today.

## Slide 2: You have ₹80.
Attendance in 10 minutes.
You're hungry.

Slot 11:01:00–11:03:00 IST (120 seconds).

Ask which facts the assistant needs: budget, diet, stock and hours. Take three answers. Students can use a laptop in pairs or follow on paper. Do not assume everyone completed the earlier workshop setup.

## Slide 3: Overconfident AI recommends…

Slot 11:03:00–11:06:00 IST (180 seconds).

Introduce Canteen Bhaiya and Overconfident AI briefly. Let pairs find the nonexistent wrap. This is a constructed bad answer, not a measured Gemini failure. Point out the real sandwich, sold-out poha, non-vegetarian chicken and over-budget dosa. Ask one student to explain the problem.

## Slide 4: AI writes the order slip. Code makes the food.

Slot 11:06:00–11:10:00 IST (240 seconds).

Slowly trace model request, application execution and tool result. Use the order-slip analogy. A tool is ordinary code. A model can request a tool but does not directly run Python. Ask a student who actually reads the menu. If the answer is unclear, repeat this diagram instead of adding MCP terminology.

## Slide 5: Google AI Studio setup

Slot 11:10:00–11:14:00 IST (240 seconds).

Four-minute demonstration, not a room-wide account troubleshooting exercise. Open AI Studio with a separate workshop account and show API Keys. New users may already have a default project/key. Otherwise create a key in the AI Studio interface. Check that the project/model has free-tier access. No Cloud Console provisioning, billing upgrade or credit purchase. Do not reveal a real key. Account access and quotas vary. Source: https://ai.google.dev/gemini-api/docs/api-key and https://ai.google.dev/gemini-api/docs/billing

## Slide 6: Connect the prepared Python demo

Slot 11:14:00–11:17:00 IST (180 seconds).

Show .env.example with a blank key on the projector. Explain that students privately copy their own key to .env as GOOGLE_API_KEY. Do not type, show or distribute your own key. A pre-recorded or masked demonstration is enough. Run check_setup.py privately before class; on stage only use a configured demo. Signing into Antigravity and configuring this API key are separate steps. If setup fails, continue with --offline. AI Studio is 18+; ineligible students use offline/paper. Sources: https://ai.google.dev/gemini-api/docs/api-key and https://ai.google.dev/gemini-api/docs/available-regions

## Slide 7: Checkpoint: open the project folder

Slot 11:17:00–11:20:00 IST (180 seconds).

Three-minute checkpoint. Students should have installed dependencies before class. Open starter/README.md. From the repository root run starter/agent.py --offline. Explain that it is a rule-based stand-in using the real agent/tool plumbing, not a real AI. If a pair is blocked, pair them with a working laptop or use the printed trace. Do not spend the next section repairing installations.

## Slide 8: Give each file one job

Slot 11:20:00–11:23:00 IST (180 seconds).

Show these files inside starter/. Explain each reader and purpose. Tests are in deep-dives/demo/tests/ for later practice. Ask: where does stock belong? Where does the run command belong? Do not lecture on every folder or require everyone to create an empty repository.

## Slide 9: Markdown basics

Slot 11:23:00–11:26:00 IST (180 seconds).

Three minutes. Type a title, a Requirements heading and two bullet points in a scratch Markdown file. Show preview. Add one fenced command example if the room is ready. Ask pairs to write one clear requirement. Avoid teaching Markdown extensions or front matter.

## Slide 10: Write the outcome before asking for code

Slot 11:26:00–11:29:00 IST (180 seconds).

The change is intentionally small. A first-year student can understand the budget change. A senior student should explain the evidence and failure cases. Read the three checks aloud. Do not expand this into a full new chatbot build.

## Slide 11: Useful instructions for an AI coder

Slot 11:29:00–11:32:00 IST (180 seconds).

Read the existing AGENTS.md. Demonstrate one shared instruction file in the active client. Current Antigravity supports workspace AGENTS.md and GEMINI.md; check loaded rules for the installed version. Mention CLAUDE.md for Claude Code and GEMINI.md for Gemini CLI in one sentence only. Do not install three clients. These files guide a coding assistant; the Python demo does not automatically read them. Source: https://www.antigravity.google/docs/rules

## Slide 12: Pair task: write five useful lines

Slot 11:32:00–11:36:00 IST (240 seconds).

Four minutes of actual student work. Each pair writes five instruction lines in a scratch file or on paper, then adds its best project-specific line to the supplied AGENTS.md. Do not replace existing instructions. Ask two pairs to read a line and explain how a reviewer could check it. If they are stuck, start with “Do not change menu records to make a test pass.”

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

Run starter/agent.py --pause with Gemini only if tested beforehand; otherwise add --offline and explicitly disclose the rule-based stand-in. The pause reveals an already-completed trace. Ask for predictions, then reveal tool requests/results. A real model may group or reorder calls. Keep this demonstration to five minutes.

## Slide 17: Pair task: make one small code change

Slot 11:52:00–12:00:00 IST (480 seconds).

Eight minutes. Follow starter/README.md. Copy starter/agent.py to starter/practice_agent.py. Change only the first QUESTION budget from Rs 80 to Rs 30, manually or using a coding assistant. Do not change MENU_ONLY_QUESTION, tools or data. Run the copy with --offline. Compare before/after and explain why nothing qualifies. Advanced pairs try --scenario sold_out and --scenario menu_timeout. Check two pairs can explain the result before moving on. Finish by 12:00.

## Slide 18: 5-minute break

Slot 12:00:00–12:05:00 IST (300 seconds).

Five-minute break, 12:00–12:05. Return at 12:05. Open the review exercise and demo 04. If installation issues remain, use a working pair/paper route after the break.

## Slide 19: Review the path to the user

Slot 12:05:00–12:08:00 IST (180 seconds).

Three minutes. Show the one-line budget diff first. Then introduce the review order: requirement, changed lines, input/tool values, failure, final text. A downloaded ZIP is not a Git repository. Use the editor comparison view. Git is optional and not a new installation topic.

## Slide 20: 24 tests passed. The answer was still wrong.

Slot 12:08:00–12:12:00 IST (240 seconds).

Four minutes. The original 24 tests passed, but the model message could still contain a fake dish. Only the recommended_dishes list was checked. Ask a student to point to the value actually returned to the user. More passing tests alone do not prove correctness.

## Slide 21: Pair review: find the unchecked value

Slot 12:12:00–12:18:00 IST (360 seconds).

Six minutes. Use the one-page Review Exercise.pdf. Ask pairs to identify the unsafe return, describe a correcting change, and write one expected input/output check. Let them work before showing the worked answer. No API call or AI account is needed. Take two answers. A rule in AGENTS.md alone does not fix the program.

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

Three minutes. Follow one normal route and one failed lookup route. Missing/invalid budget asks and ends this run; failure retries at most twice. No durable resumption is configured. Explicit graph structure can contain flexible agents. Ask which decision code should enforce.

## Slide 26: Demo 3: one graph, four routes

Slot 12:31:00–12:33:00 IST (120 seconds).

Two minutes. Use saved normal and timeout routes rather than another long live code tour. If behind, describe just one failure route. The full implementation and exercises remain in the take-home kit.

## Slide 27: Choose control before choosing a framework

Slot 12:33:00–12:36:00 IST (180 seconds).

Three-minute overview only. ReAct is a pattern, LangGraph orchestrates workflows and agents, and CrewAI provides crews and flows. They are not opposites on a deterministic-versus-autonomous scale. One model with two tools often handles lunch plus policy. Multi-agent setup and implementation are optional reference material. Sources: https://docs.langchain.com/oss/python/langgraph/overview and https://docs.crewai.com/en/concepts/crews and https://docs.crewai.com/en/concepts/flows

## Slide 28: Where would YOU give the AI freedom?

Slot 12:36:00–12:40:00 IST (240 seconds).

Four minutes. One minute pair discussion: where would you allow a model to choose, and where should code check? Use menu filtering, campus helper and a paid order only as design questions. Take two answers. Extra jargon is not a better design. Finish by 12:40.

## Slide 29: Habits you can use in your next project

Slot 12:40:00–12:44:00 IST (240 seconds).

Four minutes. Connect each habit to the change students just made. Requirements before edits, shared instructions/data with distinct roles, narrow diff review, check the final answer and failures. Do not add RAG, deployment, payments, CI configuration or another provider setup. Ainaa recording moves to optional reference discussion after the workshop.

## Slide 30: Show what you learned

Slot 12:44:00–12:50:00 IST (360 seconds).

Six minutes. Each pair submits or shows: one useful instruction, the changed budget line with the resulting answer, and one review finding/check. Ask one first-year and one senior pair to explain in plain language. This is an exit check, not a promise everyone has mastered agents. If many are unsure, recap model/tool/code instead of introducing extra concepts.

## Slide 31: Questions and your next small project

Slot 12:50:00–13:00:00 IST (600 seconds).

Ten-minute Q&A and close, ending 13:00. Share the GitHub repository URL. It contains the starter, solutions and deeper material. While private, only authorised accounts can access it. Challenge students to extend one small workflow and check a failure. Do not require all five demos as homework. If asked about an untested case, say what remains unknown and how you would check it. No invented demo URLs or product architecture claims.
