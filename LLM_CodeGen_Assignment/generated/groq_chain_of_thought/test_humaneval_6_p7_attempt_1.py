"""
Test file for humaneval_6_p7_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from humaneval_6_p7_attempt_1 import filter_by_substring

def test_filter_by_substring():
    """Test cases from the original dataset."""
    assert filter_by_substring([], 'john') == []
    assert filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    assert filter_by_substring(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']

if __name__ == "__main__":
    test_filter_by_substring()
    print("All tests passed!")
