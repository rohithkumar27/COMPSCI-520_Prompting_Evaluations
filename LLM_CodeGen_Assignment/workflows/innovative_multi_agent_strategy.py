#!/usr/bin/env python3
"""
INNOVATION: Multi-Agent Code Generation with Test-Driven Refinement Strategy

This innovative strategy combines:
1. Role-based prompting (Developer + Code Reviewer + Test Engineer)
2. Multi-step Generate → Test → Analyze → Refine cycle
3. External tool integration (unit test feedback loop)
4. Collaborative agent interaction
"""

import os
import sys
import time
import subprocess
import tempfile
from typing import Dict, List, Tuple, Optional
from datetime import datetime

# Add paths
sys.path.append('../datasets')
sys.path.append('.')

from humaneval_dataset import HUMANEVAL_PROBLEMS

class MultiAgentCodeGenerationStrategy:
    """
    Innovative Multi-Agent Strategy with Test-Driven Refinement
    
    Workflow:
    1. Developer Agent: Generates initial code
    2. Test Engineer Agent: Creates comprehensive tests
    3. Code Reviewer Agent: Reviews and suggests improvements
    4. Refinement Loop: Iteratively improve based on test feedback
    5. Final Validation: Ensure all tests pass
    """
    
    def __init__(self, model_client, model_name="Multi-Agent"):
        self.model_client = model_client
        self.model_name = model_name
        self.max_refinement_cycles = 3
        
    def generate_solution(self, problem: Dict) -> Dict:
        """Generate solution using multi-agent approach"""
        
        print(f"🤖 Starting Multi-Agent Code Generation for {problem['task_id']}")
        
        # Extract function name
        function_name = self.extract_function_name(problem)
        
        # Step 1: Developer Agent - Initial Code Generation
        print("  👨‍💻 Developer Agent: Generating initial solution...")
        initial_code = self.developer_agent_generate(problem, function_name)
        
        # Step 2: Test Engineer Agent - Create Comprehensive Tests
        print("  🧪 Test Engineer Agent: Creating comprehensive tests...")
        test_suite = self.test_engineer_agent_generate(problem, function_name, initial_code)
        
        # Step 3: Initial Test Run
        print("  ⚡ Running initial tests...")
        test_results = self.run_tests(initial_code, test_suite, function_name)
        
        # Step 4: Refinement Loop
        current_code = initial_code
        refinement_history = []
        
        for cycle in range(self.max_refinement_cycles):
            if test_results['all_passed']:
                print(f"  ✅ All tests passed in cycle {cycle}!")
                break
                
            print(f"  🔄 Refinement Cycle {cycle + 1}/{self.max_refinement_cycles}")
            
            # Code Reviewer Agent - Analyze failures and suggest improvements
            print("    👨‍🔬 Code Reviewer Agent: Analyzing failures...")
            review_feedback = self.code_reviewer_agent_analyze(
                problem, current_code, test_results, function_name
            )
            
            # Developer Agent - Refine based on feedback
            print("    👨‍💻 Developer Agent: Refining solution...")
            refined_code = self.developer_agent_refine(
                problem, current_code, review_feedback, test_results, function_name
            )
            
            # Test the refined code
            print("    ⚡ Testing refined solution...")
            test_results = self.run_tests(refined_code, test_suite, function_name)
            
            refinement_history.append({
                'cycle': cycle + 1,
                'code': refined_code,
                'test_results': test_results,
                'review_feedback': review_feedback
            })
            
            current_code = refined_code
        
        # Step 5: Final Validation
        final_validation = self.final_validation_agent(
            problem, current_code, test_results, function_name
        )
        
        return {
            'final_code': current_code,
            'initial_code': initial_code,
            'test_suite': test_suite,
            'final_test_results': test_results,
            'refinement_history': refinement_history,
            'final_validation': final_validation,
            'cycles_used': len(refinement_history),
            'success': test_results['all_passed']
        }
    
    def developer_agent_generate(self, problem: Dict, function_name: str) -> str:
        """Developer Agent: Generate initial solution"""
        
        prompt = f"""You are an EXPERT SOFTWARE DEVELOPER. Your task is to implement a high-quality solution.

PROBLEM:
{problem['prompt']}

DEVELOPER INSTRUCTIONS:
- Write clean, efficient, and well-documented code
- Follow best practices and coding standards
- Consider edge cases and error handling
- Use appropriate data structures and algorithms
- Include helpful comments for complex logic

IMPLEMENTATION REQUIREMENTS:
- Function name must be EXACTLY: {function_name}
- Include all necessary imports
- Handle all edge cases mentioned in the problem
- Optimize for both correctness and performance
- Write production-ready code

OUTPUT FORMAT:
```python
# Necessary imports
from typing import List, Optional, Tuple
import collections, math, itertools  # as needed

def {function_name}(parameters):
    \"\"\"
    High-quality implementation with proper documentation.
    
    Args:
        parameters: Description of parameters
        
    Returns:
        Description of return value
        
    Examples:
        >>> {function_name}(example_input)
        expected_output
    \"\"\"
    # Implementation here
    pass
```

Generate a complete, production-ready solution:"""

        try:
            response = self.model_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert software developer focused on writing high-quality, correct code."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return self.extract_code_from_response(response.choices[0].message.content)
        except Exception as e:
            print(f"    ❌ Developer Agent error: {e}")
            return f"def {function_name}(*args):\n    pass"
    
    def test_engineer_agent_generate(self, problem: Dict, function_name: str, code: str) -> str:
        """Test Engineer Agent: Create comprehensive test suite"""
        
        prompt = f"""You are an EXPERT TEST ENGINEER. Create a comprehensive test suite for the given code.

PROBLEM:
{problem['prompt']}

CODE TO TEST:
{code}

TEST ENGINEER INSTRUCTIONS:
- Create thorough unit tests covering all scenarios
- Include edge cases, boundary conditions, and error cases
- Test both positive and negative scenarios
- Ensure tests are independent and deterministic
- Use descriptive test names and assertions

TESTING REQUIREMENTS:
- Test the function: {function_name}
- Cover all examples from the problem description
- Add additional edge cases not covered in examples
- Include performance considerations for large inputs
- Test error handling and invalid inputs

OUTPUT FORMAT:
```python
import unittest
from typing import List, Optional, Tuple

# Test class
class Test{function_name.title()}(unittest.TestCase):
    
    def test_basic_examples(self):
        \"\"\"Test basic examples from problem description\"\"\"
        # Add test cases here
        pass
    
    def test_edge_cases(self):
        \"\"\"Test edge cases and boundary conditions\"\"\"
        # Add edge case tests here
        pass
    
    def test_error_handling(self):
        \"\"\"Test error handling and invalid inputs\"\"\"
        # Add error handling tests here
        pass

if __name__ == '__main__':
    unittest.main()
```

Create comprehensive tests:"""

        try:
            response = self.model_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert test engineer focused on creating comprehensive test suites."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1500
            )
            return self.extract_code_from_response(response.choices[0].message.content)
        except Exception as e:
            print(f"    ❌ Test Engineer Agent error: {e}")
            return f"# Basic test\ndef test_{function_name}():\n    assert {function_name}() is not None"
    
    def code_reviewer_agent_analyze(self, problem: Dict, code: str, test_results: Dict, function_name: str) -> str:
        """Code Reviewer Agent: Analyze failures and suggest improvements"""
        
        failed_tests = [t for t in test_results.get('test_details', []) if not t.get('passed', False)]
        
        prompt = f"""You are an EXPERT CODE REVIEWER. Analyze the failing code and provide specific improvement suggestions.

PROBLEM:
{problem['prompt']}

CURRENT CODE:
{code}

TEST FAILURES:
{chr(10).join([f"- {t.get('error', 'Unknown error')}" for t in failed_tests[:3]])}

PASS RATE: {test_results.get('pass_rate', 0):.1f}%

CODE REVIEWER ANALYSIS:
- Identify the root cause of test failures
- Suggest specific algorithmic improvements
- Point out logical errors or edge case issues
- Recommend better data structures or approaches
- Highlight performance or correctness issues

REVIEW REQUIREMENTS:
- Focus on the function: {function_name}
- Provide actionable, specific suggestions
- Explain WHY the current approach fails
- Suggest concrete fixes with examples
- Consider both correctness and efficiency

OUTPUT FORMAT:
## Code Review Analysis

### Issues Identified:
1. [Specific issue with explanation]
2. [Another issue with root cause]

### Recommended Fixes:
1. [Specific fix with code example]
2. [Another fix with implementation details]

### Algorithm Improvements:
- [Suggest better algorithmic approach]
- [Explain complexity improvements]

Provide detailed analysis and actionable suggestions:"""

        try:
            response = self.model_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert code reviewer focused on identifying issues and suggesting improvements."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"    ❌ Code Reviewer Agent error: {e}")
            return "Review failed - please check the implementation manually."
    
    def developer_agent_refine(self, problem: Dict, current_code: str, review_feedback: str, 
                              test_results: Dict, function_name: str) -> str:
        """Developer Agent: Refine code based on review feedback"""
        
        prompt = f"""You are an EXPERT SOFTWARE DEVELOPER. Refine the code based on the code review feedback.

PROBLEM:
{problem['prompt']}

CURRENT CODE:
{current_code}

CODE REVIEW FEEDBACK:
{review_feedback}

TEST RESULTS:
Pass Rate: {test_results.get('pass_rate', 0):.1f}%
Failed Tests: {len([t for t in test_results.get('test_details', []) if not t.get('passed', False)])}

REFINEMENT INSTRUCTIONS:
- Address ALL issues identified in the code review
- Fix the specific problems causing test failures
- Implement suggested algorithmic improvements
- Maintain code quality and readability
- Ensure all edge cases are handled properly

IMPLEMENTATION REQUIREMENTS:
- Function name must remain: {function_name}
- Keep the same interface and signature
- Fix bugs without breaking existing functionality
- Improve algorithm efficiency if suggested
- Add better error handling if needed

OUTPUT FORMAT:
```python
# Necessary imports (updated if needed)
from typing import List, Optional, Tuple

def {function_name}(parameters):
    \"\"\"
    Refined implementation addressing review feedback.
    \"\"\"
    # Improved implementation here
    pass
```

Provide the refined, improved code:"""

        try:
            response = self.model_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are an expert developer focused on implementing improvements based on code review feedback."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            return self.extract_code_from_response(response.choices[0].message.content)
        except Exception as e:
            print(f"    ❌ Developer Agent refinement error: {e}")
            return current_code  # Return original if refinement fails
    
    def final_validation_agent(self, problem: Dict, final_code: str, test_results: Dict, function_name: str) -> str:
        """Final Validation Agent: Comprehensive quality assessment"""
        
        prompt = f"""You are a SENIOR SOFTWARE ARCHITECT. Provide final validation and quality assessment.

PROBLEM:
{problem['prompt']}

FINAL CODE:
{final_code}

TEST RESULTS:
Pass Rate: {test_results.get('pass_rate', 0):.1f}%
All Tests Passed: {test_results.get('all_passed', False)}

VALIDATION REQUIREMENTS:
- Assess overall code quality and correctness
- Verify algorithmic approach is optimal
- Check for any remaining issues or improvements
- Evaluate performance and scalability
- Provide final quality score and recommendations

OUTPUT FORMAT:
## Final Validation Report

### Quality Assessment:
- Correctness: [Score/10]
- Performance: [Score/10]
- Code Quality: [Score/10]
- Test Coverage: [Score/10]

### Summary:
[Brief summary of final solution quality]

### Recommendations:
[Any final recommendations or notes]

Provide comprehensive final validation:"""

        try:
            response = self.model_client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a senior software architect focused on comprehensive quality assessment."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"    ❌ Final Validation Agent error: {e}")
            return "Validation failed - manual review recommended."
    
    def run_tests(self, code: str, test_suite: str, function_name: str) -> Dict:
        """Run tests and return detailed results"""
        
        # Combine code and tests
        test_code = f"""
{code}

# Dataset test case
{test_suite}

# Run basic validation
try:
    # Test if function exists and is callable
    if callable(globals().get('{function_name}')):
        print("Function {function_name} is callable: True")
    else:
        print("Function {function_name} is callable: False")
except Exception as e:
    print(f"Function validation error: {{e}}")
"""
        
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
                f.write(test_code)
                temp_file = f.name
            
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            # Parse results
            output = result.stdout + result.stderr
            all_passed = result.returncode == 0 and 'Error' not in output and 'Exception' not in output
            
            # Calculate pass rate (simplified)
            if 'callable: True' in output:
                pass_rate = 100.0 if all_passed else 50.0
            else:
                pass_rate = 0.0
            
            return {
                'all_passed': all_passed,
                'pass_rate': pass_rate,
                'output': output,
                'return_code': result.returncode,
                'test_details': [{'passed': all_passed, 'error': output if not all_passed else None}]
            }
            
        except Exception as e:
            return {
                'all_passed': False,
                'pass_rate': 0.0,
                'output': str(e),
                'return_code': -1,
                'test_details': [{'passed': False, 'error': str(e)}]
            }
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def extract_function_name(self, problem: Dict) -> str:
        """Extract function name from problem"""
        import re
        prompt = problem.get('prompt', '')
        match = re.search(r'def\s+(\w+)\s*\(', prompt)
        return match.group(1) if match else 'unknown_function'
    
    def extract_code_from_response(self, response: str) -> str:
        """Extract Python code from model response"""
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

# Integration with existing workflow
class InnovativeMultiAgentStrategy:
    """Integration class for the innovative multi-agent strategy"""
    
    def __init__(self):
        self.name = "Innovative_Multi_Agent_Strategy"
    
    def generate_prompt(self, problem: dict) -> str:
        """Generate prompt for multi-agent strategy (not used directly)"""
        return f"Multi-Agent Strategy for {problem['task_id']}"

if __name__ == "__main__":
    print("🚀 Innovative Multi-Agent Code Generation Strategy")
    print("="*60)
    print("This strategy combines:")
    print("1. Role-based prompting (Developer + Reviewer + Test Engineer)")
    print("2. Multi-step Generate → Test → Analyze → Refine cycle")
    print("3. External tool integration (unit test feedback loop)")
    print("4. Collaborative agent interaction")
    print("\nTo use this strategy, integrate it with your model client.")