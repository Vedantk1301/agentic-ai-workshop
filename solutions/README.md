# Worked solutions

Try the starter first. Compare changed lines and explain the result rather than copying a whole folder without reading it.

| Exercise | Worked answer | What to understand |
| --- | --- | --- |
| Useful instructions | [AGENTS.example.md](AGENTS.example.md) | Each line describes a checkable action |
| Budget change | [Runnable completed copy](budget-30/README.md), [one-line patch](budget-change.diff) | Changing the request changes qualifying results, not menu stock |
| Unsafe answer | [Review answer](review-answer.md) | Validating the dish list does not validate the free-text message |
| Harder follow-up | [Three exercises and solutions](../deep-dives/demo/exercises/README.md) | Add tools, verify output and route a closed-canteen shortcut |

From the repository root on Windows:

```powershell
.venv\Scripts\python solutions/budget-30/agent.py --offline
```

Use .venv/bin/python on macOS/Linux. The result should say nothing vegetarian fits Rs 30 and the mock canteen closes at 16:00. The offline run uses a disclosed rule-based stand-in.
