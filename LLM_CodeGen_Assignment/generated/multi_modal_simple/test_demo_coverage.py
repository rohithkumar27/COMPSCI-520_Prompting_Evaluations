"""
Test file for humaneval_1_solution.py
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_1_solution import separate_paren_groups

def test_separate_paren_groups():
    """Test cases from the original dataset."""
    
    # Test case 1: Basic functionality
    result = separate_paren_groups('( ) (( )) (( )( ))')
    expected = ['()', '(())', '(()())']
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 2: More complex nested
    result = separate_paren_groups('() (()) ((())) (((())))') 
    expected = ['()', '(())', '((()))', '(((())))']
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 3: Single complex group
    result = separate_paren_groups('(()(())((())))') 
    expected = ['(()(())((())))']
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 4: Empty string
    result = separate_paren_groups('')
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 5: Invalid characters (should return empty list)
    result = separate_paren_groups('(a)')
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"
    
    # Test case 6: Unbalanced parentheses
    result = separate_paren_groups('(()')
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_separate_paren_groups()
