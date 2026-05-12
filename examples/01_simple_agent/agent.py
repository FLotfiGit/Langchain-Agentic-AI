"""
Simple Agent - Phase 1: Basic agent with simple tools.

This is the foundational example demonstrating core agent concepts:
- Tool registration and usage
- Basic agent loop
- Thought-action-observation pattern
"""

from typing import Any, Dict, List
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents.agent_toolkits import create_openai_tools_agent
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.output_parsers import ReActJsonSingleInputOutputParser
import logging

logger = logging.getLogger(__name__)


# Define simple tools
@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


@tool
def get_weather(location: str) -> str:
    """Get weather for a location (simulated)."""
    # In a real application, this would call a weather API
    weather_data = {
        "New York": "Sunny, 72°F",
        "London": "Rainy, 54°F",
        "Tokyo": "Cloudy, 68°F",
    }
    return weather_data.get(location, "Weather data not available")


@tool
def calculate_distance(point1: str, point2: str) -> str:
    """Calculate distance between two points (simulated)."""
    # Simulated distance calculations
    distances = {
        ("New York", "Boston"): "215 miles",
        ("London", "Paris"): "215 miles",
        ("Tokyo", "Seoul"): "600 miles",
    }
    key = tuple(sorted([point1, point2]))
    return distances.get(key, "Distance not found")


class SimpleAgent:
    """
    A simple agent that uses LangChain's built-in agent framework.
    
    This agent demonstrates:
    - Tool definition and registration
    - Basic agent loop using LangChain
    - Task execution with tools
    """

    def __init__(self, verbose: bool = True):
        """
        Initialize the Simple Agent.

        Args:
            verbose: Enable verbose output
        """
        self.verbose = verbose
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        self.agent = None
        self.tools = self._setup_tools()
        self._initialize_agent()

    def _setup_tools(self) -> List[Tool]:
        """Set up available tools."""
        tools = [
            Tool(
                name="add_numbers",
                func=add_numbers.invoke,
                description="Useful for adding two numbers together",
            ),
            Tool(
                name="multiply_numbers",
                func=multiply_numbers.invoke,
                description="Useful for multiplying two numbers together",
            ),
            Tool(
                name="get_weather",
                func=get_weather.invoke,
                description="Get weather information for a location",
            ),
            Tool(
                name="calculate_distance",
                func=calculate_distance.invoke,
                description="Calculate distance between two locations",
            ),
        ]
        return tools

    def _initialize_agent(self):
        """Initialize the LangChain agent."""
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=self.verbose,
            max_iterations=5,
            handle_parsing_errors=True,
        )

    def run(self, task: str) -> str:
        """
        Run the agent on a task.

        Args:
            task: The task description

        Returns:
            Agent's response
        """
        try:
            result = self.agent.run(task)
            return result
        except Exception as e:
            logger.error(f"Agent error: {e}")
            return f"Error executing task: {str(e)}"

    def execute(self, task: str) -> Dict[str, Any]:
        """
        Execute a task and return detailed results.

        Args:
            task: The task description

        Returns:
            Dictionary with execution details
        """
        try:
            result = self.agent.run(task)
            return {
                "success": True,
                "output": result,
                "task": task,
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "task": task,
            }

    def get_tools_info(self) -> List[Dict[str, str]]:
        """Get information about available tools."""
        return [
            {
                "name": tool.name,
                "description": tool.description,
            }
            for tool in self.tools
        ]
