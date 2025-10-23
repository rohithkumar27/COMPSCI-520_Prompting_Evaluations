#!/usr/bin/env python3
"""
Run Enhanced Groq Workflow - Execute enhanced Groq evaluation
"""

import os
import sys
import time
from datetime import datetime

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from enhanced_prompting_strategies import EnhancedChainOfThoughtStrategy, EnhancedStepChainOfThoughtStrategy
from humaneval_dataset import HUMANEVAL_PROBLEMS

# Import Groq client
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    print("⚠️ Groq not available - install with: pip install groq")

class EnhancedGroqWorkflow:
    """Execute enhanced Groq evaluation workflow"""
    
    def __init__(self):
        self.failing_problems = ['Easy/1', 'Easy/4', 'Easy/9']  # Known failing problems
        self.strategies = {
            'enhanced_chain_of_thought': EnhancedChainOfThoughtStrategy(),
            'enhanced_step_chain_of_thought': EnhancedStepChainOfThoughtStrategy()
        }
        self.setup_groq()
    
    def setup_groq(self):
        """Setup Groq client"""
        if GROQ_AVAILABLE:
            try:
                groq_api_key = os.getenv('GROQ_API_KEY')
                if groq_api_key:
                    self.groq_client = Groq(api_key=groq_api_key)
                    print("✅ Groq client initialized")
                else:
                    print("❌ GROQ_API_KEY not found in environment variables")
                    self.groq_client = None
            except Exception as e:
                print(f"❌ Groq setup failed: {e}")
                self.groq_client = None
        else:
            self.groq_client = None
    
    def run_enhanced_evaluation(self, k_values=[1, 3]):
        """Run enhanced Groq evaluation"""
        
        print("🚀 ENHANCED GROQ WORKFLOW")
        print("="*50)
        
        if not self.groq_client:
            print("❌ Groq client not available. Please set GROQ_API_KEY environment variable.")
            return
        
        results = {
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S"),
            'k_values': k_values,
            'strategies': {}
        }
        
        # Get failing problems
        failing_problems = [p for p in HUMANEVAL_PROBLEMS if p['task_id'] in self.failing_problems]
        
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
                        
                        response = self.groq_client.chat.completions.create(
                            model="llama-3.1-70b-versatile",
                            messages=[
                                {"role": "system", "content": "You are an expert programmer. Generate clean, efficient Python code."},
                                {"role": "user", "content": enhanced_prompt}
                            ],
                            temperature=0.7,
                            max_tokens=1500
                        )
                        
                        solution_code = response.choices[0].message.content
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
        
        print(f"\n✅ Enhanced Groq evaluation completed!")
        print(f"📊 Report: {report_file}")
        
        return results
    
    def save_solution(self, solution_code: str, problem_id: str, strategy: str, attempt: int):
        """Save generated solution to file"""
        
        # Create directory
        output_dir = f"../generated/{strategy}"
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        problem_num = problem_id.split('/')[1]
        filename = f"humaneval_{problem_num}_p{problem_num}_attempt_{attempt}.py"
        filepath = os.path.join(output_dir, filename)
        
        # Add header
        header = f"""# Enhanced Groq solution using {strategy} (Attempt {attempt}/3)
# Dataset: Enhanced
# Problem: {problem_id}
# Difficulty: Enhanced

"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(header + solution_code)
    
    def generate_report(self, results):
        """Generate evaluation report"""
        
        timestamp = results['timestamp']
        report_file = f"ENHANCED_GROQ_EVALUATION_{timestamp}.md"
        
        report_content = f"""# 🚀 ENHANCED GROQ EVALUATION REPORT

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**K Values:** {results['k_values']}

## 📋 EXECUTION SUMMARY

### **Problems Tested:**
- Easy/1: Parentheses Grouping (regex → stack-based algorithm)
- Easy/4: Mean Absolute Deviation (median → mean formula)
- Easy/9: Make Palindrome (missing function → complete implementation)

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
- **Easy/1:** 🚨 CRITICAL: DO NOT use regex for nested parentheses
- **Easy/4:** 🚨 CRITICAL: Mean Absolute Deviation = MEAN, NOT median
- **Easy/9:** 🚨 CRITICAL: Implement BOTH functions (is_palindrome AND make_palindrome)

### **Algorithm Specifications:**
- **Easy/1:** Use stack-based approach with balance counter
- **Easy/4:** Formula: MAD = mean(|x - mean|) for all x in dataset
- **Easy/9:** Find palindromic suffix, prepend reversed prefix

### **Implementation Requirements:**
- Complete function implementations
- Proper imports and dependencies
- Correct return values
- Edge case handling

## 📁 GENERATED FILES

Solutions saved in:
- `../generated/enhanced_chain_of_thought/`
- `../generated/enhanced_step_chain_of_thought/`

## 🚀 NEXT STEPS

1. **Evaluate Solutions:** Test generated solutions against dataset test cases
2. **Calculate Pass@K:** Determine success rates for each problem
3. **Compare with Baseline:** Compare against original Groq performance
4. **Refine Prompts:** Improve based on failure analysis

---

**Report Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Workflow:** Enhanced Groq prompting with problem-specific guidance
"""
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return report_file

if __name__ == "__main__":
    workflow = EnhancedGroqWorkflow()
    workflow.run_enhanced_evaluation()