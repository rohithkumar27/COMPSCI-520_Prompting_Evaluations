# Enhanced Gemini solution using enhanced_gemini_step_chain_of_thought (Attempt 1/3)
# Dataset: Enhanced
# Problem: APPS/0
# Difficulty: Enhanced

from typing import List

def solve_knapsack_variant(n, w, k, items):
    # Initialize DP array
    dp = [0] * (w + 1)
    
    # For each item type
    for weight, value in items:
        # Iterate through capacities in reverse order
        for capacity in range(w, -1, -1):
            # Try taking 1, 2, ..., k items of current type
            for count in range(1, k + 1):
                current_weight = count * weight
                current_value = count * value
                
                # If we can fit 'count' items
                if capacity >= current_weight:
                    dp[capacity] = max(dp[capacity], dp[capacity - current_weight] + current_value)
    
    return dp[w]