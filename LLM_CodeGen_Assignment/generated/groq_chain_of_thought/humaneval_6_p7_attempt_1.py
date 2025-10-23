# Groq solution using chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/6
# Difficulty: Easy

from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
