# Groq solution using step_chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: Easy/5
# Difficulty: Easy

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result
