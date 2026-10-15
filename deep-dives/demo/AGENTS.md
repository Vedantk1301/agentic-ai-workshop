# Campus Canteen Assistant

## Purpose

Teach reliable agent design with a fictional canteen. Keep the example small enough for a beginner to explain. Read docs/PROJECT.md for requirements and docs/REVIEW.md for review criteria.

## Project map

- Numbered Python files demonstrate different ways to control the same task.
- canteen/ contains shared tools, rules, model adapters and answer formatting.
- data/ contains the fictional menu records, not instructions to an agent.
- docs/ contains requirements, design explanations and review guidance.
- tests/ checks observable behavior, including failures and invented output.

## Working approach

- State the requirement and acceptance checks before changing code.
- Make one focused change. Inspect the existing code before proposing a replacement.
- Keep the confirmed budget and vegetarian preference separate from model-proposed tool arguments.
- Treat model output as a proposal. Build final factual answers from successfully retrieved, checked records.
- A failed lookup is different from a successful lookup with no matches.
- Ask for a positive whole-number budget when it is missing or invalid.
- Keep the rule-based offline stand-in clearly labelled. Do not describe it as a real model run.

## Verification

From this directory on Windows, run:

```powershell
.venv\Scripts\python -m pytest -q -p no:cacheprovider
.venv\Scripts\python 04_graph_with_agent.py --offline --inject-mistake free_text
```

On macOS/Linux use .venv/bin/python instead. Add a regression case for a behavior bug. Report the actual command and result. State explicitly when a live Gemini call has not been tested.

## Boundaries

Use fictional data. Do not open, print or commit .env or API keys. Keep changes inside this demo project. Do not invent provider features, benchmark numbers or Ainaa implementation claims. Update the relevant docs when behavior or commands change.

These instructions guide the coding assistant. Application code and tests enforce the canteen rules.
