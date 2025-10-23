# Enhanced Groq solution using enhanced_chain_of_thought (Attempt 2/3)
# Dataset: Enhanced
# Problem: Easy/1
# Difficulty: Enhanced

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_group = ""
    balance = 0
    
    for char in paren_string:
        if char == '(':
            balance += 1
            current_group += char
        elif char == ')':
            balance -= 1
            current_group += char
            if balance == 0 and current_group:
                result.append(current_group)
                current_group = ""
        # Skip spaces
    
    return result