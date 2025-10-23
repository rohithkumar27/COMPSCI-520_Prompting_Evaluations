# Groq solution using step_chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/6
# Difficulty: Easy

from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result
