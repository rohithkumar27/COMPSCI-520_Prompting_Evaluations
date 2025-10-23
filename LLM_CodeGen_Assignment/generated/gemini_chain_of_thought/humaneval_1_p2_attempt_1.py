# Gemini solution using chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/1
# Difficulty: Easy

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group and return the list of those. Separate groups are balanced (each open brace is properly closed)
    and not nested within each other
    Input: '( ) (( )) (( )( ))'
    Output: ['()', '(())', '(()())']
    """
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
        elif char == ' ':
            continue

        if balance == 0 and current_group:
            result.append(current_group)
            current_group = ""
    return result
