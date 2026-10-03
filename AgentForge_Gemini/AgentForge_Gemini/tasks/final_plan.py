from crewai import Task


def create_final_plan_task(
    agent,
    market_task,
    business_task,
    technical_task,
    debate_task,
):
    return Task(
        description="""
Create the final improved startup plan for:

{idea}

Use the analyses and Challenger debate from the task context.

Include:

1. Executive Summary
2. Problem
3. Target Customers
4. Proposed Solution
5. Key Differentiator
6. Market Analysis
7. Business Model
8. MVP Features
9. Technical Architecture
10. Main Risks
11. Improvements After Debate
12. 90-Day Roadmap
13. 30-Second Elevator Pitch

The Challenger's findings must influence the final plan.

Be practical and concise.
Do not invent statistics.
Do not claim live web research.
""",
        expected_output="A practical final startup plan of about 800-1000 words.",
        agent=agent,
        context=[
            market_task,
            business_task,
            technical_task,
            debate_task,
        ],
    )
