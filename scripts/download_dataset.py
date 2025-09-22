#!/usr/bin/env python3
"""
Script to download the MMCSBench dataset.
"""

import os
import argparse
from pathlib import Path


def download_dataset(data_dir: str = "data/", force: bool = False):
    """
    Download the MMCSBench dataset.
    
    Args:
        data_dir: Directory to download data to
        force: Whether to overwrite existing data
    """
    data_path = Path(data_dir)
    data_path.mkdir(parents=True, exist_ok=True)
    
    print("MMCSBench Dataset Downloader")
    print("=" * 40)
    print(f"Target directory: {data_path.absolute()}")
    
    # Create directory structure
    directories = [
        "annotations",
        "images/train", 
        "images/val",
        "images/test",
        "metadata"
    ]
    
    for dir_name in directories:
        dir_path = data_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")
    
    # Create placeholder annotation files
    annotation_files = ["train.json", "val.json", "test.json"]
    for file_name in annotation_files:
        file_path = data_path / "annotations" / file_name
        if not file_path.exists() or force:
            sample_annotation = {
                "info": {
                    "description": "MMCSBench - Camouflage Scene Understanding",
                    "version": "1.0",
                    "year": 2024
                },
                "images": [],
                "annotations": []
            }
            
            import json
            with open(file_path, 'w') as f:
                json.dump(sample_annotation, f, indent=2)
            print(f"Created annotation file: {file_path}")
    
    # Create dataset info file
    info_file = data_path / "metadata" / "dataset_info.json"
    if not info_file.exists() or force:
        dataset_info = {
            "name": "MMCSBench",
            "description": "A Fine-Grained Benchmark for Large Vision-Language Models in Camouflage Scenes",
            "version": "1.0.0",
            "tasks": ["detection", "classification", "reasoning", "description"],
            "splits": {
                "train": {"num_images": 0, "num_annotations": 0},
                "val": {"num_images": 0, "num_annotations": 0}, 
                "test": {"num_images": 0, "num_annotations": 0}
            },
            "categories": {
                "camouflage_types": ["animal", "military", "adaptive", "natural"],
                "difficulty_levels": ["easy", "medium", "hard"]
            }
        }
        
        import json
        with open(info_file, 'w') as f:
            json.dump(dataset_info, f, indent=2)
        print(f"Created dataset info: {info_file}")
    
    # Create README for data directory
    readme_file = data_path / "README.md" 
    if not readme_file.exists() or force:
        readme_content = """# MMCSBench Dataset

This directory contains the MMCSBench dataset for evaluating Large Vision-Language Models on camouflage scene understanding.

## Directory Structure

- `annotations/`: JSON annotation files for each split
- `images/`: Image files organized by split (train/val/test)
- `metadata/`: Dataset metadata and documentation

## Data Format

### Annotation Format
Each annotation file contains:
- Image metadata (filename, size, etc.)
- Task-specific annotations:
  - Detection: Bounding boxes and object classes
  - Classification: Image-level labels
  - Reasoning: Question-answer pairs
  - Description: Captions and descriptions

### Image Organization
Images are organized by split and stored in standard formats (JPEG, PNG).

## Download Instructions

To download the complete dataset:
1. Run the download script: `python scripts/download_dataset.py`
2. The script will create the necessary directory structure
3. For the actual dataset files, please visit [dataset homepage] or contact the authors

## Citation

If you use this dataset, please cite:
```
@inproceedings{zhang2025mmcsbench,
  title={MMCSBench: A Fine-Grained Benchmark for Large Vision-Language Models in Camouflage Scenes},
  author={Zhang, Jin and [Other Authors]},
  booktitle={Advances in Neural Information Processing Systems},
  year={2025}
}
```
"""
        with open(readme_file, 'w') as f:
            f.write(readme_content)
        print(f"Created data README: {readme_file}")
    
    print("\nDataset structure created successfully!")
    print("\nNote: This script creates the directory structure and metadata files.")
    print("For the actual dataset images and annotations, please:")
    print("1. Visit the official MMCSBench webpage")
    print("2. Follow the data usage agreement")
    print("3. Download the complete dataset files")


def main():
    parser = argparse.ArgumentParser(description='Download MMCSBench dataset')
    parser.add_argument('--data-dir', default='data/', 
                        help='Directory to download data to (default: data/)')
    parser.add_argument('--force', action='store_true',
                        help='Overwrite existing files')
    
    args = parser.parse_args()
    download_dataset(args.data_dir, args.force)


if __name__ == "__main__":
    main()