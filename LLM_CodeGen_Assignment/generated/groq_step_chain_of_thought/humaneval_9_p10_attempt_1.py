# Groq solution using step_chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/9
# Difficulty: Easy

from typing import List

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
