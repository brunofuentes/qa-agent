from agno.agent import Agent as AgnoAgent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv
from .llm_provider import get_agno_llm

load_dotenv()


def create_playwright_agent(model_name="gemini"):
    """Create a Playwright agent that can generate Playwright tests."""

    llm_model = get_agno_llm(model_name)

    return AgnoAgent(
        model=llm_model,
        markdown=True,
        description="I am a QA Playwright agent that can generate Playwright test scripts.",
        instructions=[
            "Generate Playwright test script for a given Gherkin scenario.",
            "Generates Python code only.",
        ],
    )
