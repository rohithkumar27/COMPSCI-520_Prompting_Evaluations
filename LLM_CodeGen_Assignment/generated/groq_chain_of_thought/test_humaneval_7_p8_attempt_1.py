"""
Test file for humaneval_7_p8_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_7_p8_attempt_1 import sum_product

def test_sum_product():
    """Test cases from the original dataset."""
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 1, 1]) == (3, 1)
    assert sum_product([100, 0]) == (100, 0)
    assert sum_product([3, 5, 7]) == (15, 105)

if __name__ == "__main__":
    test_sum_product()
    print("All tests passed!")
