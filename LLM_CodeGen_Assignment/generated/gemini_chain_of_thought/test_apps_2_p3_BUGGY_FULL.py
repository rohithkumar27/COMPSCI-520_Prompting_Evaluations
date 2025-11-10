import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_2_p3_attempt_1_BUGGY import count_valid_parentheses_sequences


# Test that should catch BUG 1: Off-by-one in odd length check
def test_length_two_string():
    """This should catch Bug 1: len(s) % 2 > 0 incorrectly rejects length 2"""
    result = count_valid_parentheses_sequences("()")
    assert result == 1, f"Expected 1 for '()', got {result}"


def test_length_two_with_question():
    """This should catch Bug 1: length 2 strings incorrectly rejected"""
    result = count_valid_parentheses_sequences("??")
    assert result == 1, f"Expected 1 for '??', got {result}"


# Test that should catch BUG 2: Wrong boundary in max_open check
def test_single_close_paren():
    """This should catch Bug 2: max_open <= 0 incorrectly rejects when max_open = 0"""
    result = count_valid_parentheses_sequences("()")
    assert result == 1, f"Expected 1 for '()', got {result}"


def test_balanced_simple():
    """This should catch Bug 2: balanced parens with max_open reaching 0"""
    result = count_valid_parentheses_sequences("(())")
    assert result == 1, f"Expected 1 for '(())', got {result}"
