"""
APPS Dataset - Tough Problems
Selected challenging problems from the APPS dataset for advanced code generation evaluation.
These problems require more complex algorithmic thinking and implementation skills.
"""

APPS_TOUGH_PROBLEMS = [
    # ========== COMPETITIVE PROGRAMMING PROBLEMS ==========
    {
        "task_id": "APPS/0",
        "difficulty": "Hard",
        "source": "APPS Dataset - Competitive Programming",
        "prompt": """
def solve_knapsack_variant(n, w, k, items):
    '''
    You are given N items, each with a weight w[i] and value v[i].
    You have a knapsack with capacity W.
    However, there's a twist: you can take at most K items of each type.
    
    Find the maximum value you can achieve.
    
    Parameters:
    - n: number of item types
    - w: knapsack capacity  
    - k: max items per type
    - items: list of (weight, value) tuples
    
    Example:
    n=3, w=10, k=2
    items=[(2,3), (3,4), (4,5)]
    
    You can take at most 2 of each item type.
    Optimal: Take 2 items of type 1 (weight=4, value=6) and 2 items of type 2 (weight=6, value=8)
    Total: weight=10, value=14
    
    Return the maximum value achievable.
    '''
""",
        "test": """
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
    
    print("All knapsack tests passed!")

test_knapsack_variant()
"""
    },
    
    {
        "task_id": "APPS/1", 
        "difficulty": "Hard",
        "source": "APPS Dataset - Graph Algorithms",
        "prompt": """
def shortest_path_with_obstacles(grid, k):
    '''
    You are given a grid of size N x M where:
    - 0 represents an empty cell
    - 1 represents an obstacle
    - 2 represents the start position
    - 3 represents the end position
    
    You can move in 4 directions (up, down, left, right).
    However, you have a special ability: you can remove at most K obstacles during your journey.
    
    Find the shortest path from start to end, considering you can remove at most K obstacles.
    Return the minimum number of steps, or -1 if impossible.
    
    Parameters:
    - grid: 2D list representing the grid
    - k: maximum number of obstacles you can remove
    
    Example:
    grid = [[2, 1, 0, 0],
            [0, 1, 1, 0], 
            [0, 0, 1, 3]]
    k = 1
    
    Without removing obstacles: impossible
    With removing 1 obstacle: can reach in 5 steps
    '''
""",
        "test": """
def test_shortest_path():
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
    
    print("All shortest path tests passed!")

test_shortest_path()
"""
    },
    
    {
        "task_id": "APPS/2",
        "difficulty": "Hard", 
        "source": "APPS Dataset - Dynamic Programming",
        "prompt": """
def count_valid_parentheses_sequences(s):
    '''
    Given a string containing '(', ')', and '?', where '?' can be either '(' or ')'.
    Count the number of ways to replace '?' characters such that the resulting string
    has valid parentheses.
    
    A valid parentheses string is one where:
    1. Every '(' has a matching ')'
    2. At no point do we have more ')' than '(' when reading left to right
    
    Return the count modulo 10^9 + 7.
    
    Parameters:
    - s: string containing '(', ')', and '?' characters
    
    Examples:
    "(?)" -> 1 way: "()"
    "(??))" -> 1 way: "(())"  
    "????" -> 2 ways: "(())" and "()()"
    '''
""",
        "test": """
assert count_valid_parentheses_sequences("(())") == 1
assert count_valid_parentheses_sequences("()()") == 1
assert count_valid_parentheses_sequences("((()))") == 1
assert count_valid_parentheses_sequences("()()()") == 1
assert count_valid_parentheses_sequences("(((())))") == 1
assert count_valid_parentheses_sequences("(()())") == 1
assert count_valid_parentheses_sequences("(()(()))") == 1
assert count_valid_parentheses_sequences("(())(())") == 1
"""
    },
    
    {
        "task_id": "APPS/3",
        "difficulty": "Hard",
        "source": "APPS Dataset - Number Theory",
        "prompt": """
def count_divisible_subarrays(arr, k):
    '''
    Given an array of integers and a number K, count the number of subarrays
    whose sum is divisible by K.
    
    A subarray is a contiguous part of an array.
    
    Use modular arithmetic properties:
    If (prefix_sum[j] - prefix_sum[i]) % K == 0, then prefix_sum[j] % K == prefix_sum[i] % K
    
    Parameters:
    - arr: list of integers
    - k: divisor
    
    Examples:
    arr = [4, 5, 0, -2, -3, 1], k = 5
    Subarrays with sum divisible by 5:
    [5], [5, 0], [5, 0, -2, -3], [0], [-2, -3], [4, 5, 0, -2, -3, 1]
    Answer: 7
    '''
""",
        "test": """
assert count_divisible_subarrays([4, 5, 0, -2, -3, 1], 5) == 7
assert count_divisible_subarrays([3, 6, 2, -1, -4, 2], 5) >= 0
assert count_divisible_subarrays([10, 15, 5, -5, -10, 0], 5) >= 0
assert count_divisible_subarrays([7, 14, 3, -3, -7, 1], 7) >= 0
assert count_divisible_subarrays([8, 12, 4, -4, -8, 2], 4) >= 0
assert count_divisible_subarrays([6, 9, 3, -3, -6, 0], 3) >= 0
assert count_divisible_subarrays([11, 22, 5, -5, -11, 3], 11) >= 0
assert count_divisible_subarrays([13, 26, 7, -7, -13, 4], 13) >= 0
"""
    },
    
    {
        "task_id": "APPS/4",
        "difficulty": "Hard",
        "source": "APPS Dataset - Tree Algorithms", 
        "prompt": """
def tree_diameter_with_weights(edges, n):
    '''
    Given a weighted tree (connected acyclic graph), find the diameter.
    The diameter is the longest path between any two nodes in the tree.
    
    Parameters:
    - edges: list of tuples (u, v, weight) representing edges
    - n: number of nodes (nodes are numbered 0 to n-1)
    
    Algorithm approach:
    1. Pick any node, find the farthest node from it (using DFS/BFS)
    2. From that farthest node, find the farthest node again
    3. The distance in step 2 is the diameter
    
    Example:
    edges = [(0, 1, 5), (1, 2, 3), (2, 3, 7)]
    Tree: 0--(5)--1--(3)--2--(7)--3
    Diameter = 5 + 3 + 7 = 15
    '''
""",
        "test": """
def test_tree_diameter():
    # Test case 1: Linear tree
    edges1 = [(0, 1, 5), (1, 2, 3), (2, 3, 7)]
    result = tree_diameter_with_weights(edges1, 4)
    assert result == 15, f"Expected 15, got {result}"
    
    # Test case 2: Star tree
    edges2 = [(0, 1, 2), (0, 2, 3), (0, 3, 4)]
    result = tree_diameter_with_weights(edges2, 4)
    assert result == 7, f"Expected 7, got {result}"  # 3 + 4
    
    # Test case 3: Single edge
    edges3 = [(0, 1, 10)]
    result = tree_diameter_with_weights(edges3, 2)
    assert result == 10, f"Expected 10, got {result}"
    
    print("All tree diameter tests passed!")

test_tree_diameter()
"""
    }
]