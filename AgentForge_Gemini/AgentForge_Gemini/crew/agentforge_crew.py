import os

from crewai import Crew, LLM, Process

from agents.manager import create_manager_agent
from agents.market import create_market_agent
from agents.business import create_business_agent
from agents.technical import create_technical_agent
from agents.challenger import create_challenger_agent

from tasks.analysis import (
    create_market_task,
    create_business_task,
    create_technical_task,
)
from tasks.debate import create_debate_task
from tasks.final_plan import create_final_plan_task


# Gemini Developer API free-tier model.
# Google currently lists Gemini 2.5 Flash as available with free
# input/output tokens on the Gemini API free tier.
MODEL_NAME = "gemini/gemini-2.5-flash"


def create_llm():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    return LLM(
        model=MODEL_NAME,
        api_key=api_key,
        temperature=0.2,
    )


def run_agentforge(idea: str):
    llm = create_llm()

    manager = create_manager_agent(llm)
    market = create_market_agent(llm)
    business = create_business_agent(llm)
    technical = create_technical_agent(llm)
    challenger = create_challenger_agent(llm)

    market_task = create_market_task(market)
    business_task = create_business_task(business)
    technical_task = create_technical_task(technical)

    debate_task = create_debate_task(
        challenger,
        market_task,
        business_task,
        technical_task,
    )

    final_task = create_final_plan_task(
        manager,
        market_task,
        business_task,
        technical_task,
        debate_task,
    )

    crew = Crew(
        agents=[
            market,
            business,
            technical,
            challenger,
            manager,
        ],
        tasks=[
            market_task,
            business_task,
            technical_task,
            debate_task,
            final_task,
        ],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff(inputs={"idea": idea})

    return {
        "market": market_task.output.raw if market_task.output else "",
        "business": business_task.output.raw if business_task.output else "",
        "technical": technical_task.output.raw if technical_task.output else "",
        "debate": debate_task.output.raw if debate_task.output else "",
        "final": result.raw if hasattr(result, "raw") else str(result),
    }
