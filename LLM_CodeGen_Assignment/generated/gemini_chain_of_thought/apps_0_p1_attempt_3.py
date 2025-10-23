# Gemini solution using chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: APPS/0
# Difficulty: Hard

def solve_knapsack_variant(n: int, W: int, k: int, items: List[tuple[int, int]]) -> int:
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

    # This problem can be modeled as a bounded knapsack problem.
    # Since we can take at most k items of each type, we can effectively
    # treat each item type as having k individual items.
    # However, a more efficient approach for bounded knapsack is to use
    # dynamic programming.

    # dp[i][j] will store the maximum value that can be obtained with a
    # knapsack of capacity j using the first i item types.
    # We can optimize space by using only one row for DP.
    # dp[j] will store the maximum value for a knapsack of capacity j.

    dp = [0] * (W + 1)

    # Iterate through each item type
    for i in range(n):
        weight_i, value_i = items[i]

        # For each item type, we can take 1 to k items.
        # We can use a nested loop to consider taking 1, 2, ..., k items of the current type.
        # However, this can be optimized. The standard bounded knapsack DP
        # iterates through the capacity from W down to the item's weight.
        # To handle the "at most k" constraint, we can think of it as
        # having k copies of each item. A more efficient way to handle
        # the bounded knapsack is to use binary splitting or a queue-based optimization.
        # For simplicity and clarity, let's consider the direct DP approach first,
        # which might be O(n * W * k) if not optimized.

        # A common optimization for bounded knapsack is to convert it to an
        # unbounded knapsack problem by creating multiple copies of items,
        # or by using binary splitting.
        # For this problem, since k is relatively small, we can iterate through
        # the number of items of the current type we can take.

        # Let's use the standard 0/1 knapsack DP approach but adapt it for the bounded case.
        # For each item type, we can consider taking 1, 2, ..., k of them.
        # This can be done by iterating through the capacity from W down to 0.
        # For each capacity `cap`, we consider taking `num_items` of the current item.
        # `num_items` can range from 1 to `k`.
        # The total weight of `num_items` of item `i` is `num_items * weight_i`.
        # The total value is `num_items * value_i`.

        # We need to be careful not to use the same item multiple times within the
        # same capacity calculation for the current item type.
        # The standard DP for 0/1 knapsack iterates from W down to weight.
        # For bounded knapsack, we can iterate through the number of items of the current type.

        # Let's consider the DP state as dp[j] = max value for capacity j.
        # When considering item `i` with weight `w_i` and value `v_i`, and we can take at most `k` of them.
        # For each capacity `j` from `W` down to `0`:
        # We can try to add `m`