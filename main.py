import asyncio
from src.agents.gherkin_agent import create_gherkin_agent
from src.agents.playwright_agent import create_playwright_agent
from src.agents.browser_agent import BrowserAgent
from src.database.session import init_db
from src.database.crud import create_test_log, update_test_log
from src.prompts.gherkin_scenario_template import gherkin_scenario_template

model_name = "openai"


async def main():
    init_db()

    print("QA Agent System")
    print("---------------")
    print("Type 'exit' to quit at any time")

    browser_agent = BrowserAgent(model_name=model_name)
    gherkin_agent = create_gherkin_agent(model_name=model_name)
    playwright_agent = create_playwright_agent()

    while True:
        print("\nMain Menu:")
        print("1. Create a Gherkin scenario")
        print("2. Run browser automation")
        print("3. Exit")

        main_choice = input("Enter your choice (1-3): ")

        if main_choice == "1":
            # Gherkin scenario creation flow
            question = input(
                "\nDescribe the feature you want to create a Gherkin scenario for: "
            )

            if question.lower() == "exit":
                print("Goodbye!")
                break

            test_log = create_test_log(
                feature_description=question,
            )

            gherkin_prompt = gherkin_scenario_template(feature_description=question)
            gherkin_response = gherkin_agent.run(gherkin_prompt)

            print(gherkin_response.content)

            update_test_log(
                log_id=test_log.id,
                gherkin_scenario=gherkin_response.content,
                ai_model=model_name,
            )

            # Submenu for Gherkin scenario
            while True:
                print("\nWhat would you like to do with this Gherkin scenario?")
                print("1. Generate Playwright test")
                print("2. Run browser automation with this scenario")
                print("3. Create a new Gherkin scenario")
                print("4. Return to main menu")

                sub_choice = input("Enter your choice (1-4): ")

                if sub_choice == "1":
                    # Generate Playwright test
                    print("\nGenerating Playwright test...")

                    playwright_response = playwright_agent.run(gherkin_response.content)
                    print(playwright_response.content)

                    update_test_log(
                        log_id=test_log.id,
                        playwright_test=playwright_response.content,
                    )

                elif sub_choice == "2":
                    # Run browser automation with the Gherkin scenario
                    print("\nRunning browser automation with the Gherkin scenario...")
                    try:
                        print("Starting browser automation...")
                        browser_response = await browser_agent.run(
                            gherkin_response.content
                        )
                        print("Browser automation completed")

                        browser_results = browser_response.final_result()
                        browser_results_str = str(browser_results)

                        update_test_log(
                            log_id=test_log.id,
                            browser_test=browser_results_str,
                        )

                    except Exception as e:
                        print(f"Error during browser automation: {e}")

                elif sub_choice == "3":
                    # Create a new Gherkin scenario - break to get a new scenario
                    break

                elif sub_choice == "4" or sub_choice.lower() == "exit":
                    # Return to main menu
                    break

                else:
                    print("Invalid choice. Please enter 1, 2, 3, or 4.")

                # Ask if they want to continue with this scenario
                continue_prompt = input(
                    "\nDo you want to continue with this scenario? (yes/no): "
                )
                if continue_prompt.lower() != "yes":
                    break

        elif main_choice == "2":
            while True:
                print("\nBrowser Automation")
                task = input(
                    "Enter the task for the browser agent (e.g., 'Search for Python tutorials')\nor type 'back' to return to main menu: "
                )

                if task.lower() == "back" or task.lower() == "exit":
                    break

                try:
                    print(f"Starting browser automation for task: {task}")
                    result = await browser_agent.run(task)
                    print("Browser automation completed")

                except Exception as e:
                    print(f"Error during browser automation: {e}")

                # Ask if they want to run another browser task
                continue_prompt = input(
                    "\nDo you want to run another browser task? (yes/no): "
                )
                if continue_prompt.lower() != "yes":
                    break

        elif main_choice == "3" or main_choice.lower() == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    asyncio.run(main())
