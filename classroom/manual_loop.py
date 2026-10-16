"""Optional after class: the bounded tool loop beneath a framework agent."""
import json
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool

from menu_tools import find_food, get_canteen_hours
from workshop_runtime import arguments, banner, make_model, show_messages


def run_loop(model, question, tools, max_steps=6):
    allowed = {t.name: t for t in tools}
    model = model.bind_tools(tools)
    messages = [SystemMessage(content='Use menu tools for facts; obey budget and diet.'), HumanMessage(content=question)]
    for step in range(max_steps):
        reply = model.invoke(messages)
        messages.append(reply)
        if not reply.tool_calls:
            return messages
        for call in reply.tool_calls:
            if call['name'] not in allowed:
                raise ValueError(f"Tool {call['name']} is not allowed")
            result = allowed[call['name']].invoke(call['args'])
            messages.append(ToolMessage(content=json.dumps(result), name=call['name'], tool_call_id=call['id']))
    raise RuntimeError('Model step limit reached; stopped instead of looping forever')


if __name__ == '__main__':
    args = arguments('Optional manual bounded loop')
    banner(args.offline)
    messages = run_loop(make_model(args.offline), args.question, [tool(find_food), tool(get_canteen_hours)])
    show_messages({'messages': messages})
