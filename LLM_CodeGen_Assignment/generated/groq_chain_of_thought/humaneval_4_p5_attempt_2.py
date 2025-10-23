# Groq solution using chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/4
# Difficulty: Easy

from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = statistics.mean(numbers)
    return statistics.mean(abs(x - mean) for x in numbers)
