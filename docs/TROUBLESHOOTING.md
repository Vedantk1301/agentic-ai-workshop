# Troubleshooting

| Symptom | Next step |
| --- | --- |
| Python/py not found | Install Python 3.11, open a fresh terminal and check its version. See the root setup commands. |
| Cannot find starter/agent.py | Open the repository root, not its parent or a nested docs folder. |
| No module named langchain or canteen | Use the root .venv Python. Install root requirements.txt. Keep the script with its canteen/ and data/ folders. |
| PowerShell activation blocked | Use .venv/Scripts/python directly; the workshop needs no execution-policy change. |
| API key missing | Run --offline, or privately configure starter/.env using SETUP.md. Never print the key while diagnosing. |
| Model unavailable / quota exhausted | Inspect account/model availability privately. Continue with --offline. Do not assume creating another key adds quota. |
| GitHub repository not found | A private repository requires authorised access. Use the supplied Agentic AI GitHub Kit.zip from the coordinator, or download/clone after access is provided. |
| Test fails after a change | Read the assertion and actual output. Review your diff. Keep menu data fixed unless the requirement changes it. |

The offline stand-in gives predictable requests/results for teaching. Live Gemini may group or reorder tools or phrase its answer differently. Check facts and behavior rather than expecting identical wording.

During the large-room activity, signal 2 for help and continue the source/menu/review task while waiting. Use the saved trace if necessary and mark predicted results as not run. Helpers may assist with individual issues; the presenter continues at common checkpoints. Sharing a working device is optional. See [the starter](../starter/README.md) for the current step.
