import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_3_p4_attempt_1_BUGGY import count_divisible_subarrays


# Test that should catch BUG 1: Off-by-one in k=1 formula
def test_k_one_bug():
    """This should catch Bug 1: n*(n-1)/2 instead of n*(n+1)/2"""
    result = count_divisible_subarrays([1, 2, 3], 1)
    # For array of length 3: should be 3*4/2 = 6 subarrays
    # But buggy version gives 3*2/2 = 3
    assert result == 6, f"Expected 6 for k=1 with 3 elements, got {result}"


def test_k_one_single_element():
    """Edge case for k=1 with single element"""
    result = count_divisible_subarrays([5], 1)
    # Should be 1 subarray
    assert result == 1, f"Expected 1, got {result}"


# Test that should catch BUG 2: Wrong initialization of mod_count
def test_simple_divisible():
    """This should catch Bug 2: mod_count[0] = 0 instead of 1"""
    result = count_divisible_subarrays([5], 5)
    # Single element divisible by k should return 1
    # But buggy version with mod_count[0]=0 will return 0
    assert result == 1, f"Expected 1, got {result}"


def test_prefix_sum_zero():
    """This should catch Bug 2: missing empty prefix count"""
    result = count_divisible_subarrays([3, 3], 3)
    # [3] and [3,3] are both divisible by 3, so should be 2
    # But buggy version will miss counting from empty prefix
    assert result >= 2, f"Expected at least 2, got {result}"


def test_all_divisible_by_k():
    """Test where all elements are divisible by k"""
    result = count_divisible_subarrays([2, 4, 6], 2)
    # All subarrays should be divisible: [2], [4], [6], [2,4], [4,6], [2,4,6] = 6
    assert result == 6, f"Expected 6, got {result}"
