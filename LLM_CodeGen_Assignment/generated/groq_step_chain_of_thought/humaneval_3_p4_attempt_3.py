# Groq solution using step_chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: Easy/3
# Difficulty: Easy

from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
