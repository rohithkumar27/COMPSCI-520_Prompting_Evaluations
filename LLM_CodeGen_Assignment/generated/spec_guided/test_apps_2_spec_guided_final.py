"""
Exercise 3 - Part 2: Specification-Guided Tests for APPS/2
Problem: Count Valid Parentheses Sequences

These tests are generated from the CORRECTED formal specifications from Part 1.
Each test verifies one or more specifications.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gemini_chain_of_thought.apps_2_p3_attempt_1 import count_valid_parentheses_sequences


# ============================================================================
# Tests based on CORRECT specifications (Specs 1-6)
# ============================================================================

def test_spec1_empty_string():
    """Specification 1: Empty string returns exactly 1"""
    result = count_valid_parentheses_sequences("")
    assert result == 1, f"Expected 1 for empty string, got {result}"


def test_spec2_odd_length_three():
    """Specification 2: Odd length strings must return 0"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0, f"Expected 0 for odd length '(((', got {result}"


def test_spec2_odd_length_one():
    """Specification 2: Single character (odd length) returns 0"""
    result = count_valid_parentheses_sequences("(")
    assert result == 0, f"Expected 0 for single '(', got {result}"


def test_spec2_odd_length_five():
    """Specification 2: Odd length with mixed chars returns 0"""
    result = count_valid_parentheses_sequences("(())(")
    assert result == 0, f"Expected 0 for odd length, got {result}"


def test_spec3_starts_with_close():
    """Specification 3: String starting with ')' must return 0"""
    result = count_valid_parentheses_sequences("))(")
    assert result == 0, f"Expected 0 for string starting with ')', got {result}"


def test_spec3_starts_with_close_simple():
    """Specification 3: Simple case starting with ')'"""
    result = count_valid_parentheses_sequences(")(")
    assert result == 0, f"Expected 0 for ')(', got {result}"


def test_spec4_ends_with_open():
    """Specification 4: String ending with '(' must return 0"""
    result = count_valid_parentheses_sequences("()(")
    assert result == 0, f"Expected 0 for string ending with '(', got {result}"


def test_spec4_ends_with_open_simple():
    """Specification 4: Two opening parens"""
    result = count_valid_parentheses_sequences("((")
    assert result == 0, f"Expected 0 for '((', got {result}"


def test_spec5_result_in_range_simple():
    """Specification 5: Result is non-negative and within modulo"""
    result = count_valid_parentheses_sequences("()")
    assert 0 <= result < 10**9 + 7, f"Result {result} not in valid range"


def test_spec5_result_in_range_complex():
    """Specification 5: Result range for complex input"""
    result = count_valid_parentheses_sequences("(())()")
    assert 0 <= result < 10**9 + 7, f"Result {result} not in valid range"


def test_spec6_no_wildcard_valid():
    """Specification 6: No '?' with valid parens returns 1"""
    result = count_valid_parentheses_sequences("()")
    assert result == 1, f"Expected 1 for '()', got {result}"


def test_spec6_no_wildcard_invalid():
    """Specification 6: No '?' with invalid parens returns 0"""
    result = count_valid_parentheses_sequences("(()")
    assert result == 0, f"Expected 0 for '(()', got {result}"


def test_spec6_no_wildcard_complex_valid():
    """Specification 6: No '?' with complex valid parens"""
    result = count_valid_parentheses_sequences("(())")
    assert result == 1, f"Expected 1 for '(())', got {result}"


def test_spec6_no_wildcard_complex_invalid():
    """Specification 6: No '?' with complex invalid parens"""
    result = count_valid_parentheses_sequences("()))")
    assert result == 0, f"Expected 0 for '()))', got {result}"


# ============================================================================
# Tests based on CORRECTED specifications (Specs 7-8)
# ============================================================================

def test_spec7_all_wildcards_two():
    """Specification 7 (CORRECTED): All '?' with even length - minimal case"""
    result = count_valid_parentheses_sequences("??")
    # "??" can form "()" which is 1 way
    assert result >= 1, f"Expected >= 1 for '??', got {result}"


def test_spec7_all_wildcards_four():
    """Specification 7 (CORRECTED): All '?' with even length - 4 chars"""
    result = count_valid_parentheses_sequences("????")
    # "????" can form "(())" and "()()" which is 2 ways
    assert result >= 1, f"Expected >= 1 for '????', got {result}"


def test_spec7_mixed_with_wildcard_invalid():
    """Specification 7 (CORRECTED): Mixed chars with '?' - should NOT guarantee >= 1"""
    # This tests that we DON'T incorrectly apply spec 7 to mixed strings
    result = count_valid_parentheses_sequences("?)(")
    # This is invalid (starts with ')' if '?' becomes '(', or has ")((" if '?' becomes ')')
    # We just check it doesn't crash - result should be 0
    assert result == 0, f"Expected 0 for '?)(', got {result}"


def test_spec8_all_open_parens_two():
    """Specification 8 (CORRECTED): String with only '(' returns 0"""
    result = count_valid_parentheses_sequences("((")
    assert result == 0, f"Expected 0 for '((', got {result}"


def test_spec8_all_open_parens_four():
    """Specification 8 (CORRECTED): Four opening parens"""
    result = count_valid_parentheses_sequences("((((")
    assert result == 0, f"Expected 0 for '((((', got {result}"


def test_spec8_all_close_parens_two():
    """Specification 8 (CORRECTED): String with only ')' returns 0"""
    result = count_valid_parentheses_sequences("))")
    assert result == 0, f"Expected 0 for '))', got {result}"


def test_spec8_all_close_parens_four():
    """Specification 8 (CORRECTED): Four closing parens"""
    result = count_valid_parentheses_sequences("))))")
    assert result == 0, f"Expected 0 for '))))', got {result}"


# ============================================================================
# Additional edge case tests
# ============================================================================

def test_wildcard_at_start():
    """Edge case: Wildcard at start position"""
    result = count_valid_parentheses_sequences("?()")
    # "?()": if '?' is '(', we get "(()" which is invalid
    #        if '?' is ')', we get ")()" which is invalid (starts with ')')
    assert result == 0, f"Expected 0 for '?()', got {result}"


def test_wildcard_at_end():
    """Edge case: Wildcard at end position"""
    result = count_valid_parentheses_sequences("()?"
)
    # "()?" has odd length, should return 0
    assert result == 0, f"Expected 0 for '()?', got {result}"


def test_simple_wildcard_valid():
    """Edge case: Simple valid wildcard case"""
    result = count_valid_parentheses_sequences("(?)")
    # "(?)" can form "()" which is valid
    assert result == 1, f"Expected 1 for '(?)', got {result}"


if __name__ == "__main__":
    print("Running specification-guided tests for Count Valid Parentheses...")
    print("=" * 70)
    
    tests = [
        test_spec1_empty_string,
        test_spec2_odd_length_three,
        test_spec2_odd_length_one,
        test_spec2_odd_length_five,
        test_spec3_starts_with_close,
        test_spec3_starts_with_close_simple,
        test_spec4_ends_with_open,
        test_spec4_ends_with_open_simple,
        test_spec5_result_in_range_simple,
        test_spec5_result_in_range_complex,
        test_spec6_no_wildcard_valid,
        test_spec6_no_wildcard_invalid,
        test_spec6_no_wildcard_complex_valid,
        test_spec6_no_wildcard_complex_invalid,
        test_spec7_all_wildcards_two,
        test_spec7_all_wildcards_four,
        test_spec7_mixed_with_wildcard_invalid,
        test_spec8_all_open_parens_two,
        test_spec8_all_open_parens_four,
        test_spec8_all_close_parens_two,
        test_spec8_all_close_parens_four,
        test_wildcard_at_start,
        test_wildcard_at_end,
        test_simple_wildcard_valid,
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
