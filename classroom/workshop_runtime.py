"""Configuration and console support. The agent logic is in the lesson files."""
import argparse
import json
import os
from pathlib import Path

from dotenv import load_dotenv


def configuration():
    load_dotenv(Path(__file__).with_name('.env'), override=False)
    return os.getenv('GOOGLE_API_KEY'), os.getenv('GEMINI_MODEL', 'gemini-3.6-flash')


def make_model(offline=False):
    if offline:
        from offline_brain import ScriptedBrain
        return ScriptedBrain()
    key, name = configuration()
    if not key:
        raise RuntimeError('No Gemini key found in a .env file next to workshop_runtime.py. '
                           'Set OFFLINE = True in your my_agent.py (or add --offline to the classroom/ scripts) '
                           'for the scripted rehearsal, or see docs/SETUP.md to add your own key.')
    from langchain_google_genai import ChatGoogleGenerativeAI
    return ChatGoogleGenerativeAI(model=name, api_key=key, temperature=None, timeout=30, max_retries=0)


def arguments(description, default='Find vegetarian lunch under Rs 80 and check opening hours.'):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--offline', action='store_true', help='Scripted model, real framework/tools; not real AI')
    parser.add_argument('--question', default=default)
    return parser.parse_args()


def banner(offline, transport='local functions'):
    print('BRAIN:', 'SCRIPTED REHEARSAL (not a real AI)' if offline else 'LIVE GEMINI')
    print('TOOLS:', transport)


def payload(value):
    """Read JSON from direct tools or the MCP adapter's text content blocks."""
    if isinstance(value, dict):
        return value
    if isinstance(value, list):
        texts = [v.get('text', '') for v in value if isinstance(v, dict)]
        value = '\n'.join(texts)
    try:
        return json.loads(value)
    except (ValueError, TypeError) as exc:
        raise ValueError('Tool did not return the expected JSON; inspect the actual result.') from exc


def show_messages(result):
    for message in result['messages']:
        if message.type == 'system':
            continue
        if message.type == 'human':
            print('YOU:', message.text)
        elif message.type == 'tool':
            print('RESULT', message.name + ':', message.text)
        elif getattr(message, 'tool_calls', None):
            for call in message.tool_calls:
                print('MODEL REQUEST:', call['name'], call['args'])
        else:
            print('ANSWER:', message.text)
