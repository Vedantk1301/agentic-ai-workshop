# The team of roles, as CrewAI would write it

This is a **sketch for the slide, not run in class**. `05_team_of_roles.py` simulates the same pattern in plain Python so nothing needs installing. Check the current CrewAI docs before running this yourself: [Crews](https://docs.crewai.com/en/concepts/crews), [Flows](https://docs.crewai.com/en/concepts/flows).

```python
from crewai import Agent, Task, Crew, Process

menu_adviser = Agent(
    role="Menu adviser",
    goal="Find in-stock lunch under the student's budget",
    backstory="You only know the canteen menu.",
    tools=[find_food_tool],
)
policy_adviser = Agent(
    role="Policy adviser",
    goal="Explain whether a prepaid coupon can be refunded",
    backstory="You only know the refund policy.",
    tools=[refund_policy_tool],
)

find_lunch = Task(
    description="Find lunch under Rs {budget}.",
    expected_output="In-stock dishes with prices, or 'nothing matches'.",
    agent=menu_adviser,
)
check_refund = Task(
    description="Can a prepaid coupon be refunded?",
    expected_output="The policy text, or 'policy unavailable'. Never guess.",
    agent=policy_adviser,
)

crew = Crew(
    agents=[menu_adviser, policy_adviser],
    tasks=[find_lunch, check_refund],
    process=Process.sequential,  # or Process.hierarchical, with a manager role
)
result = crew.kickoff(inputs={"budget": 80})
```

What to point at on the slide:
- **Agent** = a role with its own goal and its own tools.
- **Task** = the job, with the expected output written down.
- **Process** = who goes when: sequential (one after another) or hierarchical (a manager assigns).
- Each agent is an AI call, so this team costs more calls and more waiting than one agent with two tools.
