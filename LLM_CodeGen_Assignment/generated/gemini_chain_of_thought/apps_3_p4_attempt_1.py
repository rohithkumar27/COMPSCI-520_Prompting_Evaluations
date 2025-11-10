from typing import List
from collections import defaultdict
# Gemini solution using chain_of_thought (Attempt 1/3)
# Dataset: APPS
# Problem: APPS/3
# Difficulty: Hard

def count_divisible_subarrays(arr: List[int], k: int) -> int:
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
    # Edge case: empty array
    if not arr:
        return 0
    
    # Edge case: k is 0 or 1
    if k == 0:
        return 0
    
    if k == 1:
        # All subarrays are divisible by 1
        n = len(arr)
        return n * (n + 1) // 2
    
    # Edge case: single element
    if len(arr) == 1:
        return 1 if arr[0] % k == 0 else 0
    
    # Use prefix sum with modular arithmetic
    # If two prefix sums have the same remainder when divided by k,
    # the subarray between them has sum divisible by k
    
    mod_count = defaultdict(int)
    mod_count[0] = 1  # Empty prefix has sum 0
    
    prefix_sum = 0
    result = 0
    
    for num in arr:
        prefix_sum += num
        
        # Handle negative remainders
        remainder = prefix_sum % k
        if remainder < 0:
            remainder += k
        
        # Count how many previous prefix sums had the same remainder
        result += mod_count[remainder]
        
        # Add current remainder to the count
        mod_count[remainder] += 1
    
    return result
