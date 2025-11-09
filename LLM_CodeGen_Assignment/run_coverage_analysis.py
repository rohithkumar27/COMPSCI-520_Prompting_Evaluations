#!/usr/bin/env python3
"""
Simple script to run coverage analysis for each model using pytest.
"""

import subprocess
import sys
from pathlib import Path


def run_pytest_coverage(directory_name, output_dir="coverage_reports"):
    """Run pytest with coverage for a specific directory."""
    
    # Create output directory
    output_path = Path(output_dir) / directory_name
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Pytest command with coverage
    cmd = [
        sys.executable, "-m", "pytest",
        f"generated/{directory_name}/",
        f"--cov=generated/{directory_name}",
        "--cov-report=term-missing",
        f"--cov-report=html:{output_path}/html",
        f"--cov-report=xml:{output_path}/coverage.xml",
        f"--cov-report=json:{output_path}/coverage.json",
        "--cov-branch",
        "-v",
        "--tb=short"
    ]
    
    print(f"\n🚀 Running coverage analysis for: {directory_name}")
    print(f"Command: {' '.join(cmd)}")
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode == 0:
            print(f"✅ Coverage analysis completed for {directory_name}")
            print(f"📊 HTML Report: {output_path}/html/index.html")
        else:
            print(f"❌ Coverage analysis failed for {directory_name}")
            print(f"Exit code: {result.returncode}")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"💥 Error running coverage for {directory_name}: {e}")
        return False


def main():
    """Run coverage analysis for all model directories."""
    
    # List of model directories to analyze
    model_directories = [
        "groq_chain_of_thought",
        "groq_step_chain_of_thought", 
        "gemini_chain_of_thought",
        "gemini_step_chain_of_thought",
        "enhanced_chain_of_thought",
        "enhanced_step_chain_of_thought",
        "enhanced_gemini_chain_of_thought",
        "enhanced_gemini_step_chain_of_thought",
        "innovative_multi_agent",
        "multi_modal_simple"
    ]
    
    print("🎯 PYTEST COVERAGE ANALYSIS FOR ALL MODELS")
    print("=" * 60)
    
    successful = 0
    failed = 0
    
    for directory in model_directories:
        # Check if directory exists
        dir_path = Path("generated") / directory
        if not dir_path.exists():
            print(f"⚠️  Directory not found: {directory}")
            continue
        
        # Check if directory has test files
        test_files = list(dir_path.glob("test_*.py"))
        if not test_files:
            print(f"⚠️  No test files found in: {directory}")
            continue
        
        # Run coverage analysis
        if run_pytest_coverage(directory):
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 COVERAGE ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Reports saved in: coverage_reports/")
    
    if successful > 0:
        print("\n🎉 Coverage reports generated!")
        print("📖 View HTML reports by opening:")
        for directory in model_directories:
            report_path = Path("coverage_reports") / directory / "html" / "index.html"
            if report_path.exists():
                print(f"   - {report_path}")


if __name__ == "__main__":
    main()