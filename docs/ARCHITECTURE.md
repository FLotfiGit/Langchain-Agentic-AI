# Project Architecture

## Overview

The project is organized into layers:

```
┌─────────────────────────────────────────┐
│         Examples / Applications         │
│  (01_simple, 02_react, 03_multi_agent) │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│       Agents & Agent Patterns          │
│         (src/agents/)                   │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Core Components                    │
│  - BaseAgent                            │
│  - ToolRegistry                         │
│  (src/core/)                            │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│    Tools & Utilities                    │
│  - Tool definitions                     │
│  - Helper functions                     │
│  (src/tools, src/utils)                 │
└─────────────────────────────────────────┘
```

## Directory Structure

### src/core/
**Purpose**: Foundation classes and utilities

- `base_agent.py`: Abstract base class for all agents
  - Defines agent interface
  - Handles execution history
  - Provides logging utilities

- `tool_registry.py`: Central tool management
  - Registers and retrieves tools
  - Manages tool metadata
  - Handles tool lifecycle

### src/agents/
**Purpose**: Concrete agent implementations

- Different agent patterns (simple, react, multi-agent)
- Agent-specific logic
- Tool initialization for each agent

### src/tools/
**Purpose**: Tool definitions

- Tool functions
- Tool schemas
- Tool validation

### src/utils/
**Purpose**: Shared utilities

- Logging helpers
- Data processing
- Common utilities

### examples/
**Purpose**: Progressive learning examples

Each phase builds on previous knowledge:

1. **01_simple_agent/**: Basic concepts
   - Simple tools
   - Basic agent loop
   - Foundation understanding

2. **02_react_agent/**: Advanced reasoning
   - Structured reasoning
   - Complex chains
   - Error handling

3. **03_multi_agent/**: Scalability
   - Agent coordination
   - Message passing
   - Collaborative solving

### tests/
**Purpose**: Unit and integration tests

- Test base components
- Test agent functionality
- Test tool registry
- Test examples

## Key Design Patterns

### 1. Base Agent Pattern

All agents inherit from `BaseAgent`:

```python
class MyAgent(BaseAgent):
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        # Implementation
        pass
    
    def run(self, input_text: str, **kwargs) -> str:
        # Implementation
        pass
```

### 2. Tool Registry Pattern

Centralized tool management:

```python
registry = ToolRegistry()
registry.register("tool_name", func, "description")
tool = registry.get("tool_name")
```

### 3. Progressive Complexity

Each phase adds complexity:
- Phase 1: Single agent, simple tools
- Phase 2: Single agent, complex reasoning
- Phase 3: Multiple agents, coordination

## Data Flow

### Simple Agent Execution Flow

```
User Input
    │
    ▼
Agent.run() / Agent.execute()
    │
    ▼
LLM Decides Action
    │
    ▼
Look Up Tool
    │
    ▼
Call Tool Function
    │
    ▼
Process Result
    │
    ▼
Log Step (if verbose)
    │
    ▼
Return to User / Loop
```

### Tool Resolution

```
Tool Name
    │
    ▼
ToolRegistry.get(name)
    │
    ▼
Tool Object
    │
    ├─ func: Callable
    ├─ description: str
    └─ schema: Optional[Dict]
```

## Extension Points

### Adding a New Agent Type

1. Create new file in `src/agents/`
2. Inherit from `BaseAgent`
3. Implement `execute()` and `run()`
4. Register tools via ToolRegistry
5. Add example in `examples/`

### Adding New Tools

1. Define tool function in `src/tools/`
2. Add to ToolRegistry
3. Update tool descriptions
4. Add tests in `tests/`

### Adding a New Phase

1. Create directory in `examples/`
2. Implement agents
3. Create main.py example
4. Write README.md with learning goals
5. Add tests

## Configuration

### Environment Variables

Defined in `.env`:
- `OPENAI_API_KEY`: LLM provider key
- `LANGCHAIN_TRACING_V2`: Enable tracing
- `DEBUG`: Verbose output
- `LOG_LEVEL`: Logging level

### Runtime Configuration

Agent configuration:
```python
agent = SimpleAgent(
    verbose=True,        # Enable logging
    model="gpt-3.5-turbo",  # LLM model
    max_iterations=10,   # Iteration limit
    tools=[...]          # Available tools
)
```

## Testing Strategy

### Unit Tests
- Test individual components
- Mock dependencies
- Test edge cases

### Integration Tests
- Test agent with real tools
- Test end-to-end workflows
- Test error handling

### Example Tests
- Verify examples run
- Check output format
- Validate results

## Performance Considerations

1. **Token Usage**: Each LLM call has a cost
   - Optimize tool descriptions
   - Limit max iterations
   - Use streaming for large outputs

2. **Latency**: Network calls to LLM
   - Cache tool descriptions
   - Reuse agent instances
   - Batch operations when possible

3. **Memory**: Agent state
   - Clear history regularly
   - Use efficient data structures
   - Monitor for leaks

## Security Considerations

1. **API Keys**: Store securely in `.env`
2. **Tool Execution**: Validate tool inputs
3. **Agent Constraints**: Set iteration limits
4. **Logging**: Don't log sensitive data

---

For more details, see specific component documentation in `docs/` and `README.md` files in each directory.
