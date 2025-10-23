# Enhanced Groq solution using enhanced_chain_of_thought (Attempt 3/3)
# Dataset: Enhanced
# Problem: Easy/4
# Difficulty: Enhanced

from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = statistics.mean(numbers)
    return statistics.mean([abs(x - mean) for x in numbers])