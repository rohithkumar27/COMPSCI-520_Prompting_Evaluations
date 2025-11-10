#!/usr/bin/env python3
"""
Extract baseline coverage from existing coverage reports for Part 2.
"""

import json
from pathlib import Path


def extract_coverage_from_json(json_file):
    """Extract coverage data from coverage.json file."""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    results = []
    
    for file_path, file_data in data['files'].items():
        if 'attempt_1' in file_path:  # Only attempt 1 files
            summary = file_data['summary']
            
            results.append({
                'file': Path(file_path).name,
                'line_coverage': summary['percent_covered'],
                'lines_covered': summary['covered_lines'],
                'lines_total': summary['num_statements'],
                'missing_lines': summary['missing_lines'],
                'has_branches': data['meta'].get('branch_coverage', False)
            })
    
    return results


def main():
    """Extract baseline coverage for all models."""
    
    models = [
        'groq_chain_of_thought',
        'groq_step_chain_of_thought',
        'gemini_chain_of_thought',
        'gemini_step_chain_of_thought'
    ]
    
    print("="*70)
    print("BASELINE COVERAGE EXTRACTION")
    print("="*70)
    
    for model in models:
        json_file = Path(f"coverage_reports/{model}_attempt1/coverage.json")
        
        if not json_file.exists():
            print(f"\n⚠️  {model}: coverage.json not found")
            continue
        
        print(f"\n📊 {model}")
        print("-"*70)
        
        results = extract_coverage_from_json(json_file)
        
        for result in results:
            print(f"\n  File: {result['file']}")
            print(f"  Line Coverage: {result['line_coverage']}%")
            print(f"  Lines: {result['lines_covered']}/{result['lines_total']}")
            print(f"  Missing Lines: {result['missing_lines']}")
            print(f"  Branch Coverage Available: {result['has_branches']}")
    
    # Generate summary for Part 2
    print("\n" + "="*70)
    print("RECOMMENDED PROBLEMS FOR PART 2")
    print("="*70)
    
    print("\n✅ Problem 1: humaneval_0_p1_attempt_1.py (has_close_elements)")
    print("   Model: groq_chain_of_thought")
    print("   Baseline: 100% line coverage")
    print("   Reason: Already at 100%, good for testing if LLM can maintain coverage")
    
    print("\n✅ Problem 2: humaneval_1_p2_attempt_1.py (separate_paren_groups)")
    print("   Model: groq_chain_of_thought")
    print("   Baseline: 100% line coverage")
    print("   Reason: Failed tests, room for improvement in test quality")


if __name__ == "__main__":
    main()
