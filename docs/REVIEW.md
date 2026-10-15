# Review the answer reaching the user

Work in pairs. Requirement: recommend only available vegetarian food within the student's confirmed Rs 80 budget, using successful menu evidence.

Inspect this deliberately unsafe sketch:

```python
check(reply["recommended_dishes"])
return reply["message"]
```

The output is:

```json
{
  "recommended_dishes": ["Veg sandwich"],
  "message": "Try the Paneer Tikka Wrap. Open until 22:00."
}
```

The test checks only that recommended_dishes contains Veg sandwich. It passes.

1. Point to the unchecked value reaching the student.
2. Write an input/output check that catches the incorrect answer.
3. Propose a correction in code.
4. Add a failed-menu-source case. Which facts may the answer honestly claim?

Use this review order for an AI-generated patch: requirement, changed/removed lines, input/tool arguments, failure path, exact returned value, checks and docs. Ask for concrete reproductions from a second reviewer and verify them yourself. In an existing Git repository, inspect git diff and open untracked files; a downloaded ZIP has no Git history, so use the editor's comparison view.

Read [the worked answer](../solutions/review-answer.md) after trying. The original full review handout is available [as a PDF](../deep-dives/learning_lab/Review%20Exercise.pdf).
