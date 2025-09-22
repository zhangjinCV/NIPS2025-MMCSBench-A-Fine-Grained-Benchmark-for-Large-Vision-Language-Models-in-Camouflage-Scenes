# MMCSBench Test Suite

This directory contains the test suite for MMCSBench.

## Running Tests

To run the full test suite:
```bash
pytest tests/
```

To run specific test files:
```bash
pytest tests/test_benchmark.py
```

To run with coverage:
```bash
pytest --cov=mmcsbench tests/
```

## Test Structure

- `test_benchmark.py` - Tests for the main benchmark functionality
- `test_models.py` - Tests for model registry and loading
- `test_datasets.py` - Tests for dataset handling
- `test_evaluation.py` - Tests for evaluation metrics and protocols

## Writing Tests

When adding new functionality, please include corresponding tests:

1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test component interactions
3. **Mock Tests**: Use mocks for external dependencies

Example test:
```python
def test_new_functionality():
    """Test description."""
    # Arrange
    setup_test_data()
    
    # Act
    result = function_under_test()
    
    # Assert
    assert result == expected_value
```

## Test Dependencies

Some tests may require additional dependencies or data files. These should be:
- Minimal and self-contained
- Created within the test functions
- Cleaned up after testing