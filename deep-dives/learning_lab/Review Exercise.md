# Review the confident patch

Work in pairs. You do not need a laptop or AI account.

## Requirement

Recommend vegetarian food under the student's confirmed Rs 80 budget. Use successful menu results. Report unavailable information honestly.

## The proposed change

```python
def answer(reply, checked_names):
    for dish in reply["recommended_dishes"]:
        assert dish in checked_names
    return reply["message"]
```

The test checks that recommended_dishes contains Veg sandwich. It passes.

The actual model output is:

```json
{
  "recommended_dishes": ["Veg sandwich"],
  "message": "Try the Paneer Tikka Wrap for Rs 60. Open until 22:00."
}
```

## Your job

1. Point to the unchecked value that reaches the student.
2. Write one concrete input/output test that catches it.
3. Describe a correction without adding another instruction to the prompt.
4. Add the menu-timeout twist: what evidence is now missing?

## Worked answer

The return statement forwards message unchanged. Checking a list does not validate the paragraph. A regression supplies a correct list and false text, then asserts that the final answer contains only checked dishes, prices and hours.

Render the answer from verified records instead of forwarding the model's paragraph. Require a successful lookup before asserting stock. Keep the original budget/diet constraints separate from the model's proposed arguments. A menu error should produce an unavailable answer, even if the model proposes a real dish from an old menu.

The corrected implementation is demo/04_graph_with_agent.py. Run it with --offline --inject-mistake free_text to compare the untrusted proposal with the final answer.
