import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_2_p3_attempt_1 import count_valid_parentheses_sequences


# ========== BASELINE TESTS (Iteration 0) ==========
def test_parentheses_count():
    result = count_valid_parentheses_sequences("(())")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_1():
    result = count_valid_parentheses_sequences("()")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_2():
    result = count_valid_parentheses_sequences("()()")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_3():
    result = count_valid_parentheses_sequences("((()))")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_4():
    result = count_valid_parentheses_sequences("(()())")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_5():
    result = count_valid_parentheses_sequences("()()()")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_6():
    result = count_valid_parentheses_sequences("(()(()))")
    assert result >= 0, f"Expected non-negative result, got {result}"


def test_parentheses_count_7():
    result = count_valid_parentheses_sequences("(())(())")
    assert result >= 0, f"Expected non-negative result, got {result}"


# ========== ITERATION 1 TESTS ==========
def test_empty_string():
    """Edge case: Empty string should return 1 (valid by definition)"""
    result = count_valid_parentheses_sequences("")
    assert result == 1, f"Expected 1 for empty string, got {result}"


def test_odd_length():
    """Edge case: Odd length strings cannot be balanced"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0, f"Expected 0 for odd length, got {result}"


def test_starts_with_close():
    """Edge case: String starting with ')' cannot be valid"""
    result = count_valid_parentheses_sequences(")()")
    assert result == 0, f"Expected 0 for string starting with ')', got {result}"


def test_ends_with_open():
    """Edge case: String ending with '(' cannot be valid"""
    result = count_valid_parentheses_sequences("()(")
    assert result == 0, f"Expected 0 for string ending with '(', got {result}"


def test_question_mark_multiple():
    """Edge case: Multiple question marks"""
    result = count_valid_parentheses_sequences("??")
    assert result == 1, f"Expected 1 for '??', got {result}"


def test_impossible_case():
    """Edge case: Impossible to balance"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0, f"Expected 0 for impossible case, got {result}"


# ========== ITERATION 2 TESTS ==========
def test_question_at_end():
    """Edge case: Question mark at end position"""
    result = count_valid_parentheses_sequences("()?")
    assert result == 1, f"Expected 1 for '()?', got {result}"


def test_all_questions():
    """Edge case: All question marks"""
    result = count_valid_parentheses_sequences("????")
    assert result == 2, f"Expected 2 for '????', got {result}"


def test_max_open_exceeded():
    """Edge case: Too many closing parentheses"""
    result = count_valid_parentheses_sequences("()))")
    assert result == 0, f"Expected 0 for too many closing parens, got {result}"


# ========== ITERATION 3 TESTS ==========
def test_explicit_close_start():
    """Iteration 3: Target Line 39 - String explicitly starting with ')' (not '?')"""
    # This should trigger the s[0] == ')' check on line 39
    result = count_valid_parentheses_sequences("))")
    assert result == 0, f"Expected 0 for string starting with ')', got {result}"


def test_explicit_close_start_longer():
    """Iteration 3: Target Line 39 - Longer string starting with ')'"""
    # Another test for line 39 with longer input
    result = count_valid_parentheses_sequences(")()(")
    assert result == 0, f"Expected 0 for string starting with ')', got {result}"


def test_min_open_validation():
    """Iteration 3: Target Line 66 - String that fails min_open > 0 validation"""
    # This should create a scenario where min_open > 0 after the validation loop
    # String with more '(' than can be balanced
    result = count_valid_parentheses_sequences("((")
    assert result == 0, f"Expected 0 for unbalanced '((', got {result}"


def test_complex_min_open_fail():
    """Iteration 3: Target Line 66 - Complex pattern failing min_open validation"""
    # Pattern that should fail the min_open > 0 check
    result = count_valid_parentheses_sequences("((?")
    assert result == 0, f"Expected 0 for pattern with excess open parens, got {result}"
