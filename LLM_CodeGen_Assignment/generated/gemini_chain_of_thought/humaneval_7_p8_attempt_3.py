from typing import List, Tuple
# Gemini solution using chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: Easy/7
# Difficulty: Easy

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    current_sum = 0
    current_product = 1

    for number in numbers:
        current_sum += number
        current_product *= number

    return (current_sum, current_product)