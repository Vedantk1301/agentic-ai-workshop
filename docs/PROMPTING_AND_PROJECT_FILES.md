# Prompting and project files: a take-home guide

Today you wrote three prompts without calling them that: the agent's `system_prompt`, the docstring on each tool, and the instructions in a project file like `AGENTS.md`. This page covers how to write each one well.

## 1. The system prompt: the agent's job description

Ours was one line: `"Use the menu tool for facts. Respect budget and diet."` That works for a toy. For anything real, cover these five things, briefly:

| Part | Canteen example |
| --- | --- |
| Role and goal | You help students choose lunch from our campus canteen. |
| Where facts come from | Use find_food for dishes and prices, and get_canteen_hours for timings. Never answer those from memory. |
| Rules | Respect the user's budget and diet. Never suggest a sold-out dish. |
| When unsure | If nothing matches, say so plainly instead of guessing. If the request is unclear, ask one short question. |
| Answer format | Reply in one or two sentences: dish, price, and whether the canteen is open. |

Good habits:

- **Be specific.** "Respect the budget" beats "be helpful".
- **Say what to do when things go wrong**, not just when they go right.
- **Put facts in tools or data, not in the prompt.** Prices change; the prompt shouldn't have to.
- **Remember that prompts guide; code enforces.** Anything that must never happen (deleting, paying, sending) needs a check in code, like the allowlist in `classroom/manual_loop.py`.
- **Change one thing at a time** and rerun the same question, so you can see what the change did.

## 2. Tool descriptions: prompts the model reads before it acts

The model never sees your function's code. It sees only the name, the arguments and the docstring. That's how it decides which tool to call and what to pass in.

```python
# Weak: the model has to guess what this does and when to use it.
def search(x: int) -> dict:
    """Does a thing."""

# Strong: clear name, when to use it, what the arguments mean.
def find_food(max_price: int, vegetarian: bool = True) -> dict:
    """Find available food within a per-person rupee budget. True means vegetarian only."""
```

- Name the tool after what it does (`find_food`, not `search`).
- Say what each argument means, including units (rupees, 24-hour time).
- Keep one job per tool. Two small tools beat one tool with a "mode" argument.
- Return plain data (a dictionary), not sentences. Let the model write the sentence.

## 3. Markdown files: each one has a job

| File | Who reads it | What goes in it |
| --- | --- | --- |
| `README.md` | People | What the project does, how to install and run it, and where things live. |
| `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` | Coding agents (Codex, Claude Code, Gemini CLI, Cursor and others) | Rules for working on this project: conventions, what not to touch, how to test. Which file name is read depends on the tool. |
| `data/*.json` | Your code | Facts. Keep them out of prompts and Markdown. |

Look at the real ones in this repository: `README.md` and `AGENTS.md` at the root, and `classroom/AGENTS.md`. Structure that works for both people and AI:

- One `#` title, then short `##` sections with clear names.
- Bullets for rules, tables for comparisons, numbered lists for steps.
- Every command in a code block, exactly as it should be typed.
- Short and current. An out-of-date instruction file is worse than none, because the agent will follow it.

A starter `AGENTS.md` for your own canteen project:

```markdown
# Canteen agent: project rules

- Menu facts come from data/menu.json. Never hard-code dishes or prices.
- Explain each change before editing, and change one thing at a time.
- After a change, run `python my_agent.py` and report what actually happened.
- Never print, commit or share .env files or API keys.
```

## 4. Prompting a coding assistant

When you ask Claude Code, Cursor, Copilot or ChatGPT to change your code:

1. **Describe the outcome**, not just the action: "Add a tool that returns the canteen's location, so the agent can answer 'where is it?'"
2. **Give the constraints**: which files to touch, what must not change.
3. **Say how you'll check it**: "It should work with OFFLINE = True and pass `python my_agent.py`."
4. **Read the change before you accept it**, then run it yourself. You are the reviewer.
5. **Ask for small steps.** "Build me an entire app" produces code you can't check.

## Quick checklist

- [ ] My system prompt says the role, where facts come from, the rules, what to do when unsure, and the answer format.
- [ ] Every tool has a clear name and a docstring that says when to use it.
- [ ] Facts live in data or tools, not in prompts.
- [ ] Anything dangerous is blocked in code, not just in the prompt.
- [ ] My README says what the project does and how to run it.
- [ ] My AGENTS.md has a few short, current rules and the test command.
