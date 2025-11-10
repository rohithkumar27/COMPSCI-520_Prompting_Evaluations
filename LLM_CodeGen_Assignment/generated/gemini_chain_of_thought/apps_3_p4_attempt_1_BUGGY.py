from typing import List
from collections import defaultdict
# BUGGY VERSION - For fault detection testing
# Bug 1: Off-by-one in k=1 formula (missing +1)
# Bug 2: Wrong initialization of mod_count (started at 0 instead of 1)

def count_divisible_subarrays(arr: List[int], k: int) -> int:
    '''
    Given an array of integers and a number K, count the number of subarrays
    whose sum is divisible by K.
    '''
    # Edge case: empty array
    if not arr:
        return 0
    
    # Edge case: k is 0 or 1
    if k == 0:
        return 0
    
    # BUG 1: Off-by-one error in k=1 formula
    # Missing the +1 in the formula
    if k == 1:
        # All subarrays are divisible by 1
        n = len(arr)
        return n * (n - 1) // 2  # ORIGINAL: return n * (n + 1) // 2
    
    # Edge case: single element
    if len(arr) == 1:
        return 1 if arr[0] % k == 0 else 0
    
    # Use prefix sum with modular arithmetic
    # If two prefix sums have the same remainder when divided by k,
    # the subarray between them has sum divisible by k
    
    mod_count = defaultdict(int)
    # BUG 2: Wrong initialization - should be 1 for empty prefix
    mod_count[0] = 0  # ORIGINAL: mod_count[0] = 1
    
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
