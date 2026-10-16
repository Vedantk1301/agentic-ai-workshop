# VIT Agentic AI Workshop Curriculum

**Event:** Hands-on Workshop on Agentic AI, Dept. of IT, VIT Mumbai
**When:** Saturday 17 October 2026, 13:30-15:00 IST (90 minutes), Lab 05
**Speaker:** Vedant Kakade
**Deck (source of truth):** https://claude.ai/artifact/9gCUF7bUg4wzA6gjYpGTaN

Generated from the deck's speaker notes. If the deck changes, regenerate this file instead of editing it by hand.

## Goals

Students with no agent experience leave able to:

- Explain an agent as model + tools + instructions + loop, and why the model only requests while code executes.
- Write a Python tool, give it to a LangChain agent, and add a second tool themselves.
- See the same tools reused through MCP, inside a LangGraph workflow, and by a two-agent CrewAI team.
- Decide who should control each step (code or model), and name the limits and failure modes of each design.

## Timetable

| Time | Min | Slides | Block |
| --- | ---: | --- | --- |
| 13:30-13:34 | 4 | 1-3 | Who is speaking, and the ₹80 lunch problem. |
| 13:34-13:51 | 17 | 4-12 | What agentic AI is, the industry in 2026, and two real products. |
| 13:51-14:19 | 28 | 13-21 | Live build in your_agent/: function, tool, agent, second tool. |
| 14:19-14:23 | 4 | 22-23 | MCP: write a tool once, plug it into any agent. |
| 14:23-14:41 | 18 | 24-30 | When to use what: grounding, control and organisation, with a group design activity. |
| 14:41-14:45 | 4 | 31-32 | Reliability, cost and failure, and how code keeps control. |
| 14:45-15:00 | 15 | 33-36 | Agents that learn on the job, the 2027 direction, and what to learn next. |

Total: 90 minutes, including a 3-minute stretch at 14:16 and 10 minutes of Q&A.

## Student build (your_agent/)

1. menu_tools.py: find_food(max_price, vegetarian), run directly. No AI yet.
2. my_agent.py: create_agent with one tool, OFFLINE=True scripted brain unless a tested live key is configured.
3. Your turn (8 min): add get_canteen_hours, change the import, tool list and question; try a Rs 30 budget.

Full step-by-step instructions, expected output and "Try this" experiments: classroom/README.md. Checkpoints: classroom/first_agent_checkpoint.py and classroom/agent.py.

## Instructor demos (repository root)

MCP probe and agent, LangGraph open/closed routes, CrewAI scout-to-planner handoff, safety allowlist. Exact commands are in the run sheet. Use --offline unless the live key was tested the same day; say clearly that offline mode is a scripted brain with real tools and framework plumbing.

## If running late

Protect the student build (slides 16-20) and Q&A. Cut in this order: skip "Inside Ainaa" (slide 10), flash the cheat sheet (slide 26), read the saved CrewAI output instead of running it (classroom/saved_runs/crew.txt), shorten the 2027 slides.

## Before class

- Two terminal tabs: Tab A in your own learner folder (python tools/start_here.py demo_agent), Tab B at the repository root.
- VS Code font 24+; switch full screen between slides and editor, never split screen.
- Confirm the workshop Python on the lab machines ($py in the README) and how the kit ZIP reached students.
- Optional: a printed A4 copy of the menu for slide 14.
