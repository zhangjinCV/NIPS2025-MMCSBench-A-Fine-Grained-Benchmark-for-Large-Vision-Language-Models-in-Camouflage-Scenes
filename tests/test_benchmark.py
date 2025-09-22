"""
Test module for MMCSBench benchmark functionality.
"""

import pytest
import tempfile
from pathlib import Path
from mmcsbench import MMCSBenchmark
from mmcsbench.models import BaseModel


class DummyModel(BaseModel):
    """Dummy model for testing."""
    
    def forward(self, image, text=None):
        import torch
        return torch.randn(1, 1000)
    
    def generate(self, image, prompt, **kwargs):
        return "Test response"


class TestBenchmark:
    """Test cases for MMCSBenchmark class."""
    
    def test_benchmark_initialization_with_dict_config(self):
        """Test benchmark initialization with dictionary config."""
        config = {
            'data_dir': 'test_data/',
            'evaluation': {'batch_size': 1}
        }
        benchmark = MMCSBenchmark(config=config)
        assert benchmark.data_dir == 'test_data/'
        assert benchmark.config == config
    
    def test_benchmark_initialization_with_file_config(self):
        """Test benchmark initialization with file config."""
        # Create temporary config file
        config_data = {
            'data_dir': 'file_test_data/',
            'evaluation': {'batch_size': 2}
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            import yaml
            yaml.dump(config_data, f)
            config_file = f.name
        
        try:
            benchmark = MMCSBenchmark(config=config_file)
            assert benchmark.data_dir == 'file_test_data/'
            assert benchmark.config['evaluation']['batch_size'] == 2
        finally:
            Path(config_file).unlink()  # Clean up temp file
    
    def test_evaluate_with_dummy_model(self):
        """Test evaluation with dummy model."""
        config = {
            'data_dir': 'test_data/',
            'evaluation': {'batch_size': 1}
        }
        benchmark = MMCSBenchmark(config=config)
        model = DummyModel()
        
        # Test with specific tasks
        results = benchmark.evaluate(
            model=model,
            tasks=['classification', 'reasoning'],
            split='test'
        )
        
        assert 'classification' in results
        assert 'reasoning' in results
        assert isinstance(results['classification'], dict)
        assert isinstance(results['reasoning'], dict)
    
    def test_evaluate_all_tasks(self):
        """Test evaluation with all tasks."""
        config = {
            'data_dir': 'test_data/',
            'evaluation': {'batch_size': 1}
        }
        benchmark = MMCSBenchmark(config=config)
        model = DummyModel()
        
        # Test with all tasks (default)
        results = benchmark.evaluate(model=model, split='test')
        
        expected_tasks = ['detection', 'classification', 'reasoning', 'description']
        for task in expected_tasks:
            assert task in results