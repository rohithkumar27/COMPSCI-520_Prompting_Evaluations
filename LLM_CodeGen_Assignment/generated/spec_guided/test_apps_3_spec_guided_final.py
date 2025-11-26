"""
Exercise 3 - Part 2: Specification-Guided Tests for APPS/3
Problem: Count Divisible Subarrays

These tests are generated from the CORRECTED formal specifications from Part 1.
Each test verifies one or more specifications.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gemini_chain_of_thought.apps_3_p4_attempt_1 import count_divisible_subarrays


# ============================================================================
# Tests based on CORRECT specifications (Specs 1-5)
# ============================================================================

def test_spec1_empty_array():
    """Specification 1: Empty array returns 0"""
    result = count_divisible_subarrays([], 5)
    assert result == 0, f"Expected 0 for empty array, got {result}"


def test_spec2_k_zero():
    """Specification 2: k=0 returns 0"""
    result = count_divisible_subarrays([1, 2, 3], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"


def test_spec2_k_zero_with_zeros():
    """Specification 2: k=0 with array of zeros"""
    result = count_divisible_subarrays([0, 0, 0], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"


def test_spec3_k_one_small():
    """Specification 3: k=1 means all subarrays divisible"""
    arr = [5, 10, 15]
    n = len(arr)
    expected = n * (n + 1) // 2  # 3*4/2 = 6 subarrays
    result = count_divisible_subarrays(arr, 1)
    assert result == expected, f"Expected {expected} for k=1, got {result}"


def test_spec3_k_one_single():
    """Specification 3: k=1 with single element"""
    result = count_divisible_subarrays([7], 1)
    assert result == 1, f"Expected 1 for k=1 with single element, got {result}"


def test_spec3_k_one_large():
    """Specification 3: k=1 with larger array"""
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    expected = n * (n + 1) // 2  # 5*6/2 = 15
    result = count_divisible_subarrays(arr, 1)
    assert result == expected, f"Expected {expected} for k=1, got {result}"


def test_spec4_result_non_negative():
    """Specification 4: Result is non-negative"""
    result = count_divisible_subarrays([1, 2, 3], 5)
    assert result >= 0, f"Result should be non-negative, got {result}"


def test_spec4_result_non_negative_negative_nums():
    """Specification 4: Non-negative result with negative numbers"""
    result = count_divisible_subarrays([-1, -2, -3], 5)
    assert result >= 0, f"Result should be non-negative, got {result}"


def test_spec5_result_bounded():
    """Specification 5: Result <= total possible subarrays"""
    arr = [1, 2, 3, 4]
    result = count_divisible_subarrays(arr, 5)
    max_subarrays = len(arr) * (len(arr) + 1) // 2
    assert result <= max_subarrays, f"Result {result} exceeds max {max_subarrays}"


def test_spec5_result_bounded_large():
    """Specification 5: Bounded result with larger array"""
    arr = [1, 2, 3, 4, 5, 6]
    result = count_divisible_subarrays(arr, 7)
    max_subarrays = len(arr) * (len(arr) + 1) // 2
    assert result <= max_subarrays, f"Result {result} exceeds max {max_subarrays}"


# ============================================================================
# Tests based on CORRECTED specifications (Specs 6-7)
# ============================================================================

def test_spec6_single_element_divisible():
    """Specification 6 (CORRECTED): Single element divisible by k returns 1"""
    result = count_divisible_subarrays([10], 5)
    assert result == 1, f"Expected 1 for single divisible element, got {result}"


def test_spec6_single_element_divisible_exact():
    """Specification 6 (CORRECTED): Single element exactly equals k"""
    result = count_divisible_subarrays([7], 7)
    assert result == 1, f"Expected 1 for [7] with k=7, got {result}"


def test_spec6_single_element_not_divisible():
    """Specification 6 (CORRECTED): Single element not divisible by k returns 0"""
    result = count_divisible_subarrays([7], 5)
    assert result == 0, f"Expected 0 for single non-divisible element, got {result}"


def test_spec6_single_element_with_k_zero():
    """Specification 6 (CORRECTED): Single element with k=0 returns 0"""
    # This tests the correction - we added k != 0 check
    result = count_divisible_subarrays([5], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"


def test_spec7_all_zeros_small():
    """Specification 7 (CORRECTED): Array of all zeros with k > 0"""
    arr = [0, 0, 0]
    n = len(arr)
    expected = n * (n + 1) // 2  # 3*4/2 = 6
    result = count_divisible_subarrays(arr, 5)
    assert result == expected, f"Expected {expected} for all zeros, got {result}"


def test_spec7_all_zeros_single():
    """Specification 7 (CORRECTED): Single zero element"""
    result = count_divisible_subarrays([0], 7)
    assert result == 1, f"Expected 1 for single zero, got {result}"


def test_spec7_all_zeros_large():
    """Specification 7 (CORRECTED): Larger array of zeros"""
    arr = [0, 0, 0, 0, 0]
    n = len(arr)
    expected = n * (n + 1) // 2  # 5*6/2 = 15
    result = count_divisible_subarrays(arr, 3)
    assert result == expected, f"Expected {expected} for all zeros, got {result}"


def test_spec7_all_zeros_with_k_zero():
    """Specification 7 (CORRECTED): All zeros with k=0 returns 0"""
    # This tests the correction - we added k > 0 check
    result = count_divisible_subarrays([0, 0, 0], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"


# ============================================================================
# Additional edge case tests
# ============================================================================

def test_mixed_with_zeros():
    """Edge case: Mixed positive and zeros"""
    result = count_divisible_subarrays([5, 0, 5, 0], 5)
    # Multiple subarrays should be divisible by 5
    assert result >= 4, f"Expected >= 4 for mixed with zeros, got {result}"


def test_negative_numbers():
    """Edge case: Negative numbers"""
    result = count_divisible_subarrays([4, 5, 0, -2, -3, 1], 5)
    # This is the example from the problem description
    assert result == 7, f"Expected 7 for example case, got {result}"


def test_large_k():
    """Edge case: k larger than any element"""
    result = count_divisible_subarrays([1, 2, 3], 100)
    # Only subarrays that sum to 0, 100, 200, etc. are divisible
    # None of these small numbers sum to 100+
    assert result >= 0, f"Result should be non-negative, got {result}"


def test_single_element_zero():
    """Edge case: Single zero element with various k"""
    result = count_divisible_subarrays([0], 10)
    assert result == 1, f"Expected 1 for [0] with k=10, got {result}"


if __name__ == "__main__":
    print("Running specification-guided tests for Count Divisible Subarrays...")
    print("=" * 70)
    
    tests = [
        test_spec1_empty_array,
        test_spec2_k_zero,
        test_spec2_k_zero_with_zeros,
        test_spec3_k_one_small,
        test_spec3_k_one_single,
        test_spec3_k_one_large,
        test_spec4_result_non_negative,
        test_spec4_result_non_negative_negative_nums,
        test_spec5_result_bounded,
        test_spec5_result_bounded_large,
        test_spec6_single_element_divisible,
        test_spec6_single_element_divisible_exact,
        test_spec6_single_element_not_divisible,
        test_spec6_single_element_with_k_zero,
        test_spec7_all_zeros_small,
        test_spec7_all_zeros_single,
        test_spec7_all_zeros_large,
        test_spec7_all_zeros_with_k_zero,
        test_mixed_with_zeros,
        test_negative_numbers,
        test_large_k,
        test_single_element_zero,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Unexpected error: {e}")
            failed += 1
    
    print("=" * 70)
    print(f"\n{passed}/{len(tests)} tests passed")
    if failed > 0:
        sys.exit(1)
