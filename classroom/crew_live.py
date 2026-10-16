"""Compatibility support for the pinned CrewAI/Gemini combination."""
from crewai.llms.providers.gemini.completion import GeminiCompletion
from google.genai import types


class WorkshopGemini(GeminiCompletion):
    def _format_messages_for_gemini(self, messages):
        contents, instruction = super()._format_messages_for_gemini(messages)
        # CrewAI's text ReAct executor appends observations in an assistant
        # turn. Gemini requires a user turn before requesting continuation.
        if contents and contents[-1].role == 'model':
            contents.append(types.Content(role='user', parts=[types.Part.from_text(
                text='Continue the task using the actual tool observation above. '
                     'Return the requested final answer when you have enough information.')]))
        return contents, instruction


def make_live_brain(key, model):
    return WorkshopGemini(model=model, api_key=key,
                          client_params={'http_options': types.HttpOptions(
                              timeout=30000, retry_options=types.HttpRetryOptions(attempts=1))})
