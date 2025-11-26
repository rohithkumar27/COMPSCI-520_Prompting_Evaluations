"""
Exercise 3 - Part 1: Generated Assertions for Problem 2
Problem: Count Divisible Subarrays

These assertions were generated based on the problem description.
They represent formal specifications of the function's behavior.

Let 'res' denote the expected return value of count_divisible_subarrays(arr, k).
"""

# Specification 1: Empty array returns 0
assert (len(arr) == 0 and res == 0) or (len(arr) > 0 and res >= 0)

# Specification 2: k=0 returns 0 (division by zero)
assert (k == 0 and res == 0) or (k != 0 and res >= 0)

# Specification 3: k=1 means all subarrays are divisible
assert (k == 1 and res == len(arr) * (len(arr) + 1) // 2) or (k != 1 and res >= 0)

# Specification 4: Result must be non-negative
assert res >= 0

# Specification 5: Result cannot exceed total possible subarrays
assert res <= len(arr) * (len(arr) + 1) // 2

# Specification 6: Single element divisible by k returns 1
# INCORRECT: Doesn't handle k=0 case (division by zero)
assert (len(arr) == 1 and arr[0] % k == 0 and res == 1) or (len(arr) != 1 and res >= 0)

# Specification 7: Array of all zeros returns n*(n+1)/2
# INCORRECT: Doesn't check k > 0, and uses side effect (sum function modifies state)
assert (all(x == 0 for x in arr) and len(arr) > 0 and res == len(arr) * (len(arr) + 1) // 2) or (not all(x == 0 for x in arr) or len(arr) == 0)
