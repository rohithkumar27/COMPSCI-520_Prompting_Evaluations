"""
Test file for apps_1_p2_attempt_1.py
Auto-generated from dataset test cases.
"""

import sys
from pathlib import Path

# Add the solution directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import the solution function
from apps_1_p2_attempt_1 import shortest_path_with_obstacles

# Test cases from dataset
def test_shortest_path_with_obstacles():
    """Test cases from the original dataset."""
    candidate = shortest_path_with_obstacles
    
    # Execute the original test cases
    
def test_shortest_path():
    from collections import deque
    
    # Test case 1: Basic example
    grid1 = [
        [2, 1, 0, 0],
        [0, 1, 1, 0], 
        [0, 0, 1, 3]
    ]
    result = shortest_path_with_obstacles(grid1, 1)
    assert result == 5, f"Expected 5, got {result}"
    
    # Test case 2: No obstacles needed to remove
    grid2 = [
        [2, 0, 0],
        [0, 0, 0],
        [0, 0, 3]
    ]
    result = shortest_path_with_obstacles(grid2, 0)
    assert result == 4, f"Expected 4, got {result}"
    
    # Test case 3: Impossible even with K removals
    grid3 = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3]
    ]
    result = shortest_path_with_obstacles(grid3, 1)
    assert result == -1, f"Expected -1, got {result}"


if __name__ == "__main__":
    test_shortest_path_with_obstacles()
    print("All tests passed!")
