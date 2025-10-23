# Gemini solution using step_chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: APPS/0
# Difficulty: Hard

def solve_knapsack_variant(n: int, W: int, k: int, items: List[Tuple[int, int]]) -> int:
    '''
    You are given N items, each with a weight w[i] and value v[i].
    You have a knapsack with capacity W.
    However, there's a twist: you can take at most K items of each type.
    
    Find the maximum value you can achieve.
    
    Parameters:
    - n: number of item types
    - W: knapsack capacity  
    - k: max items per type
    - items: list of (weight, value) tuples
    
    Example:
    n=3, W=10, k=2
    items=[(2,3), (3,4), (4,5)]
    
    You can take at most 2 of each item type.
    Optimal: Take 2 items of type 1 (weight=4, value=6) and 1 item of type 2 (weight=3, value=4)
    Total: weight=7, value=10
    
    Return the maximum value achievable.
    '''

    # Step 1: Understand the problem
    # We need to select items to maximize total value, subject to a weight capacity
    # and a constraint on the number of items of each type (at most k).
    # This is a variation of the bounded knapsack problem.

    # Step 2: Analyze the examples
    # Example 1: n=3, W=10, k=2, items=[(2,3), (3,4), (4,5)]
    # Item 0: weight=2, value=3
    # Item 1: weight=3, value=4
    # Item 2: weight=4, value=5
    # Max 2 of each.
    # Possible combinations:
    # - 2x(2,3) + 1x(3,4) = weight 4+3=7, value 6+4=10. (This is the example's optimal)
    # - 2x(2,3) + 1x(4,5) = weight 4+4=8, value 6+5=11.
    # - 1x(2,3) + 2x(3,4) = weight 2+6=8, value 3+8=11.
    # - 1x(2,3) + 1x(3,4) + 1x(4,5) = weight 2+3+4=9, value 3+4+5=12.
    # - 2x(3,4) + 1x(4,5) = weight 6+4=10, value 8+5=13.
    # - 2x(4,5) = weight 8, value 10.
    # - 1x(2,3) + 2x(4,5) = weight 2+8=10, value 3+10=13.
    # - 1x(3,4) + 2x(4,5) = weight 3+8=11 (exceeds capacity)
    # The example's optimal is not necessarily the global optimal.
    # The example states "Optimal: Take 2 items of type 1 (weight=4, value=6) and 1 item of type 2 (weight=3, value=4) Total: weight=7, value=10".
    # This implies the example might be slightly misleading or there's a misunderstanding of "type 1" and "type 2".
    # Assuming items[0] is type 0, items[1] is type 1, etc.
    # If items=[(2,3), (3,4), (4,5)]
    # Type 0: (2,3)
    # Type 1: (3,4)
    # Type 2: (4,5)
    # Example's optimal: 2x(2,3) + 1x(3,4) = weight 4+3=7, value 6+4=10.
    # Let's re-evaluate based on the example's description:
    