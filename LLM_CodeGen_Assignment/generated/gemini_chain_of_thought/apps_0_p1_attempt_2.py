from typing import List
# Gemini solution using chain_of_thought (Attempt 2/3)
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
    # "unroll" each item type into k individual items.
    # For example, if we have item type (w_i, v_i) and k=2, we can think of
    # it as two separate items: (w_i, v_i) and (w_i, v_i).
    # However, this can lead to a large number of items if k is large.
    # A more efficient approach for bounded knapsack is to use dynamic programming.

    # dp[i][j] will store the maximum value that can be obtained with a knapsack
    # of capacity j using the first i item types.
    # However, since we can take multiple items of the same type, a standard
    # 0/1 knapsack DP won't directly work.

    # We can transform this into a 0/1 knapsack problem by considering each
    # item type and the number of copies we can take.
    # For each item type (weight, value), we can take 0, 1, 2, ..., k copies.
    # This can be further optimized by using binary splitting for the number of items.
    # For example, if k=7, we can represent 7 as 1 + 2 + 4. So, instead of
    # considering 7 copies of an item, we can consider items with weights
    # 1*w, 2*w, 4*w and corresponding values 1*v, 2*v, 4*v. This reduces the
    # number of effective items to O(N log K).

    # Let's create a new list of "effective" items.
    effective_items = []
    for weight, value in items:
        count = 1
        while k > 0:
            take = min(count, k)
            effective_items.append((weight * take, value * take))
            k -= take
            count *= 2
        k = k # reset k for the next item type

    # Now, we have a list of items where each item can be taken at most once.
    # This is a standard 0/1 knapsack problem.
    # dp[j] will store the maximum value for a knapsack of capacity j.
    dp = [0] * (W + 1)

    for item_weight, item_value in effective_items:
        # Iterate from W down to item_weight to avoid using an item multiple times
        # within the same capacity calculation.
        for current_W in range(W, item_weight - 1, -1):
            dp[current_W] = max(dp[current_W], dp[current_W - item_weight] + item_value)

    return dp[W]
