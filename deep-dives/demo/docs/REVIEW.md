# Reviewing AI-generated code

The AI can propose a patch and help inspect it. You remain responsible for deciding whether its behavior matches the requirement.

## Read the requirement first

Write one sentence describing the intended behavior. List a normal case, a boundary case and a failure case. For this project: vegetarian lunch within the student's budget; budget zero; menu unavailable.

## Inspect the diff

With Git, use git diff --stat, then git diff -- the-file-you-changed. Without Git, use the editor's comparison view or keep a copy of the original. Read added and removed lines. Check for unrelated changes, new dependencies and changes to data or tests that merely make the result look correct.

## Trace one request to the visible answer

Follow input -> validation -> tool call -> result -> final rendering. Ask which values came from the user, which came from a model, and which came from an authoritative source. A schema can validate the shape of an object without proving the facts are true.

In the original workshop demo, recommended_dishes was checked but message was displayed unchanged. A valid sandwich list could accompany an invented Paneer Tikka Wrap in the message. The supplied 24 tests passed because they did not check that case. The corrected demo constructs the final answer from checked tool records.

## Verify evidence and failure handling

- Was the tool actually called, and did it succeed?
- Does the recommendation occur in that result and satisfy the original constraints?
- Are prices and opening times taken from checked records?
- Do empty results and service failures produce different answers?
- Do missing input and exhausted limits stop cleanly?
- Are secrets kept out of source control, terminal output and screenshots?

## Test behavior, not just the implementation

Run the normal example and a deliberately inconvenient case. Add a regression that fails on the old behavior and passes on the correction. Check the final answer the student sees, rather than only an intermediate list. Do not delete assertions or replace real checks with always-successful mocks to get green output.

## Review prompt you can reuse

"Review this diff against docs/PROJECT.md. Do not edit yet. Trace the final answer, check failed-tool behavior and the original budget/diet constraints, and identify concrete defects with file locations and a reproducing example. Separate confirmed defects from questions. State what you did not run."

Then ask for one focused correction, inspect the new diff, run the checks yourself, and update the relevant documentation. A second AI review is another opinion, not proof.
