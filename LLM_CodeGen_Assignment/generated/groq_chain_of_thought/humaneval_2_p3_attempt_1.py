# Groq solution using chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/2
# Difficulty: Easy

from typing import Union

def truncate_number(number: Union[int, float]) -> float:
    return number - int(number)
