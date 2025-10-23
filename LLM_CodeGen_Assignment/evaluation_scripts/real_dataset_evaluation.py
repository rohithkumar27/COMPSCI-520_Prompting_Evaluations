#!/usr/bin/env python3
"""
Real Dataset Evaluation - Using actual test cases from dataset
Proper evaluation of enhanced vs original solutions using dataset test cases
"""

import os
import sys
import subprocess
import tempfile
from typing import Dict, List, Tuple
from datetime import datetime
from collections import defaultdict

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from humaneval_dataset import HUMANEVAL_PROBLEMS
from apps_tough_problems import APPS_TOUGH_PROBLEMS

class RealDatasetEvaluator:
    """Evaluate solutions using actual test cases from the dataset"""
    
    def __init__(self):
        self.all_problems = HUMANEVAL_PROBLEMS + APPS_TOUGH_PROBLEMS
        self.problem_dict = {p['task_id']: p for p in self.all_problems}
        
    def run_real_evaluation(self):
        """Run evaluation using actual dataset test cases"""
        
        print("🔍 REAL DATASET EVALUATION")
        print("="*70)
        print("Using actual test cases from HUMANEVAL and APPS datasets")
        print("="*70)
        
        results = {
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'original_solutions': {},
            'enhanced_solutions': {},
            'comparison': {}
        }
        
        # Test original solutions
        print("\n📊 STEP 1: Testing Original Solutions with Dataset Test Cases")
        print("-"*60)
        results['original_solutions'] = self.test_original_solutions()
        
        # Test enhanced solutions
        print("\n🚀 STEP 2: Testing Enhanced Solutions with Dataset Test Cases")
        print("-"*60)
        results['enhanced_solutions'] = self.test_enhanced_solutions()
        
        # Compare results
        print("\n⚖️ STEP 3: Comparing Results")
        print("-"*60)
        results['comparison'] = self.compare_results(
            results['original_solutions'], 
            results['enhanced_solutions']
        )
        
        # Generate report
        report_file = self.generate_real_evaluation_report(results)
        
        return results, report_file
    
    def test_original_solutions(self) -> Dict:
        """Test original solutions using dataset test cases"""
        
        original_results = {}
        
        # Test original Gemini solutions
        original_dirs = ['gemini_chain_of_thought', 'gemini_step_chain_of_thought']
        
        for strategy in original_dirs:
            print(f"  📋 Testing {strategy}")
            strategy_results = self.test_strategy_solutions(f"../generated/{strategy}", strategy)
            original_results[strategy] = strategy_results
        
        return original_results
    
    def test_enhanced_solutions(self) -> Dict:
        """Test enhanced solutions using dataset test cases"""
        
        enhanced_results = {}
        
        # Test enhanced Gemini solutions
        enhanced_dirs = ['enhanced_gemini_chain_of_thought', 'enhanced_gemini_step_chain_of_thought']
        
        for strategy in enhanced_dirs:
            print(f"  🚀 Testing {strategy}")
            strategy_results = self.test_strategy_solutions(f"../generated/{strategy}", strategy)
            enhanced_results[strategy] = strategy_results
        
        return enhanced_results
    
    def test_strategy_solutions(self, strategy_dir: str, strategy_name: str) -> Dict:
        """Test all solutions in a strategy directory using dataset test cases"""
        
        strategy_results = {}
        
        if not os.path.exists(strategy_dir):
            print(f"    ❌ Directory not found: {strategy_dir}")
            return strategy_results
        
        # Group files by problem
        problem_files = defaultdict(list)
        
        for file_name in os.listdir(strategy_dir):
            if file_name.endswith('.py') and not file_name.startswith('__'):
                problem_id = self.extract_problem_id_from_filename(file_name)
                if problem_id and problem_id in self.problem_dict:
                    file_path = os.path.join(strategy_dir, file_name)
                    problem_files[problem_id].append(file_path)
        
        # Test each problem
        for problem_id, file_paths in problem_files.items():
            print(f"    📝 Testing {problem_id} ({len(file_paths)} solutions)")
            
            problem = self.problem_dict[problem_id]
            problem_results = []
            
            for file_path in file_paths:
                result = self.test_single_solution_with_dataset(file_path, problem)
                problem_results.append(result)
                
                status = "✅ PASS" if result['passed'] else "❌ FAIL"
                file_name = os.path.basename(file_path)
                print(f"      {file_name}: {status}")
            
            # Calculate Pass@K metrics
            pass_at_1 = (problem_results[0]['passed'] if problem_results else False)
            pass_at_3 = any(r['passed'] for r in problem_results[:3])
            
            strategy_results[problem_id] = {
                'solutions': problem_results,
                'pass_at_1': pass_at_1,
                'pass_at_3': pass_at_3,
                'total_solutions': len(problem_results)
            }
        
        return strategy_results
    
    def test_single_solution_with_dataset(self, file_path: str, problem: Dict) -> Dict:
        """Test a single solution using the actual dataset test case"""
        
        try:
            # Read solution code
            with open(file_path, 'r', encoding='utf-8') as f:
                solution_code = f.read()
            
            # Extract function name from problem
            function_name = self.extract_function_name(problem)
            if not function_name:
                return {
                    'file_path': file_path,
                    'passed': False,
                    'error': 'Could not extract function name',
                    'test_output': ''
                }
            
            # Create test code using dataset test case
            test_code = self.create_test_code(solution_code, problem, function_name)
            
            # Run test
            result = self.execute_test_code(test_code)
            
            return {
                'file_path': file_path,
                'passed': result['passed'],
                'test_output': result['output'],
                'error': result.get('error', ''),
                'function_name': function_name
            }
            
        except Exception as e:
            return {
                'file_path': file_path,
                'passed': False,
                'error': str(e),
                'test_output': ''
            }
    
    def create_test_code(self, solution_code: str, problem: Dict, function_name: str) -> str:
        """Create test code using the actual dataset test case"""
        
        # Clean solution code (remove headers)
        clean_solution = self.clean_solution_code(solution_code)
        
        # Get the actual test from dataset
        dataset_test = problem['test']
        
        # Create complete test code
        test_code = f"""
# Solution code
{clean_solution}

# Dataset test case
{dataset_test}
"""
        
        return test_code
    
    def clean_solution_code(self, solution_code: str) -> str:
        """Clean solution code by removing headers and comments"""
        
        lines = solution_code.split('\n')
        clean_lines = []
        
        for line in lines:
            # Skip header comments
            if line.startswith('#') and ('Enhanced' in line or 'Dataset:' in line or 'Problem:' in line or 'Difficulty:' in line):
                continue
            clean_lines.append(line)
        
        return '\n'.join(clean_lines)
    
    def execute_test_code(self, test_code: str) -> Dict:
        """Execute test code and return results"""
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(test_code)
                temp_file = f.name
            
            # Run the test
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Check if test passed (no assertion errors)
            passed = result.returncode == 0 and 'AssertionError' not in result.stderr
            
            return {
                'passed': passed,
                'output': result.stdout,
                'error': result.stderr,
                'return_code': result.returncode
            }
            
        except subprocess.TimeoutExpired:
            return {
                'passed': False,
                'output': '',
                'error': 'Test timed out',
                'return_code': -1
            }
        except Exception as e:
            return {
                'passed': False,
                'output': '',
                'error': str(e),
                'return_code': -1
            }
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def extract_problem_id_from_filename(self, filename: str) -> str:
        """Extract problem ID from filename"""
        
        if filename.startswith('humaneval_'):
            # humaneval_1_p1_attempt_1.py -> Easy/1
            parts = filename.split('_')
            if len(parts) >= 2:
                task_num = parts[1]
                return f"Easy/{task_num}"
        elif filename.startswith('apps_'):
            # apps_0_p1_attempt_1.py -> APPS/0
            parts = filename.split('_')
            if len(parts) >= 2:
                task_num = parts[1]
                return f"APPS/{task_num}"
        
        return None
    
    def extract_function_name(self, problem: Dict) -> str:
        """Extract function name from problem prompt"""
        
        import re
        prompt = problem.get('prompt', '')
        
        # Look for function definition
        match = re.search(r'def\s+(\w+)\s*\(', prompt)
        if match:
            return match.group(1)
        
        return None
    
    def compare_results(self, original: Dict, enhanced: Dict) -> Dict:
        """Compare original vs enhanced results"""
        
        comparison = {}
        
        # Compare strategies
        for orig_strategy, orig_results in original.items():
            # Find corresponding enhanced strategy
            enhanced_strategy = f"enhanced_{orig_strategy}"
            if enhanced_strategy in enhanced:
                enh_results = enhanced[enhanced_strategy]
                
                strategy_comparison = {}
                
                # Compare each problem
                for problem_id in orig_results:
                    if problem_id in enh_results:
                        orig_pass_1 = orig_results[problem_id]['pass_at_1']
                        orig_pass_3 = orig_results[problem_id]['pass_at_3']
                        enh_pass_1 = enh_results[problem_id]['pass_at_1']
                        enh_pass_3 = enh_results[problem_id]['pass_at_3']
                        
                        strategy_comparison[problem_id] = {
                            'original_pass_at_1': orig_pass_1,
                            'original_pass_at_3': orig_pass_3,
                            'enhanced_pass_at_1': enh_pass_1,
                            'enhanced_pass_at_3': enh_pass_3,
                            'pass_at_1_improvement': enh_pass_1 - orig_pass_1,
                            'pass_at_3_improvement': enh_pass_3 - orig_pass_3,
                            'improved': enh_pass_1 > orig_pass_1 or enh_pass_3 > orig_pass_3
                        }
                
                comparison[f"{orig_strategy}_vs_{enhanced_strategy}"] = strategy_comparison
        
        return comparison
    
    def generate_real_evaluation_report(self, results: Dict) -> str:
        """Generate comprehensive evaluation report using real dataset results"""
        
        timestamp = results['timestamp']
        report_file = f"REAL_DATASET_EVALUATION_{timestamp}.md"
        
        report_content = f"""# 🔍 REAL DATASET EVALUATION REPORT

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Evaluation Method:** Actual test cases from HUMANEVAL and APPS datasets
**Test Framework:** Dataset-provided test cases with assertion-based validation

## 📋 EXECUTIVE SUMMARY

This report provides evaluation results using the **actual test cases** from the HUMANEVAL and APPS datasets, ensuring objective and standardized assessment of code generation performance.

## 🧪 EVALUATION METHODOLOGY

### **Test Framework:**
1. **Dataset Test Cases:** Using original test cases from HUMANEVAL_PROBLEMS and APPS_TOUGH_PROBLEMS
2. **Assertion-Based Validation:** Tests pass only if all assertions succeed
3. **Timeout Protection:** 30-second timeout per test to prevent infinite loops
4. **Error Handling:** Proper exception catching and error reporting

### **Solutions Tested:**
- **Original Gemini:** `gemini_chain_of_thought`, `gemini_step_chain_of_thought`
- **Enhanced Gemini:** `enhanced_gemini_chain_of_thought`, `enhanced_gemini_step_chain_of_thought`

## 📊 DETAILED RESULTS

### **Original Solutions Performance:**

"""
        
        # Add original results
        for strategy, strategy_results in results['original_solutions'].items():
            report_content += f"\n#### **{strategy.upper()}**\n"
            
            if strategy_results:
                for problem_id, problem_result in strategy_results.items():
                    pass_1 = "✅" if problem_result['pass_at_1'] else "❌"
                    pass_3 = "✅" if problem_result['pass_at_3'] else "❌"
                    report_content += f"- **{problem_id}:** Pass@1: {pass_1} | Pass@3: {pass_3} | Solutions: {problem_result['total_solutions']}\n"
            else:
                report_content += "- No solutions found or tested\n"
        
        report_content += f"\n### **Enhanced Solutions Performance:**\n"
        
        # Add enhanced results
        for strategy, strategy_results in results['enhanced_solutions'].items():
            report_content += f"\n#### **{strategy.upper()}**\n"
            
            if strategy_results:
                for problem_id, problem_result in strategy_results.items():
                    pass_1 = "✅" if problem_result['pass_at_1'] else "❌"
                    pass_3 = "✅" if problem_result['pass_at_3'] else "❌"
                    report_content += f"- **{problem_id}:** Pass@1: {pass_1} | Pass@3: {pass_3} | Solutions: {problem_result['total_solutions']}\n"
            else:
                report_content += "- No solutions found or tested\n"
        
        report_content += f"\n## ⚖️ COMPARISON ANALYSIS\n"
        
        # Add comparison results
        if results['comparison']:
            for comparison_name, comparison_data in results['comparison'].items():
                report_content += f"\n### **{comparison_name.upper()}**\n\n"
                report_content += "| Problem | Original Pass@1 | Enhanced Pass@1 | Pass@1 Improvement | Original Pass@3 | Enhanced Pass@3 | Pass@3 Improvement |\n"
                report_content += "|---------|-----------------|-----------------|-------------------|-----------------|-----------------|-------------------|\n"
                
                for problem_id, comp in comparison_data.items():
                    orig_1 = "✅" if comp['original_pass_at_1'] else "❌"
                    enh_1 = "✅" if comp['enhanced_pass_at_1'] else "❌"
                    orig_3 = "✅" if comp['original_pass_at_3'] else "❌"
                    enh_3 = "✅" if comp['enhanced_pass_at_3'] else "❌"
                    
                    imp_1 = "📈" if comp['pass_at_1_improvement'] > 0 else "➡️" if comp['pass_at_1_improvement'] == 0 else "📉"
                    imp_3 = "📈" if comp['pass_at_3_improvement'] > 0 else "➡️" if comp['pass_at_3_improvement'] == 0 else "📉"
                    
                    report_content += f"| {problem_id} | {orig_1} | {enh_1} | {imp_1} | {orig_3} | {enh_3} | {imp_3} |\n"
        else:
            report_content += "No comparison data available (missing original or enhanced solutions)\n"
        
        report_content += f"""

## 🎯 KEY FINDINGS

### **Evaluation Validity:**
- ✅ **Dataset Test Cases:** Using official HUMANEVAL and APPS test cases
- ✅ **Assertion-Based:** Tests pass only if all assertions succeed
- ✅ **Standardized:** Same test framework for all solutions
- ✅ **Objective:** No subjective evaluation, only pass/fail results

### **Test Coverage:**
- **HUMANEVAL Problems:** Easy-level algorithmic problems
- **APPS Problems:** Hard-level competitive programming problems
- **Test Types:** Unit tests with multiple assertions per problem

## ✅ CONCLUSION

This evaluation uses the **actual test cases from the datasets** to provide objective, standardized assessment of code generation performance. The results are based on real test execution with assertion-based validation, ensuring reliable and reproducible evaluation metrics.

---

**Report Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Evaluation Framework:** Dataset test cases with assertion validation
**Validation Method:** Actual code execution with pass/fail determination
"""
        
        # Write report
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"📊 Real evaluation report generated: {report_file}")
        return report_file

if __name__ == "__main__":
    evaluator = RealDatasetEvaluator()
    results, report_file = evaluator.run_real_evaluation()
    
    print(f"\n✅ Real dataset evaluation completed!")
    print(f"📊 Report: {report_file}")
    print(f"🎯 Method: Actual dataset test cases with assertion validation")