"""
Main benchmark class for MMCSBench
"""

import yaml
from typing import Dict, List, Optional, Union
from pathlib import Path

from .evaluation import Evaluator
from .datasets import CamouflageDataset
from .models import ModelRegistry


class MMCSBenchmark:
    """
    Main benchmark class for evaluating Large Vision-Language Models 
    on camouflage scene understanding tasks.
    """
    
    def __init__(self, config: Union[str, Dict], data_dir: Optional[str] = None):
        """
        Initialize the benchmark.
        
        Args:
            config: Path to config file or config dictionary
            data_dir: Path to data directory
        """
        if isinstance(config, str):
            with open(config, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            self.config = config
            
        self.data_dir = data_dir or self.config.get('data_dir', 'data/')
        self.evaluator = Evaluator(self.config)
        self.dataset = CamouflageDataset(self.data_dir)
        
    def evaluate(self, model, tasks: Optional[List[str]] = None, split: str = 'test') -> Dict:
        """
        Evaluate a model on the benchmark tasks.
        
        Args:
            model: Model to evaluate
            tasks: List of tasks to evaluate on. If None, evaluates on all tasks.
            split: Data split to use ('train', 'val', 'test')
            
        Returns:
            Dictionary containing evaluation results
        """
        if tasks is None:
            tasks = ['detection', 'classification', 'reasoning', 'description']
            
        results = {}
        for task in tasks:
            print(f"Evaluating on {task} task...")
            task_results = self.evaluator.evaluate_task(model, task, split)
            results[task] = task_results
            
        return results
    
    def generate_report(self, results: Dict, output_dir: str = 'results/'):
        """
        Generate a detailed evaluation report.
        
        Args:
            results: Evaluation results dictionary
            output_dir: Directory to save the report
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Generate report logic here
        print(f"Report generated in {output_dir}")