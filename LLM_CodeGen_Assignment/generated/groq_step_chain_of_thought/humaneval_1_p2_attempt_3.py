# Groq solution using step_chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: Easy/1
# Difficulty: Easy

from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    # Find all balanced groups of parentheses in the input string
    groups = re.findall(r'\([^()]+\)', paren_string)
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each group
    for group in groups:
        # Initialize an empty stack to keep track of opening parentheses
        stack = []
        
        # Initialize an empty string to build the result
        temp = ''
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it to the stack
            if char == '(':
                stack.append(char)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                if stack:
                    stack.pop()
            # If the stack is empty, it means we've found a balanced group, so add it to the result
            elif not stack:
                temp += char
        
        # If the stack is empty after iterating over the entire group, it means the group is balanced
        if not stack:
            result.append(temp)
    
    # Return the list of balanced groups
    return result
