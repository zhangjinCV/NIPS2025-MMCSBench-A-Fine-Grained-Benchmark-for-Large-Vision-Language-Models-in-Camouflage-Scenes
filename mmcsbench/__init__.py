"""
MMCSBench: A Fine-Grained Benchmark for Large Vision-Language Models in Camouflage Scenes

This package provides a comprehensive benchmark for evaluating Large Vision-Language Models
on camouflage scene understanding tasks.
"""

__version__ = "1.0.0"
__author__ = "Jin Zhang"
__email__ = ""

from .benchmark import MMCSBenchmark
from .models import ModelRegistry, load_model
from .evaluation import Evaluator
from .datasets import CamouflageDataset

__all__ = [
    "MMCSBenchmark",
    "ModelRegistry", 
    "load_model",
    "Evaluator",
    "CamouflageDataset",
]