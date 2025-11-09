"""
Test file for humaneval_2_p1_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_2_p1_attempt_1 import truncate_number

def test_truncate_number():
    """Test cases from the original dataset."""
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
    assert abs(truncate_number(123.456) - 0.456) < 1e-6

if __name__ == "__main__":
    test_truncate_number()
    print("All tests passed!")
