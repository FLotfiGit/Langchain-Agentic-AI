"""
Track 01: Smart Task Execution Agent - Main Example.

This script demonstrates practical task-planning workflows with the agent.
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Add this example directory to path so the script can be run directly.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from agent import SimpleAgent


def main():
    """Run representative planning tasks with the smart task execution agent."""
    
    logger.info("Initializing Smart Task Execution Agent...")
    agent = SimpleAgent(verbose=True)
    
    # Example requests aligned with real planning workflows.
    tasks = [
        "Prioritize this backlog: Prepare project proposal (3h), Respond to client email (0.5h), Fix release blocker urgent (2h), Review PR #42 (1h), Schedule interview prep session (1h)",
        "Build a day plan with hours: 7. Tasks: Finalize grant proposal draft (3h), Review production bugfix (1.5h), Team sync notes (0.5h), Interview prep (1.5h), Inbox cleanup (0.5h)",
        "Assess execution risks for these tasks: waiting on API approval, integrate new auth flow, blocked by missing credentials, finalize deployment checklist",
        "Suggest next actions for: Prepare for senior applied AI scientist interview next week",
        "Create an execution plan for today: I have 6 hours and need to finish a proposal, unblock deployment, and send client updates.",
    ]
    
    logger.info("=" * 60)
    logger.info("SMART TASK EXECUTION AGENT EXAMPLES")
    logger.info("=" * 60)
    
    print("\nAvailable Tools:")
    for tool_info in agent.get_tools_info():
        print(f"  - {tool_info['name']}: {tool_info['description']}")
    
    print("\n" + "=" * 60)
    print("EXECUTING TASKS")
    print("=" * 60)
    
    for i, task in enumerate(tasks, 1):
        print(f"\nTask {i}: {task}")
        print("-" * 60)
        try:
            result = agent.run(task)
            print(f"Result: {result}")
        except Exception as e:
            logger.error(f"Error executing task {i}: {e}")
    
    print("\n" + "=" * 60)
    logger.info("Smart Task Execution Agent examples completed!")


if __name__ == "__main__":
    main()
