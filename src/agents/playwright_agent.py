from agno.agent import Agent as AgnoAgent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()


def create_playwright_agent():
    """Create a Playwright agent that can generate Playwright tests."""

    return AgnoAgent(
        model=Gemini(
            id="gemini-2.0-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
        markdown=True,
        description="I am a QA Playwright agent that can generate Playwright test scripts.",
        instructions=[
            "Generate Playwright test script for a given Gherkin scenario.",
            "Generates Python code only.",
        ],
    )
