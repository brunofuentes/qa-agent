from agno.agent import Agent as AgnoAgent
from .llm_provider import get_agno_llm


def create_gherkin_agent(model_name="gemini"):
    """Create a Gherkin agent that can generate Gherkin scenarios."""

    llm_model = get_agno_llm(model_name)

    return AgnoAgent(
        model=llm_model,
        markdown=True,
        description="I am a QA Tester agent that generates Gherkin scenarios.",
        instructions=[
            "Validate if the feature is implemented",
            "Generate Gherkin scenarios for a given feature.",
            "Use proper Gherkin syntax with Feature, Scenario, Given, When, Then",
            "Include tags for organization",
            "Use the most recent version of the Gherkin syntax",
            "Focus on functional requirements",
            "Create as few scenarios as possible to cover the feature",
        ],
    )
