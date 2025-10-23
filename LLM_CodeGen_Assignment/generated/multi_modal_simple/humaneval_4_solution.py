# Multi-Modal Solution (Groq + Gemini)
# Problem: Easy/4
# Generated: 2025-10-22 19:45:00

from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a list of numbers around their mean.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Raises:
        ValueError: If the input list is empty, as MAD cannot be calculated.

    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
        >>> mean_absolute_deviation([10.0])
        0.0
        >>> mean_absolute_deviation([5.0, 5.0, 5.0])
        0.0
        >>> mean_absolute_deviation([-1.0, 0.0, 1.0])
        0.6666666666666666
    """
    # 1. Handle edge case: empty list
    if not numbers:
        raise ValueError("Input list cannot be empty. Mean Absolute Deviation requires at least one number.")

    n = len(numbers)

    # 2. Optimization for edge case: single element list
    # If there's only one number, its mean is itself, and the absolute deviation from the mean is 0.
    if n == 1:
        return 0.0

    # 3. Calculate the mean of the input list (first pass)
    # Using statistics.mean for robustness and efficiency (often implemented in C).
    data_mean = statistics.mean(numbers)

    # 4. Calculate the sum of absolute deviations from the mean (second pass)
    # Using a generator expression with sum() avoids creating an intermediate list
    # for 'absolute_deviations'. This significantly improves memory efficiency
    # for very large datasets, as it doesn't store all deviations in memory simultaneously.
    sum_abs_deviations = sum(abs(num - data_mean) for num in numbers)

    # 5. Calculate the Mean Absolute Deviation
    mad = sum_abs_deviations / n

    return mad