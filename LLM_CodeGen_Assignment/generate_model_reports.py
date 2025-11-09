#!/usr/bin/env python3
"""
Generate comprehensive test and coverage reports for all models.
"""

import subprocess
import sys
import re
from pathlib import Path
import json
from datetime import datetime


class ModelReportGenerator:
    """Generate detailed reports for each model."""
    
    def __init__(self):
        self.models = [
            "groq_chain_of_thought",
            "groq_step_chain_of_thought", 
            "gemini_chain_of_thought",
            "gemini_step_chain_of_thought"
        ]
        self.reports_dir = Path("reports/model_analysis")
        self.reports_dir.mkdir(parents=True, exist_ok=True)
    
    def run_model_analysis(self, model_name):
        """Run complete analysis for a single model."""
        print(f"\n🚀 Analyzing {model_name}...")
        
        # Run pytest with coverage
        coverage_result = self._run_coverage_analysis(model_name)
        
        # Run detailed test analysis
        test_result = self._run_test_analysis(model_name)
        
        # Generate report
        report_data = {
            'model_name': model_name,
            'timestamp': datetime.now().isoformat(),
            'coverage_analysis': coverage_result,
            'test_analysis': test_result
        }
        
        # Save JSON report
        json_file = self.reports_dir / f"{model_name}_analysis.json"
        with open(json_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Generate markdown report
        self._generate_markdown_report(model_name, report_data)
        
        return report_data
    
    def _run_coverage_analysis(self, model_name):
        """Run coverage analysis for a model."""
        cmd = [
            sys.executable, "-m", "pytest",
            f"generated/{model_name}/",
            "-k", "attempt_1",
            f"--cov=generated/{model_name}",
            "--cov-report=term-missing",
            f"--cov-report=html:coverage_reports/{model_name}_attempt1/html",
            f"--cov-report=json:coverage_reports/{model_name}_attempt1/coverage.json",
            "-v", "--tb=short"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            
            # Parse coverage information
            coverage_info = self._parse_coverage_output(result.stdout)
            
            return {
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'coverage_summary': coverage_info,
                'html_report': f"coverage_reports/{model_name}_attempt1/html/index.html"
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _run_test_analysis(self, model_name):
        """Run detailed test analysis for a model."""
        cmd = [
            sys.executable, "-m", "pytest",
            f"generated/{model_name}/",
            "-k", "attempt_1",
            "-v", "--tb=short", "--no-cov"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            # Parse test results
            test_results = self._parse_test_results(result.stdout, model_name)
            
            return {
                'success': result.returncode == 0,
                'test_results': test_results,
                'stdout': result.stdout,
                'stderr': result.stderr
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _parse_coverage_output(self, output):
        """Parse coverage information from pytest output."""
        lines = output.split('\n')
        
        # Look for coverage summary
        coverage_data = {}
        in_coverage_section = False
        
        for line in lines:
            if "coverage:" in line.lower() and "platform" in line:
                in_coverage_section = True
                continue
            
            if in_coverage_section and "TOTAL" in line:
                # Parse total coverage line
                parts = line.split()
                if len(parts) >= 4:
                    try:
                        coverage_data['total_statements'] = int(parts[1])
                        coverage_data['missed_statements'] = int(parts[2])
                        coverage_data['coverage_percentage'] = float(parts[3].rstrip('%'))
                    except:
                        pass
                break
        
        return coverage_data
    
    def _parse_test_results(self, output, model_name):
        """Parse test results from pytest output."""
        lines = output.split('\n')
        
        test_files = []
        current_test = None
        
        # Parse test execution lines
        for line in lines:
            if "::test_" in line and ("PASSED" in line or "FAILED" in line):
                parts = line.split("::")
                if len(parts) >= 2:
                    test_file = parts[0].split("/")[-1]
                    test_function = parts[1].split()[0]
                    status = "PASSED" if "PASSED" in line else "FAILED"
                    
                    # Count assertions in test file
                    test_file_path = Path("generated") / model_name / test_file
                    assertion_count = self._count_assertions(test_file_path)
                    
                    test_files.append({
                        'file': test_file,
                        'function': test_function,
                        'status': status,
                        'assertions': assertion_count
                    })
        
        # Calculate summary
        total_files = len(test_files)
        passed_files = len([t for t in test_files if t['status'] == 'PASSED'])
        total_assertions = sum(t['assertions'] for t in test_files)
        
        return {
            'test_files': test_files,
            'summary': {
                'total_files': total_files,
                'passed_files': passed_files,
                'failed_files': total_files - passed_files,
                'pass_rate': (passed_files / total_files * 100) if total_files > 0 else 0,
                'total_assertions': total_assertions,
                'avg_assertions_per_file': total_assertions / total_files if total_files > 0 else 0
            }
        }
    
    def _count_assertions(self, file_path):
        """Count assertions in a test file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return len(re.findall(r'^\s*assert\s+', content, re.MULTILINE))
        except:
            return 0
    
    def _generate_markdown_report(self, model_name, report_data):
        """Generate markdown report for a model."""
        
        # Extract data
        test_analysis = report_data.get('test_analysis', {})
        coverage_analysis = report_data.get('coverage_analysis', {})
        
        test_results = test_analysis.get('test_results', {})
        test_summary = test_results.get('summary', {})
        coverage_summary = coverage_analysis.get('coverage_summary', {})
        
        # Generate report content
        report_content = f"""# {model_name.replace('_', ' ').title()} - Test Analysis Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Executive Summary

### Test Results
- **Total Test Files:** {test_summary.get('total_files', 0)}
- **Passed Files:** {test_summary.get('passed_files', 0)} ({test_summary.get('pass_rate', 0):.1f}%)
- **Failed Files:** {test_summary.get('failed_files', 0)}
- **Total Test Cases:** {test_summary.get('total_assertions', 0)}
- **Avg Test Cases per File:** {test_summary.get('avg_assertions_per_file', 0):.1f}

### Coverage Results
- **Total Statements:** {coverage_summary.get('total_statements', 'N/A')}
- **Coverage Percentage:** {coverage_summary.get('coverage_percentage', 'N/A')}%
- **Missed Statements:** {coverage_summary.get('missed_statements', 'N/A')}

## 📝 Detailed Test Results

| Test File | Function | Status | Test Cases |
|-----------|----------|--------|------------|
"""
        
        # Add test file details
        for test_file in test_results.get('test_files', []):
            status_icon = "✅" if test_file['status'] == 'PASSED' else "❌"
            report_content += f"| `{test_file['file']}` | `{test_file['function']}` | {status_icon} {test_file['status']} | {test_file['assertions']} |\n"
        
        report_content += f"""
## 🎯 Performance Analysis

### Strengths
"""
        
        # Add strengths based on results
        passed_files = [t for t in test_results.get('test_files', []) if t['status'] == 'PASSED']
        if passed_files:
            report_content += f"- Successfully implemented {len(passed_files)} out of {test_summary.get('total_files', 0)} functions\n"
            report_content += f"- High code coverage: {coverage_summary.get('coverage_percentage', 'N/A')}% of code executed\n"
        
        report_content += """
### Areas for Improvement
"""
        
        # Add areas for improvement
        failed_files = [t for t in test_results.get('test_files', []) if t['status'] == 'FAILED']
        if failed_files:
            report_content += f"- {len(failed_files)} functions need debugging:\n"
            for failed_file in failed_files:
                report_content += f"  - `{failed_file['function']}` in `{failed_file['file']}`\n"
        
        report_content += f"""
## 📈 Coverage Details

**HTML Coverage Report:** `{coverage_analysis.get('html_report', 'N/A')}`

Open the HTML report in your browser for detailed line-by-line coverage analysis.

## 🔧 How to Reproduce

```bash
# Run tests with coverage
pytest generated/{model_name}/ -k "attempt_1" --cov=generated/{model_name} --cov-report=html -v

# Run detailed analysis
python detailed_test_analysis.py --directory {model_name}
```

## 📊 Raw Data

### Test Analysis Success: {test_analysis.get('success', False)}
### Coverage Analysis Success: {coverage_analysis.get('success', False)}

---
*Report generated by automated testing pipeline*
"""
        
        # Save markdown report
        md_file = self.reports_dir / f"{model_name}_report.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"✅ Generated report: {md_file}")
    
    def generate_all_reports(self):
        """Generate reports for all models."""
        print("🚀 GENERATING COMPREHENSIVE MODEL REPORTS")
        print("=" * 60)
        
        all_results = {}
        
        for model in self.models:
            try:
                result = self.run_model_analysis(model)
                all_results[model] = result
                print(f"✅ Completed: {model}")
            except Exception as e:
                print(f"❌ Failed: {model} - {e}")
                all_results[model] = {'error': str(e)}
        
        # Generate summary report
        self._generate_summary_report(all_results)
        
        print(f"\n🎉 All reports generated in: {self.reports_dir}")
        return all_results
    
    def _generate_summary_report(self, all_results):
        """Generate a summary report comparing all models."""
        
        summary_content = f"""# Model Comparison Summary Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Model Performance Comparison

| Model | Test Files | Pass Rate | Total Test Cases | Coverage |
|-------|------------|-----------|------------------|----------|
"""
        
        for model_name, result in all_results.items():
            if 'error' in result:
                summary_content += f"| {model_name} | ERROR | - | - | - |\n"
                continue
            
            test_summary = result.get('test_analysis', {}).get('test_results', {}).get('summary', {})
            coverage_summary = result.get('coverage_analysis', {}).get('coverage_summary', {})
            
            pass_rate = test_summary.get('pass_rate', 0)
            total_files = test_summary.get('total_files', 0)
            total_assertions = test_summary.get('total_assertions', 0)
            coverage_pct = coverage_summary.get('coverage_percentage', 0)
            
            summary_content += f"| {model_name} | {total_files} | {pass_rate:.1f}% | {total_assertions} | {coverage_pct}% |\n"
        
        summary_content += f"""
## 🏆 Best Performing Models

### By Test Pass Rate
"""
        
        # Sort by pass rate
        sorted_models = []
        for model_name, result in all_results.items():
            if 'error' not in result:
                test_summary = result.get('test_analysis', {}).get('test_results', {}).get('summary', {})
                pass_rate = test_summary.get('pass_rate', 0)
                sorted_models.append((model_name, pass_rate))
        
        sorted_models.sort(key=lambda x: x[1], reverse=True)
        
        for i, (model_name, pass_rate) in enumerate(sorted_models[:3], 1):
            summary_content += f"{i}. **{model_name}**: {pass_rate:.1f}% pass rate\n"
        
        summary_content += """
## 📁 Individual Reports

"""
        
        for model_name in self.models:
            summary_content += f"- [{model_name}_report.md](./{model_name}_report.md)\n"
        
        summary_content += """
---
*Generated by automated model analysis pipeline*
"""
        
        # Save summary report
        summary_file = self.reports_dir / "MODEL_COMPARISON_SUMMARY.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"✅ Generated summary: {summary_file}")


def main():
    """Main function to generate all reports."""
    generator = ModelReportGenerator()
    results = generator.generate_all_reports()
    
    print(f"\n📊 REPORT GENERATION COMPLETE!")
    print(f"📁 Reports saved in: reports/model_analysis/")
    print(f"📄 Files generated:")
    
    reports_dir = Path("reports/model_analysis")
    for file in reports_dir.glob("*.md"):
        print(f"   - {file.name}")


if __name__ == "__main__":
    main()