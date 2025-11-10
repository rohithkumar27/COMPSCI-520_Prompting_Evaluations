#!/usr/bin/env python3
"""
LLM-Assisted Test Generation & Coverage Improvement Workflow
Part 2 of Assignment - Iterative test generation until convergence
"""

import subprocess
import sys
import json
from pathlib import Path
import re
from datetime import datetime


class LLMTestGenerationWorkflow:
    """Iterative test generation to improve coverage."""
    
    def __init__(self, problem_file, test_file):
        self.problem_file = Path(problem_file)
        self.test_file = Path(test_file)
        self.iteration = 0
        self.coverage_history = []
        self.convergence_threshold = 3.0  # 3% threshold
        self.report_dir = Path("reports/llm_test_generation")
        self.report_dir.mkdir(parents=True, exist_ok=True)
        
    def get_current_coverage(self):
        """Run coverage and get current metrics."""
        
        cmd = [
            sys.executable, "-m", "pytest",
            str(self.test_file),
            f"--cov={self.problem_file.parent}",
            "--cov-branch",
            "--cov-report=term",
            "--cov-report=json:coverage_temp.json",
            "-v"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            # Parse coverage from JSON
            if Path("coverage_temp.json").exists():
                with open("coverage_temp.json", 'r') as f:
                    cov_data = json.load(f)
                
                # Get coverage for our specific file
                file_key = str(self.problem_file).replace('\\', '/')
                
                # Find the file in coverage data
                for key in cov_data['files'].keys():
                    if self.problem_file.name in key:
                        file_data = cov_data['files'][key]
                        
                        summary = file_data['summary']
                        
                        return {
                            'line_coverage': summary['percent_covered'],
                            'branch_coverage': summary.get('percent_covered_display', 'N/A'),
                            'lines_covered': summary['covered_lines'],
                            'lines_total': summary['num_statements'],
                            'branches_covered': summary.get('covered_branches', 0),
                            'branches_total': summary.get('num_branches', 0),
                            'missing_lines': summary.get('missing_lines', 0),
                            'output': result.stdout
                        }
            
            # Fallback: parse from terminal output
            return self._parse_coverage_from_output(result.stdout)
            
        except Exception as e:
            print(f"Error getting coverage: {e}")
            return None
    
    def _parse_coverage_from_output(self, output):
        """Parse coverage from pytest output."""
        
        lines = output.split('\n')
        
        for line in lines:
            if self.problem_file.name in line:
                # Parse line like: "file.py    10    2    4    1    85%"
                parts = line.split()
                if len(parts) >= 6:
                    try:
                        return {
                            'line_coverage': float(parts[-1].rstrip('%')),
                            'branch_coverage': 'N/A',
                            'lines_total': int(parts[1]),
                            'lines_covered': int(parts[1]) - int(parts[2]),
                            'branches_total': int(parts[3]),
                            'branches_covered': int(parts[3]) - int(parts[4]),
                            'output': output
                        }
                    except:
                        pass
        
        return {
            'line_coverage': 0,
            'branch_coverage': 'N/A',
            'output': output
        }
    
    def check_convergence(self):
        """Check if coverage has converged."""
        
        if len(self.coverage_history) < 3:
            return False
        
        # Get last 3 iterations
        current = self.coverage_history[-1]['branch_coverage']
        two_back = self.coverage_history[-3]['branch_coverage']
        
        # Handle N/A case
        if current == 'N/A' or two_back == 'N/A':
            current = self.coverage_history[-1]['line_coverage']
            two_back = self.coverage_history[-3]['line_coverage']
        
        improvement = abs(float(current) - float(two_back))
        
        print(f"\n📊 Convergence Check:")
        print(f"   Current coverage: {current}%")
        print(f"   Coverage 2 iterations ago: {two_back}%")
        print(f"   Improvement: {improvement:.2f}%")
        print(f"   Threshold: {self.convergence_threshold}%")
        
        return improvement <= self.convergence_threshold
    
    def generate_prompt_for_iteration(self, coverage_data):
        """Generate prompt for LLM to create new tests."""
        
        # Read current source code
        with open(self.problem_file, 'r') as f:
            source_code = f.read()
        
        # Read current tests
        with open(self.test_file, 'r') as f:
            current_tests = f.read()
        
        prompt = f"""
I need you to generate additional unit tests to improve code coverage for the following Python function.

**Current Coverage:**
- Line Coverage: {coverage_data['line_coverage']}%
- Branch Coverage: {coverage_data.get('branch_coverage', 'N/A')}
- Lines Covered: {coverage_data.get('lines_covered', 'N/A')}/{coverage_data.get('lines_total', 'N/A')}
- Branches Covered: {coverage_data.get('branches_covered', 'N/A')}/{coverage_data.get('branches_total', 'N/A')}

**Source Code:**
```python
{source_code}
```

**Existing Tests:**
```python
{current_tests}
```

**Task:**
Generate NEW test cases that:
1. Increase branch coverage by testing untested conditional paths
2. Test edge cases not covered by existing tests
3. Are NOT duplicates of existing tests
4. Focus on improving branch coverage specifically

**Requirements:**
- Generate 3-5 new test functions
- Each test should target a specific uncovered branch or edge case
- Use descriptive test names like `test_edge_case_empty_input()`
- Include assertions to verify behavior
- Do NOT duplicate existing test logic

**Output Format:**
Provide ONLY the new test functions (no explanations, just code):

```python
def test_new_case_1():
    # Your test here
    pass

def test_new_case_2():
    # Your test here
    pass
```
"""
        
        return prompt
    
    def save_iteration_report(self, iteration, coverage_data, prompt_used, new_tests):
        """Save detailed report for this iteration."""
        
        report_file = self.report_dir / f"iteration_{iteration}_report.md"
        
        content = f"""# Test Generation Iteration {iteration}

**Problem:** `{self.problem_file.name}`  
**Test File:** `{self.test_file.name}`  
**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Coverage Results

- **Line Coverage:** {coverage_data['line_coverage']}%
- **Branch Coverage:** {coverage_data.get('branch_coverage', 'N/A')}
- **Lines Covered:** {coverage_data.get('lines_covered', 'N/A')}/{coverage_data.get('lines_total', 'N/A')}
- **Branches Covered:** {coverage_data.get('branches_covered', 'N/A')}/{coverage_data.get('branches_total', 'N/A')}

## 📝 Prompt Used

```
{prompt_used}
```

## 🧪 New Tests Generated

```python
{new_tests}
```

## 📈 Coverage History

| Iteration | Line Coverage | Branch Coverage | Improvement |
|-----------|---------------|-----------------|-------------|
"""
        
        for i, hist in enumerate(self.coverage_history):
            improvement = ""
            if i > 0:
                prev = self.coverage_history[i-1]['line_coverage']
                curr = hist['line_coverage']
                improvement = f"+{curr - prev:.1f}%"
            
            content += f"| {i} | {hist['line_coverage']}% | {hist.get('branch_coverage', 'N/A')} | {improvement} |\n"
        
        content += f"""
---
*Generated by LLM Test Generation Workflow*
"""
        
        with open(report_file, 'w') as f:
            f.write(content)
        
        print(f"✅ Iteration report saved: {report_file}")
    
    def run_workflow(self, max_iterations=10):
        """Run the complete iterative workflow."""
        
        print(f"\n{'='*70}")
        print(f"🚀 LLM TEST GENERATION WORKFLOW")
        print(f"{'='*70}")
        print(f"Problem: {self.problem_file}")
        print(f"Test File: {self.test_file}")
        print(f"Convergence Threshold: {self.convergence_threshold}%")
        print(f"{'='*70}\n")
        
        # Get initial coverage
        print(f"📊 Iteration 0: Getting baseline coverage...")
        initial_coverage = self.get_current_coverage()
        
        if not initial_coverage:
            print("❌ Failed to get initial coverage")
            return
        
        self.coverage_history.append(initial_coverage)
        
        print(f"   Line Coverage: {initial_coverage['line_coverage']}%")
        print(f"   Branch Coverage: {initial_coverage.get('branch_coverage', 'N/A')}")
        
        # Iterative improvement
        for iteration in range(1, max_iterations + 1):
            print(f"\n{'='*70}")
            print(f"🔄 Iteration {iteration}")
            print(f"{'='*70}")
            
            # Check convergence
            if iteration >= 3 and self.check_convergence():
                print(f"\n✅ CONVERGED after {iteration} iterations!")
                print(f"   Coverage improvement < {self.convergence_threshold}% for 3 consecutive iterations")
                break
            
            # Generate prompt
            print(f"\n📝 Generating prompt for LLM...")
            prompt = self.generate_prompt_for_iteration(self.coverage_history[-1])
            
            # Save prompt to file for manual LLM interaction
            prompt_file = self.report_dir / f"iteration_{iteration}_prompt.txt"
            with open(prompt_file, 'w') as f:
                f.write(prompt)
            
            print(f"   Prompt saved: {prompt_file}")
            print(f"\n⚠️  MANUAL STEP REQUIRED:")
            print(f"   1. Copy the prompt from: {prompt_file}")
            print(f"   2. Send it to your LLM (ChatGPT, Claude, etc.)")
            print(f"   3. Save the generated tests to: {self.report_dir}/iteration_{iteration}_new_tests.py")
            print(f"   4. Press Enter when ready to continue...")
            
            input()
            
            # Load new tests
            new_tests_file = self.report_dir / f"iteration_{iteration}_new_tests.py"
            if not new_tests_file.exists():
                print(f"❌ New tests file not found: {new_tests_file}")
                print(f"   Skipping iteration {iteration}")
                continue
            
            with open(new_tests_file, 'r') as f:
                new_tests = f.read()
            
            # Append new tests to test file
            with open(self.test_file, 'a') as f:
                f.write(f"\n\n# ===== Iteration {iteration} - Generated Tests =====\n")
                f.write(new_tests)
            
            print(f"✅ New tests appended to {self.test_file}")
            
            # Run coverage again
            print(f"\n📊 Running coverage with new tests...")
            new_coverage = self.get_current_coverage()
            
            if not new_coverage:
                print(f"❌ Failed to get coverage for iteration {iteration}")
                continue
            
            self.coverage_history.append(new_coverage)
            
            # Show improvement
            improvement = new_coverage['line_coverage'] - self.coverage_history[-2]['line_coverage']
            print(f"   Line Coverage: {new_coverage['line_coverage']}% ({improvement:+.1f}%)")
            print(f"   Branch Coverage: {new_coverage.get('branch_coverage', 'N/A')}")
            
            # Save iteration report
            self.save_iteration_report(iteration, new_coverage, prompt, new_tests)
        
        # Generate final summary
        self.generate_final_summary()
    
    def generate_final_summary(self):
        """Generate final summary report."""
        
        summary_file = self.report_dir / "FINAL_SUMMARY.md"
        
        initial = self.coverage_history[0]
        final = self.coverage_history[-1]
        
        content = f"""# LLM Test Generation - Final Summary

**Problem:** `{self.problem_file.name}`  
**Test File:** `{self.test_file.name}`  
**Total Iterations:** {len(self.coverage_history) - 1}  
**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Coverage Improvement

### Initial Coverage (Iteration 0)
- **Line Coverage:** {initial['line_coverage']}%
- **Branch Coverage:** {initial.get('branch_coverage', 'N/A')}

### Final Coverage (Iteration {len(self.coverage_history) - 1})
- **Line Coverage:** {final['line_coverage']}%
- **Branch Coverage:** {final.get('branch_coverage', 'N/A')}

### Total Improvement
- **Line Coverage:** +{final['line_coverage'] - initial['line_coverage']:.1f}%
- **Branch Coverage:** {final.get('branch_coverage', 'N/A')}

## 📈 Coverage History

| Iteration | Line Coverage | Branch Coverage | Improvement from Previous |
|-----------|---------------|-----------------|---------------------------|
"""
        
        for i, hist in enumerate(self.coverage_history):
            improvement = ""
            if i > 0:
                prev = self.coverage_history[i-1]['line_coverage']
                curr = hist['line_coverage']
                improvement = f"+{curr - prev:.1f}%"
            else:
                improvement = "Baseline"
            
            content += f"| {i} | {hist['line_coverage']}% | {hist.get('branch_coverage', 'N/A')} | {improvement} |\n"
        
        content += f"""
## 🎯 Convergence Analysis

**Convergence Threshold:** {self.convergence_threshold}%  
**Converged:** {'Yes' if len(self.coverage_history) >= 3 and self.check_convergence() else 'No'}

## 📁 Generated Files

"""
        
        for i in range(1, len(self.coverage_history)):
            content += f"- `iteration_{i}_prompt.txt` - Prompt used for iteration {i}\n"
            content += f"- `iteration_{i}_new_tests.py` - Tests generated in iteration {i}\n"
            content += f"- `iteration_{i}_report.md` - Detailed report for iteration {i}\n"
        
        content += f"""
## 🔍 Key Findings

1. **Initial Coverage:** {initial['line_coverage']}%
2. **Final Coverage:** {final['line_coverage']}%
3. **Total Improvement:** {final['line_coverage'] - initial['line_coverage']:.1f}%
4. **Iterations Required:** {len(self.coverage_history) - 1}

---
*Generated by LLM Test Generation Workflow*
"""
        
        with open(summary_file, 'w') as f:
            f.write(content)
        
        print(f"\n✅ Final summary saved: {summary_file}")


def main():
    """Main function."""
    
    if len(sys.argv) < 3:
        print("Usage: python llm_test_generation_workflow.py <problem_file> <test_file>")
        print("\nExample:")
        print("  python llm_test_generation_workflow.py \\")
        print("    generated/groq_chain_of_thought/humaneval_0_p1_attempt_1.py \\")
        print("    generated/groq_chain_of_thought/test_humaneval_0_p1_attempt_1.py")
        sys.exit(1)
    
    problem_file = sys.argv[1]
    test_file = sys.argv[2]
    
    workflow = LLMTestGenerationWorkflow(problem_file, test_file)
    workflow.run_workflow()


if __name__ == "__main__":
    main()
