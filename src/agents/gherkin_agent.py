from agno.agent import Agent as AgnoAgent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()


def create_gherkin_agent():
    """Create a Gherkin agent that can generate Gherkin scenarios."""

    return AgnoAgent(
        model=Gemini(
            id="gemini-2.0-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
        markdown=True,
        description="I am a Gherkin agent that can generate Gherkin scenarios.",
        instructions=[
            "Generate Gherkin scenarios for a given feature.",
            "Use proper Gherkin syntax with Feature, Scenario, Given, When, Then",
            "Include tags for organization",
            "Use the most recent version of the Gherkin syntax",
            "Focus on functional requirements",
        ],
    )
