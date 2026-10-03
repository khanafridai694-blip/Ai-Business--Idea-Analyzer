from crewai import Task


def create_debate_task(agent, market_task, business_task, technical_task):
    return Task(
        description="""
You are the Challenger Agent.

Startup idea:

{idea}

Review the Market, Business, and Technical analyses from the task context.

Identify the most important:

1. Weak assumption
2. Customer problem
3. Business problem
4. Technical problem
5. Contradiction
6. Improvement

For each important issue, briefly explain:
- What is wrong?
- Why does it matter?
- What should change?

Focus only on the most important issues.
Do not invent statistics.
""",
        expected_output="A concise challenge/debate analysis of about 400-500 words.",
        agent=agent,
        context=[
            market_task,
            business_task,
            technical_task,
        ],
    )
