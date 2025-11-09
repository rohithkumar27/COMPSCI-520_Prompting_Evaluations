from typing import List
# Gemini solution using step_chain_of_thought (Attempt 1/1)
# Dataset: Unknown
# Problem: Easy/0
# Difficulty: Easy

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False

    # Sort the list to bring close elements together
    sorted_numbers = sorted(numbers)

    # Iterate through the sorted list and compare adjacent elements
    for i in range(len(sorted_numbers) - 1):
        if abs(sorted_numbers[i+1] - sorted_numbers[i]) < threshold:
            return True

    # If no close elements are found after checking all adjacent pairs
    return False
