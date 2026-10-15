# Campus Canteen Assistant: project brief

## User and outcome

A student wants vegetarian lunch within a confirmed budget and may ask whether the canteen is open. Return an answer backed by current fictional records. The core example is: "Find vegetarian lunch under Rs 80, and tell me whether the canteen is still open."

## Scope

Read-only lookups. No orders, payment, real student information or real refund promises. The menu and coupon policy are fictional teaching data. A model may choose tools; ordinary code executes them and checks important results.

## Data contract

The source menu is data/menu.json. Each record has a unique name, an integer price in rupees, and boolean vegetarian and available fields. JSON booleans are true/false; Python booleans are True/False. Do not use prose or an instruction file as the live stock database.

The fixture clock is 12:30, or 16:30 for after_hours. Opening hours are 09:00 inclusive to 16:00 exclusive. This is a repeatable demonstration clock, not a claim about the real time or a real canteen.

## Acceptance checks

| Case | Expected behavior |
| --- | --- |
| Veg, budget Rs 80, normal | Veg sandwich, Rs 60; poha unavailable, chicken not vegetarian, dosa over budget |
| Budget missing or zero | Ask for a positive whole-number budget before searching |
| Sandwich sold out | Successful empty result; no made-up dish |
| Menu fails once | Graph retries once, then continues from the successful result |
| Menu keeps failing | Stop after two attempts; report unavailable information |
| Model proposes the wrong dish or budget | Verify against the student's original constraints and actual tool evidence |
| Empty lookup used narrower filters than the request | Report incomplete evidence; do not claim no matching food exists |
| Tool accepts a numeric string such as "80" | Verify the schema-normalized value without crashing |
| Model writes false facts in a separate paragraph | Do not forward that paragraph; render checked records |
| Policy cannot be retrieved | Do not state a refund rule |

## Implementation notes

01 is a fixed workflow. 02 is a model-driven tool loop. 03 uses explicit graph routes. 04 puts the model-driven agent inside a graph and renders the final answer in code. 05 is a plain-Python simulation of roles, not a live CrewAI run.

The simple request parser recognises a few English phrases; it is not a general language-understanding system. A production application needs a suitable input contract and validation. The toy verification reads the local canonical menu; real services need appropriate freshness, access and consistency checks.

## Definition of done

The requested behavior works; relevant failure cases are checked; the full local suite passes; a reviewer can explain the changed lines; the commands and docs match the implementation. Offline checks do not establish live-model compatibility, latency or quota availability.
