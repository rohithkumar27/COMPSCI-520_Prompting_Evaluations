#!/usr/bin/env python3
"""
Count individual assertion pass/fail for each problem.
Shows X/Y assertions passed per problem.
"""

import subprocess
import sys
import re
from pathlib import Path
import ast


def count_assertions_in_file(test_file_path):
    """Count total assertions in a test file."""
    try:
        with open(test_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count assert statements
        assert_count = len(re.findall(r'^\s*assert\s+', content, re.MULTILINE))
        return assert_count
    except Exception as e:
        return 0


def run_pytest_with_verbose(model_name, attempt_num=1):
    """Run pytest with very verbose output to see individual assertion results."""
    
    cmd = [
        sys.executable, "-m", "pytest",
        f"generated/{model_name}/",
        "-k", f"attempt_{attempt_num}",
        "-vv",
        "--tb=line",
        "--no-header",
        "-x"  # Stop on first failure to see which assertion failed
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return str(e)


def analyze_problem_assertions(model_name, attempt_num=1):
    """Analyze each problem and count passed/total assertions."""
    
    model_dir = Path("generated") / model_name
    test_files = sorted(model_dir.glob(f"test_*_attempt_{attempt_num}.py"))
    
    results = []
    
    for test_file in test_files:
        # Extract problem info from filename
        filename = test_file.name
        
        # Count total assertions
        total_assertions = count_assertions_in_file(test_file)
        
        if total_assertions == 0:
            continue
        
        # Run pytest for this specific file
        cmd = [
            sys.executable, "-m", "pytest",
            str(test_file),
            "-v",
            "--tb=short"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            output = result.stdout + result.stderr
            
            # Check if test passed
            if "PASSED" in output and result.returncode == 0:
                passed_assertions = total_assertions
                status = "PASSED"
            else:
                # Try to determine which assertion failed
                # If it failed, we need to count how many passed before failure
                passed_assertions = 0
                
                # Parse the output to see if we can determine assertion count
                # For now, if it failed, assume 0 passed (conservative)
                # We could enhance this by running assertions individually
                status = "FAILED"
            
            results.append({
                'file': filename,
                'total_assertions': total_assertions,
                'passed_assertions': passed_assertions if status == "PASSED" else 0,
                'status': status,
                'output': output
            })
            
        except Exception as e:
            results.append({
                'file': filename,
                'total_assertions': total_assertions,
                'passed_assertions': 0,
                'status': "ERROR",
                'error': str(e)
            })
    
    return results


def generate_assertion_report(model_name, attempt_num=1):
    """Generate detailed assertion count report."""
    
    print(f"\n{'='*70}")
    print(f"📊 ASSERTION-LEVEL ANALYSIS: {model_name}")
    print(f"{'='*70}\n")
    
    results = analyze_problem_assertions(model_name, attempt_num)
    
    if not results:
        print("⚠️  No test files found")
        return
    
    total_assertions = 0
    total_passed = 0
    
    print(f"{'Problem':<40} {'Assertions':<15} {'Status':<10}")
    print(f"{'-'*70}")
    
    for result in results:
        filename = result['file']
        passed = result['passed_assertions']
        total = result['total_assertions']
        status = result['status']
        
        total_assertions += total
        total_passed += passed
        
        status_icon = "✅" if status == "PASSED" else "❌"
        
        print(f"{filename:<40} {passed}/{total:<13} {status_icon} {status}")
    
    print(f"{'-'*70}")
    print(f"{'TOTAL':<40} {total_passed}/{total_assertions:<13} {total_passed/total_assertions*100:.1f}%")
    print()
    
    return results


def generate_markdown_report(model_name, results, attempt_num=1):
    """Generate markdown report with assertion counts."""
    
    report_dir = Path("reports") / "assertion_analysis"
    report_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = report_dir / f"{model_name}_attempt{attempt_num}_assertions.md"
    
    total_assertions = sum(r['total_assertions'] for r in results)
    total_passed = sum(r['passed_assertions'] for r in results)
    
    content = f"""# Assertion-Level Analysis: {model_name}

**Attempt:** {attempt_num}  
**Total Assertions:** {total_assertions}  
**Passed Assertions:** {total_passed}  
**Pass Rate:** {total_passed/total_assertions*100:.1f}%

## 📊 Detailed Results

| Problem | Assertions Passed | Total Assertions | Pass Rate | Status |
|---------|-------------------|------------------|-----------|--------|
"""
    
    for result in results:
        filename = result['file']
        passed = result['passed_assertions']
        total = result['total_assertions']
        status = result['status']
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        status_icon = "✅" if status == "PASSED" else "❌"
        
        content += f"| `{filename}` | {passed} | {total} | {pass_rate:.1f}% | {status_icon} {status} |\n"
    
    content += f"""
## 📈 Summary

- **Total Test Files:** {len(results)}
- **Total Assertions:** {total_assertions}
- **Passed Assertions:** {total_passed}
- **Failed Assertions:** {total_assertions - total_passed}
- **Overall Pass Rate:** {total_passed/total_assertions*100:.1f}%

---
*Generated by assertion-level analyzer*
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Report saved: {report_file}")


def main():
    """Main function."""
    
    if len(sys.argv) < 2:
        print("Usage: python count_assertion_results.py <model_name> [attempt_num]")
        print("\nAvailable models:")
        print("  - groq_chain_of_thought")
        print("  - groq_step_chain_of_thought")
        print("  - gemini_chain_of_thought")
        print("  - gemini_step_chain_of_thought")
        sys.exit(1)
    
    model_name = sys.argv[1]
    attempt_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    
    results = generate_assertion_report(model_name, attempt_num)
    
    if results:
        generate_markdown_report(model_name, results, attempt_num)


if __name__ == "__main__":
    main()
