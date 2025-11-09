"""
Test file for humaneval_8_p9_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_8_p9_attempt_1 import rolling_max

def test_rolling_max():
    """Test cases from the original dataset."""
    assert rolling_max([]) == []
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert rolling_max([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

if __name__ == "__main__":
    test_rolling_max()
    print("All tests passed!")
