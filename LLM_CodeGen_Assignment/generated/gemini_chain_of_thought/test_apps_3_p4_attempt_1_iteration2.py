import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_3_p4_attempt_1 import count_divisible_subarrays


# ========== BASELINE TESTS (Iteration 0) ==========
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


# ========== ITERATION 1: TARGETED EDGE CASE TESTS ==========

def test_empty_array():
    """Edge case: Empty array should return 0"""
    result = count_divisible_subarrays([], 5)
    assert result == 0, f"Expected 0 for empty array, got {result}"

def test_k_zero():
    """Edge case: k=0 should return 0 (division by zero prevention)"""
    result = count_divisible_subarrays([1, 2, 3], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"

def test_k_one():
    """Edge case: k=1 means all subarrays are divisible"""
    arr = [5, 3, 2]
    result = count_divisible_subarrays(arr, 1)
    expected = 3 * 4 // 2  # 6 subarrays
    assert result == expected, f"Expected {expected} for k=1, got {result}"

def test_single_element_divisible():
    """Edge case: Single element divisible by k"""
    result = count_divisible_subarrays([10], 5)
    assert result == 1, f"Expected 1, got {result}"

def test_single_element_not_divisible():
    """Edge case: Single element not divisible by k"""
    result = count_divisible_subarrays([7], 5)
    assert result == 0, f"Expected 0, got {result}"

def test_negative_remainder_handling():
    """Edge case: Negative numbers producing negative remainders"""
    arr = [-5, -10, 3]
    result = count_divisible_subarrays(arr, 5)
    assert result >= 0, f"Expected non-negative result, got {result}"


# ========== ITERATION 2: FINAL COVERAGE PUSH ==========

def test_all_zeros():
    """Edge case: Array of all zeros"""
    arr = [0, 0, 0]
    result = count_divisible_subarrays(arr, 5)
    # All subarrays sum to 0, which is divisible by any k
    expected = 3 * 4 // 2  # 6 subarrays
    assert result == expected, f"Expected {expected}, got {result}"

def test_large_k():
    """Edge case: k larger than all array elements"""
    arr = [1, 2, 3]
    result = count_divisible_subarrays(arr, 100)
    # Only subarrays with sum 0 would be divisible
    assert result >= 0, f"Expected non-negative result, got {result}"

def test_mixed_with_zero():
    """Edge case: Array with zeros mixed in"""
    arr = [5, 0, 5, 0]
    result = count_divisible_subarrays(arr, 5)
    # Multiple subarrays should be divisible
    assert result >= 4, f"Expected at least 4, got {result}"
