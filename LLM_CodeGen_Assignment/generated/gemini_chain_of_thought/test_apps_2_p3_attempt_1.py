import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apps_2_p3_attempt_1 import count_valid_parentheses_sequences


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
