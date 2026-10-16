# Classroom starter

> Earlier edition, optional reference. For the current build-first workshop start with classroom/README.md from the repository root.


Use the repository-root setup in [README](../README.md). Keep one .venv at the root. All commands below run from that root, not from this folder. Work on your own laptop where available. Sharing is optional; take turns editing and keep an individual note of what you understand.

The instructor will demonstrate a small step, give everyone time to try, then check the room. Show **1 finger: ready, 2: need help, 3: using a saved trace**. A helper may come to you; continue the next reading/review task while waiting. Do not wait for the instructor to inspect every laptop.

Save a copy of [the notes template](workshop_notes.template.md) as `my_workshop_notes.md`, or use paper. Each student records an instruction, a changed line and result, and a review finding. Never put an API key in these notes. Live API setup is optional outside the student activity; all live student commands below use `--offline`.

## Checkpoint 0. Follow one request

```powershell
.venv\Scripts\python starter/agent.py --offline
```

Use .venv/bin/python on macOS/Linux. Read the request, tool arguments, returned records and answer. Which component requests the tool? Which executes it? Why are poha, chicken and dosa excluded? The stand-in is a simulation, not a real AI.

**Ready:** you ran the program and can point to the Rs 60 sandwich and 16:00 closing time. If setup is blocked, open [the saved trace](../deep-dives/demo/saved_runs/02_agent_lunch_and_hours_OFFLINE.txt) and [the menu](data/menu.json). Reading a trace is a fallback, not evidence that your local program ran. Continue the note and review tasks without installing or creating accounts during the activity.

## Checkpoint 1. Write useful Markdown and instructions

Open [the project brief](docs/PROJECT.md), [AGENTS.md](AGENTS.md) and [one menu record](data/menu.json). Explain the difference between requirements, coding instructions and data.

Create a scratch Markdown note with a title, a Requirements heading and two bullets. Then write five concrete instructions. For example:

```markdown
# Canteen change

## Requirements

- Use Rs 30 as the default lunch budget.
- Keep the menu and filtering rules unchanged.
```

Add your best instruction to AGENTS.md without removing the supplied guidance. Ask your coding assistant to identify its loaded rules and inspect its settings if unclear. Instructions guide the coding assistant; the Python API call does not automatically read these files.

**Ready:** record one concrete instruction and how someone could check it. Manual editing is sufficient; a coding-assistant account is optional.

## Checkpoint 2. Make one small change

Before editing, save a copy of agent.py as practice_agent.py in this starter folder. Open the copy. Change only the first QUESTION budget from Rs 80 to Rs 30. Keep the menu, tools and MENU_ONLY_QUESTION unchanged.

Edit manually, or give your coding assistant this focused task:

> Read starter/AGENTS.md and starter/docs/PROJECT.md. In starter/practice_agent.py, change only the default QUESTION budget from Rs 80 to Rs 30. Explain the expected result and show the diff. Keep other requests, tools and data unchanged. Do not make a live API call.

Inspect the proposed lines, then run:

```powershell
.venv\Scripts\python starter/practice_agent.py --offline
```

Expected: no vegetarian food fits Rs 30; the hours are unchanged. Explain why a changed budget should not alter stock. An input-only alternative is to run starter/agent.py --offline --question "veg lunch under Rs 30".

**Ready:** record the changed line and the observed answer. If you could not execute it, write the proposed edit and label your result **predicted, not run**. Ask for help using the room signal; continue to the review exercise while waiting.

If you finish early, run the original starter with --scenario sold_out and --scenario menu_timeout. Explain how no matches differs from a failed source. Compare the [worked solution](../solutions/README.md) after trying.

## Checkpoint 3. Review the actual answer

Complete [the review exercise](../docs/REVIEW.md). Point to the unchecked value and write a behavior check before reading the worked answer. The instructor will demonstrate the corrected graph; you can run it later from the repository root:

```powershell
.venv\Scripts\python deep-dives/demo/04_graph_with_agent.py --offline --inject-mistake free_text
```

The untrusted MODEL PROPOSAL contains the injected mistake. ANSWER uses checked records. The mistake is deliberately simulated.

**Ready:** identify the unchecked value and write an input/output check that would catch it. Everyone can complete this review without Python or an AI account. The instructor demonstrates the graph; running the deeper implementation yourself is optional after class.

## Checkpoint 4. Explain three things

1. A useful instruction and how to check it.
2. The changed line and observed answer.
3. A review finding and the behavior a regression should assert.

Save your own notes. Be ready to explain one answer aloud; you do not need to join a queue for individual instructor approval. Mark which outputs you actually executed. Compare with a neighbour if useful, and swap roles if sharing a device.

Continue with [the learning path](../docs/LEARNING_PATH.md) after class. Optional API setup is in [SETUP](../docs/SETUP.md). Nobody needs to complete all deeper examples during the workshop.
