# Contributing Guide

## Development Setup

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/langchain-agentic-ai.git
cd langchain-agentic-ai
```

### 2. Create Development Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .  # Install in development mode
```

### 3. Set Up Pre-commit Hooks

```bash
pre-commit install
```

## Code Style Guidelines

### Python Style

We follow PEP 8 with some preferences:

- Line length: 100 characters
- Use type hints for all functions
- Docstrings for all public modules, classes, and functions

### Formatting

```bash
# Format code with black
black src/ examples/

# Sort imports with isort
isort src/ examples/

# Check linting
flake8 src/ examples/

# Type checking
mypy src/
```

## Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Write Code

- Follow code style guidelines
- Add type hints
- Add docstrings
- Keep functions focused and small

### 3. Write Tests

Every feature should have tests:

```bash
# Create test file in tests/
pytest tests/test_your_feature.py -v
```

### 4. Update Documentation

- Update README if adding features
- Update docstrings
- Add examples if appropriate

## Testing

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Tests

```bash
pytest tests/test_specific.py -v
```

### With Coverage

```bash
pytest tests/ --cov=src
```

### Examples

Run example scripts to ensure they work:

```bash
python examples/01_simple_agent/main.py
```

## Commit Guidelines

Use clear, descriptive commit messages:

```
feat: Add new agent type
fix: Correct tool registry bug
docs: Update architecture guide
test: Add tests for X feature
refactor: Simplify agent loop
```

Format: `<type>: <description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `refactor`: Code refactoring
- `chore`: Maintenance

## Pull Request Process

1. **Ensure tests pass**: `pytest tests/ -v`
2. **Check code style**: `black . && flake8 . && mypy .`
3. **Update documentation**: As needed
4. **Create pull request** with clear description
5. **Address review comments**

## Adding New Agents

When adding a new agent type:

1. Create file in `src/agents/`
2. Inherit from `BaseAgent`
3. Implement required methods
4. Add tools
5. Create example in `examples/`
6. Add tests
7. Document with README and docstrings

## Adding New Tools

When adding tools:

1. Define in `src/tools/`
2. Use `@tool` decorator or Tool class
3. Add clear descriptions
4. Validate inputs
5. Handle errors
6. Add tests
7. Document usage

## Adding New Phases

When adding a new learning phase:

1. Create `examples/<number>_<name>/` directory
2. Implement new agent patterns
3. Create `main.py` with examples
4. Write comprehensive `README.md`
5. Add tests in `tests/`
6. Update main project README
7. Document learning objectives

## Documentation Standards

### Docstrings

Use Google-style docstrings:

```python
def function(arg1: str, arg2: int) -> bool:
    """Short description.
    
    Longer description if needed.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When something is invalid
    """
```

### Comments

- Explain WHY, not WHAT
- Keep comments updated with code
- Remove commented-out code

### Type Hints

Use comprehensive type hints:

```python
def process_data(items: List[str]) -> Dict[str, Any]:
    """Process items and return results."""
```

## Troubleshooting Development

### Issue: Tests Fail

```bash
# Clear cache
find . -type d -name __pycache__ -exec rm -r {} +
pytest tests/ -v --tb=short
```

### Issue: Import Errors

```bash
# Reinstall in development mode
pip install -e .
```

### Issue: Style Errors

```bash
# Auto-fix
black src/ examples/
isort src/ examples/
```

## Performance Testing

When optimizing:

1. Benchmark before changes
2. Profile the code
3. Document improvements
4. Keep tests passing

## Release Process

Releases follow semantic versioning (MAJOR.MINOR.PATCH):

1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Create git tag
4. Push to repository

---

Thank you for contributing! Questions? Open an issue or discussion.
