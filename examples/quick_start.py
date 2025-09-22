#!/usr/bin/env python3
"""
Quick start demo for MMCSBench
"""

from mmcsbench import MMCSBenchmark
from mmcsbench.models import BaseModel

try:
    import torch
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("Warning: PyTorch not available. Using mock implementation.")


class DummyModel(BaseModel):
    """Dummy model for demonstration purposes."""
    
    def forward(self, image, text=None):
        # Simple dummy implementation
        if TORCH_AVAILABLE:
            return torch.randn(1, 1000)
        else:
            return [0.5] * 1000  # Mock tensor-like output
    
    def generate(self, image, prompt, **kwargs):
        # Generate dummy text response
        return "This is a dummy response for camouflage detection."


def main():
    print("MMCSBench Quick Start Demo")
    print("=" * 40)
    
    # Initialize benchmark with default config
    config = {
        'data_dir': 'data/',
        'evaluation': {'batch_size': 1}
    }
    benchmark = MMCSBenchmark(config=config)
    
    # Create a dummy model for demonstration
    model = DummyModel()
    
    # Run evaluation on a subset of tasks
    print("Running evaluation with dummy model...")
    try:
        results = benchmark.evaluate(
            model=model,
            tasks=['classification', 'reasoning'],
            split='test'
        )
        
        # Display results
        print("\nResults:")
        for task, metrics in results.items():
            print(f"{task}: {metrics}")
            
    except Exception as e:
        print(f"Note: This is a demo with dummy data. Error: {e}")
        print("To run actual evaluation, please set up the dataset first.")
    
    print("\nDemo completed!")
    print("For full functionality, please:")
    print("1. Download the actual MMCSBench dataset")
    print("2. Install a real vision-language model")
    print("3. Run: python examples/evaluate_model.py --model your_model")


if __name__ == "__main__":
    main()