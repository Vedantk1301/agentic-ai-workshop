# Agentic AI in Practice

Build, review and control a small Campus Canteen Assistant. Prepared for Vedant's VIT Mumbai workshop, 17 October 2026.

**Start with [the starter lesson](starter/README.md).** You will write useful project instructions, change one request, and review an unsafe answer. The advanced folders are optional after class.

## Get the project

Clone this repository, or use GitHub's **Code > Download ZIP**, extract it and open the extracted folder. Git knowledge is optional. While the repository is private, access is limited to authorised GitHub accounts.

```sh
git clone https://github.com/Vedantk1301/agentic-ai-workshop.git
cd agentic-ai-workshop
```

Install Python 3.11 and one editor first. Antigravity is optional. From the repository root on Windows:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python starter/agent.py --offline
```

macOS/Linux:

```sh
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python starter/agent.py --offline
```

The default request finds vegetarian lunch under Rs 80. Expect the Rs 60 sandwich and mock closing time 16:00. The offline model is a clearly labelled rule-based stand-in; the real agent/tool plumbing still executes. Dependencies need internet for the initial installation.

## Choose your next step

| Stage | Open | Finish when you can |
| --- | --- | --- |
| In class | [Starter](starter/README.md) | Explain an instruction, one changed line and one review finding |
| Compare afterward | [Solutions](solutions/README.md) | Explain why the completed exercise gives its result |
| Study the systems | [Deep dives](deep-dives/README.md) | Trace tools, agents, graph routes and a simulated team |
| Improve your method | [Learning path](docs/LEARNING_PATH.md), [AI coding](docs/AI_CODING.md), [review](docs/REVIEW.md) | Specify, change, review, verify and document a small feature |
| Present/revise | [Classroom slides](slides/Agentic%20AI%20in%20Practice.pdf) | Follow the single canteen story, with [speaker notes](slides/Speaker%20Script.md) |

You do not need to read or build every example during the workshop.

## Optional live Gemini

Follow [setup and AI Studio guidance](docs/SETUP.md). Live calls use your own eligible account and key, configured privately in starter/.env. No paid plan or Cloud Console provisioning is needed for the core offline activities. Available free-tier models and quota depend on the account. A coding-assistant login and the Python application's API key are separate setup steps.

The records are fictional. The parser is intentionally small. There are no orders, payments or production access controls. Offline tests do not establish live model compatibility, latency or quota.

## Check your environment

From the repository root:

```powershell
.venv\Scripts\python tools/verify_workshop.py
.venv\Scripts\python -m pytest deep-dives/demo/tests -q -p no:cacheprovider
```

Use .venv/bin/python on macOS/Linux. The first command runs five offline examples, including the worked budget change and a rejected invented message. The second runs the full behavioral suite. The GitHub workflow performs the same checks without API credentials.

Read [troubleshooting](docs/TROUBLESHOOTING.md) if setup fails. Start with the outcome and changed lines before asking an AI to fix the entire project.
