# Running the workshop in a large room

Plan for a possible 100-200 mixed first- to fourth-year IT/CS students. Actual attendance, available laptops and volunteer support still need confirmation with the coordinator. The lesson remains a two-hour, 31-slide guided workshop on one fictional canteen assistant.

## Participation

Students use their own laptops where available. Sharing is optional, with turns at the keyboard and individual notes. Every student aims to write a useful instruction, make and explain a small code change, and identify an unchecked answer. A saved trace supports reading and predictions when setup fails; it does not count as a locally executed exercise.

Use one cycle throughout: demonstrate a small step, let students do it, show the expected evidence, then check progress from the front. Ask for 1 finger for ready, 2 for help and 3 for saved-trace participation. Do not rely on colour alone. Helpers handle individual issues if available. State these signals on slide 7.

## Before the day

- Send the exact repository or Agentic AI GitHub Kit.zip and root README setup instructions. A private GitHub link only works for authorised accounts; distribute the supplied ZIP through the coordinator while access is private.
- Ask for the expected headcount, laptop availability, Wi-Fi, power, projector readability and 4-6 technical volunteers. This is a support request, not confirmed staffing or a guarantee that every setup problem can be solved.
- Ask volunteers to complete the starter themselves. Assign seating zones and one lead volunteer who reports common issues to the presenter. Have helpers work beside the student and avoid collecting API keys.
- Students install Python 3.11, dependencies and one editor beforehand. Antigravity, live API access and coding-assistant accounts are optional. Core edits can be manual.
- Prepare large terminal text, a tested offline run, local saved outputs, the PDF deck and a brief recorded demo if possible. Test live Gemini separately if showing it.

## Five common checkpoints

| Checkpoint | Time IST | Evidence each student records |
| --- | --- | --- |
| 0: starter runs or trace is open | By 11:20 | Sandwich at Rs 60, closing at 16:00, and executed/trace status |
| 1: useful instructions | By 11:36 | One concrete instruction and how to check it |
| 2: change and run | By 12:00 | Rs 80 to Rs 30 diff, result and explanation |
| 3: review the answer | By 12:18 | Unchecked message plus a catching input/output check |
| 4: explain the result | By 12:50 | Individual note with all three practical outcomes |

Use [the starter](../starter/README.md) and its notes template. The instructor demonstrates the graph correction; students do not install another framework or build the entire graph during the session. Keep the five-minute break at 12:00 and Q&A at 12:50.

## Handling a stuck laptop

Ask students to note the command and error without sharing secrets. They signal for help and continue the menu-reading, instruction or review task. A helper investigates while the presenter continues. If several students have the same issue, demonstrate one common correction to the room, then return to the current checkpoint.

Use [the saved normal trace](../deep-dives/demo/saved_runs/02_agent_lunch_and_hours_OFFLINE.txt), the supplied source and menu when the environment is unavailable. Have students write the proposed edit and predicted output, marked **not run**. They can complete execution afterward. This preserves participation without claiming everyone finished a hands-on run.

## If no volunteers are available

Teach from the front and keep the same small tasks. Explain that individual installation support cannot be guaranteed during the session. Use progress signals, address repeated issues briefly, and direct blocked students to the prepared trace or optional sharing. Do not visit every laptop or hold a queue of 100 students for approval. The coordinator can collect unresolved setup questions for a later response through an existing channel.

## Live API demonstration

Show the AI Studio/key workflow from the presenter's screen using blank or masked configuration. Avoid simultaneous account creation and live model calls across the audience. Students use `--offline` during core activities and can configure their own eligible accounts privately outside the activity. Preserve the distinction between real Gemini, a rule-based stand-in and deliberately injected mistakes.

## Checking learning and timing

Ask for individual written answers before optional discussion with a neighbour. Sample explanations from different seating areas; volunteers can also spot misunderstandings. A progress signal shows readiness, not mastery. If many cannot explain who executes a tool, revisit that example and shorten the framework overview. Preserve the code activity, review task and questions. Save the notes individually; use a collection channel only if the coordinator has already arranged one.
