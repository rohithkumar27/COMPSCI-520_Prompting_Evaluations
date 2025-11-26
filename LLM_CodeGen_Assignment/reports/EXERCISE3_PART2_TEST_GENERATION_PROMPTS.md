# Exercise 3 - Part 2: Test Generation Prompts

## Overview

This document contains the exact prompts used to generate specification-guided test cases from the corrected formal specifications in Part 1.

---

## Problem 1: Count Valid Parentheses Sequences (APPS/2)

### LLM Prompt for Test Generation

```
Based on the following CORRECTED formal specifications from Part 1, generate comprehensive test cases for the function:

def count_valid_parentheses_sequences(s: str) -> int

CORRECTED SPECIFICATIONS (from Part 1):

# Specification 1: Empty string returns exactly 1
assert (s == "" and res == 1) or (s != "" and res >= 0)

# Specification 2: Odd length strings must return 0
assert (len(s) % 2 == 1 and res == 0) or (len(s) % 2 == 0 and res >= 0)

# Specification 3: String starting with ')' must return 0
assert (len(s) > 0 and s[0] == ')' and res == 0) or (len(s) == 0 or s[0] != ')' and res >= 0)

# Specification 4: String ending with '(' must return 0
assert (len(s) > 0 and s[-1] == '(' and res == 0) or (len(s) == 0 or s[-1] != '(' and res >= 0)

# Specification 5: Result must be in valid range [0, 10^9+7)
assert 0 <= res < 10**9 + 7

# Specification 6: String with no '?' has at most 1 valid way
assert ('?' not in s and res <= 1) or ('?' in s and res >= 0)

# Specification 7 (CORRECTED): String of ALL '?' with even length has at least 1 way
assert (all(c == '?' for c in s) and len(s) > 0 and len(s) % 2 == 0 and res >= 1) or (not all(c == '?' for c in s) or len(s) == 0 or len(s) % 2 == 1)

# Specification 8 (CORRECTED): String with only '(' characters returns 0
assert (len(s) > 0 and all(c == '(' for c in s) and res == 0) or (len(s) == 0 or not all(c == '(' for c in s) and res >= 0)

YOUR TASK:

Generate test cases that verify each specification. Each test should:
1. Have a descriptive name indicating which specification it tests (e.g., test_spec1_empty_string)
2. Include a docstring explaining what specification is being verified
3. Call the function with appropriate input
4. Assert the expected behavior based on the specification
5. Include clear, simple inputs that directly test the specification

REQUIREMENTS:
- Generate 2-3 test cases per specification to cover variations
- Include edge cases for each specification
- Add a few additional tests for complex scenarios not covered by individual specs
- Use clear, descriptive test names
- Include assertion messages for better debugging

FORMAT:
```python
def test_spec1_empty_string():
    """Specification 1: Empty string returns exactly 1"""
    result = count_valid_parentheses_sequences("")
    assert result == 1, f"Expected 1 for empty string, got {result}"

def test_spec2_odd_length_three():
    """Specification 2: Odd length strings must return 0"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0, f"Expected 0 for odd length '(((', got {result}"

# ... continue for all specifications
```

Generate approximately 20-25 test cases total.
```

---

## Problem 2: Count Divisible Subarrays (APPS/3)

### LLM Prompt for Test Generation

```
Based on the following CORRECTED formal specifications from Part 1, generate comprehensive test cases for the function:

def count_divisible_subarrays(arr: List[int], k: int) -> int

CORRECTED SPECIFICATIONS (from Part 1):

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

# Specification 6 (CORRECTED): Single element divisible by k returns 1 (when k != 0)
assert (len(arr) == 1 and k != 0 and arr[0] % k == 0 and res == 1) or (len(arr) != 1 or k == 0 and res >= 0)

# Specification 7 (CORRECTED): Array of all zeros with k > 0 returns n*(n+1)/2
assert (all(x == 0 for x in arr) and len(arr) > 0 and k > 0 and res == len(arr) * (len(arr) + 1) // 2) or (not all(x == 0 for x in arr) or len(arr) == 0 or k <= 0)

YOUR TASK:

Generate test cases that verify each specification. Each test should:
1. Have a descriptive name indicating which specification it tests (e.g., test_spec1_empty_array)
2. Include a docstring explaining what specification is being verified
3. Call the function with appropriate input
4. Assert the expected behavior based on the specification
5. Include clear, simple inputs that directly test the specification

REQUIREMENTS:
- Generate 2-3 test cases per specification to cover variations
- Include edge cases for each specification
- Add a few additional tests for complex scenarios not covered by individual specs
- Use clear, descriptive test names
- Include assertion messages for better debugging
- Pay special attention to the CORRECTED specifications (6 and 7) which now include k != 0 and k > 0 checks

FORMAT:
```python
def test_spec1_empty_array():
    """Specification 1: Empty array returns 0"""
    result = count_divisible_subarrays([], 5)
    assert result == 0, f"Expected 0 for empty array, got {result}"

def test_spec2_k_zero():
    """Specification 2: k=0 returns 0"""
    result = count_divisible_subarrays([1, 2, 3], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"

def test_spec6_single_element_with_k_zero():
    """Specification 6 (CORRECTED): Single element with k=0 returns 0"""
    # This tests the correction - we added k != 0 check
    result = count_divisible_subarrays([5], 0)
    assert result == 0, f"Expected 0 for k=0, got {result}"

# ... continue for all specifications
```

Generate approximately 20-25 test cases total.
```

---

## Key Differences from Part 1 Prompts

### Part 1 (Specification Generation):
- **Input:** Problem description + method signature
- **Output:** Formal specifications as assertions
- **Goal:** Define behavioral requirements
- **Constraints:** No function calls, no side effects, pure logic only

### Part 2 (Test Generation):
- **Input:** Corrected formal specifications from Part 1
- **Output:** Executable test functions
- **Goal:** Verify specifications are met by implementation
- **Constraints:** Must call the function, must have assertions

---

## Prompt Design Rationale

### 1. Include Corrected Specifications
- Shows which specifications were fixed in Part 1
- Highlights the corrections (e.g., k != 0 check)
- Ensures tests verify the corrected behavior

### 2. Clear Requirements
- 2-3 tests per specification for coverage
- Descriptive names linked to specifications
- Assertion messages for debugging

### 3. Format Examples
- Provides concrete examples of expected output
- Shows naming convention (test_specN_description)
- Demonstrates docstring format

### 4. Emphasis on Corrections
- Explicitly mentions CORRECTED specifications
- Asks for tests that verify the corrections
- Example: test_spec6_single_element_with_k_zero() tests the k != 0 fix

---

## Generated Test Files

### Problem 1 Output:
**File:** `test_apps_2_spec_guided_final.py`
- **Tests Generated:** 24
- **Specifications Covered:** All 8 specifications
- **Additional Tests:** 3 edge cases

### Problem 2 Output:
**File:** `test_apps_3_spec_guided_final.py`
- **Tests Generated:** 22
- **Specifications Covered:** All 7 specifications
- **Additional Tests:** 4 edge cases

---

## Test Generation Strategy

### For Each Specification:

1. **Basic Test:** Simple, direct test of the specification
   ```python
   def test_spec1_empty_array():
       result = count_divisible_subarrays([], 5)
       assert result == 0
   ```

2. **Variation Test:** Different input that tests same specification
   ```python
   def test_spec2_k_zero_with_zeros():
       result = count_divisible_subarrays([0, 0, 0], 0)
       assert result == 0
   ```

3. **Edge Case Test:** Boundary condition for the specification
   ```python
   def test_spec6_single_element_with_k_zero():
       # Tests the CORRECTED specification with k=0
       result = count_divisible_subarrays([5], 0)
       assert result == 0
   ```

### Additional Tests:

Tests for scenarios not covered by individual specifications:
- Complex combinations of conditions
- Real-world examples from problem description
- Boundary cases between specifications

---

## Comparison with Exercise 2 Test Generation

| Aspect | Exercise 2 (Coverage-Driven) | Exercise 3 (Spec-Guided) |
|--------|----------------------------|--------------------------|
| **Input** | Coverage report (uncovered lines) | Formal specifications |
| **Approach** | Target specific uncovered branches | Verify all specifications |
| **Focus** | Implementation coverage | Behavioral correctness |
| **Prompt** | "Generate tests for uncovered lines X, Y, Z" | "Generate tests for specifications 1-8" |
| **Output** | Tests targeting specific code paths | Tests verifying requirements |

---

## Effectiveness Analysis

### Problem 1 (APPS/2):
- **Specifications:** 8
- **Tests Generated:** 24
- **Coverage Achieved:** 97% stmt, 97% branch
- **Improvement:** +2% stmt, +4% branch from Exercise 2
- **Effectiveness:** ✅ High - Improved coverage through systematic testing

### Problem 2 (APPS/3):
- **Specifications:** 7
- **Tests Generated:** 22
- **Coverage Achieved:** 94% stmt, 92% branch
- **Improvement:** No change from Exercise 2
- **Effectiveness:** ⚪ Moderate - Same ceiling, but better documentation

---

## Lessons Learned

### What Worked Well:
1. ✅ Including corrected specifications in the prompt
2. ✅ Asking for 2-3 tests per specification
3. ✅ Providing format examples
4. ✅ Emphasizing the corrections from Part 1

### What Could Be Improved:
1. ⚠️ Could ask for more complex combination tests
2. ⚠️ Could request tests for specification interactions
3. ⚠️ Could specify coverage goals explicitly

### Key Insight:
Specification-guided test generation is most effective when:
- Specifications are correct (hence the Part 1 evaluation step)
- Tests systematically cover all specifications
- Additional tests explore specification interactions
- Clear examples guide the LLM's output format

---

## Files Referenced

### Input Files (Part 1):
- `assertions_problem1_raw.py` - Raw specifications
- `assertions_problem2_raw.py` - Raw specifications
- `EXERCISE3_PART1_COMPLETED_FINAL.md` - Corrected specifications

### Output Files (Part 2):
- `test_apps_2_spec_guided_final.py` - Generated tests
- `test_apps_3_spec_guided_final.py` - Generated tests

### Coverage Reports:
- `coverage_reports/spec_guided_apps2/index.html`
- `coverage_reports/spec_guided_apps3/index.html`

---

**Document Purpose:** For PDF submission - shows the exact prompts used in Part 2 to generate test cases from specifications.
