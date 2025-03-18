from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def get_llm(model_name="gemini"):
    """Get the LLM based on the chosen model name.

    Args:
        model_name (str): The name of the model to use - "gemini", "claude", or "openai"

    Returns:
        The language model instance configured for use
    """
    models = {
        "gemini": ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2,
        ),
        "claude": ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.2,
        ),
        "openai": ChatOpenAI(
            model="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.2,
        ),
    }

    return models.get(model_name.lower(), models["gemini"])
