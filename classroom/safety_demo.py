"""One injected forbidden tool request, caught before execution. No model call."""
from langchain_core.messages import AIMessage
from manual_loop import run_loop


class InjectedRequest:
    def bind_tools(self, tools):
        return self

    def invoke(self, messages):
        return AIMessage(content='', tool_calls=[{'name': 'delete_everything', 'args': {}, 'id': 'injected'}])


if __name__ == '__main__':
    print('INJECTED REQUEST for teaching; no real AI, no deletion tool.')
    try:
        run_loop(InjectedRequest(), 'Find lunch', [], max_steps=2)
    except ValueError as exc:
        print('REFUSED BEFORE EXECUTION:', exc)
