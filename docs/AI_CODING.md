# Use a coding assistant for one understandable change

Build the first tool and agent using classroom/README.md. A coding assistant is optional. Give it a small goal after you understand the starting code, for example:

```text
Read menu_tools.py and my_agent.py. Explain how a tool result reaches the model.
Then propose a canteen-location tool. Show the change before applying it.
Keep menu data and API configuration unchanged. Report what you ran.
```

Review the new function, its registration and its output. Run the tool directly, then ask the agent a question that needs it. A confident explanation is not evidence that code ran. Ask for the actual command and result.

## Small project documentation

README.md: what the project does and how to run it. data/menu.json: fictional records. Python: behavior. A supported coding instruction file: clear project rules. Use a heading, bullets and a run command; keep secrets out.

AGENTS.md, CLAUDE.md and GEMINI.md are client conventions with differing support. Check what your chosen client actually reads. Markdown instructions guide an assistant; runtime allowlists, validation and loop limits enforce boundaries.

## A short review

Explain what changed and why; check the diff for unrelated edits; run the relevant behavior; verify the final user-visible result against actual tool facts. The longer docs/REVIEW.md exercise is optional after the first build.
