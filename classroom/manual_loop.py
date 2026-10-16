"""Optional after class: the bounded tool loop beneath a framework agent.

create_agent hides this loop. Here it is written out, so you can see that an
"agent" is just: ask the model, run the tools it requests, repeat, with limits.
    python classroom/manual_loop.py --offline
"""
import json
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

from menu_tools import find_food, get_canteen_hours
from workshop_runtime import arguments, banner, make_model, show_messages


def run_loop(model, question, tools, max_steps=6):
    allowed = {t.name: t for t in tools}          # the allowlist: only these names may run
    model = model.bind_tools(tools)               # tell the model which tools exist
    messages = [SystemMessage(content='Use menu tools for facts; obey budget and diet.'), HumanMessage(content=question)]
    for step in range(max_steps):                 # step limit: never loop forever
        reply = model.invoke(messages)            # THINK: the model reads everything so far
        messages.append(reply)
        if not reply.tool_calls:                  # no tool requested means the model is done
            return messages
        for call in reply.tool_calls:
            if call['name'] not in allowed:       # code enforces the boundary, not the prompt
                raise ValueError(f"Tool {call['name']} is not allowed")
            result = allowed[call['name']].invoke(call['args'])   # ACT: OUR code runs the tool
            # OBSERVE: send the real result back to the model as a new message
            messages.append(ToolMessage(content=json.dumps(result), name=call['name'], tool_call_id=call['id']))
    raise RuntimeError('Model step limit reached; stopped instead of looping forever')


if __name__ == '__main__':
    args = arguments('Optional manual bounded loop')
    banner(args.offline)
    messages = run_loop(make_model(args.offline), args.question, [tool(find_food), tool(get_canteen_hours)])
    show_messages({'messages': messages})
