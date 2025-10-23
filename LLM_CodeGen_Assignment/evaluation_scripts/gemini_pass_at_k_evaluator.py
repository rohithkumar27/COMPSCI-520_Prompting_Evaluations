#!/usr/bin/env python3
"""
Gemini Pass@K Evaluator - Evaluate Pass@K metrics for Gemini-generated solutions
"""

import os
import sys
import subprocess
import tempfile
from typing import Dict, List, Any
from collections import defaultdict
import json
from datetime import datetime

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from humaneval_dataset import HUMANEVAL_PROBLEMS
from apps_tough_problems import APPS_TOUGH_PROBLEMS

class GeminiPassAtKEvaluator:
    """Pass@K evaluator specifically for Gemini-generated solutions"""
    
    def __init__(self):
        self.all_problems = HUMANEVAL_PROBLEMS + APPS_TOUGH_PROBLEMS
        self.results = defaultdict(lambda: defaultdict(list))
        
    def evaluate_gemini_solutions(self, k_values=[1, 3, 5]):
        """Evaluate Pass@K for Gemini solutions"""
        
        print("🔍 GEMINI PASS@K EVALUATION")
        print("=" * 50)
        print(f"Evaluating Pass@{k_values} metrics")
        
        # Find Gemini solution directories
        gemini_dirs = self.find_gemini_directories()
        
        if not gemini_dirs:
            print("❌ No Gemini solution directories found!")
            return
        
        print(f"Found Gemini strategies: {', '.join(gemini_dirs)}")
        
        # Collect and test all solutions
        self.collect_and_test_gemini_solutions(gemini_dirs)
        
        # Calculate Pass@K for each strategy
        results = {}
        for strategy in gemini_dirs:
            print(f"\n🔍 Evaluating {strategy}")
            strategy_results = self.calculate_strategy_pass_at_k(strategy, k_values)
            results[strategy] = strategy_results
        
        # Generate comprehensive report
        self.generate_gemini_pass_at_k_report(results, k_values)
        
        return results
    
    def find_gemini_directories(self) -> List[str]:
        """Find all Gemini solution directories"""
        gemini_dirs = []
        generated_base = "../generated"
        
        if os.path.exists(generated_base):
            for item in os.listdir(generated_base):
                if "gemini" in item.lower() and os.path.isdir(os.path.join(generated_base, item)):
                    gemini_dirs.append(item)
        
        return gemini_dirs
    
    def collect_and_test_gemini_solutions(self, strategies: List[str]):
        """Collect and test all Gemini solutions for Pass@K calculation"""
        
        print(f"\n📥 Collecting and testing Gemini solutions...")
        
        for strategy in strategies:
            strategy_dir = f"../generated/{strategy}"
            
            if not os.path.exists(strategy_dir):
                continue
            
            # Group files by problem
            problem_files = defaultdict(list)
            
            for file_name in os.listdir(strategy_dir):
                if file_name.endswith('.py') and not file_name.startswith('__'):
                    problem_id = self.extract_problem_id(file_name)
                    if problem_id:
                        file_path = os.path.join(strategy_dir, file_name)
                        problem_files[problem_id].append(file_path)
            
            # Test all solutions for each problem
            for problem_id, file_paths in problem_files.items():
                problem = self.find_problem_by_id(problem_id)
                if problem:
                    print(f"  Testing {len(file_paths)} solutions for {strategy}/{problem_id}")
                    
                    for file_path in file_paths:
                        result = self.test_solution(file_path, problem)
                        self.results[strategy][problem_id].append({
                            'file_path': file_path,
                            'passed': result['passed'],
                            'error': result.get('error', ''),
                            'attempt_number': self.extract_attempt_number(file_path)
                        })
    
    def extract_problem_id(self, file_name: str) -> str:
        """Extract problem ID from filename"""
        # Parse: humaneval_0_p1_attempt_1.py or apps_0_p1_attempt_1.py
        if file_name.startswith('humaneval_'):
            task_num = file_name.split('_')[1]
            return f"Easy/{task_num}"
        elif file_name.startswith('apps_'):
            task_num = file_name.split('_')[1]
            return f"APPS/{task_num}"
        return None
    
    def extract_attempt_number(self, file_path: str) -> int:
        """Extract attempt number from filename"""
        try:
            # Extract from: humaneval_0_p1_attempt_1.py
            parts = os.path.basename(file_path).split('_')
            for i, part in enumerate(parts):
                if part == 'attempt' and i + 1 < len(parts):
                    return int(parts[i + 1].split('.')[0])
        except:
            pass
        return 1
    
    def find_problem_by_id(self, problem_id: str) -> Dict:
        """Find problem by ID"""
        for problem in self.all_problems:
            if problem['task_id'] == problem_id:
                return problem
        return None
    
    def test_solution(self, file_path: str, problem: Dict) -> Dict:
        """Test a solution against its problem test cases"""
        
        try:
            # Read the solution
            with open(file_path, 'r', encoding='utf-8') as f:
                solution_code = f.read()
            
            # Extract just the function code (remove comments)
            lines = solution_code.split('\n')
            function_lines = []
            for line in lines:
                if not line.strip().startswith('#'):
                    function_lines.append(line)
            
            clean_code = '\n'.join(function_lines)
            
            # Create test file
            test_code = f"""
{clean_code}

{problem['test']}
"""
            
            # Run test
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(test_code)
                temp_file = f.name
            
            try:
                result = subprocess.run(
                    ['python', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                passed = result.returncode == 0
                return {
                    'passed': passed,
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                    'return_code': result.returncode
                }
                
            finally:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    
        except Exception as e:
            return {
                'passed': False,
                'error': str(e),
                'stdout': '',
                'stderr': str(e)
            }
    
    def calculate_strategy_pass_at_k(self, strategy: str, k_values: List[int]) -> Dict:
        """Calculate Pass@K metrics using the correct mathematical formula"""
        import math
        
        strategy_results = {}
        
        for k in k_values:
            pass_at_k_scores = []
            total_problems = 0
            
            for problem_id, solutions in self.results[strategy].items():
                n = len(solutions)  # Total solutions for this problem
                if n >= k:
                    total_problems += 1
                    c = sum(1 for sol in solutions if sol['passed'])  # Correct solutions
                    
                    # Correct Pass@K formula: 1 - C(n-c, k) / C(n, k)
                    if c >= k:
                        # If we have k or more correct solutions, Pass@K = 1.0
                        pass_at_k_score = 1.0
                    elif c == 0:
                        # If no correct solutions, Pass@K = 0.0
                        pass_at_k_score = 0.0
                    else:
                        # Calculate using binomial coefficients
                        try:
                            # C(n, k) = n! / (k! * (n-k)!)
                            c_n_k = math.comb(n, k)
                            c_n_minus_c_k = math.comb(n - c, k) if (n - c) >= k else 0
                            pass_at_k_score = 1.0 - (c_n_minus_c_k / c_n_k)
                        except (ValueError, ZeroDivisionError):
                            # Fallback to simple method if math fails
                            pass_at_k_score = 1.0 if c > 0 else 0.0
                    
                    pass_at_k_scores.append(pass_at_k_score)
            
            # Average Pass@K across all problems
            avg_pass_at_k = (sum(pass_at_k_scores) / len(pass_at_k_scores)) if pass_at_k_scores else 0.0
            pass_at_k_percentage = avg_pass_at_k * 100
            
            # Also calculate simple "at least 1 passes" for comparison
            simple_passed = 0
            for problem_id, solutions in self.results[strategy].items():
                if len(solutions) >= k:
                    k_solutions = solutions[:k]
                    if any(sol['passed'] for sol in k_solutions):
                        simple_passed += 1
            
            simple_rate = (simple_passed / total_problems * 100) if total_problems > 0 else 0
            
            strategy_results[f"Pass@{k}"] = {
                'rate': pass_at_k_percentage,
                'simple_rate': simple_rate,
                'problems_evaluated': total_problems,
                'individual_scores': pass_at_k_scores
            }
            
            print(f"  Pass@{k} (Correct Formula): {pass_at_k_percentage:.1f}%")
            print(f"  Pass@{k} (Simple Method): {simple_rate:.1f}%")
            print(f"  Problems evaluated: {total_problems}")
        
        return strategy_results
    
    def generate_gemini_pass_at_k_report(self, results: Dict, k_values: List[int]):
        """Generate comprehensive Pass@K report for Gemini"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"gemini_pass_at_k_report_{timestamp}.md"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Gemini Pass@K Evaluation Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Model:** Gemini 2.5 Flash-Lite\n")
            f.write(f"**K Values:** {k_values}\n\n")
            
            # Summary table
            f.write("## Summary Results\n\n")
            f.write("| Strategy | " + " | ".join([f"Pass@{k}" for k in k_values]) + " | Problems |\n")
            f.write("|----------|" + "|".join(["--------" for _ in k_values]) + "|----------|\n")
            
            for strategy, strategy_results in results.items():
                strategy_name = strategy.replace('gemini_', '').replace('_', ' ').title()
                row = f"| {strategy_name} |"
                
                total_problems = 0
                for k in k_values:
                    pass_k_data = strategy_results[f"Pass@{k}"]
                    row += f" {pass_k_data['rate']:.1f}% |"
                    total_problems = pass_k_data['problems_evaluated']
                
                row += f" {total_problems} |\n"
                f.write(row)
            
            # Detailed analysis
            f.write("\n## Detailed Analysis\n\n")
            
            for strategy, strategy_results in results.items():
                strategy_name = strategy.replace('gemini_', '').replace('_', ' ').title()
                f.write(f"### {strategy_name}\n\n")
                
                for k in k_values:
                    pass_k_data = strategy_results[f"Pass@{k}"]
                    f.write(f"- **Pass@{k}**: {pass_k_data['rate']:.1f}% ")
                    f.write(f"({pass_k_data['passed']}/{pass_k_data['total']} problems)\n")
                
                f.write("\n")
            
            # Problem-by-problem breakdown
            f.write("## Problem-by-Problem Results\n\n")
            
            for strategy in results.keys():
                strategy_name = strategy.replace('gemini_', '').replace('_', ' ').title()
                f.write(f"### {strategy_name}\n\n")
                
                for problem_id, solutions in self.results[strategy].items():
                    passed_solutions = sum(1 for sol in solutions if sol['passed'])
                    total_solutions = len(solutions)
                    
                    f.write(f"- **{problem_id}**: {passed_solutions}/{total_solutions} solutions passed\n")
                
                f.write("\n")
        
        print(f"\n📄 Detailed report saved: {report_file}")

def main():
    """Main function"""
    
    evaluator = GeminiPassAtKEvaluator()
    
    print("🚀 Starting Gemini Pass@K Evaluation...")
    
    # Evaluate with different K values
    k_values = [1, 3, 5]
    results = evaluator.evaluate_gemini_solutions(k_values)
    
    if results:
        print(f"\n✅ Evaluation completed!")
        print(f"📊 Results for {len(results)} Gemini strategies")
    else:
        print(f"\n❌ No results generated")

if __name__ == "__main__":
    main()