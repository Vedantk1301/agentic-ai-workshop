"""Safe setup check. --live makes one real agent run; no key is displayed."""
import argparse
from importlib.metadata import version
import sys

from menu_tools import find_food, get_canteen_hours


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true', help='One real Gemini agent/tool run using your private configuration')
    args = parser.parse_args()
    print('Python:', sys.version.split()[0])
    for package in ['langchain', 'langgraph', 'langchain-google-genai', 'mcp', 'langchain-mcp-adapters']:
        print(package + ':', version(package))
    assert find_food(80)['matches'] == [{'name': 'Veg sandwich', 'price': 60}]
    assert get_canteen_hours()['open_now']
    print('Local menu and mock hours: OK')
    if args.live:
        from agent import build_agent
        try:
            result = build_agent().invoke({'messages': [('user', 'Use find_food to find vegetarian lunch under Rs 80.')]},
                                           {'recursion_limit': 10})
            assert any(m.type == 'tool' and m.name == 'find_food' for m in result['messages'])
        except Exception as exc:
            print('Live check failed:', type(exc).__name__)
            print('Check private key, model access, network and quota. No credentials or raw provider errors are printed.')
            return 1
        print('LIVE Gemini agent requested and received a menu tool result: OK')
    else:
        print('Live Gemini: NOT TESTED. Add --live only after privately configuring classroom/.env.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
