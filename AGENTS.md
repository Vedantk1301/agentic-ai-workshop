# Workshop repository instructions

## Purpose and map

Teach beginners to specify, review and check a fictional canteen assistant. Read README.md and docs/LEARNING_PATH.md. starter/ is the classroom project; solutions/ holds worked answers; deep-dives/ holds optional implementations and guides; docs/ explains the method.

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
.venv\Scripts\python -m pytest deep-dives/demo/tests -q -p no:cacheprovider
```

Use .venv/bin/python on macOS/Linux. Report actual commands/results and untested live behavior. Add a behavior regression for a bug; keep docs consistent with commands and paths.
