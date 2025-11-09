from typing import List
# Gemini solution using chain_of_thought (Attempt 1/3)
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

    # This problem can be modeled as a variation of the unbounded knapsack problem,
    # but with a limit on the number of items of each type.
    # We can transform this into a 0/1 knapsack problem by "unrolling" the items.
    # For each item type (weight_i, value_i), we can take 0, 1, 2, ..., k of them.
    # This means we can consider k copies of each item type, each with the same weight and value.
    # However, this would lead to a very large number of items if k is large.

    # A more efficient approach is to use dynamic programming.
    # Let dp[i][j] be the maximum value that can be obtained using the first i item types
    # with a knapsack capacity of j.

    # The state transition would involve considering how many items of the i-th type we take.
    # dp[i][j] = max(dp[i-1][j - count * weight_i] + count * value_i) for count from 0 to k
    # such that j - count * weight_i >= 0.

    # We can optimize space by using only one row for DP.
    # Let dp[j] be the maximum value for a knapsack of capacity j.
    # When considering item type i (weight_i, value_i), we iterate through the knapsack
    # capacities from W down to 0.
    # For each capacity j, we consider taking 'count' items of type i.
    # dp[j] = max(dp[j], dp[j - count * weight_i] + count * value_i) for count from 1 to k.

    # Initialize DP table. dp[j] will store the maximum value for capacity j.
    dp = [0] * (W + 1)

    # Iterate through each item type
    for weight_i, value_i in items:
        # Iterate through knapsack capacities from W down to 0
        # We iterate downwards to ensure that when we update dp[j],
        # we are using values from the previous item type's calculations,
        # effectively simulating the dp[i-1] state.
        for j in range(W, -1, -1):
            # Consider taking 'count' items of the current type
            for count in range(1, k + 1):
                current_weight = count * weight_i
                current_value = count * value_i

                # If taking 'count' items of the current type does not exceed capacity j
                if j >= current_weight:
                    # Update dp[j] by considering the possibility of taking 'count' items
                    # of the current type. The value would be the value obtained from
                    # the remaining capacity (j - current_weight) plus the value of
                    # the 'count' items.
                    dp[j] = max(dp[j], dp[j - current_weight] + current_value)
                else:
                    # If taking 'count' items exceeds capacity j, we can't take more
                    # of this item type for this capacity, so break the inner loop.
                    break

    # The maximum