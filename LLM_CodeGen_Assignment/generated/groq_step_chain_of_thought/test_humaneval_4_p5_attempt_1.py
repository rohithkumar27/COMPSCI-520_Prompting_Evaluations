"""
Test file for humaneval_4_p5_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_4_p5_attempt_1 import mean_absolute_deviation

def test_mean_absolute_deviation():
    """Test cases from the original dataset."""
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) - 1.2) < 1e-6
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) - 1.5) < 1e-6

if __name__ == "__main__":
    test_mean_absolute_deviation()
    print("All tests passed!")
