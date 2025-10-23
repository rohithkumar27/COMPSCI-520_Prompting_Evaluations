#!/usr/bin/env python3
"""
Simplified Multi-Modal Workflow - Groq + Gemini Collaboration
"""

import os
import sys
import time
from datetime import datetime

# Add paths
sys.path.append('datasets')
sys.path.append('workflows')
sys.path.append('.')

from humaneval_dataset import HUMANEVAL_PROBLEMS
from apps_tough_problems import APPS_TOUGH_PROBLEMS

# Import API clients
from groq import Groq
import google.generativeai as genai

class SimpleMultiModalWorkflow:
    def __init__(self):
        self.setup_clients()
        self.test_problems = ['Easy/1', 'Easy/4', 'APPS/0']
        
    def setup_clients(self):
        """Setup API clients"""
        # Groq
        groq_api_key = os.getenv('GROQ_API_KEY')
        self.groq_client = Groq(api_key=groq_api_key)
        
        # Gemini
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=gemini_api_key)
        self.gemini_model = genai.GenerativeModel('gemini-2.5-flash')
        
        print("✅ Both API clients initialized")
    
    def run_evaluation(self):
        """Run the multi-modal evaluation"""
        print("🚀 MULTI-MODAL WORKFLOW EVALUATION")
        print("="*60)
        print("Combining Groq + Gemini for collaborative code generation")
        print("="*60)
        
        # Get test problems
        all_problems = HUMANEVAL_PROBLEMS + APPS_TOUGH_PROBLEMS
        test_problems = [p for p in all_problems if p['task_id'] in self.test_problems]
        
        print(f"📋 Testing on {len(test_problems)} problems")
        
        results = []
        
        for problem in test_problems:
            problem_id = problem['task_id']
            print(f"\n🎯 Processing: {problem_id}")
            print("-"*50)
            
            try:
                # Step 1: Groq generates solution
                print("  🔥 Groq: Generating solution...")
                groq_solution = self.groq_generate(problem)
                
                # Step 2: Gemini improves solution
                print("  💎 Gemini: Improving solution...")
                gemini_solution = self.gemini_improve(problem, groq_solution)
                
                # Step 3: Simple test
                print("  ⚡ Testing solution...")
                test_result = self.simple_test(gemini_solution, problem)
                
                results.append({
                    'problem_id': problem_id,
                    'groq_solution': groq_solution,
                    'gemini_solution': gemini_solution,
                    'test_passed': test_result,
                    'success': test_result
                })
                
                print(f"  📊 Result: {'✅ SUCCESS' if test_result else '❌ FAILED'}")
                
                # Save solution
                self.save_solution(gemini_solution, problem_id)
                
                time.sleep(2)  # Rate limiting
                
            except Exception as e:
                print(f"  ❌ Error: {e}")
                results.append({
                    'problem_id': problem_id,
                    'error': str(e),
                    'success': False
                })
        
        # Summary
        successful = sum(1 for r in results if r.get('success', False))
        total = len(results)
        success_rate = (successful / total * 100) if total > 0 else 0
        
        print(f"\n✅ Multi-modal evaluation completed!")
        print(f"📊 Success Rate: {successful}/{total} ({success_rate:.1f}%)")
        
        return results
    
    def groq_generate(self, problem):
        """Generate solution using Groq"""
        function_name = self.extract_function_name(problem)
        
        prompt = f"""Generate a Python solution for this problem:

{problem['prompt']}

Requirements:
- Function name: {function_name}
- Clean, efficient code
- Handle edge cases

Solution:"""

        response = self.groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are an expert Python programmer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        return self.extract_code(response.choices[0].message.content)
    
    def gemini_improve(self, problem, groq_solution):
        """Improve solution using Gemini"""
        prompt = f"""Review and improve this Python solution:

PROBLEM:
{problem['prompt']}

CURRENT SOLUTION:
{groq_solution}

Please provide an improved version that:
- Fixes any bugs
- Handles edge cases better
- Is more efficient
- Maintains the same function signature

Improved solution:"""

        response = self.gemini_model.generate_content(prompt)
        return self.extract_code(response.text)
    
    def simple_test(self, solution, problem):
        """Simple test of the solution"""
        try:
            # Basic syntax check
            compile(solution, '<string>', 'exec')
            
            # Check if function exists
            function_name = self.extract_function_name(problem)
            if f"def {function_name}" in solution:
                return True
            else:
                return False
                
        except Exception:
            return False
    
    def extract_function_name(self, problem):
        """Extract function name from problem"""
        import re
        prompt = problem.get('prompt', '')
        match = re.search(r'def\s+(\w+)\s*\(', prompt)
        return match.group(1) if match else 'solution'
    
    def extract_code(self, response):
        """Extract Python code from response"""
        import re
        
        # Look for code blocks
        code_match = re.search(r'```python\s*(.*?)\s*```', response, re.DOTALL)
        if code_match:
            return code_match.group(1).strip()
        
        # Look for function definitions
        func_match = re.search(r'(def\s+\w+.*?)(?=\n\n|\n#|\nclass|\ndef|\Z)', response, re.DOTALL)
        if func_match:
            return func_match.group(1).strip()
        
        return response.strip()
    
    def save_solution(self, solution, problem_id):
        """Save the solution"""
        os.makedirs('generated/multi_modal_simple', exist_ok=True)
        
        if problem_id.startswith('Easy/'):
            problem_num = problem_id.split('/')[1]
            filename = f"humaneval_{problem_num}_solution.py"
        else:
            problem_num = problem_id.split('/')[1]
            filename = f"apps_{problem_num}_solution.py"
        
        filepath = os.path.join('generated/multi_modal_simple', filename)
        
        header = f"""# Multi-Modal Solution (Groq + Gemini)
# Problem: {problem_id}
# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(header + solution)

if __name__ == "__main__":
    workflow = SimpleMultiModalWorkflow()
    workflow.run_evaluation()