#!/usr/bin/env python3
"""
Generate a comprehensive HTML report combining test results and coverage for all models.
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime
import re


class CombinedReportGenerator:
    """Generate comprehensive HTML report for all models."""
    
    def __init__(self):
        self.models = {
            'groq_chain_of_thought': 'GROQ Chain of Thought',
            'groq_step_chain_of_thought': 'GROQ Step Chain of Thought',
            'gemini_chain_of_thought': 'Gemini Chain of Thought',
            'gemini_step_chain_of_thought': 'Gemini Step Chain of Thought'
        }
        self.results = {}
    
    def analyze_model(self, model_dir):
        """Analyze a single model directory."""
        print(f"Analyzing {model_dir}...")
        
        # Run pytest to get test results
        test_results = self._run_tests(model_dir)
        
        # Parse coverage data
        coverage_data = self._get_coverage_data(model_dir)
        
        return {
            'test_results': test_results,
            'coverage_data': coverage_data
        }
    
    def _run_tests(self, model_dir):
        """Run tests and collect results."""
        cmd = [
            sys.executable, "-m", "pytest",
            f"generated/{model_dir}/",
            "-k", "attempt_1",
            "-v", "--tb=no", "--no-cov"
        ]
        
        # Add ignore flags for problematic files
        if 'gemini' in model_dir:
            cmd.extend([
                f"--ignore=generated/{model_dir}/test_apps_0_p1_attempt_1.py",
                f"--ignore=generated/{model_dir}/test_apps_1_p2_attempt_1.py"
            ])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            return self._parse_test_output(result.stdout, model_dir)
        except Exception as e:
            print(f"Error running tests for {model_dir}: {e}")
            return []
    
    def _parse_test_output(self, output, model_dir):
        """Parse pytest output to extract test results."""
        lines = output.split('\n')
        test_results = []
        
        for line in lines:
            if "::test_" in line and ("PASSED" in line or "FAILED" in line):
                # Extract test info
                parts = line.split("::")
                if len(parts) >= 2:
                    test_file = parts[0].split("/")[-1]
                    test_function = parts[1].split()[0]
                    status = "PASSED" if "PASSED" in line else "FAILED"
                    
                    # Extract problem name
                    problem_match = re.search(r'(humaneval|apps)_(\d+)', test_file)
                    problem_name = f"{problem_match.group(1)}_{problem_match.group(2)}" if problem_match else "unknown"
                    
                    # Count assertions
                    test_file_path = Path("generated") / model_dir / test_file
                    assertions = self._count_assertions(test_file_path)
                    
                    # Get coverage for this specific file
                    solution_file = test_file.replace("test_", "")
                    coverage_info = self._get_file_coverage(model_dir, solution_file)
                    
                    test_results.append({
                        'problem': problem_name,
                        'test_file': test_file,
                        'function': test_function,
                        'status': status,
                        'assertions': assertions,
                        'line_coverage': coverage_info.get('line_coverage', 0),
                        'branch_coverage': coverage_info.get('branch_coverage', 0),
                        'statements': coverage_info.get('statements', 0),
                        'missing': coverage_info.get('missing', 0)
                    })
        
        return test_results
    
    def _count_assertions(self, file_path):
        """Count assertions in a test file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return len(re.findall(r'^\s*assert\s+', content, re.MULTILINE))
        except:
            return 0
    
    def _get_coverage_data(self, model_dir):
        """Get coverage data from JSON report."""
        json_path = Path(f"coverage_reports/{model_dir}_attempt1/coverage.json")
        
        if not json_path.exists():
            # Try alternate path
            json_path = Path(f"coverage_reports/{model_dir}/coverage.json")
        
        if json_path.exists():
            try:
                with open(json_path, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {}
    
    def _get_file_coverage(self, model_dir, solution_file):
        """Get coverage info for a specific file."""
        coverage_data = self._get_coverage_data(model_dir)
        
        if not coverage_data or 'files' not in coverage_data:
            return {}
        
        # Find the file in coverage data
        for file_path, file_data in coverage_data.get('files', {}).items():
            if solution_file in file_path and 'attempt_1' in file_path:
                summary = file_data.get('summary', {})
                
                total_statements = summary.get('num_statements', 0)
                covered_lines = summary.get('covered_lines', 0)
                line_coverage = summary.get('percent_covered', 0)
                
                total_branches = summary.get('num_branches', 0)
                covered_branches = summary.get('covered_branches', 0)
                branch_coverage = (covered_branches / total_branches * 100) if total_branches > 0 else 0
                
                return {
                    'line_coverage': line_coverage,
                    'branch_coverage': branch_coverage,
                    'statements': total_statements,
                    'missing': summary.get('missing_lines', 0),
                    'covered_lines': covered_lines
                }
        
        return {}
    
    def generate_html_report(self):
        """Generate comprehensive HTML report."""
        
        # Collect data for all models
        for model_dir, model_name in self.models.items():
            self.results[model_dir] = self.analyze_model(model_dir)
        
        # Generate HTML
        html_content = self._create_html()
        
        # Save report
        output_path = Path("reports/COMBINED_COVERAGE_REPORT.html")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n✅ Combined HTML report generated: {output_path}")
        return output_path
    
    def _create_html(self):
        """Create HTML content."""
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Combined Model Coverage Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .summary-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-left: 5px solid #667eea;
            transition: transform 0.3s;
        }}
        
        .summary-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}
        
        .summary-card h3 {{
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.1em;
        }}
        
        .summary-card .value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
            margin: 10px 0;
        }}
        
        .summary-card .label {{
            color: #666;
            font-size: 0.9em;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .model-section {{
            margin-bottom: 40px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        }}
        
        .model-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            font-size: 1.5em;
            font-weight: bold;
        }}
        
        .model-stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            padding: 20px;
            background: #f8f9fa;
        }}
        
        .stat-box {{
            background: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .stat-box .stat-value {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        
        .stat-box .stat-label {{
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            position: sticky;
            top: 0;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .status-passed {{
            background: #d4edda;
            color: #155724;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
        }}
        
        .status-failed {{
            background: #f8d7da;
            color: #721c24;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
        }}
        
        .coverage-bar {{
            width: 100%;
            height: 20px;
            background: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
            position: relative;
        }}
        
        .coverage-fill {{
            height: 100%;
            background: linear-gradient(90deg, #28a745 0%, #20c997 100%);
            transition: width 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 0.8em;
            font-weight: bold;
        }}
        
        .coverage-low {{ background: linear-gradient(90deg, #dc3545 0%, #e74c3c 100%); }}
        .coverage-medium {{ background: linear-gradient(90deg, #ffc107 0%, #ff9800 100%); }}
        .coverage-high {{ background: linear-gradient(90deg, #28a745 0%, #20c997 100%); }}
        
        .notes {{
            font-size: 0.85em;
            color: #666;
            font-style: italic;
        }}
        
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 2px solid #e0e0e0;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Combined Model Coverage Report</h1>
            <p>Comprehensive Analysis of Test Results and Code Coverage</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        {self._generate_summary_section()}
        
        <div class="content">
            {self._generate_model_sections()}
        </div>
        
        <div class="footer">
            <p>Generated by Pytest Coverage Analysis Pipeline</p>
            <p style="margin-top: 5px; font-size: 0.9em;">Models: GROQ & Gemini | Strategies: Chain of Thought & Step Chain of Thought</p>
        </div>
    </div>
</body>
</html>"""
        
        return html
    
    def _generate_summary_section(self):
        """Generate overall summary section."""
        total_tests = 0
        total_passed = 0
        total_coverage = []
        
        for model_dir, data in self.results.items():
            test_results = data.get('test_results', [])
            total_tests += len(test_results)
            total_passed += len([t for t in test_results if t['status'] == 'PASSED'])
            
            coverages = [t['line_coverage'] for t in test_results if t['line_coverage'] > 0]
            if coverages:
                total_coverage.extend(coverages)
        
        avg_coverage = sum(total_coverage) / len(total_coverage) if total_coverage else 0
        pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        return f"""
        <div class="summary">
            <div class="summary-card">
                <h3>📊 Total Tests</h3>
                <div class="value">{total_tests}</div>
                <div class="label">Test Cases Executed</div>
            </div>
            <div class="summary-card">
                <h3>✅ Tests Passed</h3>
                <div class="value">{total_passed}</div>
                <div class="label">{pass_rate:.1f}% Pass Rate</div>
            </div>
            <div class="summary-card">
                <h3>📈 Average Coverage</h3>
                <div class="value">{avg_coverage:.1f}%</div>
                <div class="label">Line Coverage</div>
            </div>
            <div class="summary-card">
                <h3>🤖 Models Analyzed</h3>
                <div class="value">{len(self.models)}</div>
                <div class="label">GROQ & Gemini</div>
            </div>
        </div>
        """
    
    def _generate_model_sections(self):
        """Generate sections for each model."""
        sections = []
        
        for model_dir, model_name in self.models.items():
            data = self.results.get(model_dir, {})
            test_results = data.get('test_results', [])
            
            if not test_results:
                continue
            
            # Calculate model stats
            total_tests = len(test_results)
            passed_tests = len([t for t in test_results if t['status'] == 'PASSED'])
            pass_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
            
            coverages = [t['line_coverage'] for t in test_results if t['line_coverage'] > 0]
            avg_coverage = sum(coverages) / len(coverages) if coverages else 0
            
            total_assertions = sum(t['assertions'] for t in test_results)
            
            section = f"""
            <div class="model-section">
                <div class="model-header">{model_name}</div>
                
                <div class="model-stats">
                    <div class="stat-box">
                        <div class="stat-value">{passed_tests}/{total_tests}</div>
                        <div class="stat-label">Tests Passed</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">{pass_rate:.1f}%</div>
                        <div class="stat-label">Pass Rate</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">{avg_coverage:.1f}%</div>
                        <div class="stat-label">Avg Coverage</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-value">{total_assertions}</div>
                        <div class="stat-label">Total Assertions</div>
                    </div>
                </div>
                
                <table>
                    <thead>
                        <tr>
                            <th>Problem</th>
                            <th>Status</th>
                            <th>Tests</th>
                            <th>Line Coverage</th>
                            <th>Branch Coverage</th>
                            <th>Statements</th>
                            <th>Notes</th>
                        </tr>
                    </thead>
                    <tbody>
                        {self._generate_table_rows(test_results)}
                    </tbody>
                </table>
            </div>
            """
            
            sections.append(section)
        
        return '\n'.join(sections)
    
    def _generate_table_rows(self, test_results):
        """Generate table rows for test results."""
        rows = []
        
        for test in test_results:
            status_class = 'status-passed' if test['status'] == 'PASSED' else 'status-failed'
            
            line_cov = test['line_coverage']
            branch_cov = test['branch_coverage']
            
            # Determine coverage class
            cov_class = 'coverage-high' if line_cov >= 80 else ('coverage-medium' if line_cov >= 50 else 'coverage-low')
            
            # Generate notes
            notes = []
            if test['status'] == 'FAILED':
                notes.append("Test failed")
            if line_cov == 100:
                notes.append("Perfect coverage")
            elif line_cov == 0:
                notes.append("No coverage")
            if test['missing'] > 0:
                notes.append(f"{test['missing']} lines missed")
            
            notes_text = ", ".join(notes) if notes else "All good"
            
            row = f"""
                <tr>
                    <td><strong>{test['problem']}</strong></td>
                    <td><span class="{status_class}">{test['status']}</span></td>
                    <td>{test['assertions']} assertions</td>
                    <td>
                        <div class="coverage-bar">
                            <div class="coverage-fill {cov_class}" style="width: {line_cov}%">
                                {line_cov:.1f}%
                            </div>
                        </div>
                    </td>
                    <td>
                        <div class="coverage-bar">
                            <div class="coverage-fill {cov_class}" style="width: {branch_cov}%">
                                {branch_cov:.1f}%
                            </div>
                        </div>
                    </td>
                    <td>{test['statements']} total</td>
                    <td class="notes">{notes_text}</td>
                </tr>
            """
            
            rows.append(row)
        
        return '\n'.join(rows)


def main():
    """Main function."""
    print("🚀 Generating Combined HTML Coverage Report...")
    print("=" * 60)
    
    generator = CombinedReportGenerator()
    output_path = generator.generate_html_report()
    
    print(f"\n🎉 Report generated successfully!")
    print(f"📁 Location: {output_path}")
    print(f"\n💡 Open the file in your browser to view the report")


if __name__ == "__main__":
    main()