# Part 2: New Complex Problems - Baseline Coverage

**Generated:** 2025-11-10  
**Purpose:** Demonstrate iterative test generation with complex problems

---

## Problem Selection Rationale

We selected 2 new complex problems from the APPS dataset that have:
1. **More complex logic** with multiple branches and edge cases
2. **Lower baseline coverage** (40-70%) to show meaningful improvement
3. **Real-world algorithmic challenges** (DP, modular arithmetic)

---

## Problem 1: apps_3_p4_attempt_1.py - Count Divisible Subarrays

### Problem Description
Count the number of subarrays whose sum is divisible by K using prefix sum and modular arithmetic.

### Algorithm Complexity
- Uses hash map (defaultdict) for tracking remainders
- Handles edge cases: empty array, k=0, k=1, single element, negative remainders
- Time Complexity: O(n)
- Space Complexity: O(k)

### Baseline Test (Iteration 0)
```python
def test_divisible_subarrays():
    """Minimal baseline test - only 1 simple test case."""
    arr1 = [4, 5, 0, -2, -3, 1]
    result = count_divisible_subarrays(arr1, 5)
    assert result == 7
```

### Baseline Coverage Metrics

**Line Coverage:** 69% (18/24 statements)
- **Covered:** 18 statements
- **Missed:** 6 statements

**Branch Coverage:** 58% (7/12 branches)
- **Covered:** 7 branches
- **Partial:** 5 branches
- **Missed:** 5 branches

### Uncovered Edge Cases

1. **Empty array** - Line 22: `if not arr: return 0`
2. **k == 0** - Line 25-26: `if k == 0: return 0`
3. **k == 1** - Lines 28-31: All subarrays divisible by 1
4. **Single element** - Lines 34-35: Single element array
5. **Negative remainders** - Lines 48-50: Handling negative modulo

### Improvement Potential

**Target Coverage:** 95%+ line and branch coverage

**Missing Test Scenarios:**
- Empty array input
- k = 0 (invalid divisor)
- k = 1 (all subarrays valid)
- Single element arrays (divisible and non-divisible)
- Arrays with negative numbers (negative remainder handling)
- Arrays where no subarrays are divisible

---

## Problem 2: apps_2_p3_attempt_1.py - Count Valid Parentheses Sequences

### Problem Description
Count ways to replace '?' characters in a string to form valid parentheses sequences.

### Algorithm Complexity
- Uses dynamic programming with memoization
- Recursive approach tracking open parentheses count
- Handles '(', ')', and '?' characters
- Time Complexity: O(n²)
- Space Complexity: O(n²)

### Current Status
⚠️ **Implementation has bugs** - baseline tests are failing

**Test Result:** FAILED
```
AssertionError: Expected 1, got 0
```

### Next Steps for Problem 2
1. Fix the implementation to pass baseline tests
2. Measure baseline coverage
3. Identify uncovered branches
4. Generate iterative test improvements

---

## Recommended Workflow for Part 2

### For Problem 1 (apps_3_p4_attempt_1.py) - READY

**Iteration 0 (Baseline):**
- Coverage: 69% line, 58% branch
- Tests: 1 basic test case
- Status: ✅ Ready for iterative improvement

**Iteration 1:**
- Add tests for edge cases (empty array, k=0, k=1)
- Target: 80-85% coverage

**Iteration 2:**
- Add tests for single element and negative numbers
- Target: 90-95% coverage

**Iteration 3:**
- Add tests for boundary conditions and stress cases
- Target: 95%+ coverage

### For Problem 2 (apps_2_p3_attempt_1.py) - NEEDS FIX

**Current Status:** Implementation needs debugging
**Action Required:** Fix algorithm before proceeding with test generation

---

## Summary

✅ **Problem 1 (Count Divisible Subarrays):**
- Baseline: 69% line, 58% branch coverage
- 6 missed statements, 5 partial branches
- Excellent candidate for demonstrating iterative test generation
- Clear path to 95%+ coverage through systematic edge case testing

⚠️ **Problem 2 (Valid Parentheses):**
- Implementation has bugs
- Needs fixing before coverage analysis
- Will be good second problem once fixed

**Recommendation:** Start Part 2 iterations with Problem 1 (apps_3_p4_attempt_1.py) as it's ready and has ideal baseline coverage for demonstration.

---

## Files Created

1. `generated/gemini_chain_of_thought/apps_3_p4_attempt_1.py` - Source code
2. `generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1.py` - Baseline test
3. `generated/gemini_chain_of_thought/apps_2_p3_attempt_1.py` - Source code (needs fix)
4. `generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1.py` - Baseline test (failing)

---

*Use Problem 1 for your Part 2 assignment to demonstrate the iterative LLM-assisted test generation process!*
