"""Ordinary functions first. These exact functions also back the MCP server."""
import json
from datetime import datetime
from pathlib import Path

MENU = json.loads((Path(__file__).parent / 'data' / 'menu.json').read_text(encoding='utf-8'))


def find_food(max_price: int, vegetarian: bool = True) -> dict:
    """Find available food within a per-person rupee budget. True means vegetarian only."""
    if type(max_price) is not int or max_price < 0:
        raise ValueError('max_price must be a nonnegative whole number')
    if type(vegetarian) is not bool:
        raise ValueError('vegetarian must be true or false')
    matches = []
    for dish in MENU:
        if not dish['available'] or dish['price'] > max_price:
            continue
        if vegetarian and not dish['vegetarian']:
            continue
        matches.append({'name': dish['name'], 'price': dish['price']})
    return {'status': 'ok', 'matches': matches}


def get_canteen_hours(at: str = '12:30') -> dict:
    """Read fictional hours at a mock time. Default 12:30; not a live clock."""
    now = datetime.strptime(at, '%H:%M').time()
    opens = datetime.strptime('09:00', '%H:%M').time()
    closes = datetime.strptime('16:00', '%H:%M').time()
    return {'opens': '09:00', 'closes': '16:00', 'now': at,
            'open_now': opens <= now < closes, 'mock_clock': True}


if __name__ == '__main__':
    print(find_food(80))
    print(get_canteen_hours())
