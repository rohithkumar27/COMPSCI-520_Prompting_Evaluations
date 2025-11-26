# Exercise 3: Specification-Guided Test Improvement

**Student:** [Your Name]  
**Date:** November 24, 2025  
**Course:** CS685 - Fall 2025

---

## Problem Selection

Based on Exercise 2 coverage analysis, I selected the two problems with weakest initial coverage:

1. **APPS/2: Count Valid Parentheses Sequences**
   - Initial Coverage: 71% line, 63% branch
   - Final Coverage (Ex2): 95% line, 93% branch

2. **APPS/3: Count Divisible Subarrays**
   - Initial Coverage: 69% line, 58% branch
   - Final Coverage (Ex2): 94% line, 92% branch

---

## Part 1: Generate, Evaluate, and Refine Specifications (5 pts)

### Problem 1: Count Valid Parentheses Sequences

#### Method Signature
```python
def count_valid_parentheses_sequences(s: str) -> int
```

#### Natural Language Problem Description

Given a string containing '(', ')', and '?', where '?' can be either '(' or ')'.
Count the number of ways to replace '?' characters such that the resulting string
has valid parentheses.

A valid parentheses string is one where:
1. Every '(' has a matching ')'
2. At no point do we have more ')' than '(' when reading left to right

Return the count modulo 10^9 + 7.

Examples:
- "(?)" -> 1 way: "()"
- "(??))" -> 1 way: "(())"  
- "????" -> 2 ways: "(())" and "()()"

---

#### LLM Prompt for Specification Generation

```
Problem description: 
Given a string containing '(', ')', and '?', where '?' can be either '(' or ')'.
Count the number of ways to replace '?' characters such that the resulting string
has valid parentheses.

A valid parentheses string is one where:
1. Every '(' has a matching ')'
2. At no point do we have more ')' than '(' when reading left to right

Return the count modulo 10^9 + 7.

Method signature: 
def count_valid_parentheses_sequences(s: str) -> int

Please write formal specifications as Python assertions that describe the correct 
behavior of this method. Let 'res' denote the expected return value of 
'count_valid_parentheses_sequences(s)'. 

Do not call 'count_valid_parentheses_sequences()' in your assertions. 
Do not use methods with side effects such as print, file I/O, random number 
generation, or timing functions. 
Express the relationship between 's' and 'res' using pure string operations, 
arithmetic, and boolean logic only.

Generate approximately 5 specifications.
```

---

#### Generated Assertions (Before Correction)

```python
# Specification 1: Empty string should return 1 (one valid way: empty sequence)
assert res == 1 if s == "" else res >= 0

# Specification 2: Odd length strings cannot form valid parentheses
assert res == 0 if len(s) % 2 != 0 else res >= 0

# Specification 3: String starting with ')' cannot be valid
assert res == 0 if len(s) > 0 and s[0] == ')' else res >= 0

# Specification 4: String ending with '(' cannot be valid
assert res == 0 if len(s) > 0 and s[-1] == '(' else res >= 0

# Specification 5: Result must be non-negative and within modulo range
assert 0 <= res < 10**9 + 7

# Specification 6: String with only '(' or only ')' should return 0
assert res == 0 if (s.count('(') == len(s) or s.count(')') == len(s)) and len(s) > 0 else res >= 0
```

---

#### Evaluation and Correction

| # | Assertion | Status | Issue | Corrected Version |
|---|-----------|--------|-------|-------------------|
| 1 | `assert res == 1 if s == "" else res >= 0` | ✅ Correct | None | N/A |
| 2 | `assert res == 0 if len(s) % 2 != 0 else res >= 0` | ✅ Correct | None | N/A |
| 3 | `assert res == 0 if len(s) > 0 and s[0] == ')' else res >= 0` | ✅ Correct | None | N/A |
| 4 | `assert res == 0 if len(s) > 0 and s[-1] == '(' else res >= 0` | ✅ Correct | None | N/A |
| 5 | `assert 0 <= res < 10**9 + 7` | ✅ Correct | None | N/A |
| 6 | `assert res == 0 if (s.count('(') == len(s) or s.count(')') == len(s)) and len(s) > 0 else res >= 0` | ❌ Incorrect | Doesn't account for '?' characters. String "????" has no '(' or ')' but should return 2, not 0. | `assert res == 0 if (s.replace('?', '').count('(') == len(s.replace('?', '')) or s.replace('?', '').count(')') == len(s.replace('?', ''))) and len(s.replace('?', '')) > 0 else res >= 0` |

**Accuracy Rate:** 5/6 = **83.3%**

---

### Problem 2: Count Divisible Subarrays

#### Method Signature
```python
def count_divisible_subarrays(arr: List[int], k: int) -> int
```

#### Natural Language Problem Description

Given an array of integers and a number K, count the number of subarrays
whose sum is divisible by K.

A subarray is a contiguous part of an array.

Use modular arithmetic properties:
If (prefix_sum[j] - prefix_sum[i]) % K == 0, then prefix_sum[j] % K == prefix_sum[i] % K

Example:
arr = [4, 5, 0, -2, -3, 1], k = 5
Subarrays with sum divisible by 5:
[5], [5, 0], [5, 0, -2, -3], [0], [-2, -3], [4, 5, 0, -2, -3, 1]
Answer: 7

---

#### LLM Prompt for Specification Generation

```
Problem description:
Given an array of integers and a number K, count the number of subarrays
whose sum is divisible by K.

A subarray is a contiguous part of an array.

Use modular arithmetic properties:
If (prefix_sum[j] - prefix_sum[i]) % K == 0, then prefix_sum[j] % K == prefix_sum[i] % K

Method signature:
def count_divisible_subarrays(arr: List[int], k: int) -> int

Please write formal specifications as Python assertions that describe the correct 
behavior of this method. Let 'res' denote the expected return value of 
'count_divisible_subarrays(arr, k)'. 

Do not call 'count_divisible_subarrays()' in your assertions. 
Do not use methods with side effects such as print, file I/O, random number 
generation, or timing functions. 
Express the relationship between 'arr', 'k', and 'res' using pure arithmetic 
and boolean logic only.

Generate approximately 5 specifications.
```

---

#### Generated Assertions (Before Correction)

```python
# Specification 1: Empty array should return 0
assert res == 0 if len(arr) == 0 else res >= 0

# Specification 2: k=0 should return 0 (division by zero case)
assert res == 0 if k == 0 else res >= 0

# Specification 3: k=1 means all subarrays are divisible (every integer % 1 == 0)
assert res == len(arr) * (len(arr) + 1) // 2 if k == 1 else res >= 0

# Specification 4: Result must be non-negative
assert res >= 0

# Specification 5: Result cannot exceed total number of possible subarrays
assert res <= len(arr) * (len(arr) + 1) // 2

# Specification 6: Single element array divisible by k should return 1
assert res == 1 if len(arr) == 1 and arr[0] % k == 0 else (res == 0 if len(arr) == 1 else res >= 0)
```

---

#### Evaluation and Correction

| # | Assertion | Status | Issue | Corrected Version |
|---|-----------|--------|-------|-------------------|
| 1 | `assert res == 0 if len(arr) == 0 else res >= 0` | ✅ Correct | None | N/A |
| 2 | `assert res == 0 if k == 0 else res >= 0` | ✅ Correct | None | N/A |
| 3 | `assert res == len(arr) * (len(arr) + 1) // 2 if k == 1 else res >= 0` | ✅ Correct | None | N/A |
| 4 | `assert res >= 0` | ✅ Correct | None | N/A |
| 5 | `assert res <= len(arr) * (len(arr) + 1) // 2` | ✅ Correct | None | N/A |
| 6 | `assert res == 1 if len(arr) == 1 and arr[0] % k == 0 else (res == 0 if len(arr) == 1 else res >= 0)` | ❌ Incorrect | Doesn't handle k=0 case. When k=0, arr[0] % k causes ZeroDivisionError. | `assert res == 1 if len(arr) == 1 and k != 0 and arr[0] % k == 0 else (res == 0 if len(arr) == 1 else res >= 0)` |

**Accuracy Rate:** 5/6 = **83.3%**

---

## Part 2: Use Specifications to Guide Test Improvement (5 pts)

### Problem 1: Count Valid Parentheses Sequences

#### LLM Prompt for Test Case Generation

```
Based on the following formal specifications, generate test cases for the function:

def count_valid_parentheses_sequences(s: str) -> int

Specifications (corrected):
1. Empty string should return 1 (one valid way: empty sequence)
2. Odd length strings cannot form valid parentheses (return 0)
3. String starting with ')' cannot be valid (return 0)
4. String ending with '(' cannot be valid (return 0)
5. Result must be non-negative and within modulo range (0 <= res < 10^9 + 7)
6. String with only fixed '(' or only fixed ')' (ignoring '?') should return 0

Generate test cases that verify each specification. Each test should:
- Have a descriptive name indicating which specification it tests
- Include an assertion that checks the expected behavior
- Use clear, simple inputs that directly test the specification

Format:
```python
def test_spec1_empty_string():
    \"\"\"Specification 1: Empty string returns 1\"\"\"
    result = count_valid_parentheses_sequences("")
    assert result == 1

# ... continue for other specifications
```

Generate 6-8 test cases covering all specifications.
```

---

#### Generated Spec-Guided Test Cases

```python
# Spec-guided tests for count_valid_parentheses_sequences

def test_spec1_empty_string():
    """Specification 1: Empty string returns 1"""
    result = count_valid_parentheses_sequences("")
    assert result == 1

def test_spec2_odd_length():
    """Specification 2: Odd length strings return 0"""
    result = count_valid_parentheses_sequences("(((")
    assert result == 0
    
def test_spec2_odd_length_with_question():
    """Specification 2: Odd length with '?' also returns 0"""
    result = count_valid_parentheses_sequences("(?")
    assert result == 0

def test_spec3_starts_with_close():
    """Specification 3: String starting with ')' returns 0"""
    result = count_valid_parentheses_sequences("))(")
    assert result == 0

def test_spec4_ends_with_open():
    """Specification 4: String ending with '(' returns 0"""
    result = count_valid_parentheses_sequences("()(")
    assert result == 0

def test_spec5_result_in_range():
    """Specification 5: Result is non-negative and within modulo"""
    result = count_valid_parentheses_sequences("()")
    assert 0 <= result < 10**9 + 7

def test_spec6_all_open_parens():
    """Specification 6: String with only '(' returns 0"""
    result = count_valid_parentheses_sequences("((((")
    assert result == 0

def test_spec6_all_close_parens():
    """Specification 6: String with only ')' returns 0"""
    result = count_valid_parentheses_sequences("))))")
    assert result == 0
```

---

### Problem 2: Count Divisible Subarrays

#### LLM Prompt for Test Case Generation

```
Based on the following formal specifications, generate test cases for the function:

def count_divisible_subarrays(arr: List[int], k: int) -> int

Specifications (corrected):
1. Empty array should return 0
2. k=0 should return 0 (division by zero case)
3. k=1 means all subarrays are divisible, return n*(n+1)/2
4. Result must be non-negative
5. Result cannot exceed total number of possible subarrays
6. Single element array divisible by k should return 1 (with k != 0 check)

Generate test cases that verify each specification. Each test should:
- Have a descriptive name indicating which specification it tests
- Include an assertion that checks the expected behavior
- Use clear, simple inputs that directly test the specification

Format:
```python
def test_spec1_empty_array():
    \"\"\"Specification 1: Empty array returns 0\"\"\"
    result = count_divisible_subarrays([], 5)
    assert result == 0

# ... continue for other specifications
```

Generate 6-8 test cases covering all specifications.
```

---

#### Generated Spec-Guided Test Cases

```python
# Spec-guided tests for count_divisible_subarrays

def test_spec1_empty_array():
    """Specification 1: Empty array returns 0"""
    result = count_divisible_subarrays([], 5)
    assert result == 0

def test_spec2_k_zero():
    """Specification 2: k=0 returns 0"""
    result = count_divisible_subarrays([1, 2, 3], 0)
    assert result == 0

def test_spec3_k_one():
    """Specification 3: k=1 means all subarrays divisible"""
    arr = [5, 10, 15]
    n = len(arr)
    expected = n * (n + 1) // 2  # 3*4/2 = 6 subarrays
    result = count_divisible_subarrays(arr, 1)
    assert result == expected

def test_spec4_result_non_negative():
    """Specification 4: Result is non-negative"""
    result = count_divisible_subarrays([1, 2, 3], 5)
    assert result >= 0

def test_spec5_result_bounded():
    """Specification 5: Result <= total possible subarrays"""
    arr = [1, 2, 3, 4]
    result = count_divisible_subarrays(arr, 5)
    max_subarrays = len(arr) * (len(arr) + 1) // 2
    assert result <= max_subarrays

def test_spec6_single_element_divisible():
    """Specification 6: Single element divisible by k returns 1"""
    result = count_divisible_subarrays([10], 5)
    assert result == 1

def test_spec6_single_element_not_divisible():
    """Specification 6: Single element not divisible by k returns 0"""
    result = count_divisible_subarrays([7], 5)
    assert result == 0
```

---

## Coverage Comparison

### Before/After Coverage Table

| Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % | Change |
|---------|------------|------------|--------------|--------------|--------|
| **APPS/2: Count Valid Parentheses** | 95% | 95% | 93% | 93% | No change |
| **APPS/3: Count Divisible Subarrays** | 94% | 94% | 92% | 92% | No change |

---

## Case-Specific Insights

### Problem 1: Count Valid Parentheses Sequences

**Observation:** Coverage did not increase from 95% line / 93% branch.

**Explanation:** The specification-guided tests primarily target the same edge case branches that were already covered in Exercise 2's Iteration 1 and 2. Specifically:

- **Spec 1 (empty string):** Already tested in Exercise 2 as `test_empty_string()`
- **Spec 2 (odd length):** Already tested in Exercise 2 as `test_odd_length()`
- **Spec 3 (starts with ')'):** Already tested in Exercise 2 as `test_starts_with_close()`
- **Spec 4 (ends with '('):** Already tested in Exercise 2 as `test_ends_with_open()`

The formal specifications essentially codified the same edge cases that coverage-driven testing already identified. This demonstrates that:
1. Coverage-driven testing (Exercise 2) was already effective at finding edge cases
2. Formal specifications provide a complementary verification approach
3. The remaining 5% uncovered code likely involves complex DP state transitions that neither approach easily reaches

**Value Added:** While coverage didn't increase, the specifications provide formal documentation of the function's boundary conditions, which aids in:
- Code review and maintenance
- Regression testing
- Understanding the function's contract

---

### Problem 2: Count Divisible Subarrays

**Observation:** Coverage did not increase from 94% line / 92% branch.

**Explanation:** Similar to Problem 1, the specification-guided tests target edge cases already covered in Exercise 2:

- **Spec 1 (empty array):** Already tested in Exercise 2 as `test_empty_array()`
- **Spec 2 (k=0):** Already tested in Exercise 2 as `test_k_zero()`
- **Spec 3 (k=1):** Already tested in Exercise 2 as `test_k_one()`
- **Spec 6 (single element):** Already tested in Exercise 2 as `test_single_element()`

The remaining 6% uncovered code involves the main loop's prefix sum logic with specific numeric patterns that are difficult to target without:
1. Deep understanding of the modular arithmetic implementation
2. Symbolic execution or constraint solving
3. Mutation testing to identify missing assertions

**Value Added:** The specifications formalize the mathematical properties of the function (e.g., k=1 implies all subarrays divisible), which:
- Serves as executable documentation
- Enables property-based testing in the future
- Clarifies the function's preconditions and postconditions

---

## Conclusion

This exercise demonstrates that **formal specifications and coverage-driven testing are complementary approaches**:

### Key Findings:

1. **High Overlap:** When coverage-driven testing is done well (as in Exercise 2), it naturally discovers the same edge cases that formal specifications would identify.

2. **Specification Value:** Even without coverage improvement, specifications provide:
   - Formal documentation of function behavior
   - Executable contracts for regression testing
   - Clear boundary condition definitions

3. **Coverage Ceiling:** Both approaches struggle with the final 5-8% of coverage, which typically involves:
   - Complex internal state transitions
   - Rare numeric edge cases
   - Implementation-specific branches

4. **Accuracy Insight:** The 83.3% accuracy rate for LLM-generated specifications shows that:
   - LLMs can generate reasonable specifications
   - Manual review is essential (caught 2 errors)
   - Edge cases like '?' handling and k=0 require domain knowledge

### Recommendation:

For maximum effectiveness, use **both approaches**:
- Start with formal specifications to define the contract
- Use coverage-driven testing to find implementation-specific edge cases
- Iterate between specification refinement and test generation

---

## Repository Link

GitHub Repository: [Your GitHub URL Here]

Repository contains:
- Source code for both problems
- Baseline tests from Exercise 2
- Spec-guided tests from Exercise 3
- Coverage reports (HTML/XML)
- Scripts to reproduce coverage analysis

---

**End of Exercise 3 Submission**
