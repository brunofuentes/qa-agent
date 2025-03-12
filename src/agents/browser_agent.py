from browser_use import Agent as BrowserUseAgent
from browser_use import Browser
from browser_use import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()

browser = Browser()
controller = Controller()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

anthropic_llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    temperature=0.2,
)


def create_browser_agent(task):
    """Create a browser agent using browser-use with Google Gemini."""

    # Create the browser-use Agent with the Gemini LLM
    return BrowserUseAgent(
        task=task,
        llm=gemini_llm,
        browser=browser,
        controller=controller,
    )


async def run_browser_agent(task):
    """Run the browser agent with the specified task."""

    agent = BrowserUseAgent(
        task=task,
        llm=gemini_llm,
    )
    return await agent.run()
