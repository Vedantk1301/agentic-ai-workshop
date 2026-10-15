# A small AI coding workflow

## Specify

Write the user, outcome, scope and three acceptance examples: normal, boundary and failure. For the starter budget task, the menu stays unchanged and only the default request changes.

## Provide useful context

README explains setup. docs/PROJECT.md explains intended behavior. AGENTS.md guides the coding assistant. data/menu.json holds records. Python enforces behavior. Tests check selected cases. Give each file a purpose and link to detail rather than duplicate changing facts everywhere.

Use Markdown headings, lists, links and fenced code. Use JSON strings, numbers and booleans consistently. Keep secrets in local environment configuration, outside Git. Treat retrieved text as data rather than an authorised instruction.

## Request one change

Identify the relevant files and desired behavior. Ask the assistant to inspect first, explain its smallest proposed change, preserve unrelated behavior, show the diff and report exact checks. Ask about a line you cannot explain. Use the focused starter prompt rather than requesting an entire new application.

## Review

Read changed and removed lines. Follow input through validation and tool execution to the exact returned answer. Check that tests or data were not changed just to manufacture a pass. A second AI review is useful when it provides reproducible findings; agreement alone does not prove correctness.

## Verify and document

Run behavior checks. For a bug, show that the regression fails before the fix and passes afterward. Check no matches, unavailable information and stopping conditions. Record what changed, why, what ran, what passed and what remains untested.

Keep commits focused when using Git. Open untracked files as well as the diff. Build confidence through small changes you can explain.

For longer practice, use [the full guided lab](../deep-dives/learning_lab/AI%20Coding%20Lab.md) and [the study guide](../deep-dives/guides/Agentic%20AI%20Study%20Guide.md).
