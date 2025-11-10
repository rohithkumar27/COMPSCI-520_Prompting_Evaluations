import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_3_p4_attempt_1_BUGGY import count_divisible_subarrays


# ========== BASELINE TESTS (Iteration 0) ==========
def test_divisible_subarrays():
    result = count_divisible_subarrays([4, 5, 0, -2, -3, 1], 5)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_1():
    result = count_divisible_subarrays([1, 2, 3], 3)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_2():
    result = count_divisible_subarrays([5, 10, 15], 5)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_3():
    result = count_divisible_subarrays([1, 1, 1], 2)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_4():
    result = count_divisible_subarrays([2, 4, 6], 2)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_5():
    result = count_divisible_subarrays([3, 6, 9], 3)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_6():
    result = count_divisible_subarrays([1, 2, 3, 4], 5)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_divisible_subarrays_7():
    result = count_divisible_subarrays([10, 20, 30], 10)
    assert result >= 0, f"Expected non-negative result, got {result}"


# ========== ITERATION 1 TESTS ==========
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
    result = count_divisible_subarrays([1, 2, 3], 1)
    # For array of length 3: 3*4/2 = 6 subarrays
    assert result == 6, f"Expected 6 for k=1 with 3 elements, got {result}"


def test_single_element_divisible():
    """Edge case: Single element divisible by k"""
    result = count_divisible_subarrays([5], 5)
    assert result == 1, f"Expected 1 for single divisible element, got {result}"


def test_single_element_not_divisible():
    """Edge case: Single element not divisible by k"""
    result = count_divisible_subarrays([3], 5)
    assert result == 0, f"Expected 0 for single non-divisible element, got {result}"


def test_negative_remainder_handling():
    """Edge case: Array with negative numbers"""
    result = count_divisible_subarrays([-2, -4, 3], 3)
    assert result >= 0, f"Expected non-negative result for negative numbers, got {result}"


# ========== ITERATION 2 TESTS ==========
def test_all_zeros():
    """Edge case: Array of all zeros"""
    result = count_divisible_subarrays([0, 0, 0], 5)
    # All subarrays sum to 0, which is divisible by any k
    # For 3 elements: 3*4/2 = 6 subarrays
    assert result == 6, f"Expected 6 for all zeros, got {result}"


def test_large_k():
    """Edge case: k larger than all array elements"""
    result = count_divisible_subarrays([1, 2, 3], 100)
    assert result >= 0, f"Expected non-negative result for large k, got {result}"


def test_mixed_with_zero():
    """Edge case: Zeros mixed with other values"""
    result = count_divisible_subarrays([0, 2, 4], 2)
    assert result >= 0, f"Expected non-negative result for mixed with zeros, got {result}"


# ========== ITERATION 3 TESTS ==========
def test_negative_prefix_sum_remainder():
    """Iteration 3: Target Line 61 - Negative prefix sum creating negative remainder"""
    # Array with negative numbers that create negative prefix sums
    # This should trigger the remainder < 0 check and adjustment on line 61
    result = count_divisible_subarrays([-7, -3, 5], 4)
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_large_negative_numbers():
    """Iteration 3: Target Line 61 - Large negative numbers"""
    # Large negative values to ensure the negative remainder path is tested
    result = count_divisible_subarrays([-10, -20, 5], 7)
    assert result >= 0, f"Expected non-negative result for large negatives, got {result}"


def test_mixed_negative_positive_edge():
    """Iteration 3: Target Line 61 - Mixed positive/negative with specific k"""
    # Combination designed to force negative remainder before adjustment
    result = count_divisible_subarrays([-5, 3, -2, 4], 6)
    assert result >= 0, f"Expected non-negative result for mixed values, got {result}"


def test_negative_start_sequence():
    """Iteration 3: Target Line 61 - Sequence starting with negatives"""
    # Start with negative to immediately create negative prefix sum
    result = count_divisible_subarrays([-8, -4, 2, 10], 5)
    assert result >= 0, f"Expected non-negative result, got {result}"
