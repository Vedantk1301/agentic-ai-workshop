# Workshop repository instructions

## Purpose and map

Teach beginners to build a small canteen agent in a new file, add a tool, reuse it through MCP and compare LangChain, LangGraph and CrewAI. Read README.md and classroom/README.md. classroom/ is the current lesson and checkpoints; starter/, solutions/ and deep-dives/ are optional references from the previous edition; docs/ explains setup and follow-up.

## Working rules

- Make one focused change and explain its intended result before editing.
- Keep user constraints separate from model-proposed tool arguments.
- Treat instruction files as coding guidance, not runtime enforcement.
- Keep fictional menu records unchanged unless a task explicitly changes the dataset.
- A successful empty lookup and a failed source have different meanings.
- Check the exact answer reaching the user. A schema-valid field does not validate a separate paragraph.
- Label the offline stand-in, role simulation and injected mistakes honestly.
- Do not open, print, commit or transmit .env files or API keys. Only blank .env.example templates belong in Git.
- Do not change repository visibility or publish elsewhere as part of an ordinary code task.

## Verification

From the repository root on Windows:

```powershell
.venv\Scripts\python tools/verify_workshop.py
.venv\Scripts\python -m pytest classroom/tests deep-dives/demo/tests -q -p no:cacheprovider
```

Install requirements-instructor.txt for the CrewAI integration check, or select -k "not crew" for the core suite. Use .venv/bin/python on macOS/Linux. Report actual commands/results and untested live behavior. Add a behavior regression for a bug; keep docs consistent with commands and paths.
