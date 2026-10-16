# Live run sheet

**Event:** Hands-on Workshop on Agentic AI, Dept. of IT, VIT Mumbai
**When:** Saturday 17 October 2026, 13:30-15:00 IST (90 minutes), Lab 05
**Speaker:** Vedant Kakade
**Deck (source of truth):** https://claude.ai/artifact/9gCUF7bUg4wzA6gjYpGTaN

Generated from the deck's speaker notes. If the deck changes, regenerate this file instead of editing it by hand.

| # | Time | Min | Screen | Slide | Commands |
| ---: | --- | ---: | --- | --- | --- |
| 1 | 13:30 | 1 | Slides | Build your first AI agent. |  |
| 2 | 13:31 | 4 | Slides | Vedant Kakade |  |
| 3 | 13:35 | 2 | Slides | You have ₹80 and ten minutes before your next lecture. |  |
| 4 | 13:37 | 2 | Slides | A model answers. An agent gets it done. |  |
| 5 | 13:39 | 2 | Slides | Every agent has four parts. |  |
| 6 | 13:41 | 2 | Slides | Think, act, observe. Repeat. |  |
| 7 | 13:43 | 2 | Slides | Agents went to work. |  |
| 8 | 13:45 | 3 | Slides | Three choices behind every AI system. |  |
| 9 | 13:48 | 2 | Slides | An AI stylist for Indian fashion. |  |
| 10 | 13:50 | 2 | Slides | Recipes with receipts. |  |
| 11 | 13:52 | 1 | Slides | Ainaa gets flexibility. Kranti gets control. |  |
| 12 | 13:53 | 1 | Editor (your_agent) | Let’s build one. Together. |  |
| 13 | 13:54 | 2 | Slides | Who does what? |  |
| 14 | 13:56 | 1 | Slides | Our whole canteen, in four rows. |  |
| 15 | 13:57 | 5 | Editor (your_agent) | A tool is just a function. | `python menu_tools.py` |
| 16 | 14:02 | 2 | Editor (your_agent) | Bring in the pieces. |  |
| 17 | 14:04 | 4 | Editor (your_agent) | Hand the function to a model. | `python my_agent.py` |
| 18 | 14:08 | 2 | Slides | What actually happened. |  |
| 19 | 14:10 | 8 | Slides | Give it a second ability. |  |
| 20 | 14:18 | 3 | Slides | Three minutes. |  |
| 21 | 14:21 | 2 | Slides | Write the tool once. Plug it in anywhere. |  |
| 22 | 14:23 | 2 | Terminal demo (your_agent) | Same tools, now over MCP. | `python ../classroom/mcp_agent.py --offline`<br>`python ../classroom/mcp_probe.py` |
| 23 | 14:25 | 1 | Slides | When to use what. |  |
| 24 | 14:26 | 3 | Slides | Give the model only the control it needs. |  |
| 25 | 14:29 | 1 | Slides | Every pattern has a weakness. |  |
| 26 | 14:30 | 2 | Slides | State, nodes, edges. |  |
| 27 | 14:32 | 2 | Terminal demo (your_agent) | What if the canteen is closed? | `python ../classroom/graph.py --offline` |
| 28 | 14:34 | 1 | Slides | Agents, tasks, a crew. |  |
| 29 | 14:35 | 2 | Terminal demo (your_agent) | A scout hands off to a planner. | `python ../classroom/crew.py --offline` |
| 30 | 14:37 | 4 | Slides | Pick one. Choose the design. Name one way it fails. |  |
| 31 | 14:41 | 2 | Slides | The reason matters more than the label. |  |
| 32 | 14:43 | 2 | Slides | What agents still get wrong. |  |
| 33 | 14:45 | 2 | Terminal demo (your_agent) | Prompts guide. Code enforces. | `python ../classroom/safety_demo.py` |
| 34 | 14:47 | 2 | Slides | Agents that learn on the job. |  |
| 35 | 14:49 | 1 | Slides | Where this is heading. |  |
| 36 | 14:50 | 3 | Slides | What I’d do in your place. |  |
| 37 | 14:53 | 7 | Slides | Your agent is 30 lines long. What will you give it next? |  |
| 38 | 15:00 | 0 | Slides | Thank you. |  |

Everything runs in ONE terminal inside your learner folder (your_agent/ or demo_agent/). Demo commands reach the ready-made scripts with ../classroom/. Use the .venv-build-first Python for the CrewAI demo.
