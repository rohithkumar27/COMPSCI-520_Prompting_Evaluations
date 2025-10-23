#!/usr/bin/env python3
"""
Comprehensive Pass@K Evaluator - Detailed problem-wise analysis with test case breakdown
"""

import os
import sys
import subprocess
import tempfile
import math
import re
from typing import Dict, List, Any
from collections import defaultdict
from datetime import datetime

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from humaneval_dataset import HUMANEVAL_PROBLEMS
from apps_tough_problems import APPS_TOUGH_PROBLEMS

class ComprehensivePassAtKEvaluator:
    """Comprehensive evaluator with detailed test case analysis"""
    
    def __init__(self):
        self.all_problems = HUMANEVAL_PROBLEMS + APPS_TOUGH_PROBLEMS
        self.detailed_results = defaultdict(lambda: defaultdict(list))
        
    def evaluate_with_detailed_analysis(self, provider_filter="gemini", k_values=[1, 3, 5]):
        """Comprehensive evaluation with detailed test case analysis"""
        
        print("🔍 COMPREHENSIVE PASS@K EVALUATION WITH DETAILED ANALYSIS")
        print("=" * 70)
        print(f"Formula: Pass@K = E[1 - C(n-c, k) / C(n, k)]")
        print(f"Provider: {provider_filter}")
        print(f"K Values: {k_values}")
        
        # Find solution directories
        solution_dirs = self.find_solution_directories(provider_filter)
        
        if not solution_dirs:
            print(f"❌ No solution directories found!")
            return {}
        
        print(f"Found strategies: {', '.join(solution_dirs)}")
        
        # Detailed testing with individual test case analysis
        self.detailed_testing_with_test_cases(solution_dirs)
        
        # Calculate Pass@K with detailed breakdown
        results = {}
        for strategy in solution_dirs:
            print(f"\n🔍 DETAILED ANALYSIS: {strategy}")
            print("-" * 50)
            strategy_results = self.calculate_detailed_pass_at_k(strategy, k_values)
            results[strategy] = strategy_results
        
        # Generate comprehensive report
        self.generate_comprehensive_report(results, k_values, provider_filter)
        
        return results
    
    def find_solution_directories(self, provider_filter="") -> List[str]:
        """Find solution directories"""
        solution_dirs = []
        generated_base = "../generated"
        
        if os.path.exists(generated_base):
            for item in os.listdir(generated_base):
                if os.path.isdir(os.path.join(generated_base, item)):
                    if not provider_filter or provider_filter.lower() in item.lower():
                        solution_dirs.append(item)
        
        return solution_dirs
    
    def detailed_testing_with_test_cases(self, strategies: List[str]):
        """Test solutions with individual test case breakdown"""
        
        print(f"\n📥 Detailed testing with individual test case analysis...")
        
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
            
            # Test each problem's solutions with detailed analysis
            for problem_id, file_paths in problem_files.items():
                problem = self.find_problem_by_id(problem_id)
                if problem:
                    print(f"  📋 {strategy}/{problem_id}: Testing {len(file_paths)} solutions")
                    
                    for file_path in file_paths:
                        detailed_result = self.test_solution_with_test_cases(file_path, problem)
                        self.detailed_results[strategy][problem_id].append({
                            'file_path': file_path,
                            'file_name': os.path.basename(file_path),
                            'overall_passed': detailed_result['overall_passed'],
                            'test_cases': detailed_result['test_cases'],
                            'total_test_cases': detailed_result['total_test_cases'],
                            'passed_test_cases': detailed_result['passed_test_cases'],
                            'error': detailed_result.get('error', ''),
                            'attempt_number': self.extract_attempt_number(file_path)
                        })
    
    def test_solution_with_test_cases(self, file_path: str, problem: Dict) -> Dict:
        """Test solution with individual test case breakdown"""
        
        try:
            # Read solution
            with open(file_path, 'r', encoding='utf-8') as f:
                solution_code = f.read()
            
            # Extract function code
            lines = solution_code.split('\n')
            function_lines = []
            for line in lines:
                if not line.strip().startswith('#'):
                    function_lines.append(line)
            
            clean_code = '\n'.join(function_lines)
            
            # Extract individual test cases from problem test
            test_cases = self.extract_individual_test_cases(problem['test'])
            
            # Test each case individually
            individual_results = []
            for i, test_case in enumerate(test_cases, 1):
                test_result = self.run_individual_test(clean_code, test_case, i)
                individual_results.append(test_result)
            
            # Overall result
            overall_passed = all(result['passed'] for result in individual_results)
            passed_count = sum(1 for result in individual_results if result['passed'])
            
            return {
                'overall_passed': overall_passed,
                'test_cases': individual_results,
                'total_test_cases': len(individual_results),
                'passed_test_cases': passed_count
            }
            
        except Exception as e:
            return {
                'overall_passed': False,
                'test_cases': [],
                'total_test_cases': 0,
                'passed_test_cases': 0,
                'error': str(e)
            }
    
    def extract_individual_test_cases(self, test_code: str) -> List[str]:
        """Extract individual assert statements from test code"""
        
        test_cases = []
        lines = test_code.split('\n')
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('assert '):
                test_cases.append(stripped)
        
        return test_cases
    
    def run_individual_test(self, function_code: str, test_case: str, test_num: int) -> Dict:
        """Run individual test case"""
        
        try:
            # Create test file for individual test case
            test_code = f"""
{function_code}

# Individual test case {test_num}
try:
    {test_case}
    print("PASS")
except Exception as e:
    print(f"FAIL: {{str(e)}}")
"""
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(test_code)
                temp_file = f.name
            
            try:
                result = subprocess.run(
                    ['python', temp_file],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                
                passed = "PASS" in result.stdout
                error_msg = result.stdout.replace("PASS", "").replace("FAIL: ", "").strip()
                
                return {
                    'test_number': test_num,
                    'test_case': test_case,
                    'passed': passed,
                    'error': error_msg if not passed else None
                }
                
            finally:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    
        except Exception as e:
            return {
                'test_number': test_num,
                'test_case': test_case,
                'passed': False,
                'error': str(e)
            }
    
    def calculate_detailed_pass_at_k(self, strategy: str, k_values: List[int]) -> Dict:
        """Calculate Pass@K with detailed problem breakdown"""
        
        strategy_results = {}
        problem_details = {}
        
        for k in k_values:
            pass_at_k_scores = []
            problems_evaluated = 0
            
            print(f"\n📊 Pass@{k} Analysis:")
            
            for problem_id, solutions in self.detailed_results[strategy].items():
                n = len(solutions)
                
                if n >= k:
                    problems_evaluated += 1
                    c = sum(1 for sol in solutions if sol['overall_passed'])
                    
                    # Calculate Pass@K score for this problem
                    if c >= k:
                        pass_at_k_score = 1.0
                    elif c == 0:
                        pass_at_k_score = 0.0
                    else:
                        try:
                            if (n - c) >= k:
                                c_n_k = math.comb(n, k)
                                c_n_minus_c_k = math.comb(n - c, k)
                                pass_at_k_score = 1.0 - (c_n_minus_c_k / c_n_k)
                            else:
                                pass_at_k_score = 1.0
                        except:
                            pass_at_k_score = 1.0 if c > 0 else 0.0
                    
                    pass_at_k_scores.append(pass_at_k_score)
                    
                    # Store problem details
                    if problem_id not in problem_details:
                        problem_details[problem_id] = {}
                    
                    problem_details[problem_id][f"Pass@{k}"] = {
                        'score': pass_at_k_score,
                        'correct_solutions': c,
                        'total_solutions': n,
                        'solutions_detail': []
                    }
                    
                    # Add solution details
                    for sol in solutions:
                        problem_details[problem_id][f"Pass@{k}"]['solutions_detail'].append({
                            'file_name': sol['file_name'],
                            'passed': sol['overall_passed'],
                            'test_cases_passed': f"{sol['passed_test_cases']}/{sol['total_test_cases']}",
                            'failing_tests': [tc for tc in sol['test_cases'] if not tc['passed']]
                        })
                    
                    # Print problem-wise results
                    status = "✅ PASS" if pass_at_k_score > 0 else "❌ FAIL"
                    print(f"    {problem_id}: {status} (Score: {pass_at_k_score:.2f}, {c}/{n} correct)")
            
            # Calculate overall Pass@K
            avg_pass_at_k = sum(pass_at_k_scores) / len(pass_at_k_scores) if pass_at_k_scores else 0.0
            
            strategy_results[f"Pass@{k}"] = {
                'percentage': avg_pass_at_k * 100,
                'problems_evaluated': problems_evaluated,
                'problem_details': problem_details
            }
            
            print(f"  📊 Overall Pass@{k}: {avg_pass_at_k * 100:.1f}% ({problems_evaluated} problems)")
        
        return strategy_results
    
    def extract_problem_id(self, file_name: str) -> str:
        """Extract problem ID from filename"""
        if file_name.startswith('humaneval_'):
            task_num = file_name.split('_')[1]
            return f"Easy/{task_num}"
        elif file_name.startswith('apps_'):
            task_num = file_name.split('_')[1]
            return f"APPS/{task_num}"
        return None
    
    def extract_attempt_number(self, file_path: str) -> int:
        """Extract attempt number"""
        try:
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