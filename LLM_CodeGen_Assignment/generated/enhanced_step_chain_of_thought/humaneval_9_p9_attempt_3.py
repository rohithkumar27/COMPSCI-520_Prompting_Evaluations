# Enhanced Groq solution using enhanced_step_chain_of_thought (Attempt 3/3)
# Dataset: Enhanced
# Problem: Easy/9
# Difficulty: Enhanced

def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if is_palindrome(string):
        return string
    
    for i in range(len(string)):
        suffix = string[i:]
        if is_palindrome(suffix):
            return string + string[:i][::-1]
    
    return string + string[:-1][::-1]