"""
Two prompting strategies for code generation:
1. Chain of Thought (CoT)
2. Self Debugging
"""

class PromptingStrategy:
    def __init__(self, name: str):
        self.name = name
    
    def generate_prompt(self, problem: dict) -> str:
        raise NotImplementedError

class ChainOfThoughtStrategy(PromptingStrategy):
    """Chain of Thought prompting strategy - optimized for code generation"""
    
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
    """Step Chain of Thought prompting strategy - optimized for code generation"""
    
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

