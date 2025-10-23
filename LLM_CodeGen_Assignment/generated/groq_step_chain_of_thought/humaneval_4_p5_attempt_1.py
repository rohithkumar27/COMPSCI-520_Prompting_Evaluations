# Groq solution using step_chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/4
# Difficulty: Easy

from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        raise ValueError("Input list cannot be empty")
    mean = statistics.mean(numbers)
    return statistics.median([abs(x - mean) for x in numbers])
