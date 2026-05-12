"""
Tool Registry - Manages tool definitions and resolution.

This module provides a central registry for all tools available to agents.
"""

from typing import Any, Callable, Dict, List, Optional
from pydantic import BaseModel, Field


class Tool(BaseModel):
    """Represents a tool that an agent can use."""

    name: str = Field(..., description="Tool name")
    description: str = Field(..., description="Tool description")
    func: Callable = Field(..., description="Callable function")
    input_schema: Optional[Dict[str, Any]] = Field(
        None, description="Input parameter schema"
    )

    class Config:
        arbitrary_types_allowed = True


class ToolRegistry:
    """
    Central registry for managing agent tools.

    This class maintains all tools available to agents and provides
    methods for registration, lookup, and introspection.
    """

    def __init__(self):
        """Initialize an empty tool registry."""
        self._tools: Dict[str, Tool] = {}

    def register(
        self,
        name: str,
        func: Callable,
        description: str,
        input_schema: Optional[Dict[str, Any]] = None,
    ) -> Tool:
        """
        Register a new tool.

        Args:
            name: Tool name
            func: Callable function
            description: Tool description
            input_schema: Input parameter schema

        Returns:
            Registered Tool object

        Raises:
            ValueError: If tool with same name already exists
        """
        if name in self._tools:
            raise ValueError(f"Tool '{name}' is already registered")

        tool = Tool(name=name, func=func, description=description, input_schema=input_schema)
        self._tools[name] = tool
        return tool

    def get(self, name: str) -> Optional[Tool]:
        """Get a tool by name."""
        return self._tools.get(name)

    def get_tool_function(self, name: str) -> Optional[Callable]:
        """Get a tool's function by name."""
        tool = self.get(name)
        return tool.func if tool else None

    def list_tools(self) -> List[Tool]:
        """Get all registered tools."""
        return list(self._tools.values())

    def list_tool_names(self) -> List[str]:
        """Get names of all registered tools."""
        return list(self._tools.keys())

    def tool_exists(self, name: str) -> bool:
        """Check if a tool exists."""
        return name in self._tools

    def unregister(self, name: str) -> bool:
        """
        Unregister a tool.

        Args:
            name: Tool name to unregister

        Returns:
            True if tool was unregistered, False if not found
        """
        if name in self._tools:
            del self._tools[name]
            return True
        return False

    def clear(self):
        """Clear all registered tools."""
        self._tools.clear()

    def __len__(self) -> int:
        """Get number of registered tools."""
        return len(self._tools)

    def __repr__(self) -> str:
        return f"ToolRegistry({len(self._tools)} tools)"
