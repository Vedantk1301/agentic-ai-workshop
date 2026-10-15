# Agentic AI Workshop Quick Reference

Use this after working through the study guide. Its purpose is to help recall component roles and explain the canteen request during rehearsal.

## Component roles

| Component | Responsibility |
| --- | --- |
| Gemini | Interprets context and produces responses or proposed tool calls |
| Application runtime | Validates, authorises and executes allowed operations |
| Menu tool | Reads records and applies exact filtering rules |
| LangChain | Supplies integrations and the agent interface |
| LangGraph | Supports explicit stateful orchestration and persistence |
| MCP client | Communicates with an MCP server |
| MCP server | Exposes capabilities and context through the protocol |
| Antigravity | Helps develop and review code |
| Google Cloud | Hosts configured services and model access through the chosen backend |

## The request trace

User question -> application supplies context -> model requests a tool -> application validates and runs it -> tool returns records -> model responds -> application checks important output fields.

The model selects a proposed action. The application executes it. The tool result is an observation; a plan or a confident sentence is not proof of execution.

## Distinctions to remember

- Prompting supplies instructions; training changes model parameters.
- Structured output checks form; business validation checks allowed and correct values.
- A workflow fixes routing in code; an agent allows more dynamic model decisions.
- MCP connects capabilities; it does not provide intelligence or automatic trust.
- RAG retrieves supporting information; memory retains information across interactions.
- Authentication identifies a caller; authorisation determines its permissions.
- CLI configuration and application credentials need separate verification.
- A budget alert notifies; it is not a hard spending cap.
- An empty result is successful with no matches; a timeout is a failed observation.

## Failure checklist

| Symptom | First things to inspect |
| --- | --- |
| Wrong food or price | Actual records, filter arguments and final answer validation |
| Tool never called | Registration, description, user request and observed response |
| MCP will not connect | Transport, process or endpoint, discovery and server logs |
| Stdio messages corrupted | Diagnostic output accidentally written to stdout |
| Permission error | Runtime identity, backend, project, model and granted permissions |
| Quota error | Active project and model limits, request frequency and retries |
| Repeated tool loop | Stop condition, step limit, duplicate requests and failures |
| Slow run | Number of model calls, tool latency and growing context |
| Duplicate order | Retry behavior and idempotency contract |

## A short opening

"We'll build a small agent that answers questions about a canteen menu. You'll see how it requests a tool, where that code runs, and how MCP lets us expose the same capability through a standard connection."

## A response when you do not know

"I haven't tested that case. Here is how I would investigate it." Explain a useful check, without turning an assumption into a claim of tested behavior.

## Official references

[LangChain agents](https://docs.langchain.com/oss/python/langchain/agents), [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview), [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture), [Google integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai), [Gemini quotas](https://ai.google.dev/gemini-api/docs/rate-limits), [Google authentication](https://docs.cloud.google.com/docs/authentication/application-default-credentials), [Cloud budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets).
