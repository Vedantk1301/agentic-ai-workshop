"""A deliberately small rule script for rehearsal, not an autonomous model.

It reads actual tool results. Keep this fallback out of the first live build.
"""
import re
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult

from workshop_runtime import payload


class ScriptedBrain(BaseChatModel):
    tool_names: list[str] = []

    @property
    def _llm_type(self):
        return 'labelled-scripted-canteen-rehearsal'

    def bind_tools(self, tools, **kwargs):
        names = [t.name if hasattr(t, 'name') else t.__name__ for t in tools]
        return self.model_copy(update={'tool_names': names})

    def _generate(self, messages, stop=None, run_manager=None, **kwargs: Any):
        question = next(str(m.content) for m in messages if m.type == 'human')
        budget_match = re.search(r'(?:Rs\.?|rupees?|under|budget)\s*(\d+)', question, re.I)
        budget = int(budget_match.group(1)) if budget_match else 80
        results = {m.name: payload(m.content) for m in messages if m.type == 'tool'}
        needs_hours = any(word in question.lower() for word in ['hours', 'open', 'clos'])
        wants_veg = 'non-vegetarian' not in question.lower() and 'non vegetarian' not in question.lower()
        request = None
        if 'find_food' not in results and 'find_food' in self.tool_names:
            request = ('find_food', {'max_price': budget, 'vegetarian': wants_veg})
        elif needs_hours and 'get_canteen_hours' not in results and 'get_canteen_hours' in self.tool_names:
            request = ('get_canteen_hours', {})
        if request:
            answer = AIMessage(content='', tool_calls=[{'name': request[0], 'args': request[1], 'id': f'call-{len(results)}'}])
        else:
            menu = results.get('find_food', {})
            options = menu.get('matches', [])
            text = ', '.join(f"{d['name']} (Rs {d['price']})" for d in options)
            text = text or f'No matching available food under Rs {budget}.'
            hours = results.get('get_canteen_hours')
            if hours:
                text += f" Canteen {'open' if hours['open_now'] else 'closed'} at mock time {hours['now']}; closes {hours['closes']}."
            answer = AIMessage(content=text)
        return ChatResult(generations=[ChatGeneration(message=answer)])
