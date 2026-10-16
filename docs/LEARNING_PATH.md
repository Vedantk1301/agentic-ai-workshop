# Continue after your first agent

First finish classroom/README.md: one ordinary function, one LangChain agent, one added tool, then a local MCP call. Explain who requests, executes and returns the result before adding more concepts.

## Explore one pattern at a time

| Question | File |
| --- | --- |
| What is inside the agent loop? | classroom/manual_loop.py |
| How do the same tools cross a process boundary? | classroom/mcp_server.py, mcp_connection.py and mcp_agent.py |
| How can code control a route around an agent? | classroom/graph.py |
| What passes between two real agent roles? | classroom/crew.py |
| How does a manager choose workers? | [Orchestrator and A2A notes](PATTERNS.md) |

ReAct is a pattern. LangChain, LangGraph and CrewAI are frameworks. MCP and A2A are protocols. A graph can contain a ReAct-style agent; a crew can be part of a controlled flow. Framework choice alone does not determine autonomy.

## Add one useful capability

Try a canteen-location tool, a clearer closed response, or a one-agent group lunch proposal. State the goal, change one small piece, inspect it and run a normal and relevant boundary case. Write the useful run command and result in your README. Choose the simplest design that meets your need.

## Optional advanced references

The older starter/, solutions/ and deep-dives/ examples teach answer verification, error versus no-match handling, bounded loops and more elaborate workflows. They use the previous lesson layout and are not the current classroom starting point. Demo 05 in deep-dives is a role simulation; classroom/crew.py is the actual CrewAI example.

Use the longer study guides for APIs, retrieval, memory, evaluation and operations after the workshop. A first-year student is not expected to master those in the two-hour session.
