# Solutions (try first!)

## 1. New tool

In `02_react_agent.py`, change the default tools:

```python
def build_agent(offline: bool, tools=lc_tools.ALL_TOOLS):
```

and the same default in `run(...)`. The model now sees `get_refund_policy` in its tool list, so it can ask for it. With `policy_unavailable`, the tool returns `{"status": "error"}` and a well-instructed agent says the policy is unavailable instead of inventing one.

## 2. Verify the budget

In `fixed_workflow`, after `menu = tools.find_food(...)`:

```python
over = [m for m in menu["matches"] if m["price"] > constraints["budget"]]
if over:
    step(f"   WARNING: tool returned dishes over budget: {over}. Removing them.")
    menu["matches"] = [m for m in menu["matches"] if m["price"] <= constraints["budget"]]
```

## 3. Closed shortcut

In `03_langgraph_flow.py`, replace the existing `build_graph()` with the complete block below, placed above `run()`. It reuses the existing node functions, state, rules and imports. This variant checks hours in a visible node, once, before menu search.

```python
def closed_answer(state):
    hours = state["hours"]
    return {"answer": f"Closed now, opens at {hours['opens']}.", "path": ["closed_answer"]}

def before_hours(state):
    return "check_hours" if rules.valid_budget(state["constraints"]["budget"]) else "ask_for_budget"

def after_hours(state):
    return "search_menu" if state["hours"]["open_now"] else "closed_answer"

def after_menu_early_hours(state):
    if state.get("menu_error") and state["attempts"] < MAX_MENU_ATTEMPTS:
        return "search_menu"
    return "verify"

def build_graph():
    graph = StateGraph(CanteenState)
    for node in (read_request, ask_for_budget, check_hours, search_menu,
                 verify, answer, closed_answer):
        graph.add_node(node.__name__, node)
    graph.add_edge(START, "read_request")
    graph.add_conditional_edges("read_request", before_hours, ["ask_for_budget", "check_hours"])
    graph.add_conditional_edges("check_hours", after_hours, ["search_menu", "closed_answer"])
    graph.add_conditional_edges("search_menu", after_menu_early_hours, ["search_menu", "verify"])
    graph.add_edge("verify", "answer")
    graph.add_edge("ask_for_budget", END)
    graph.add_edge("closed_answer", END)
    graph.add_edge("answer", END)
    return graph.compile()
```

Expected routes: closed: `read_request -> check_hours -> closed_answer`; open: `read_request -> check_hours -> search_menu -> verify -> answer`; missing/zero budget: `read_request -> ask_for_budget`. The retry stays bounded at two attempts while open.

The supplied suite executes this documented solution and checks its routes and number of menu calls. After experimenting, restore the original file or keep the deliberate change and update affected route tests.
