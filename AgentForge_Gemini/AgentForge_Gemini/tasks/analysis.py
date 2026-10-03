from crewai import Task


def create_market_task(agent):
    return Task(
        description="""
Analyze this idea:

{idea}

Give a concise market analysis covering:
1. Target customer
2. Main problem
3. Existing alternatives
4. Differentiation
5. Market opportunity
6. Key market risks

Use reasoning rather than invented statistics.
Keep the response concise.
""",
        expected_output="A concise market analysis of about 300-400 words.",
        agent=agent,
    )


def create_business_task(agent):
    return Task(
        description="""
Analyze this idea as a business:

{idea}

Give a concise business analysis covering:
1. Value proposition
2. Revenue model
3. Pricing approach
4. Customer acquisition
5. Business opportunities
6. Business risks

Do not promise specific revenue.
Keep the response concise.
""",
        expected_output="A concise business analysis of about 300-400 words.",
        agent=agent,
    )


def create_technical_task(agent):
    return Task(
        description="""
Analyze the technical feasibility of this idea:

{idea}

Give a concise technical analysis covering:
1. MVP features
2. Recommended technology
3. Main components
4. AI requirements
5. Technical risks
6. Simplest implementation

Avoid over-engineering.
Keep the response concise.
""",
        expected_output="A concise technical analysis of about 300-400 words.",
        agent=agent,
    )
