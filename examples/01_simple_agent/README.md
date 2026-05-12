# Track 01: Simple Agent

## Objective

Deliver a minimal single-agent implementation with tool calling, deterministic behavior, and clear execution output.

## Included Components

- `agent.py`: `SimpleAgent` implementation and tool registration
- `main.py`: executable entry point with representative task prompts

## Implemented Capabilities

- Arithmetic tool invocation (`add_numbers`, `multiply_numbers`)
- Simulated data retrieval tools (`get_weather`, `calculate_distance`)
- Agent execution loop using `AgentType.ZERO_SHOT_REACT_DESCRIPTION`
- Bounded iteration and parsing error handling

## Runtime Flow

1. Build LLM client and register tools.
2. Initialize LangChain agent executor.
3. Submit task prompt.
4. Execute Thought/Action/Observation loop.
5. Return final output.

## Run

```bash
cd examples/01_simple_agent
python main.py
```

## Operational Notes

- Requires valid provider credentials in `.env`.
- Tool outputs are intentionally simple for deterministic behavior.
- Example is intended as the baseline track for subsequent ReAct and multi-agent implementations.

## Known Constraints

- Weather and distance tools are simulated, not API-backed.
- Current model default is fixed in code (`gpt-3.5-turbo`).

## Next Track

Track 02 will extend this baseline with a structured ReAct-style reasoning flow and stronger tool orchestration.

## References

- [LangChain Agents](https://python.langchain.com/docs/modules/agents/)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
