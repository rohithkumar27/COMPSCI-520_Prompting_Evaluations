"""
Test file for humaneval_1_solution.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_1_solution import separate_paren_groups


def test_separate_paren_groups():
    """Test cases from the original dataset."""
    candidate = separate_paren_groups
    
    # Test case 1
    result1 = candidate('( ) (( )) (( )( ))')
    expected1 = ['()', '(())', '(()())']
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    result2 = candidate('() (()) ((())) (((())))') 
    expected2 = ['()', '(())', '((()))', '(((())))']
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    
    # Test case 3
    result3 = candidate('(()(())((())))') 
    expected3 = ['(()(())((())))']
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_separate_paren_groups()