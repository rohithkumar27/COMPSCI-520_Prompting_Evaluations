# Groq solution using step_chain_of_thought (Attempt 2/3)
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
        # Initialize an empty stack to check if the group is balanced
        stack = []
        
        # Initialize an empty string to build the group
        new_group = ''
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an open parenthesis, push it to the stack
            if char == '(':
                stack.append(char)
                new_group += char
            # If the character is a close parenthesis, pop the stack
            elif char == ')':
                if stack:
                    stack.pop()
                    new_group += char
                else:
                    # If the stack is empty, it means the group is not balanced, so break the loop
                    break
            # If the character is not a parenthesis, add it to the new group
            else:
                new_group += char
        
        # If the stack is empty after iterating over the group, it means the group is balanced
        if not stack:
            result.append(new_group)
    
    # Return the list of balanced groups
    return result
