# Troubleshooting

| Symptom | Next step |
| --- | --- |
| Python/py not found | Install Python 3.11, open a fresh terminal and check its version. See the root setup commands. |
| Cannot find classroom/agent.py | Run reference commands from the extracted repository root. Run your own my_agent.py from your_agent/. |
| No module named langchain, mcp or menu_tools | Use the prepared .venv Python and install root requirements.txt. Create menu_tools.py in the same learner folder as my_agent.py. |
| PowerShell activation blocked | Use .venv/Scripts/python directly; the workshop needs no execution-policy change. |
| API key missing | Use --offline on reference demos or OFFLINE=True in your typed build. Configure classroom/.env for references or your_agent/.env for the learner build; see SETUP.md. Never print keys. |
| Model unavailable / quota exhausted | Inspect account/model availability privately. Continue with --offline. Do not assume creating another key adds quota. |
| GitHub repository not found or git missing | Check the URL: https://github.com/Vedantk1301/agentic-ai-workshop. Without Git, use Code → Download ZIP on that page, or the Agentic AI GitHub Kit.zip from the coordinator. |
| Test fails after a change | Read the assertion and actual output. Review your diff. Keep menu data fixed unless the requirement changes it. |
| start_here refuses to overwrite | The learner folder is already prepared. Continue at Step 1 in classroom/README.md, or choose a new empty destination. Do not delete your work to rerun setup. |
| Missing crewai | Only the instructor needs requirements-instructor.txt. Continue the core agent/MCP lesson; run tests with -k "not crew" if CrewAI is not installed. |
| MCP probe waits without results | Use the same environment for client and server. Keep the exact mcp_server.py filename and avoid print statements on server stdout. The client launches the local server automatically. |

The offline stand-in gives predictable requests/results for teaching. Live Gemini may group or reorder tools or phrase its answer differently. Check facts and behavior rather than expecting identical wording.

During the large-room activity, signal for help and use a completed checkpoint or saved output if necessary, recording what you actually ran. Helpers may assist while the presenter continues at common checkpoints. Sharing a working device is optional. See [the current lesson](../classroom/README.md). The older starter/ uses starter/.env only for its own optional reference examples.
