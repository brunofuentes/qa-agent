def gherkin_scenario_template(feature_description: str) -> str:
    """Generate a minimal Gherkin scenario for testing a feature.

    Args:
        feature_description: User's description of the feature to test

    Returns:
        Formatted prompt for the agent
    """
    return f"""You are an experienced QA Engineer. Your task is to create the MINIMAL Gherkin scenario needed to test the following feature:

FEATURE DESCRIPTION:
{feature_description}

Create exactly ONE scenario that effectively tests the core functionality.
Follow these guidelines:
1. Use proper Gherkin syntax with Feature, Scenario, Given, When, Then
2. Include only the ESSENTIAL steps needed to test the feature
3. Be specific and concrete in your test steps
4. Avoid unnecessary complexity or edge cases
5. Focus on the happy path first
6. Use realistic test data

Respond ONLY with the Gherkin scenario. No explanations or additional text.
"""
