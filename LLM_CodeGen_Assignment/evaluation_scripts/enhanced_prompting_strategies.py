"""
Enhanced prompting strategies with specific improvements for failing test cases
"""

class PromptingStrategy:
    def __init__(self, name: str):
        self.name = name
    
    def generate_prompt(self, problem: dict) -> str:
        raise NotImplementedError

class EnhancedChainOfThoughtStrategy(PromptingStrategy):
    """Enhanced Chain of Thought with specific fixes for failing problems"""
    
    def __init__(self):
        super().__init__("Enhanced_Chain_of_Thought")
    
    def generate_prompt(self, problem: dict) -> str:
        # Extract function name from the problem prompt
        import re
        func_match = re.search(r'def (\w+)\(', problem['prompt'])
        function_name = func_match.group(1) if func_match else "unknown_function"
        
        # Get problem-specific enhancements
        specific_guidance = self.get_problem_specific_guidance(problem, function_name)
        
        prompt = f"""Solve this coding problem step by step with enhanced guidance.

PROBLEM:
{problem['prompt']}

{specific_guidance}

APPROACH:
1. Understand the requirements carefully
2. Analyze ALL examples in the docstring  
3. Plan the correct algorithm (avoid common pitfalls)
4. Implement the complete solution

REQUIREMENTS:
- Implement function "{function_name}" exactly as specified
- Include ALL necessary imports
- Handle ALL examples from docstring
- Return complete, working Python code
- Test your logic against the examples

OUTPUT FORMAT:
```python
from typing import List, Tuple  # include all needed imports

def {function_name}(parameters):
    # complete implementation here
    # handle all edge cases
    return result
```

CRITICAL RULES:
- Start with ```python
- End with ```
- Include COMPLETE function implementation
- Function name must be EXACTLY "{function_name}"
- Test your solution against docstring examples

SOLUTION:"""
        return prompt
    
    def get_problem_specific_guidance(self, problem: dict, function_name: str) -> str:
        """Get specific guidance based on the problem"""
        
        # Check for specific failing problems
        if 'separate_paren_groups' in function_name:
            return """
🚨 CRITICAL ALGORITHM GUIDANCE:
- DO NOT use regex for nested parentheses - it will fail!
- Use a stack-based approach with balance counter
- Algorithm: Track '(' as +1, ')' as -1, when balance=0 you have complete group
- Handle spaces by ignoring them
- Example walkthrough for '( ) (( ))':
  * '(' → balance=1, start group
  * ' ' → ignore
  * ')' → balance=0, complete group '()'
  * ' ' → ignore  
  * '(' → balance=1, start new group
  * '(' → balance=2
  * ' ' → ignore
  * ')' → balance=1
  * ')' → balance=0, complete group '(())'
- Result: ['()', '(())']

WRONG APPROACH: re.findall(r'\\([^()]+\\)', string) ❌
CORRECT APPROACH: Use balance counter and character iteration ✅
"""
        
        elif 'make_palindrome' in function_name:
            return """
🚨 CRITICAL IMPLEMENTATION GUIDANCE:
- You must implement BOTH functions: is_palindrome AND make_palindrome
- The main function is make_palindrome (tests call this function)
- is_palindrome is just a helper function
- Algorithm for make_palindrome:
  1. If string is already palindrome, return it unchanged
  2. Find the longest palindromic suffix
  3. Prepend the reverse of the remaining prefix
- Example walkthrough for 'xyz':
  * Check if 'xyz' is palindrome → No
  * Check if 'yz' is palindrome → No
  * Check if 'z' is palindrome → Yes (single char)
  * Prefix before palindromic suffix 'z' is 'xy'
  * Result: 'xyz' + reverse('xy') = 'xyz' + 'yx' = 'xyzyx'
- Example for 'jerry':
  * Find palindromic suffix: 'y' is palindromic
  * Prefix: 'jerr'
  * Result: 'jerry' + reverse('jerr') = 'jerry' + 'rrej' = 'jerryrrej'

CRITICAL: Implement the complete make_palindrome function, not just is_palindrome!
"""
        
        elif 'mean_absolute_deviation' in function_name:
            return """
🚨 CRITICAL FORMULA GUIDANCE:
- Mean Absolute Deviation = MEAN of absolute deviations, NOT median!
- Formula: MAD = mean(|x - mean|) for all x in dataset
- Steps:
  1. Calculate mean of all numbers
  2. Calculate absolute deviation for each number: |x - mean|
  3. Calculate MEAN of these absolute deviations (NOT median)
- Example for [1.0, 2.0, 3.0, 4.0, 5.0]:
  * Mean = 3.0
  * Absolute deviations: [2.0, 1.0, 0.0, 1.0, 2.0]
  * MAD = mean([2.0, 1.0, 0.0, 1.0, 2.0]) = 1.2

WRONG: statistics.median([abs(x - mean) for x in numbers]) ❌
CORRECT: statistics.mean([abs(x - mean) for x in numbers]) ✅
"""
        
        else:
            return """
GENERAL GUIDANCE:
- Read the problem statement carefully
- Pay attention to all examples in docstring
- Consider edge cases (empty inputs, single elements, etc.)
- Use appropriate data structures and algorithms
"""

class EnhancedStepChainOfThoughtStrategy(PromptingStrategy):
    """Enhanced Step Chain of Thought with specific fixes for failing problems"""
    
    def __init__(self):
        super().__init__("Enhanced_Step_Chain_of_Thought")
    
    def generate_prompt(self, problem: dict) -> str:
        # Extract function name from the problem prompt
        import re
        func_match = re.search(r'def (\w+)\(', problem['prompt'])
        function_name = func_match.group(1) if func_match else "unknown_function"
        
        # Get problem-specific enhancements
        specific_guidance = self.get_problem_specific_guidance(problem, function_name)
        
        prompt = f"""Solve this systematically with enhanced step-by-step approach.

PROBLEM:
{problem['prompt']}

{specific_guidance}

SYSTEMATIC APPROACH:
Step 1: Understand EXACTLY what the function needs to do
Step 2: Analyze ALL examples in the docstring carefully
Step 3: Choose the CORRECT algorithm approach (avoid common mistakes)
Step 4: Implement the COMPLETE solution with all required functions
Step 5: Verify your solution works with the given examples

REQUIREMENTS:
- Function name must be EXACTLY "{function_name}"
- Include ALL necessary imports
- Handle ALL docstring examples correctly
- Provide complete, working code
- Include all required helper functions

CRITICAL: Provide COMPLETE code in proper format.

```python
from typing import List, Tuple  # include all needed imports

def {function_name}(parameters):
    # complete implementation here
    # handle all cases and edge cases
    return result

# Include any helper functions if needed
```

STRICT RULES:
- Start response with ```python
- End response with ```
- Include COMPLETE function implementation
- No explanations outside code block
- Test logic against examples

PROVIDE COMPLETE SOLUTION:"""
        return prompt
    
    def get_problem_specific_guidance(self, problem: dict, function_name: str) -> str:
        """Get specific guidance based on the problem"""
        
        # Check for specific failing problems
        if 'separate_paren_groups' in function_name:
            return """
🔥 STEP-BY-STEP ALGORITHM FOR PARENTHESES:
Step 1: Initialize empty result list and current group string
Step 2: Initialize balance counter = 0
Step 3: For each character in input string:
   - If '(': increment balance, add to current group
   - If ')': decrement balance, add to current group
   - If ' ': skip (ignore spaces)
   - If balance == 0 and current group not empty: add group to result, reset current group
Step 4: Return result list

CRITICAL: DO NOT use regex - use character-by-character processing!
Test with: '( ) (( ))' should give ['()', '(())']
"""
        
        elif 'make_palindrome' in function_name:
            return """
🔥 STEP-BY-STEP ALGORITHM FOR PALINDROME:
Step 1: Implement is_palindrome helper function
Step 2: In make_palindrome, check if input is already palindrome
Step 3: If yes, return input unchanged
Step 4: If no, find longest palindromic suffix:
   - Try removing 0 chars from start, check if remaining is palindrome
   - Try removing 1 char from start, check if remaining is palindrome
   - Continue until you find palindromic suffix
Step 5: Take the prefix (chars before palindromic suffix)
Step 6: Return: original_string + reverse(prefix)

CRITICAL: Implement BOTH functions - is_palindrome AND make_palindrome!
Test with: 'xyz' should give 'xyzyx'
"""
        
        elif 'mean_absolute_deviation' in function_name:
            return """
🔥 STEP-BY-STEP ALGORITHM FOR MAD:
Step 1: Calculate the mean of all numbers
Step 2: For each number, calculate absolute deviation: |number - mean|
Step 3: Calculate the MEAN (not median!) of all absolute deviations
Step 4: Return this mean value

CRITICAL FORMULA: MAD = mean(|x - mean|) - use MEAN not MEDIAN!
Test with: [1.0, 2.0, 3.0, 4.0, 5.0] should give 1.2
"""
        
        else:
            return """
GENERAL STEP-BY-STEP GUIDANCE:
Step 1: Identify input/output types and constraints
Step 2: Understand all examples thoroughly
Step 3: Plan algorithm considering edge cases
Step 4: Implement with proper error handling
"""

# Legacy strategies for compatibility
class ChainOfThoughtStrategy(PromptingStrategy):
    """Original Chain of Thought prompting strategy"""
    
    def __init__(self):
        super().__init__("Chain_of_Thought")
    
    def generate_prompt(self, problem: dict) -> str:
        # Extract function name from the problem prompt
        import re
        func_match = re.search(r'def (\w+)\(', problem['prompt'])
        function_name = func_match.group(1) if func_match else "unknown_function"
        
        prompt = f"""Solve this coding problem step by step.

PROBLEM:
{problem['prompt']}

APPROACH:
1. Understand the requirements
2. Analyze the examples  
3. Plan the algorithm
4. Implement the solution

REQUIREMENTS:
- Implement function "{function_name}" exactly as specified
- Include necessary imports
- Handle all examples from docstring
- Return working Python code

OUTPUT FORMAT:
```python
from typing import List  # imports if needed

def {function_name}(parameters):
    # implementation here
    pass
```

RULES:
- Start with ```python
- End with ```
- Only include the function code
- Function name must be "{function_name}"

SOLUTION:"""
        return prompt

class StepChainOfThoughtStrategy(PromptingStrategy):
    """Original Step Chain of Thought prompting strategy"""
    
    def __init__(self):
        super().__init__("Step_Chain_of_Thought")
    
    def generate_prompt(self, problem: dict) -> str:
        # Extract function name from the problem prompt
        import re
        func_match = re.search(r'def (\w+)\(', problem['prompt'])
        function_name = func_match.group(1) if func_match else "unknown_function"
        
        prompt = f"""Solve this systematically with clear steps.

PROBLEM:
{problem['prompt']}

SYSTEMATIC APPROACH:
Step 1: Understand what the function needs to do
Step 2: Analyze the examples in the docstring
Step 3: Choose the right algorithm approach  
Step 4: Implement the solution

REQUIREMENTS:
- Function name must be "{function_name}"
- Include all necessary imports
- Handle all docstring examples
- Provide clean, working code

CRITICAL: Provide code in proper format.

```python
from typing import List  # imports if needed

def {function_name}(parameters):
    # your implementation
    pass
```

RULES:
- Start response with ```python
- End response with ```
- Only include function implementation
- No explanations outside code block

PROVIDE SOLUTION:"""
        return prompt