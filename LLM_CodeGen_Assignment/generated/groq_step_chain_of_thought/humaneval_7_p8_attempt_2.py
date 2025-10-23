# Groq solution using step_chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/7
# Difficulty: Easy

from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_result = 0
    product_result = 1
    
    for number in numbers:
        sum_result += number
        product_result *= number
    
    return sum_result, product_result
