# Workshop setup

Install Python 3.11, one editor and requirements.txt before class using the root README commands. An AI coding editor is optional. Core students need LangChain, the Gemini integration and local MCP support; CrewAI is an optional instructor installation in requirements-instructor.txt.

Run classroom/check_setup.py, then classroom/mcp_probe.py. The first checks the menu/configured package versions. The second discovers and calls the actual local MCP server without a model. Complete installation while internet is available.

## Optional real Gemini access

Open [Google AI Studio](https://aistudio.google.com/), sign in with an eligible account and open API Keys. Use an available project/key or create one through the supported interface. Check that its model and free tier are available to your account. AI Studio access is 18+ and region/account restrictions apply. Limited free-tier quota is not a cash credit and is separate from any coding editor allowance. No billing upgrade or Cloud Console provisioning is part of this lesson.

From the repository root on Windows:

```powershell
Copy-Item classroom/.env.example classroom/.env
notepad classroom/.env
.venv\Scripts\python classroom/check_setup.py --live
```

Put your key only in the private .env file, never in source or a projected terminal command. Set GEMINI_MODEL to a model your account can actually use. The supplied model name is configurable, not a promise of access. Do not reveal .env in a screen share or commit it. Never distribute the instructor key.

For the new learner project, use your_agent/.env instead. Its copied runtime reads the .env beside it. The completed reference reads classroom/.env. A successful check in one folder does not configure the other automatically.

The safe --live check makes a real agent call and verifies a requested menu tool ran. It prints no key or raw provider error. After it succeeds, rehearse classroom/agent.py without --offline, then mcp_agent.py, both graph routes and crew.py if used live. Check the actual final answer as well as tool use. These calls consume your own quota.

## Offline rehearsal

Use --offline on the completed examples, or OFFLINE=True in your new-file lesson. The model is a labelled rule script, while the functions, MCP connection and framework orchestration execute. A recording or scripted output supports explanation but is different from your own live model run.

## Instructor machine already prepared

On Vedant's machine the separate tested environment is C:\vedant-side\workshop\.venv-build-first\Scripts\python.exe. Use it by full path for rehearsal; student instructions stay portable. The earlier demo/.venv remains the previous environment. Do not assume it contains MCP or CrewAI.

## MCP connection

The client launches the local mcp_server.py through sys.executable using an absolute path. No second terminal is required. Keep stdout free for MCP protocol messages; log debugging to stderr. A local process instance belongs to each client; this is the same server code and dataset rather than a centrally deployed campus service.

## Sources

[Google API keys](https://ai.google.dev/gemini-api/docs/api-key), [free-tier information](https://ai.google.dev/gemini-api/docs/billing), [access requirements](https://ai.google.dev/gemini-api/docs/available-regions), [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), [LangChain MCP adapters](https://github.com/langchain-ai/langchain-mcp-adapters) and [CrewAI MCP](https://docs.crewai.com/en/mcp/overview).
