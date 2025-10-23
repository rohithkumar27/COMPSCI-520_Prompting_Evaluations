#!/usr/bin/env python3
"""
Run Enhanced Gemini Workflow - Execute enhanced Gemini evaluation
"""

import os
import sys
import time
from datetime import datetime

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from enhanced_gemini_prompting_strategies import EnhancedGeminiChainOfThoughtStrategy, EnhancedGeminiStepChainOfThoughtStrategy
from apps_tough_problems import APPS_TOUGH_PROBLEMS

# Import Gemini client
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️ Gemini not available - install with: pip install google-generativeai")

class EnhancedGeminiWorkflow:
    """Execute enhanced Gemini evaluation workflow"""
    
    def __init__(self):
        self.failing_problems = ['APPS/0', 'APPS/1']  # Known failing problems
        self.strategies = {
            'enhanced_gemini_chain_of_thought': EnhancedGeminiChainOfThoughtStrategy(),
            'enhanced_gemini_step_chain_of_thought': EnhancedGeminiStepChainOfThoughtStrategy()
        }
        self.setup_gemini()
    
    def setup_gemini(self):
        """Setup Gemini client"""
        if GEMINI_AVAILABLE:
            try:
                gemini_api_key = os.getenv('GEMINI_API_KEY')
                if gemini_api_key:
                    genai.configure(api_key=gemini_api_key)
                    self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')
                    print("✅ Gemini client initialized")
                else:
                    print("❌ GEMINI_API_KEY not found in environment variables")
                    self.gemini_model = None
            except Exception as e:
                print(f"❌ Gemini setup failed: {e}")
                self.gemini_model = None
        else:
            self.gemini_model = None
    
    def run_enhanced_evaluation(self, k_values=[1, 3]):
        """Run enhanced Gemini evaluation"""
        
        print("🚀 ENHANCED GEMINI WORKFLOW")
        print("="*50)
        
        if not self.gemini_model:
            print("❌ Gemini client not available. Please set GEMINI_API_KEY environment variable.")
            return
        
        results = {
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'k_values': k_values,
            'strategies': {}
        }
        
        # Get failing problems
        failing_problems = [p for p in APPS_TOUGH_PROBLEMS if p['task_id'] in self.failing_problems]
        
        print(f"📋 Testing {len(failing_problems)} failing problems with enhanced prompts")
        
        # Test each strategy
        for strategy_name, strategy in self.strategies.items():
            print(f"\n🎯 Testing {strategy_name}")
            print("-"*40)
            
            strategy_results = {}
            
            for problem in failing_problems:
                problem_id = problem['task_id']
                print(f"  📝 Generating solutions for {problem_id}")
                
                # Generate enhanced prompt
                enhanced_prompt = strategy.generate_prompt(problem)
                
                # Generate k solutions
                solutions = []
                for attempt in range(max(k_values)):
                    try:
                        print(f"    🎯 Attempt {attempt + 1}/{max(k_values)}")
                        
                        response = self.gemini_model.generate_content(enhanced_prompt)
                        solution_code = response.text
                        solutions.append(solution_code)
                        
                        # Save solution
                        self.save_solution(solution_code, problem_id, strategy_name, attempt + 1)
                        
                        time.sleep(1)  # Rate limiting
                        
                    except Exception as e:
                        print(f"      ❌ Error: {e}")
                        solutions.append(None)
                
                strategy_results[problem_id] = {
                    'solutions': solutions,
                    'enhanced_prompt_length': len(enhanced_prompt)
                }
            
            results['strategies'][strategy_name] = strategy_results
        
        # Generate report
        report_file = self.generate_report(results)
        
        print(f"\n✅ Enhanced Gemini evaluation completed!")
        print(f"📊 Report: {report_file}")
        
        return results
    
    def save_solution(self, solution_code: str, problem_id: str, strategy: str, attempt: int):
        """Save generated solution to file"""
        
        # Create directory
        output_dir = f"../generated/{strategy}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        problem_num = problem_id.split('/')[1]
        filename = f"apps_{problem_num}_p{problem_num}_attempt_{attempt}.py"
        filepath = os.path.join(output_dir, filename)
        
        # Add header
        header = f"""# Enhanced Gemini solution using {strategy} (Attempt {attempt}/3)
# Dataset: Enhanced
# Problem: {problem_id}
# Difficulty: Enhanced

"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(header + solution_code)
    
    def generate_report(self, results):
        """Generate evaluation report"""
        
        timestamp = results['timestamp']
        report_file = f"ENHANCED_GEMINI_EVALUATION_{timestamp}.md"
        
        report_content = f"""# 🚀 ENHANCED GEMINI EVALUATION REPORT

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**K Values:** {results['k_values']}

## 📋 EXECUTION SUMMARY

### **Problems Tested:**
- APPS/0: Bounded Knapsack Problem (0/1 knapsack → bounded knapsack DP)
- APPS/1: Shortest Path with Obstacles (missing imports → complete BFS with state)

### **Strategies Executed:**
"""
        
        for strategy_name, strategy_results in results['strategies'].items():
            report_content += f"\n#### **{strategy_name.upper()}**\n"
            
            for problem_id, result in strategy_results.items():
                successful_solutions = sum(1 for s in result['solutions'] if s is not None)
                total_solutions = len(result['solutions'])
                report_content += f"- **{problem_id}:** {successful_solutions}/{total_solutions} solutions generated\n"
        
        report_content += f"""

## 🎯 ENHANCED PROMPT FEATURES

### **Problem-Specific Guidance:**
- **APPS/0:** 🚨 CRITICAL: This is a BOUNDED KNAPSACK problem (limited items per type)
- **APPS/1:** 🚨 CRITICAL: BFS with STATE tracking (row, col, obstacles_removed)

### **Algorithm Specifications:**
- **APPS/0:** Use dynamic programming with 2D state: dp[item_type][capacity]
- **APPS/1:** State: (row, col, obstacles_removed) with 3D visited array

### **Implementation Requirements:**
- **APPS/0:** MUST return dp[W] at the end, not leave incomplete
- **APPS/1:** CRITICAL IMPORTS NEEDED: from collections import deque

### **Step-by-Step Guidance:**
- **APPS/0:** 7-step detailed DP algorithm with reverse capacity iteration
- **APPS/1:** 7-step BFS implementation with obstacle removal logic

## 📁 GENERATED FILES

Solutions saved in:
- `../generated/enhanced_gemini_chain_of_thought/`
- `../generated/enhanced_gemini_step_chain_of_thought/`

## 🚀 NEXT STEPS

1. **Evaluate Solutions:** Test generated solutions against dataset test cases
2. **Calculate Pass@K:** Determine success rates for each problem
3. **Compare with Baseline:** Compare against original Gemini performance
4. **Refine Prompts:** Improve based on failure analysis

---

**Report Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Workflow:** Enhanced Gemini prompting with problem-specific guidance
"""
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return report_file

if __name__ == "__main__":
    workflow = EnhancedGeminiWorkflow()
    workflow.run_enhanced_evaluation()