# Live run sheet

**Event:** Hands-on Workshop on Agentic AI, Dept. of IT, VIT Mumbai
**When:** Saturday 17 October 2026, 13:30-15:00 IST (90 minutes), Lab 05
**Speaker:** Vedant Kakade
**Deck (source of truth):** https://claude.ai/artifact/9gCUF7bUg4wzA6gjYpGTaN

Generated from the deck's speaker notes. If the deck changes, regenerate this file instead of editing it by hand.

| # | Time | Min | Screen | Slide | Commands |
| ---: | --- | ---: | --- | --- | --- |
| 1 | 13:30 | 1 | Slides | Build your first AI agent. |  |
| 2 | 13:31 | 1 | Slides | Vedant Kakade |  |
| 3 | 13:32 | 2 | Slides | You have ₹80 and ten minutes before your next lecture. |  |
| 4 | 13:34 | 2 | Slides | A model answers. An agent gets it done. |  |
| 5 | 13:36 | 2 | Slides | Every agent has four parts. |  |
| 6 | 13:38 | 2 | Slides | Think, act, observe. Repeat. |  |
| 7 | 13:40 | 2 | Slides | Agents went to work. |  |
| 8 | 13:42 | 3 | Slides | Three choices behind every AI system. |  |
| 9 | 13:45 | 2 | Slides | An AI stylist for Indian fashion. |  |
| 10 | 13:47 | 1 | Slides | What sits behind the chat box. |  |
| 11 | 13:48 | 2 | Slides | Recipes with receipts. |  |
| 12 | 13:50 | 1 | Slides | Ainaa gets flexibility. Kranti gets control. |  |
| 13 | 13:51 | 1 | Editor (your_agent) | Let’s build one. Together. | `python tools/start_here.py` |
| 14 | 13:52 | 2 | Slides | Who does what? |  |
| 15 | 13:54 | 1 | Slides | Our whole canteen, in four rows. |  |
| 16 | 13:55 | 5 | Editor (your_agent) | A tool is just a function. | `python menu_tools.py` |
| 17 | 14:00 | 2 | Editor (your_agent) | Bring in the pieces. |  |
| 18 | 14:02 | 4 | Editor (your_agent) | Hand the function to a model. | `python my_agent.py` |
| 19 | 14:06 | 2 | Slides | What actually happened. |  |
| 20 | 14:08 | 8 | Slides | Give it a second ability. | `python my_agent.py` |
| 21 | 14:16 | 3 | Terminal (repo root) | Three minutes. | `python classroom/mcp_probe.py` |
| 22 | 14:19 | 2 | Slides | Write the tool once. Plug it in anywhere. |  |
| 23 | 14:21 | 2 | Terminal (repo root) | Same tools, now over MCP. | `python classroom/mcp_agent.py --offline`<br>`python classroom/mcp_probe.py` |
| 24 | 14:23 | 1 | Slides | When to use what. |  |
| 25 | 14:24 | 3 | Slides | Give the model only the control it needs. |  |
| 26 | 14:27 | 2 | Slides | Every pattern has a weakness. |  |
| 27 | 14:29 | 3 | Terminal (repo root) | What if the canteen is closed? | `python classroom/graph.py --offline` |
| 28 | 14:32 | 3 | Slides | A scout hands off to a planner. | `python classroom/crew.py --offline` |
| 29 | 14:35 | 4 | Slides | Pick one. Choose the design. Name one way it fails. |  |
| 30 | 14:39 | 2 | Slides | The reason matters more than the label. |  |
| 31 | 14:41 | 2 | Slides | What agents still get wrong. |  |
| 32 | 14:43 | 2 | Terminal (repo root) | Prompts guide. Code enforces. | `python classroom/safety_demo.py` |
| 33 | 14:45 | 2 | Slides | Agents that learn on the job. |  |
| 34 | 14:47 | 2 | Slides | Where this is heading. |  |
| 35 | 14:49 | 1 | Slides | What to do after today. |  |
| 36 | 14:50 | 10 | Slides | Your agent is 30 lines long. What will you give it next? |  |

Editor commands run inside your_agent/ (or your demo_agent/). Commands starting with classroom/ run from the repository root.
