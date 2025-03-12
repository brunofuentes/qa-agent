from agno.agent import Agent as AgnoAgent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()


def create_simple_qa_agent():
    """Create the most basic agent that just answers questions."""

    return AgnoAgent(
        model=Gemini(
            id="gemini-2.0-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
        markdown=True,
        description="I am a simple QA agent that answers questions directly.",
        instructions=[
            "Provide clear and concise answers to questions.",
            "If you don't know the answer, say so.",
        ],
    )
