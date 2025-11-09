#!/usr/bin/env python3
"""
Enhanced test case analysis showing individual test case pass/fail per problem.
"""

import subprocess
import sys
import re
from pathlib import Path
from datetime import datetime
import ast


class DetailedTestCaseAnalyzer:
    """Analyze test cases in detail for each problem."""
    
    def __init__(self, model_name):
        self.model_name = model_name
        self.model_dir = Path("generated") / model_name
        self.report_dir = Path("reports") / "detailed_test_cases"
        self.report_dir.mkdir(parents=True, exist_ok=True)
    
    def analyze_test_file(self, test_file_path):
        """Analyze a single test file to extract test cases."""
        try:
            with open(test_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the file to extract test function and assertions
            tree = ast.parse(content)
            
            test_cases = []
            test_function_name = None
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                    test_function_name = node.name
                    
                    # Extract assertions
                    for stmt in ast.walk(node):
                        if isinstance(stmt, ast.Assert):
                            # Get the assertion line
                            line_no = stmt.lineno
                            test_cases.append({
                                'line': line_no,
                                'type': 'assert'
                            })
            
            # Also count by simple regex for more accuracy
            assert_lines = []
            for i, line in enumerate(content.split('\n'), 1):
                if re.match(r'^\s*assert\s+', line):
                    assert_lines.append({
                        'line': i,
                        'content': line.strip()
                    })
            
            return {
                'test_function': test_function_name,
                'total_assertions': len(assert_lines),
                'assertions': assert_lines
            }
            
        except Exception as e:
            return {
                'error': str(e),
                'total_assertions': 0
            }
    
    def run_pytest_verbose(self, attempt_num=1):
        """Run pytest with maximum verbosity to capture individual test case results."""
        
        cmd = [
            sys.executable, "-m", "pytest",
            f"generated/{self.model_name}/",
            "-k", f"attempt_{attempt_num}",
            "--cov", f"generated/{self.model_name}",
            "--cov-branch",
            "--cov-report=term",
            f"--cov-report=html:coverage_reports/{self.model_name}_attempt{attempt_num}/html",
            "-vv",  # Very verbose
            "--tb=short",
            "--no-header"
        ]
        
        print(f"Running: {' '.join(cmd)}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            return {
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
        except Exception as e:
            return {
                'error': str(e)
            }
    
    def parse_pytest_output(self, output):
        """Parse pytest output to extract detailed results."""
        
        lines = output.split('\n')
        
        problems = []
        current_problem = None
        in_coverage_section = False
        coverage_data = {}
        
        for line in lines:
            # Match test execution lines
            if '::test_' in line and ('PASSED' in line or 'FAILED' in line):
                # Try multiple patterns for different naming conventions
                
                # Pattern 1: test_humaneval_X_pY_attempt_Z.py
                match = re.search(r'test_humaneval_(\d+)_p(\d+)_attempt_(\d+)\.py::(\w+)\s+(PASSED|FAILED)', line)
                if match:
                    humaneval_id = match.group(1)
                    problem_id = match.group(2)
                    attempt = match.group(3)
                    test_func = match.group(4)
                    status = match.group(5)
                    
                    current_problem = {
                        'humaneval_id': humaneval_id,
                        'problem_id': problem_id,
                        'attempt': attempt,
                        'test_function': test_func,
                        'status': status,
                        'file': f"test_humaneval_{humaneval_id}_p{problem_id}_attempt_{attempt}.py"
                    }
                    problems.append(current_problem)
                    continue
                
                # Pattern 2: test_apps_X_pY_attempt_Z.py
                match = re.search(r'test_apps_(\d+)_p(\d+)_attempt_(\d+)\.py::(\w+)\s+(PASSED|FAILED)', line)
                if match:
                    apps_id = match.group(1)
                    problem_id = match.group(2)
                    attempt = match.group(3)
                    test_func = match.group(4)
                    status = match.group(5)
                    
                    current_problem = {
                        'humaneval_id': f"APPS_{apps_id}",
                        'problem_id': problem_id,
                        'attempt': attempt,
                        'test_function': test_func,
                        'status': status,
                        'file': f"test_apps_{apps_id}_p{problem_id}_attempt_{attempt}.py"
                    }
                    problems.append(current_problem)
                    continue
            
            # Match assertion errors for failed tests
            elif 'AssertionError:' in line and current_problem and current_problem['status'] == 'FAILED':
                if 'failure_reason' not in current_problem:
                    current_problem['failure_reason'] = line.strip()
            
            # Parse coverage section
            elif 'Name' in line and 'Stmts' in line and 'Branch' in line:
                in_coverage_section = True
            elif in_coverage_section and 'humaneval_' in line:
                # Parse coverage line
                parts = line.split()
                if len(parts) >= 6:
                    file_name = parts[0].split('\\')[-1]
                    try:
                        coverage_data[file_name] = {
                            'statements': int(parts[1]),
                            'missed': int(parts[2]),
                            'branches': int(parts[3]),
                            'branch_partial': int(parts[4]),
                            'coverage': parts[5]
                        }
                    except:
                        pass
            elif in_coverage_section and 'TOTAL' in line:
                parts = line.split()
                if len(parts) >= 6:
                    try:
                        coverage_data['TOTAL'] = {
                            'statements': int(parts[1]),
                            'missed': int(parts[2]),
                            'branches': int(parts[3]),
                            'branch_partial': int(parts[4]),
                            'coverage': parts[5]
                        }
                    except:
                        pass
                in_coverage_section = False
        
        return problems, coverage_data
    
    def generate_detailed_report(self, attempt_num=1):
        """Generate comprehensive report with test case details."""
        
        print(f"\n{'='*70}")
        print(f"🔍 DETAILED TEST CASE ANALYSIS: {self.model_name}")
        print(f"{'='*70}\n")
        
        # Run pytest
        pytest_result = self.run_pytest_verbose(attempt_num)
        
        if 'error' in pytest_result:
            print(f"❌ Error running pytest: {pytest_result['error']}")
            return
        
        # Parse results
        problems, coverage_data = self.parse_pytest_output(pytest_result['stdout'])
        
        # Analyze each test file
        detailed_problems = []
        for problem in problems:
            test_file_path = self.model_dir / problem['file']
            test_analysis = self.analyze_test_file(test_file_path)
            
            problem['test_cases'] = test_analysis.get('total_assertions', 0)
            problem['assertions'] = test_analysis.get('assertions', [])
            
            # Get coverage for this file
            solution_file = problem['file'].replace('test_', '')
            if solution_file in coverage_data:
                problem['coverage'] = coverage_data[solution_file]
            
            detailed_problems.append(problem)
        
        # Generate markdown report
        self._generate_markdown_report(detailed_problems, coverage_data, attempt_num)
        
        # Print summary to console
        self._print_console_summary(detailed_problems, coverage_data)
        
        return detailed_problems, coverage_data
    
    def _print_console_summary(self, problems, coverage_data):
        """Print summary to console."""
        
        print(f"\n{'='*70}")
        print(f"📊 TEST RESULTS SUMMARY")
        print(f"{'='*70}\n")
        
        total_problems = len(problems)
        
        if total_problems == 0:
            print("⚠️  No problems found - check test file naming or pytest output")
            return
        
        passed_problems = len([p for p in problems if p['status'] == 'PASSED'])
        failed_problems = total_problems - passed_problems
        
        print(f"Total Problems: {total_problems}")
        print(f"✅ Passed: {passed_problems} ({passed_problems/total_problems*100:.1f}%)")
        print(f"❌ Failed: {failed_problems} ({failed_problems/total_problems*100:.1f}%)")
        
        print(f"\n{'='*70}")
        print(f"📝 DETAILED PROBLEM BREAKDOWN")
        print(f"{'='*70}\n")
        
        for problem in problems:
            status_icon = "✅" if problem['status'] == 'PASSED' else "❌"
            print(f"{status_icon} Problem {problem['problem_id']} (HumanEval {problem['humaneval_id']})")
            print(f"   Function: {problem['test_function']}")
            print(f"   Test Cases: {problem['test_cases']}")
            
            if 'coverage' in problem:
                cov = problem['coverage']
                print(f"   Coverage: {cov['coverage']} (Stmts: {cov['statements']}, Branches: {cov['branches']})")
            
            if problem['status'] == 'FAILED' and 'failure_reason' in problem:
                print(f"   ⚠️  Failure: {problem['failure_reason'][:80]}...")
            
            print()
        
        # Coverage summary
        if 'TOTAL' in coverage_data:
            total_cov = coverage_data['TOTAL']
            print(f"{'='*70}")
            print(f"📈 COVERAGE SUMMARY")
            print(f"{'='*70}\n")
            print(f"Total Coverage: {total_cov['coverage']}")
            print(f"Statements: {total_cov['statements']} (Missed: {total_cov['missed']})")
            print(f"Branches: {total_cov['branches']} (Partial: {total_cov['branch_partial']})")
            print()
    
    def _generate_markdown_report(self, problems, coverage_data, attempt_num):
        """Generate detailed markdown report."""
        
        report_file = self.report_dir / f"{self.model_name}_attempt{attempt_num}_detailed.md"
        
        total_problems = len(problems)
        passed_problems = len([p for p in problems if p['status'] == 'PASSED'])
        total_test_cases = sum(p.get('test_cases', 0) for p in problems)
        
        # Handle case where no problems were found
        if total_problems == 0:
            print(f"⚠️  No problems found for {self.model_name} attempt {attempt_num}")
            return
        
        content = f"""# Detailed Test Case Analysis: {self.model_name}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Attempt:** {attempt_num}

## 📊 Executive Summary

- **Total Problems:** {total_problems}
- **Passed:** {passed_problems} ({passed_problems/total_problems*100:.1f}%)
- **Failed:** {total_problems - passed_problems} ({(total_problems - passed_problems)/total_problems*100:.1f}%)
- **Total Test Cases:** {total_test_cases}
- **Avg Test Cases per Problem:** {total_test_cases/total_problems:.1f}

"""
        
        if 'TOTAL' in coverage_data:
            total_cov = coverage_data['TOTAL']
            content += f"""## 📈 Coverage Summary

- **Overall Coverage:** {total_cov['coverage']}
- **Total Statements:** {total_cov['statements']}
- **Missed Statements:** {total_cov['missed']}
- **Total Branches:** {total_cov['branches']}
- **Partial Branches:** {total_cov['branch_partial']}

"""
        
        content += """## 📝 Detailed Problem Results

| Problem | Function | Status | Test Cases | Coverage | Branches |
|---------|----------|--------|------------|----------|----------|
"""
        
        for problem in problems:
            status_icon = "✅" if problem['status'] == 'PASSED' else "❌"
            cov_str = problem.get('coverage', {}).get('coverage', 'N/A')
            branches = problem.get('coverage', {}).get('branches', 'N/A')
            
            content += f"| P{problem['problem_id']} (HE{problem['humaneval_id']}) | `{problem['test_function']}` | {status_icon} {problem['status']} | {problem['test_cases']} | {cov_str} | {branches} |\n"
        
        content += "\n## 🔍 Individual Problem Analysis\n\n"
        
        for problem in problems:
            status_icon = "✅" if problem['status'] == 'PASSED' else "❌"
            
            content += f"### {status_icon} Problem {problem['problem_id']} - {problem['test_function']}\n\n"
            content += f"**File:** `{problem['file']}`  \n"
            content += f"**Status:** {problem['status']}  \n"
            content += f"**Test Cases:** {problem['test_cases']}  \n"
            
            if 'coverage' in problem:
                cov = problem['coverage']
                content += f"**Coverage:** {cov['coverage']}  \n"
                content += f"**Statements:** {cov['statements']} (Missed: {cov['missed']})  \n"
                content += f"**Branches:** {cov['branches']} (Partial: {cov['branch_partial']})  \n"
            
            if problem['status'] == 'FAILED' and 'failure_reason' in problem:
                content += f"\n**Failure Reason:**\n```\n{problem['failure_reason']}\n```\n"
            
            # Show test case details
            if problem.get('assertions'):
                content += f"\n**Test Case Details:**\n"
                for i, assertion in enumerate(problem['assertions'], 1):
                    content += f"{i}. Line {assertion['line']}: `{assertion['content']}`\n"
            
            content += "\n---\n\n"
        
        content += f"""## 🎯 Key Insights

### Strengths
- {passed_problems} out of {total_problems} problems passed all test cases
- Average of {total_test_cases/total_problems:.1f} test cases per problem
"""
        
        if 'TOTAL' in coverage_data:
            content += f"- Overall code coverage: {coverage_data['TOTAL']['coverage']}\n"
        
        failed_problems = [p for p in problems if p['status'] == 'FAILED']
        if failed_problems:
            content += f"\n### Areas for Improvement\n"
            content += f"- {len(failed_problems)} problems need debugging:\n"
            for p in failed_problems:
                content += f"  - Problem {p['problem_id']}: `{p['test_function']}`\n"
        
        content += f"""
## 📁 Coverage Report

**HTML Report:** `coverage_reports/{self.model_name}_attempt{attempt_num}/html/index.html`

Open this file in your browser to see:
- Line-by-line coverage
- Branch coverage details
- Missed lines highlighted

---
*Generated by detailed test case analyzer*
"""
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Detailed report saved: {report_file}")


def main():
    """Main function."""
    
    if len(sys.argv) < 2:
        print("Usage: python detailed_test_case_analysis.py <model_name> [attempt_num]")
        print("\nAvailable models:")
        print("  - groq_chain_of_thought")
        print("  - groq_step_chain_of_thought")
        print("  - gemini_chain_of_thought")
        print("  - gemini_step_chain_of_thought")
        print("  - enhanced_chain_of_thought")
        sys.exit(1)
    
    model_name = sys.argv[1]
    attempt_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    analyzer = DetailedTestCaseAnalyzer(model_name)
    analyzer.generate_detailed_report(attempt_num)


if __name__ == "__main__":
    main()
