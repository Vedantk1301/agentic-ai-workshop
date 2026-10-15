# Take-home exercises

Do these with the demo code from the workshop. Each one practises one idea from the session. Answers are in `solutions.md`; try first.

## 1. Teach the agent a new tool (easy)

`02_react_agent.py` only gives the agent `find_food` and `get_canteen_hours`. Give it `get_refund_policy` too (it already exists in `canteen/lc_tools.py`), then ask:

> Find vegetarian lunch under Rs 80, and can I get a refund on my prepaid coupon?

**Check:** does the model now ask for the refund tool? Try `--scenario policy_unavailable`. Does it refuse to guess the rule?

**The lesson:** the model can only *ask* for tools you give it. Adding a capability is your decision, not the model's.

## 2. Don't trust, verify (medium)

In `canteen/tools.py`, pretend someone broke `find_food`: change `item["price"] <= max_price` to `item["price"] <= max_price + 20`. Now the dosa (Rs 90) sneaks in under an Rs 80 budget.

Add a check to the fixed workflow in `01_tools_and_fixed_workflow.py` that removes any dish over the budget and prints a warning.

**Check:** with the broken tool, your answer must still never recommend the dosa. Then fix the tool back.

**The lesson:** check important outputs, even from your own tools.

## 3. Add a "closed" shortcut to the graph (harder)

In `03_langgraph_flow.py`, if the canteen is closed there's no point searching the menu. Add a node that checks the hours first, and route straight to an answer like *"Closed now, opens at 09:00"* when it's closed.

**Check:** `--scenario after_hours` should go `read_request -> check_hours -> closed_answer` and never call the menu. While open, check hours once, then search/verify/answer. Missing or zero budgets must ask for valid input before any lookup.

**The lesson:** edges are your code's decisions. A good graph skips work that can't help.

## The real challenge

Start with `../../learning_lab/AI Coding Lab.md`: write the outcome and acceptance examples, inspect project instructions, request one focused change, review its diff, run checks and update the docs. Pair-review exercise: `../../learning_lab/Review Exercise.md`.

Build one small agent for an annoying problem in **your own** life: a timetable checker, a "what's due this week" helper, a hostel mess-menu bot. One or two tools, a step limit, and an honest "I don't know". Then show a friend the trace.
