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
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('(()(())((())))') == ['(()(())((())))']

if __name__ == "__main__":
    test_separate_paren_groups()
    print("All tests passed!")
