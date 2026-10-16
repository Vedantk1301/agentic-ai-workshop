"""Scripted CrewAI rehearsal brains. Real tasks/tools; no autonomous AI."""
import json
from crewai import BaseLLM


def find_menu(messages):
    """Extract records from the actual tool observation or handed-off scout output."""
    text = '\n'.join(str(m.get('content', '')) for m in messages) if isinstance(messages, list) else str(messages)
    decoder = json.JSONDecoder()
    found = None
    for i, char in enumerate(text):
        if char != '{':
            continue
        try:
            value, _ = decoder.raw_decode(text[i:])
        except ValueError:
            continue
        if isinstance(value, dict) and 'matches' in value:
            found = value
        elif isinstance(value, dict) and 'text' in value:
            try:
                inner = json.loads(value['text'])
                if isinstance(inner, dict) and 'matches' in inner:
                    found = inner
            except (ValueError, TypeError):
                pass
    return found


class ScriptedCrewBrain(BaseLLM):
    def __init__(self, role):
        super().__init__(model='scripted-rehearsal-not-real-ai', temperature=0)
        self.role = role

    def supports_function_calling(self):
        return False

    def call(self, messages, tools=None, callbacks=None, available_functions=None, **kwargs):
        menu = find_menu(messages)
        if self.role == 'scout':
            if menu is not None:
                return 'Final Answer: ' + json.dumps(menu)
            return 'Thought: I need the actual menu.\nAction: find_food\nAction Input: {"max_price": 75, "vegetarian": true}'
        if menu is None:
            raise RuntimeError('Planner did not receive the scout tool result')
        if not menu['matches']:
            return 'Final Answer: No matching food was returned; ask to change the budget.'
        dish = menu['matches'][0]
        total = dish['price'] * 2
        return f"Final Answer: Two people: 2 x {dish['name']} at Rs {dish['price']} = Rs {total}. Group budget Rs 150."
