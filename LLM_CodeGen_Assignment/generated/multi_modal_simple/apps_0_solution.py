# Multi-Modal Solution (Groq + Gemini)
# Problem: APPS/0
# Generated: 2025-10-22 19:46:19

import math
from typing import Any

def solve_knapsack_variant(n, w, k, items):
    """
    Solves the knapsack variant problem with item type limit using dynamic programming
    with binary splitting for improved efficiency.

    You are given N item types, each with a weight w[i] and value v[i].
    You have a knapsack with capacity W.
    You can take at most K items of each type.

    Find the maximum value you can achieve.

    Parameters:
    - n: number of item types (Note: len(items) is used internally for robustness)
    - w: knapsack capacity
    - k: max items per type
    - items: list of (weight, value) tuples

    Returns:
    - The maximum value achievable.
    """
    # --- Input Validation and Edge Cases ---
    if w < 0 or k < 0:
        raise ValueError("Knapsack capacity (w) and max items per type (k) cannot be negative.")
    
    # If there are no items, no capacity, or no items can be taken, max value is 0.
    # We use len(items) as the definitive source for the number of item types.
    if len(items) == 0 or w == 0 or k == 0:
        return 0

    # --- Step 1: Transform Bounded Knapsack Items into 0/1 Knapsack Meta-Items ---
    # This uses binary splitting. Each item type with a limit 'k' is decomposed
    # into several "meta-items" that can be chosen at most once (0/1).
    # For example, if k=10, we create meta-items representing 1, 2, 4, and 3 (10 - 1 - 2 - 4) items.
    # Any number of items from 1 to 10 can be formed by combining these meta-items.
    
    transformed_items = []
    for item_weight_orig, item_value_orig in items:
        # Item weights cannot be negative, as this implies adding capacity, which is typically not allowed
        # in standard knapsack problems.
        if item_weight_orig < 0:
            raise ValueError(f"Item weight cannot be negative: {item_weight_orig}")

        count_remaining = k
        power_of_2_batch_size = 1

        while count_remaining > 0:
            # Determine the size of the current batch (power of 2 or the remainder)
            num_to_add = min(power_of_2_batch_size, count_remaining)
            
            # Create a meta-item for this batch
            batch_weight = num_to_add * item_weight_orig
            batch_value = num_to_add * item_value_orig
            
            # Add the meta-item to our list. Zero-weight meta-items are handled correctly
            # by the 0/1 knapsack DP (their value will be added to all reachable states).
            transformed_items.append((batch_weight, batch_value))
            
            # Update remaining count and prepare for the next power of 2
            count_remaining -= num_to_add
            power_of_2_batch_size *= 2

    # --- Step 2: Solve the 0/1 Knapsack Problem with the Transformed Meta-Items ---
    # dp[j] will store the maximum value achievable for a knapsack of capacity 'j'.
    dp = [0] * (w + 1)

    for item_weight, item_value in transformed_items:
        # Iterate capacity downwards to ensure each meta-item is used at most once.
        # This is the standard procedure for 1D DP in 0/1 knapsack problems.
        # If item_weight is 0, the range effectively processes all capacities from 'w' down to 0,
        # correctly adding the item's value to all states without consuming capacity.
        for current_capacity in range(w, item_weight - 1, -1):
            dp[current_capacity] = max(dp[current_capacity], dp[current_capacity - item_weight] + item_value)

    # The maximum value for the full knapsack capacity 'w' is our result.
    return dp[w]