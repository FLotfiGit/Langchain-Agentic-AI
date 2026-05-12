"""
Tests for base agent functionality.
"""

import pytest
from src.core.base_agent import BaseAgent
from typing import Dict, Any


class MockAgent(BaseAgent):
    """Mock agent for testing base functionality."""

    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Mock execute method."""
        return {
            "success": True,
            "output": f"Mock result for: {task}",
            "steps": ["step1", "step2"],
            "total_iterations": 2,
        }

    def run(self, input_text: str, **kwargs) -> str:
        """Mock run method."""
        return f"Mock output for: {input_text}"


def test_agent_initialization():
    """Test agent initialization."""
    agent = MockAgent(
        name="TestAgent",
        description="A test agent",
        model=None,
        tools=[],
        verbose=False,
    )
    
    assert agent.name == "TestAgent"
    assert agent.description == "A test agent"
    assert len(agent.tools) == 0


def test_agent_execution():
    """Test agent execution."""
    agent = MockAgent(
        name="TestAgent",
        description="A test agent",
        model=None,
    )
    
    result = agent.execute("Test task")
    
    assert result["success"] is True
    assert "Test task" in result["output"]


def test_execution_history():
    """Test execution history logging."""
    agent = MockAgent(
        name="TestAgent",
        description="A test agent",
        model=None,
    )
    
    # Log some steps
    agent.log_step(1, "Thinking about task", "action1", "observation1")
    agent.log_step(2, "Continuing", "action2", "observation2")
    
    history = agent.get_execution_history()
    
    assert len(history) == 2
    assert history[0]["step"] == 1
    assert history[1]["step"] == 2
    assert history[0]["thought"] == "Thinking about task"


def test_history_clear():
    """Test clearing execution history."""
    agent = MockAgent(
        name="TestAgent",
        description="A test agent",
        model=None,
    )
    
    agent.log_step(1, "Test", "action", "observation")
    assert len(agent.get_execution_history()) == 1
    
    agent.clear_history()
    assert len(agent.get_execution_history()) == 0
