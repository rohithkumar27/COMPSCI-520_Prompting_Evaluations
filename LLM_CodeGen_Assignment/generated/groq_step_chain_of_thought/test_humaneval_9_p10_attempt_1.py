"""
Test file for humaneval_9_p10_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_9_p10_attempt_1 import is_palindrome

def test_is_palindrome():
    """Test cases from the original dataset."""
    assert is_palindrome('') == ''
    assert is_palindrome('x') == 'x'
    assert is_palindrome('xyz') == 'xyzyx'
    assert is_palindrome('xyx') == 'xyx'
    assert is_palindrome('jerry') == 'jerryrrej'

if __name__ == "__main__":
    test_is_palindrome()
    print("All tests passed!")
