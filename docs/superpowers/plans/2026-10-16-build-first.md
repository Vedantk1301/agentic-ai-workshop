# Build First Workshop Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement these tasks in this session. User authorised rebuilding the complete kit after reviewing the revised curriculum.

**Goal:** Deliver a coherent two-hour beginner workshop with a first agent build, common MCP tools, three framework examples, slides and rehearsal instructions.

**Architecture:** A self-contained classroom directory has ordinary menu functions, small framework clients and a local stdio MCP server. Scripted model fallbacks exercise real framework/tool plumbing without claiming live AI. Existing advanced material remains available after class.

**Tech stack:** Python 3.11, the existing pinned LangChain/LangGraph/Gemini packages, compatible MCP adapters and CrewAI; Artifact Tool for editable slides; PowerPoint PDF export.

**Spec:** C:/vedant-side/workshop/VIT Workshop Curriculum.md, approved by the user's instruction to rebuild all materials.

## Global constraints

- 120 minutes, Saturday 17 October 2026, 11:00-13:00 IST; five-minute break and ten-minute Q&A.
- Beginner audience, possible 100-200 students. Build one agent; demonstrate graph and team.
- Preserve the four fictional menu records and label the 12:30 fixture clock.
- All writes inside C:/vedant-side/workshop. Preserve personal practice files. Keep GitHub private.
- Never open, print, commit or distribute credentials. Live API tests require privately configured eligible access.
- One common MCP program and contract for all three framework clients. A scripted brain must be explicitly labelled.

## Review focus

1. A new learner folder works without hidden imports or files from the old environment.
2. MCP calls execute across a real stdio boundary and match direct tool results.
3. Closing-time boundary and closed route do not accidentally run the lunch agent.
4. Unknown tool requests and endless model loops cannot execute arbitrary code or run forever.
5. The CrewAI demo uses actual CrewAI tasks/agents and passes its scout output to the planner.

## Task 1: Small tools and a first agent

Files: classroom/menu_tools.py, agent.py, workshop_runtime.py, offline_brain.py, manual_loop.py, data/menu.json; classroom/tests/test_classroom.py.

Interfaces: find_food(max_price: int, vegetarian: bool = True) -> dict; get_canteen_hours(at: str = '12:30') -> dict; build_agent(offline: bool = False, with_hours: bool = True); run_loop(model, question, tools, max_steps=6) -> list.

- [x] Write tests for Rs 80 sandwich, Rs 30 no match, nonvegetarian requests, invalid budgets, hours boundaries, tool calls and refusal of unregistered tools.
- [x] Run pytest classroom/tests -q and observe missing implementation failures.
- [x] Implement the small ordinary functions and LangChain agent. Keep the first agent file readable and run configurable questions. Scripted fallback uses actual returned data.
- [x] Run direct tools, menu-only agent, two-tool agent and bounded manual loop tests.

Example behavioral check:

```python
assert find_food(80)['matches'] == [{'name': 'Veg sandwich', 'price': 60}]
assert find_food(30)['matches'] == []
assert get_canteen_hours('16:00')['open_now'] is False
```

## Task 2: Common MCP and framework comparisons

Files: classroom/mcp_server.py, mcp_connection.py, mcp_agent.py, graph.py, crew.py, crew_brain.py; integration tests.

Consumes the two Task 1 functions. Produces the local server, real MCP-connected LangChain agent, graph with one hours branch and actual sequential CrewAI tasks.

- [x] Write and run integration tests for discovery and direct/result equivalence, both graph routes and a real offline CrewAI handoff.
- [x] Implement MCP server registration and clients with sys.executable and an absolute local server path.
- [x] Use async context management for MCP and close connections after use. Treat unexpected tool errors as errors, not no-match results.
- [x] Exercise each framework with a labelled scripted model. Verify actual MCP payloads and task context, rather than only matching printed role names.
- [x] Pin resolved versions; keep CrewAI in an optional instructor requirement file if its dependency set is heavier.

## Task 3: A new-file learner route and rehearsal

Files: classroom/README.md, tools/start_here.py, classroom/check_setup.py, docs/SETUP.md, ROOM_GUIDE.md, LEARNING_PATH.md, AI_CODING.md, COORDINATOR_MESSAGE.md, root README and instruction files; local preparation guide.

- [x] Make start_here.py create a fresh local learner directory with data/config/fallback support and empty learner application files. Refuse to overwrite a nonempty destination.
- [x] Provide exact small code additions, copyable run commands, expected results and checkpoints. Keep AI coding optional.
- [x] Show the student the first function, then create_agent, then a second tool; MCP follows that result.
- [x] Smoke-test the documented commands from a freshly generated workspace, including a path with spaces.
- [x] Provide a slide/editor switch sheet, API-key setup without displaying secrets, time cuts and backup commands.

## Task 4: Slides and aligned documentation

Files: local slides/build_first_content.json, build_first.mjs, slide-switch run sheet, Speaker Script.md; final PPTX/PDF and curriculum PDF; repository slides copies.

- [x] Write a compact deck with one idea per slide, runnable code excerpts and explicit editor switches. Speaker notes have timings, spoken explanations, student activity and fallback.
- [x] Ensure slide slots sum to 7200 seconds and match the approved block boundaries.
- [x] Build using Artifact Tool, validate structure/fonts/geometry, export through PowerPoint, render and inspect every slide.
- [x] Fix rendering problems and repeat affected checks. Promote only verified final files.
- [x] Update current curriculum/kit status to distinguish tested local integrations from untested Gemini calls.

## Task 5: Review and delivery

- [x] Run the old regression suite plus new classroom/integration checks and pip check.
- [x] Use one fresh read-only reviewer for the completed branch. Fix material issues with targeted regression checks.
- [x] Check for credentials, environments and generated caches in tracked files. Keep private visibility.
- [x] Commit the coherent kit, update the authorised private repository, verify CI and export an exact git archive ZIP.
- [x] Show the final slides and give Vedant one clear starting instruction for rehearsal. Report live-model limitations precisely.

Execution record: 62 behavior/integration tests and11 CLI checks passed locally; pip check is clean. The fresh read-only review has no remaining P1/P2 findings after fixes. Slides were rendered in PowerPoint and visually checked. Live Gemini remains untested pending a private configured key; actual delivery pace needs a timed rehearsal.
