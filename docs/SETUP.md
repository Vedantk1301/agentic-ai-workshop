# Setup and optional AI Studio access

## Local environment

Install Python 3.11 and one editor. Clone or download/extract the repository. Use the root README commands to create one root .venv and install requirements.txt. Activation is optional; the documented commands call the environment's Python directly.

Run starter/agent.py with --offline once before class. Offline examples need no account or key after dependencies are installed. The core exercises can also use a paired laptop or printed trace.

## Optional Gemini API setup

1. Sign into [Google AI Studio](https://aistudio.google.com/) with an eligible account. AI Studio access is 18+. Continue offline if access is unavailable.
2. Open API Keys. New users may already have a default project/key; otherwise create a key through AI Studio's interface.
3. Check the project's tier and available model/quota. The supplied default is gemini-3.6-flash. Free-tier access is limited and account/model dependent. No billing upgrade or credit purchase is required for core activities.
4. In starter/, copy .env.example to .env only if you do not already have a configured file. Edit it privately, filling GOOGLE_API_KEY and keeping a supported GEMINI_MODEL. Never paste a real key into Markdown, source code, a shared chat or a projected screen.
5. From the repository root, run the setup check and then the actual agent. These commands make live API calls when configured:

```powershell
.venv\Scripts\python starter/check_setup.py
.venv\Scripts\python starter/agent.py
```

Use .venv/bin/python on macOS/Linux. A text call alone does not establish agent tool-calling compatibility. If access/quota fails, add --offline and continue; a key does not guarantee free calls. The initial repository checks did not exercise live Gemini.

Each independent example loads its own local .env: starter/.env, solutions/budget-30/.env or deep-dives/demo/.env. For the workshop, configure only starter/.env if choosing live use. Do not copy keys into the repository history.

## Coding assistant

Antigravity is optional; manual edits work. Its sign-in is separate from the Python application's API key. Inspect the loaded project rules for your installed client/version. The supplied AGENTS.md is shared coding guidance, with CLAUDE.md/GEMINI.md entry points for their clients. Ordinary provider API calls do not automatically read these files.

Official references: [API keys](https://ai.google.dev/gemini-api/docs/api-key), [free tier](https://ai.google.dev/gemini-api/docs/billing), [access](https://ai.google.dev/gemini-api/docs/available-regions), [Antigravity rules](https://www.antigravity.google/docs/rules).
