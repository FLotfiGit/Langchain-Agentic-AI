"""
Phase 1: Simple Agent - Main Example

This script demonstrates how to use the SimpleAgent with various tasks.
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
    """Run example tasks with the SimpleAgent."""
    
    logger.info("Initializing Simple Agent...")
    agent = SimpleAgent(verbose=True)
    
    # Example tasks
    tasks = [
        "What is 15 plus 25?",
        "Multiply 7 by 8",
        "What's the weather in New York?",
        "How far is it from London to Paris?",
        "Calculate what 10 times 5 equals, then add 20 to that result",
    ]
    
    logger.info("=" * 60)
    logger.info("SIMPLE AGENT EXAMPLES")
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
    logger.info("Simple Agent examples completed!")


if __name__ == "__main__":
    main()
