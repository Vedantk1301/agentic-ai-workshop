# Agent patterns and communication

## ReAct style

A model chooses a next action, a tool executes, the model observes the result and continues or finishes. An implementation needs a termination limit and permitted tools. Inspect tool events; do not ask for private chain-of-thought. The classroom agent illustrates this loop rather than reproducing all details of the original ReAct paper.

## Graph workflow

Code defines steps and routes around or inside model decisions. Our graph checks hours and invokes an agent only when open. LangGraph supports both explicit workflows and dynamic agents, including multiple agents.

## Sequential team

The menu scout passes facts to a lunch planner. This is a two-task sequence. Two role labels alone do not make a multi-agent implementation; classroom/crew.py constructs actual CrewAI Agent, Task and Crew objects.

## Orchestrator and workers

A coordinator decides which specialist should work and combines its result. For example, a support coordinator can route a question to a menu specialist or a facilities specialist. Dynamic assignment is different from always running scout then planner. This is an optional extension, not the implementation in classroom/crew.py. CrewAI hierarchical processes or a graph can implement manager/worker designs; compare the additional calls with a single agent first.

```text
User -> Coordinator -> Selected specialist(s) -> Coordinator -> Answer
```

## MCP and A2A

MCP standardizes tool discovery and calls. Our local MCP server exposes ordinary functions over stdio. A2A standardizes collaboration between independent agent systems. A manager calling workers inside one process is not automatically an A2A implementation. A2A discovery and distributed task exchange are follow-up topics rather than another live setup.

[ReAct](https://arxiv.org/abs/2210.03629), [LangGraph patterns](https://docs.langchain.com/oss/python/langgraph/workflows-agents), [CrewAI processes](https://docs.crewai.com/en/concepts/processes), [A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/).
