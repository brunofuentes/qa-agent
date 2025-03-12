from agno import Agent, Task
from typing import Dict, Any
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


class QATestingAgent(Agent):
    """Agent for QA testing automation."""

    def __init__(self):
        super().__init__()

        # Configure the LLM
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.2,
            top_p=0.95,
            top_k=40,
            max_output_tokens=2048,
        )

        # Agent configuration
        self.config = {
            "name": "QA Testing Agent",
            "description": "Performs automated QA testing on web applications",
            "capabilities": ["web testing", "UI verification", "test reporting"],
            "max_retries": 3,
            "timeout_seconds": 300,
        }

    async def execute(self, task: Task) -> Dict[str, Any]:
        """Execute the QA testing task."""

        # Get the test parameters from the task
        test_url = task.inputs.get("url")
        test_scenario = task.inputs.get("scenario")

        # Use the LLM to generate test steps from the scenario
        test_plan_prompt = f"""
        Create a detailed test plan for the following scenario:
        URL: {test_url}
        Scenario: {test_scenario}

        Format the test plan as a list of specific steps to execute.
        """

        llm_response = await self.llm.agenerate([test_plan_prompt])
        test_steps = llm_response.generations[0].text

        self.logger.info(f"Generated test plan with {test_steps.count('\\n')} steps")

        # Execute test steps (simplified for example)
        # In a real implementation, you would use browser-use here
        test_results = {
            "url": test_url,
            "scenario": test_scenario,
            "status": "passed",
            "steps": test_steps,
            "steps_executed": 5,
            "steps_passed": 5,
            "execution_time": "2.3s",
        }

        return {
            "results": test_results,
            "summary": f"Test for {test_url} completed successfully.",
        }
