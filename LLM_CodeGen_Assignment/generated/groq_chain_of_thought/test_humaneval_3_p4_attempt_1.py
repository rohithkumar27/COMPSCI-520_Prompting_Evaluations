"""
Test file for humaneval_3_p4_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_3_p4_attempt_1 import below_zero

def test_below_zero():
    """Test cases from the original dataset."""
    assert below_zero([]) == False
    assert below_zero([1, 2, -3, 1, 2, -3]) == False
    assert below_zero([1, 2, -4, 5, 6]) == True
    assert below_zero([1, 2, -4, 5]) == True

if __name__ == "__main__":
    test_below_zero()
    print("All tests passed!")
