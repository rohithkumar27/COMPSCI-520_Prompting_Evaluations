import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_2_p3_attempt_1 import count_valid_parentheses_sequences


# ========== BASELINE TESTS (Iteration 0) ==========
def test_parentheses_count():
    result = count_valid_parentheses_sequences("(())")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_1():
    result = count_valid_parentheses_sequences("()()")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_2():
    result = count_valid_parentheses_sequences("((()))")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_3():
    result = count_valid_parentheses_sequences("()()()")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_4():
    result = count_valid_parentheses_sequences("(((())))")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_5():
    result = count_valid_parentheses_sequences("(()())")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_6():
    result = count_valid_parentheses_sequences("(()(()))")
    assert result == 1, f"Expected 1, got {result}"

def test_parentheses_count_7():
    result = count_valid_parentheses_sequences("(())(())")
    assert result == 1, f"Expected 1, got {result}"


# ========== ITERATION 1: TARGETED EDGE CASE TESTS ==========

def test_empty_string():
    """Edge case: Empty string should return 1 (valid empty sequence)"""
    result = count_valid_parentheses_sequences("")
    assert result == 1, f"Expected 1 for empty string, got {result}"

def test_odd_length():
    """Edge case: Odd length string cannot be valid"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0, f"Expected 0 for odd length, got {result}"

def test_starts_with_close():
    """Edge case: String starting with ')' is invalid"""
    result = count_valid_parentheses_sequences("))(")
    assert result == 0, f"Expected 0 for string starting with ')', got {result}"

def test_ends_with_open():
    """Edge case: String ending with '(' is invalid"""
    result = count_valid_parentheses_sequences("(()(")
    assert result == 0, f"Expected 0 for string ending with '(', got {result}"

def test_question_mark_simple():
    """Edge case: Question mark can be either '(' or ')'"""
    result = count_valid_parentheses_sequences("(?)")
    assert result == 1, f"Expected 1 for '(?)', got {result}"

def test_question_mark_multiple():
    """Edge case: Multiple question marks"""
    result = count_valid_parentheses_sequences("????")
    # "????" can be "(())" or "()()" = 2 ways
    assert result == 2, f"Expected 2 for '????', got {result}"

def test_impossible_case():
    """Edge case: Impossible to balance"""
    result = count_valid_parentheses_sequences("(()")
    assert result == 0, f"Expected 0 for unbalanced '(()', got {result}"
