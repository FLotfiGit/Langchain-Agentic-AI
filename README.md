# Langchain Agentic AI

I'm Fatemeh Lotfi, an Applied AI Scientist, PhD, and this repository is my hands-on LangChain learning project. I built it to start simple, then grow into more advanced agentic workflows as I go.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![LangChain](https://img.shields.io/badge/langchain-agentic_ai-orange.svg)](https://python.langchain.com/)

## Project Overview

This repository is my practical exploration of agentic AI with LangChain. I keep it structured as a learning journey so each phase builds on the last one in a way that is easy to follow and easy to extend.

### Key Features
- Progressive learning path: Simple → ReAct → Multi-Agent → Advanced patterns
- Clean architecture with reusable core components
- Example-driven learning with working code for each phase
- Testing and documentation included from the start
- Built to show real engineering habits, not just demo code

## Quick Start

### Prerequisites
- Python 3.10+
- pip or poetry
- OpenAI API key (or other LLM provider)

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd langchain-agentic-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your API keys
```

### Run Phase 1

```bash
cd examples/01_simple_agent
python main.py
```

You should see the agent print available tools and then run through a few sample prompts.

## Project Structure

```
langchain-agentic-ai/
├── src/                    # Core source code
│   ├── core/              # Base agent classes and utilities
│   ├── agents/            # Agent implementations
│   ├── tools/             # Tool definitions
│   └── utils/             # Utility functions
├── examples/              # Progressive examples
│   ├── 01_simple_agent/   # Phase 1: Basic agent
│   ├── 02_react_agent/    # Phase 2: ReAct reasoning
│   └── 03_multi_agent/    # Phase 3: Multi-agent systems
├── tests/                 # Unit and integration tests
├── docs/                  # Documentation and guides
└── logs/                  # Execution logs and traces
```

## Learning Path

### Phase 1: Simple Agent (Beginner)
- Basic agent with simple tools
- Understanding agent loop
- Tool calling and parsing
- **Focus**: Core concepts and architecture

### Phase 2: ReAct Agent (Intermediate)
- Reasoning + Acting pattern
- Complex tool composition
- Error handling and recovery
- **Focus**: Advanced reasoning patterns

### Phase 3: Multi-Agent Systems (Advanced)
- Agent collaboration and delegation
- Inter-agent communication
- Shared memory and context
- **Focus**: Scalable architectures

### Phase 4+: Production Patterns (Expert)
- Memory management and optimization
- Custom planning strategies
- Monitoring and logging
- Real-world integration

## Core Concepts

### Agents
Autonomous entities that use LLMs to reason and execute tasks through a loop of:
1. **Thought**: LLM analyzes the situation
2. **Action**: LLM decides what tool to use
3. **Observation**: Tool result is observed
4. **Repeat**: Until goal is reached

### Tools
Functions that agents can call to interact with the world:
- Data retrieval
- Calculations
- API calls
- External systems

## Documentation

See [docs/](docs/) for detailed guides:
- Architecture overview
- Agent design patterns
- Tool development guide
- Troubleshooting guide

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test file
pytest tests/test_agents.py -v
```

## Environment Setup

Create a `.env` file with required API keys:

```env
# LLM Provider (choose one)
OPENAI_API_KEY=your_key_here
# OR
ANTHROPIC_API_KEY=your_key_here

# Optional: Other services
SERPAPI_API_KEY=your_key_here
LANGSMITH_API_KEY=your_key_here
```

## References

### LangChain Documentation
- [LangChain Docs](https://python.langchain.com/)
- [Agents & Tools](https://python.langchain.com/docs/modules/agents/)

### Research Papers
- ReAct: Synergizing Reasoning and Acting in Language Models
- Multi-Agent Systems for Complex Problem Solving
- LangChain Framework Architecture

## Contributing

This is a learning project. Feel free to:
- Experiment with new agent patterns
- Improve examples and documentation
- Add new tool implementations
- Create advanced variants

## License

MIT License - See LICENSE file for details

## Author

Fatemeh Lotfi

Applied AI Scientist, PhD

---

**Status**: Active development
**Last Updated**: May 2026
**Current Phase**: 1 - Simple Agents
