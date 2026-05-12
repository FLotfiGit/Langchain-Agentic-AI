"""
Base Agent class - Foundation for all agent implementations.

This module provides the base class for building LangChain-based agents.
All agents should inherit from BaseAgent and implement required methods.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    
    Defines the interface and core functionality that all agents must implement.
    Handles logging, state management, and execution tracing.
    """

    def __init__(
        self,
        name: str,
        description: str,
        model: Any,
        tools: Optional[List[Any]] = None,
        max_iterations: int = 10,
        verbose: bool = False,
    ):
        """
        Initialize the base agent.

        Args:
            name: Agent name
            description: Agent description
            model: LLM instance (e.g., ChatOpenAI)
            tools: List of tools available to the agent
            max_iterations: Maximum iterations in agent loop
            verbose: Enable verbose logging
        """
        self.name = name
        self.description = description
        self.model = model
        self.tools = tools or []
        self.max_iterations = max_iterations
        self.verbose = verbose
        self.execution_history = []

        logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    @abstractmethod
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """
        Execute the agent on a given task.

        Args:
            task: The task description or query
            **kwargs: Additional arguments specific to the agent

        Returns:
            Dictionary containing:
                - output: Final result
                - steps: Execution steps
                - total_iterations: Number of iterations
                - success: Whether execution was successful
        """
        pass

    @abstractmethod
    def run(self, input_text: str, **kwargs) -> str:
        """
        Simple interface to run the agent.

        Args:
            input_text: Input text/query
            **kwargs: Additional arguments

        Returns:
            String output from the agent
        """
        pass

    def log_step(self, step_number: int, thought: str, action: str, observation: str):
        """
        Log a single step in the agent's reasoning process.

        Args:
            step_number: Current step number
            thought: Agent's thought process
            action: Action taken
            observation: Result of the action
        """
        step_record = {
            "timestamp": datetime.now().isoformat(),
            "step": step_number,
            "thought": thought,
            "action": action,
            "observation": observation,
        }
        self.execution_history.append(step_record)

        if self.verbose:
            logger.debug(f"Step {step_number}:")
            logger.debug(f"  Thought: {thought}")
            logger.debug(f"  Action: {action}")
            logger.debug(f"  Observation: {observation}")

    def get_execution_history(self) -> List[Dict[str, Any]]:
        """Get the complete execution history."""
        return self.execution_history

    def clear_history(self):
        """Clear the execution history."""
        self.execution_history = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', tools={len(self.tools)})"
