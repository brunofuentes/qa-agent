from browser_use import Agent as BrowserUseAgent
from browser_use import Browser
from browser_use import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
from .llm_provider import get_langchain_llm

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


class BrowserAgent:
    def __init__(self, model_name="gemini"):
        """Initialize the browser agent with a specific model."""
        self.browser = Browser()
        self.controller = Controller()
        self.llm = get_langchain_llm(model_name=model_name)
        self.model_name = model_name

    def create(self, task):
        """Create a browser agent for a specific task."""
        return BrowserUseAgent(
            task=task,
            llm=self.llm,
            browser=self.browser,
            controller=self.controller,
        )

    async def run(self, task):
        """Run the browser agent on a specific task."""
        agent = BrowserUseAgent(
            task=task,
            llm=self.llm,
        )
        return await agent.run()


default_agent = BrowserAgent()


def create_browser_agent(task, model_name="gemini"):
    """Create a browser agent using browser-use with specified model."""
    agent = BrowserAgent(model_name)
    return agent.create(task)


async def run_browser_agent(task):
    """Run the browser agent with the specified task using default model."""
    return await default_agent.run(task)
