# Gemini solution using chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/2
# Difficulty: Easy

from typing import List  # Include any needed imports

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)
