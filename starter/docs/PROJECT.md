# Campus Canteen project brief

## Outcome

A student wants vegetarian lunch within a budget and asks whether the canteen is open. Use fictional records; do not invent a dish, price, stock or hours.

## Data and boundaries

data/menu.json has a vegetarian sandwich at Rs 60 in stock, poha at Rs 35 sold out, a chicken roll at Rs 75 in stock and a vegetarian dosa at Rs 90 in stock. The mock clock is 12:30; opening hours are 09:00 inclusive to 16:00 exclusive. This is a lookup exercise, with no orders or payments.

## Today's small change

Copy agent.py to practice_agent.py in the same starter folder. Change only the default QUESTION budget in practice_agent.py from Rs 80 to Rs 30. Keep MENU_ONLY_QUESTION, tools and data unchanged.

## Acceptance examples

- Before the change: the Rs 60 sandwich qualifies under Rs 80.
- After the change: no vegetarian food qualifies under Rs 30. The hours answer remains unchanged.
- A menu timeout means unavailable information, not proof of stock.

The starter shows the agent loop and its proposed answer. The deeper graph example separately demonstrates checks around model output. Prompt instructions alone do not enforce factual correctness.
