#!/usr/bin/env python3
"""
Example script demonstrating how to use MMCSBench for model evaluation.
"""

import argparse
from mmcsbench import MMCSBenchmark, load_model


def main():
    parser = argparse.ArgumentParser(description='Run MMCSBench evaluation')
    parser.add_argument('--config', default='configs/default.yaml', 
                        help='Path to configuration file')
    parser.add_argument('--model', required=True,
                        help='Model name to evaluate')
    parser.add_argument('--tasks', nargs='+', 
                        choices=['detection', 'classification', 'reasoning', 'description'],
                        help='Tasks to evaluate (default: all)')
    parser.add_argument('--split', default='test', choices=['train', 'val', 'test'],
                        help='Data split to use')
    parser.add_argument('--output-dir', default='results/',
                        help='Output directory for results')
    
    args = parser.parse_args()
    
    # Initialize benchmark
    print(f"Loading benchmark with config: {args.config}")
    benchmark = MMCSBenchmark(config=args.config)
    
    # Load model
    print(f"Loading model: {args.model}")
    model = load_model(args.model)
    
    # Run evaluation
    print(f"Running evaluation on {args.split} split...")
    results = benchmark.evaluate(
        model=model,
        tasks=args.tasks,
        split=args.split
    )
    
    # Print results
    print("\nEvaluation Results:")
    print("=" * 50)
    for task, metrics in results.items():
        print(f"\n{task.upper()} Task:")
        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    # Generate detailed report
    print(f"\nGenerating detailed report in {args.output_dir}")
    benchmark.generate_report(results, args.output_dir)
    
    print("Evaluation completed!")


if __name__ == "__main__":
    main()