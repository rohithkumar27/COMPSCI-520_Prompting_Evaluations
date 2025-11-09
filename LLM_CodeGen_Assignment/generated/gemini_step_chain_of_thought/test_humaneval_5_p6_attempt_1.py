"""
Test file for humaneval_5_p6_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_5_p6_attempt_1 import intersperse

def test_intersperse():
    """Test cases from the original dataset."""
    assert intersperse([], 7) == []
    assert intersperse([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2]

if __name__ == "__main__":
    test_intersperse()
    print("All tests passed!")
