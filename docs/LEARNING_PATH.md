# Your learning path

## During the workshop

Complete starter/README.md. Show one useful instruction, one budget change plus its output, and one review finding. You need to understand model/tool/code responsibilities before adding more framework vocabulary.

## Afterward: explain the finished change

Compare solutions/ with your work. Explain the one changed default budget and why stock/hours are unchanged. Read the worked review answer and run the checked graph with a deliberately invented message.

## Then: study one design at a time

| Step | Example | Question to answer |
| --- | --- | --- |
| 1 | [Tools and fixed workflow](../deep-dives/demo/01_tools_and_fixed_workflow.py) | Which decisions does ordinary code make? |
| 2 | [Agent loop](../deep-dives/demo/02_react_agent.py) | Which allowed tool does the model request next? |
| 3 | [Explicit graph](../deep-dives/demo/03_langgraph_flow.py) | Where are state, routes, clarification and retry limits? |
| 4 | [Agent inside a graph](../deep-dives/demo/04_graph_with_agent.py) | How are proposals checked before reaching the user? |
| 5 | [Role-team simulation](../deep-dives/demo/05_team_of_roles.py) | Does splitting responsibilities help this problem? |

ReAct is a pattern, LangGraph orchestrates workflows and agents, and CrewAI provides crews and flows. Framework choice and degree of autonomy are separate decisions. Demo 05 is a plain-Python role simulation; its output is not a live multi-agent benchmark.

## Build one extension

Try the [three exercises](../deep-dives/demo/exercises/README.md). Add a tool first; verify an incorrect output next; then implement the closed-canteen shortcut. Write requirements, inspect the diff and test a boundary/failure case. The worked graph solution is checked by a test that executes its documented code.

## Go deeper when you need it

The [study guide](../deep-dives/guides/Agentic%20AI%20Study%20Guide.md) covers programming/API foundations, models, context, tools, workflows, MCP, retrieval, memory, evaluation and operations. Use the [practice questions](../deep-dives/guides/Practice%20and%20Answer%20Key.md) before reading answers. These are optional learning resources, not a claim you should master every topic in two hours.

For a real project, choose a clear data source, verify freshness and permissions, trace failures, measure behavior on realistic requests, and add human approval where actions require it. Start with the simplest architecture that meets the need.
