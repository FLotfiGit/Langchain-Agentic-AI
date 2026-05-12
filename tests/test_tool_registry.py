"""
Tests for tool registry.
"""

import pytest
from src.core.tool_registry import ToolRegistry


def test_tool_registry_initialization():
    """Test tool registry initialization."""
    registry = ToolRegistry()
    assert len(registry) == 0


def test_register_tool():
    """Test registering a tool."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    tool = registry.register(
        "test_tool",
        dummy_tool,
        "A test tool",
    )
    
    assert tool.name == "test_tool"
    assert len(registry) == 1


def test_get_tool():
    """Test retrieving a tool."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    registry.register("test_tool", dummy_tool, "A test tool")
    tool = registry.get("test_tool")
    
    assert tool is not None
    assert tool.name == "test_tool"


def test_get_nonexistent_tool():
    """Test retrieving a nonexistent tool."""
    registry = ToolRegistry()
    tool = registry.get("nonexistent")
    
    assert tool is None


def test_tool_exists():
    """Test checking if tool exists."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    registry.register("test_tool", dummy_tool, "A test tool")
    
    assert registry.tool_exists("test_tool") is True
    assert registry.tool_exists("nonexistent") is False


def test_unregister_tool():
    """Test unregistering a tool."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    registry.register("test_tool", dummy_tool, "A test tool")
    assert len(registry) == 1
    
    success = registry.unregister("test_tool")
    assert success is True
    assert len(registry) == 0


def test_list_tools():
    """Test listing all tools."""
    registry = ToolRegistry()
    
    def tool1(x: int) -> int:
        return x * 2
    
    def tool2(x: int) -> int:
        return x * 3
    
    registry.register("tool1", tool1, "First tool")
    registry.register("tool2", tool2, "Second tool")
    
    tools = registry.list_tools()
    assert len(tools) == 2
    
    names = registry.list_tool_names()
    assert "tool1" in names
    assert "tool2" in names


def test_duplicate_registration():
    """Test that registering duplicate tool names raises error."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    registry.register("test_tool", dummy_tool, "A test tool")
    
    with pytest.raises(ValueError):
        registry.register("test_tool", dummy_tool, "Another tool")


def test_clear_registry():
    """Test clearing the registry."""
    registry = ToolRegistry()
    
    def dummy_tool(x: int) -> int:
        return x * 2
    
    registry.register("tool1", dummy_tool, "Tool 1")
    registry.register("tool2", dummy_tool, "Tool 2")
    
    assert len(registry) == 2
    registry.clear()
    assert len(registry) == 0
