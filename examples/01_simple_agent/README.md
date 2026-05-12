# Phase 1: Simple Agent

## Overview

This phase establishes the first working track in the broader LangChain project.

### What This Phase Covers

1. **Agent Fundamentals**
   - What is an agent?
   - The agent loop: Thought → Action → Observation
   - How LLMs make decisions

2. **Tools**
   - Defining tools
   - Tool registration
   - Tool calling and parameter parsing

3. **Basic Agent Patterns**
   - ReAct (Reasoning + Acting)
   - Error handling
   - Simple task execution

### Key Concepts

#### Agent Loop

```
Input: "What is 5 times 3, plus 10?"
    ↓
[Thought]: "I need to multiply 5 by 3, then add 10"
    ↓
[Action]: Use multiply_numbers tool with (5, 3)
    ↓
[Observation]: Got 15
    ↓
[Thought]: "Now I need to add 10 to 15"
    ↓
[Action]: Use add_numbers tool with (15, 10)
    ↓
[Observation]: Got 25
    ↓
Output: "The answer is 25"
```

#### Tool Definition

A tool is a function that an agent can call. In LangChain:

```python
@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b
```

### Running the Example

```bash
# Navigate to this directory
cd examples/01_simple_agent

# Set up environment (if not already done)
cp ../../.env.example ../../.env
# Edit .env with your OpenAI API key

# Run the example
python main.py
```

### Code Structure

- `agent.py` - SimpleAgent class and tool definitions
- `main.py` - Example usage and test cases

### Understanding the Code

#### SimpleAgent Initialization

```python
agent = SimpleAgent(verbose=True)
```

- Creates an LLM instance (ChatOpenAI)
- Registers available tools
- Initializes LangChain's agent framework

#### Running Tasks

```python
result = agent.run("What is 15 plus 25?")
```

The agent will:
1. Parse the task
2. Decide which tool to use
3. Call the appropriate tool
4. Observe the result
5. Return the final answer

### Exercises

Try modifying the code:

1. **Add a new tool**: Create a subtraction function and register it
2. **Complex tasks**: Try multi-step problems requiring multiple tool calls
3. **Error handling**: What happens with invalid inputs?
4. **Tool descriptions**: Improve tool descriptions to guide the agent better

### Common Issues

**Issue**: Agent doesn't use the right tool
- **Solution**: Improve tool descriptions to be more specific

**Issue**: Agent gets stuck in a loop
- **Solution**: Lower `max_iterations` or improve tool output clarity

**Issue**: API errors
- **Solution**: Check `.env` file and ensure OPENAI_API_KEY is set correctly

### Next Steps

Once you're comfortable with this phase:
- Move to Phase 2: ReAct Agent for more complex reasoning
- Explore error handling and recovery mechanisms
- Implement custom tool resolution logic

### References

- [LangChain Agent Documentation](https://python.langchain.com/docs/modules/agents/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
