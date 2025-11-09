"""
Test file for apps_0_p1_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from apps_0_p1_attempt_1 import solve_knapsack_variant

# Test cases from dataset
def test_solve_knapsack_variant():
    """Test cases from the original dataset."""
    candidate = solve_knapsack_variant
    
    # Execute the original test cases
    
def test_knapsack_variant():
    # Test case 1: Basic example
    # N=3, W=10, K=2, items=[(2,3), (3,4), (4,5)]
    result = solve_knapsack_variant(3, 10, 2, [(2,3), (3,4), (4,5)])
    assert result == 14, f"Expected 14, got {result}"
    
    # Test case 2: All items fit
    # N=2, W=20, K=3, items=[(2,5), (3,7)]
    result = solve_knapsack_variant(2, 20, 3, [(2,5), (3,7)])
    assert result == 36, f"Expected 36, got {result}"  # 3*5 + 3*7 = 36
    
    # Test case 3: Single item type
    result = solve_knapsack_variant(1, 5, 2, [(3,4)])
    assert result == 4, f"Expected 4, got {result}"  # Can take 1 item


if __name__ == "__main__":
    test_solve_knapsack_variant()
    print("All tests passed!")
