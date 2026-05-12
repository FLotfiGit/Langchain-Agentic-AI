# Getting Started with Langchain Agents

## Prerequisites

- Python 3.10 or higher
- pip or poetry
- An OpenAI API key (or other LLM provider)

## Installation Steps

### 1. Clone and Setup

```bash
cd langchain-agentic-ai
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
OPENAI_API_KEY=sk-your-key-here
```

### 4. Verify Installation

```bash
# Run tests to verify everything works
pytest tests/ -v
```

## Quick Start - Phase 1

### Run Your First Agent

```bash
cd examples/01_simple_agent
python main.py
```

### Understanding the Output

The agent will process your tasks and show:
- **Thought**: What the agent is thinking
- **Action**: Which tool it's using
- **Observation**: The tool's result
- **Final Answer**: The agent's conclusion

## Development Path

### Phase 1: Simple Agent ✓
- Basic agent with simple tools
- Understanding the agent loop
- Tool definition and registration

**Next Steps**:
1. Run `examples/01_simple_agent/main.py`
2. Try modifying the example tasks
3. Add your own tools

### Phase 2: ReAct Agent (Coming Soon)
- Structured reasoning patterns
- Complex tool composition
- Multi-step reasoning

### Phase 3: Multi-Agent Systems (Coming Soon)
- Agent collaboration
- Task delegation
- Shared context

## Common Commands

```bash
# Run tests
pytest tests/ -v

# Run specific test file
pytest tests/test_base_agent.py -v

# Run with coverage
pytest tests/ --cov=src

# Format code
black src/ examples/

# Lint code
flake8 src/ examples/

# Run type checking
mypy src/
```

## Troubleshooting

### API Key Issues

**Problem**: `openai.error.AuthenticationError`

**Solution**:
1. Check `.env` file exists and has correct path
2. Verify API key is correct
3. Check API key has appropriate permissions

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'langchain'`

**Solution**:
```bash
pip install -r requirements.txt
# or reinstall
pip install langchain langchain-openai python-dotenv
```

### Agent Not Using Right Tool

**Problem**: Agent uses wrong tool for the task

**Solution**:
- Improve tool descriptions to be more specific
- Check if tool parameters are clear
- Add examples to tool docstrings

## Next Steps

1. **Explore Phase 1**: Understand simple agents thoroughly
2. **Modify Examples**: Add new tools and tasks
3. **Read Documentation**: Check `docs/` folder for detailed guides
4. **Run Tests**: Ensure everything works
5. **Build Confidence**: Experiment before moving to Phase 2

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [OpenAI API Docs](https://platform.openai.com/docs/)

## Getting Help

1. Check the example README in each phase directory
2. Review the docstrings in the code
3. Run tests to understand expected behavior
4. Check LangChain documentation
