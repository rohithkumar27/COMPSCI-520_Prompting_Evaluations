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

def test_question_mark_multiple():
    """Edge case: Multiple question marks"""
    result = count_valid_parentheses_sequences("????")
    assert result == 2, f"Expected 2 for '????', got {result}"

def test_impossible_case():
    """Edge case: Impossible to balance"""
    result = count_valid_parentheses_sequences("(()")
    assert result == 0, f"Expected 0 for unbalanced '(()', got {result}"


# ========== ITERATION 2: FINAL COVERAGE PUSH ==========

def test_question_at_start():
    """Edge case: Question mark at start position"""
    result = count_valid_parentheses_sequences("?()")
    # '?' can be '(' making "(())" which is valid
    assert result >= 1, f"Expected at least 1, got {result}"

def test_question_at_end():
    """Edge case: Question mark at end position"""
    result = count_valid_parentheses_sequences("()?"
)
    # '?' can be ')' making "()" which is invalid (odd after removing ?)
    # Actually "()?" has length 3 (odd), should return 0
    assert result == 0, f"Expected 0 for odd length, got {result}"

def test_all_questions():
    """Edge case: All question marks (even length)"""
    result = count_valid_parentheses_sequences("??")
    # Can be "()" which is valid
    assert result == 1, f"Expected 1 for '??', got {result}"

def test_complex_question_pattern():
    """Edge case: Complex pattern with questions"""
    result = count_valid_parentheses_sequences("(?(?")
    # Length 4, but ends with '(' - should be 0
    assert result == 0, f"Expected 0, got {result}"

def test_max_open_exceeded():
    """Edge case: Too many closing parens"""
    result = count_valid_parentheses_sequences("()))")
    assert result == 0, f"Expected 0 for too many ')', got {result}"
