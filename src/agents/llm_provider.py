from agno.models.google import Gemini
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def get_agno_llm(model_name="gemini"):
    """Get the Agno LLM based on the chosen model name.

    Args:
        model_name (str): The name of the model to use - "gemini", "claude", or "openai"

    Returns:
        The Agno model instance configured for use
    """
    models = {
        "gemini": Gemini(
            id="gemini-2.0-flash-exp",
            api_key=os.getenv("GOOGLE_API_KEY"),
        ),
        "claude": Claude(
            id="claude-3-5-sonnet-20240620",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        ),
        "openai": OpenAIChat(
            id="gpt-4o",
            api_key=os.getenv("OPENAI_API_KEY"),
        ),
    }

    return models.get(model_name.lower(), models["gemini"])


def get_langchain_llm(model_name="gemini"):
    """Get the LangChain LLM based on the chosen model name.

    Args:
        model_name (str): The name of the model to use - "gemini", "claude", or "openai"

    Returns:
        The LangChain model instance configured for use
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
