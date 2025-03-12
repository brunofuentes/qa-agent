from agno.agent import Agent as AgnoAgent


def gherkin_to_playwright_prompt(gherkin_scenario: str) -> str:
    """
    Convert a Gherkin scenario into a structured prompt for generating Playwright code.

    Args:
        gherkin_scenario (str): The Gherkin scenario text

    Returns:
        str: A structured prompt for the AI to generate Playwright code
    """

    prompt = f"""
# Gherkin Scenario to Playwright Test Conversion

## Gherkin Scenario:
```gherkin
{gherkin_scenario}
```

## Task:
Convert the above Gherkin scenario into a complete, working Playwright Python script.

## Requirements:
1. Use Playwright's Page Object Model pattern if appropriate
2. The file should include ALL necessary imports for Playwright
3. Implement all Given/When/Then steps from the scenario
4. Add appropriate assertions to verify the expected behavior
5. Include error handling and timeout management
6. Add comments explaining the implementation

## Output Format:
Return ONLY the Python code without any additional explanation.
"""

    return prompt.strip()


def generate_playwright_code(agent: AgnoAgent, gherkin_scenario: str) -> str:
    """
    Generate Playwright code from a Gherkin scenario using an AI agent.

    Args:
        agent: The AI agent to use for code generation
        gherkin_scenario (str): The Gherkin scenario text

    Returns:
        The agent's response containing the generated code
    """
    prompt = gherkin_to_playwright_prompt(gherkin_scenario)
    return agent.print_response(prompt, stream=True)
