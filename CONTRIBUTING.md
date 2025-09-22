# Contributing to MMCSBench

We welcome contributions to MMCSBench! This document provides guidelines for contributing to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Types of Contributions](#types-of-contributions)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/NIPS2025-MMCSBench-A-Fine-Grained-Benchmark-for-Large-Vision-Language-Models-in-Camouflage-Scenes.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Submit a pull request

## Types of Contributions

We welcome the following types of contributions:

### 🐛 Bug Fixes
- Fix incorrect behavior
- Improve error handling
- Documentation corrections

### ✨ New Features
- New evaluation metrics
- Support for additional models
- New benchmark tasks
- Performance improvements

### 📚 Documentation
- API documentation improvements
- Tutorial enhancements
- Example code

### 🔧 Infrastructure
- CI/CD improvements
- Testing enhancements
- Build system updates

## Development Setup

1. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

2. **Install pre-commit hooks:**
   ```bash
   pre-commit install
   ```

3. **Run tests to ensure everything works:**
   ```bash
   pytest tests/
   ```

## Coding Standards

### Python Code Style
- Follow PEP 8 style guidelines
- Use type hints where possible
- Maximum line length: 88 characters (Black default)
- Use meaningful variable and function names

### Code Formatting
We use the following tools for code formatting:
- **Black**: Code formatter
- **isort**: Import sorting
- **flake8**: Linting

Run formatting tools:
```bash
black .
isort .
flake8 .
```

### Documentation
- Use docstrings for all public functions and classes
- Follow Google docstring format
- Include examples in docstrings when helpful

Example:
```python
def evaluate_model(model, task: str, split: str = 'test') -> Dict[str, float]:
    """
    Evaluate a model on a specific task.
    
    Args:
        model: The model to evaluate
        task: Task name ('detection', 'classification', etc.)
        split: Data split to use (default: 'test')
        
    Returns:
        Dictionary containing evaluation metrics
        
    Example:
        >>> results = evaluate_model(my_model, 'detection')
        >>> print(results['mAP'])
        0.75
    """
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_benchmark.py

# Run with coverage
pytest --cov=mmcsbench tests/
```

### Writing Tests
- Write tests for all new features and bug fixes
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies

Example:
```python
def test_benchmark_initialization():
    """Test that benchmark initializes correctly."""
    config = {'data_dir': 'test_data/'}
    benchmark = MMCSBenchmark(config)
    assert benchmark.data_dir == 'test_data/'
```

## Pull Request Process

1. **Before submitting:**
   - Ensure all tests pass
   - Run code formatting tools
   - Update documentation if needed
   - Add tests for new functionality

2. **Pull Request Description:**
   - Clearly describe what your changes do
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

3. **Review Process:**
   - At least one maintainer review is required
   - Address all review comments
   - Ensure CI checks pass

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

## Issue Reporting

When reporting issues, please include:

1. **Bug Reports:**
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)
   - Error messages and stack traces

2. **Feature Requests:**
   - Clear description of the proposed feature
   - Use case and motivation
   - Possible implementation approach

3. **Questions:**
   - Check existing documentation first
   - Provide context about what you're trying to achieve
   - Include relevant code snippets

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help create a welcoming environment for all contributors

## Getting Help

- Open an issue for questions
- Check existing issues and documentation
- Reach out to maintainers for guidance

Thank you for contributing to MMCSBench! 🎉