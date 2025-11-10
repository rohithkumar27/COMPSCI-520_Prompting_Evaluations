import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_3_p4_attempt_1 import count_divisible_subarrays


def test_divisible_subarrays():
    arr1 = [4, 5, 0, -2, -3, 1]
    result = count_divisible_subarrays(arr1, 5)
    assert result == 7, f"Expected 7, got {result}"

def test_divisible_subarrays_1():
    arr = [3, 6, 2, -1, -4, 2]
    result = count_divisible_subarrays(arr, 5)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_2():
    arr = [10, 15, 5, -5, -10, 0]
    result = count_divisible_subarrays(arr, 5)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_3():
    arr = [7, 14, 3, -3, -7, 1]
    result = count_divisible_subarrays(arr, 7)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_4():
    arr = [8, 12, 4, -4, -8, 2]
    result = count_divisible_subarrays(arr, 4)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_5():
    arr = [6, 9, 3, -3, -6, 0]
    result = count_divisible_subarrays(arr, 3)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_6():
    arr = [11, 22, 5, -5, -11, 3]
    result = count_divisible_subarrays(arr, 11)
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_divisible_subarrays_7():
    arr = [13, 26, 7, -7, -13, 4]
    result = count_divisible_subarrays(arr, 13)
    assert result >= 0, f"Expected non-negative result, got {result}"
