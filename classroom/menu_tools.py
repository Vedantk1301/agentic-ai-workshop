"""Ordinary functions first. These exact functions also back the MCP server.

Nothing in this file uses AI. A "tool" is just a normal Python function that
an agent is allowed to call. Run this file directly to test the tools by hand:
    python classroom/menu_tools.py
"""
import json
from datetime import datetime
from pathlib import Path

# Load the four fictional menu records once, from data/menu.json next to this file.
# MENU becomes a list of dictionaries like {"name": "Poha", "price": 35, ...}.
MENU = json.loads((Path(__file__).parent / 'data' / 'menu.json').read_text(encoding='utf-8'))


def find_food(max_price: int, vegetarian: bool = True) -> dict:
    """Find available food within a per-person rupee budget. True means vegetarian only."""
    # The type hints (int, bool) and the docstring above are not decoration:
    # LangChain sends them to the model as the tool's description and arguments.

    # Input checks: refuse bad arguments instead of guessing. A model can send
    # odd values (a negative price, text instead of a number), so the tool protects itself.
    if type(max_price) is not int or max_price < 0:
        raise ValueError('max_price must be a nonnegative whole number')
    if type(vegetarian) is not bool:
        raise ValueError('vegetarian must be true or false')

    matches = []
    for dish in MENU:
        # Rule 1: skip anything sold out or over budget.
        if not dish['available'] or dish['price'] > max_price:
            continue
        # Rule 2: if the user wants vegetarian, skip non-veg dishes.
        if vegetarian and not dish['vegetarian']:
            continue
        matches.append({'name': dish['name'], 'price': dish['price']})
    # Return plain data. An empty matches list is a correct answer, not an error.
    return {'status': 'ok', 'matches': matches}


def get_canteen_hours(at: str = '12:30') -> dict:
    """Read fictional hours at a mock time. Default 12:30; not a live clock."""
    # We use a fixed, fake clock so every run in class gives the same result.
    now = datetime.strptime(at, '%H:%M').time()
    opens = datetime.strptime('09:00', '%H:%M').time()
    closes = datetime.strptime('16:00', '%H:%M').time()
    return {'opens': '09:00', 'closes': '16:00', 'now': at,
            'open_now': opens <= now < closes, 'mock_clock': True}


if __name__ == '__main__':
    # Only runs when you execute this file directly, not when an agent imports it.
    print(find_food(80))
    print(get_canteen_hours())
