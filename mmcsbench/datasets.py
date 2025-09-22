"""
Dataset classes for MMCSBench
"""

import json
import os
from typing import Dict, List, Tuple, Optional
from pathlib import Path

try:
    from PIL import Image
    import torch
    from torch.utils.data import Dataset
except ImportError:
    # Make imports optional for basic functionality
    Image = None
    torch = None
    Dataset = object


class CamouflageDataset(Dataset):
    """
    Main dataset class for MMCSBench camouflage scenes.
    """
    
    def __init__(self, data_dir: str, split: str = 'train', transform=None):
        """
        Initialize the dataset.
        
        Args:
            data_dir: Path to dataset directory
            split: Data split ('train', 'val', 'test')
            transform: Optional image transformations
        """
        self.data_dir = Path(data_dir)
        self.split = split
        self.transform = transform
        
        # Load annotations
        self.annotations = self._load_annotations()
        self.images_dir = self.data_dir / 'images' / split
        
    def _load_annotations(self) -> List[Dict]:
        """Load dataset annotations."""
        annotation_file = self.data_dir / 'annotations' / f'{self.split}.json'
        if annotation_file.exists():
            with open(annotation_file, 'r') as f:
                return json.load(f)
        else:
            # Return empty list if annotation file doesn't exist
            return []
    
    def __len__(self) -> int:
        """Return dataset size."""
        return len(self.annotations)
    
    def __getitem__(self, idx: int) -> Dict:
        """
        Get a dataset item.
        
        Args:
            idx: Item index
            
        Returns:
            Dictionary containing image, annotations, and metadata
        """
        if not self.annotations:
            # Return dummy data if no annotations
            if torch:
                dummy_image = torch.zeros(3, 224, 224)
            else:
                dummy_image = None
            return {
                'image': dummy_image,
                'image_id': f'dummy_{idx}',
                'annotations': {}
            }
            
        annotation = self.annotations[idx]
        
        # Load image
        image_path = self.images_dir / annotation['image_file']
        if image_path.exists() and Image:
            image = Image.open(image_path).convert('RGB')
            if self.transform:
                image = self.transform(image)
        else:
            # Return dummy image if file doesn't exist or PIL not available
            if torch:
                image = torch.zeros(3, 224, 224)
            else:
                image = None
        
        return {
            'image': image,
            'image_id': annotation.get('image_id', f'item_{idx}'),
            'annotations': annotation
        }
    
    def get_task_data(self, task: str) -> List[Dict]:
        """
        Get data for a specific task.
        
        Args:
            task: Task name ('detection', 'classification', 'reasoning', 'description')
            
        Returns:
            List of task-specific data items
        """
        task_data = []
        for annotation in self.annotations:
            if task in annotation.get('tasks', {}):
                task_data.append(annotation['tasks'][task])
        return task_data