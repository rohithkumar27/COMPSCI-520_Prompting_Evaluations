# Exercise 3 - Part 1: Specification Generation and Evaluation

**Student Name:** [Your Name]  
**Date:** November 24, 2025

---

## Problem 1: Count Valid Parentheses Sequences

### Function Signature
```python
def count_valid_parentheses_sequences(s: str) -> int
```

### Natural Language Description

Given a string containing '(', ')', and '?', where '?' can be either '(' or ')'.
Count the number of ways to replace '?' characters such that the resulting string
has valid parentheses.

A valid parentheses string is one where:
1. Every '(' has a matching ')'
2. At no point do we have more ')' than '(' when reading left to right

Return the count modulo 10^9 + 7.

---

### LLM Prompt Used

```
Problem description: 
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

Method signature: 
def count_valid_parentheses_sequences(s: str) -> int

Please write formal specifications as Python assertions that describe the correct 
behavior of this method. Let 'res' denote the expected return value of 
'count_valid_parentheses_sequences(s)'. 

IMPORTANT CONSTRAINTS:
- Do NOT call 'count_valid_parentheses_sequences()' in your assertions
- Do NOT use methods with side effects such as:
  - print, input, file I/O operations
  - random number generation (random.random(), etc.)
  - timing functions (datetime.now(), time.time(), etc.)
  - data structure modifications (list.append(), dict.update(), etc.)
- Express the relationship between 's' and 'res' using ONLY:
  - Pure string operations (len(), count(), indexing, slicing)
  - Arithmetic operations (+, -, *, //, %, **)
  - Boolean logic (and, or, not, ==, !=, <, >, <=, >=)
  - Conditional expressions (if-else in assertions)

Generate approximately 5 formal specifications as Python assert statements.

Format each specification like this:
```python
# Specification 1: [Description]
assert [condition involving s and res]
```
```

---

### Generated Assertions (Raw LLM Output)

**LLM Used:** [ChatGPT-4 / Claude / Gemini / etc.]

```python
[PASTE THE EXACT OUTPUT FROM YOUR LLM HERE]

Example:
# Specification 1: Empty string should return 1
assert res == 1 if s == "" else res >= 0

# Specification 2: Odd length strings cannot form valid parentheses
assert res == 0 if len(s) % 2 != 0 else res >= 0

[... continue with all generated assertions ...]
```

---

### Evaluation of Generated Assertions

| # | Assertion | Status | Issue (if incorrect) |
|---|-----------|--------|---------------------|
| 1 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 2 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 3 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 4 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 5 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 6 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |

---

### Accuracy Rate

```
Total Assertions Generated: [X]
Correct Assertions: [Y]
Incorrect Assertions: [Z]

Accuracy Rate = Y / X = [percentage]%
```

---

### Corrections for Incorrect Assertions

#### Incorrect Assertion #1 (if any)

**Original:**
```python
[paste the incorrect assertion]
```

**Problem:** 
[Explain what's wrong - e.g., "Uses side effects", "Calls the function", "Missing edge case", etc.]

**Corrected Version:**
```python
[paste the corrected assertion]
```

---

#### Incorrect Assertion #2 (if any)

**Original:**
```python
[paste the incorrect assertion]
```

**Problem:** 
[Explain what's wrong]

**Corrected Version:**
```python
[paste the corrected assertion]
```

---

[Continue for all incorrect assertions]

---

### Final Correct Specifications (Problem 1)

These are the specifications that will be used in Part 2:

```python
# Specification 1: [description]
assert [condition]

# Specification 2: [description]
assert [condition]

# Specification 3: [description]
assert [condition]

# Specification 4: [description]
assert [condition]

# Specification 5: [description]
assert [condition]

[Include all correct specifications - original correct ones + corrected versions]
```

---

## Problem 2: Count Divisible Subarrays

### Function Signature
```python
def count_divisible_subarrays(arr: List[int], k: int) -> int
```

### Natural Language Description

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

### LLM Prompt Used

```
Problem description:
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

Method signature:
def count_divisible_subarrays(arr: List[int], k: int) -> int

Please write formal specifications as Python assertions that describe the correct 
behavior of this method. Let 'res' denote the expected return value of 
'count_divisible_subarrays(arr, k)'. 

IMPORTANT CONSTRAINTS:
- Do NOT call 'count_divisible_subarrays()' in your assertions
- Do NOT use methods with side effects such as:
  - print, input, file I/O operations
  - random number generation (random.random(), etc.)
  - timing functions (datetime.now(), time.time(), etc.)
  - data structure modifications (list.append(), dict.update(), etc.)
- Express the relationship between 'arr', 'k', and 'res' using ONLY:
  - Pure list operations (len(), indexing, slicing)
  - Arithmetic operations (+, -, *, //, %, **)
  - Boolean logic (and, or, not, ==, !=, <, >, <=, >=)
  - Conditional expressions (if-else in assertions)

Generate approximately 5 formal specifications as Python assert statements.

Format each specification like this:
```python
# Specification 1: [Description]
assert [condition involving arr, k, and res]
```
```

---

### Generated Assertions (Raw LLM Output)

**LLM Used:** [ChatGPT-4 / Claude / Gemini / etc.]

```python
[PASTE THE EXACT OUTPUT FROM YOUR LLM HERE]

Example:
# Specification 1: Empty array should return 0
assert res == 0 if len(arr) == 0 else res >= 0

# Specification 2: k=0 should return 0
assert res == 0 if k == 0 else res >= 0

[... continue with all generated assertions ...]
```

---

### Evaluation of Generated Assertions

| # | Assertion | Status | Issue (if incorrect) |
|---|-----------|--------|---------------------|
| 1 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 2 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 3 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 4 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 5 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |
| 6 | `[paste full assertion]` | ✅ Correct / ❌ Incorrect | [If incorrect, explain why] |

---

### Accuracy Rate

```
Total Assertions Generated: [X]
Correct Assertions: [Y]
Incorrect Assertions: [Z]

Accuracy Rate = Y / X = [percentage]%
```

---

### Corrections for Incorrect Assertions

#### Incorrect Assertion #1 (if any)

**Original:**
```python
[paste the incorrect assertion]
```

**Problem:** 
[Explain what's wrong]

**Corrected Version:**
```python
[paste the corrected assertion]
```

---

[Continue for all incorrect assertions]

---

### Final Correct Specifications (Problem 2)

These are the specifications that will be used in Part 2:

```python
# Specification 1: [description]
assert [condition]

# Specification 2: [description]
assert [condition]

# Specification 3: [description]
assert [condition]

# Specification 4: [description]
assert [condition]

# Specification 5: [description]
assert [condition]

[Include all correct specifications - original correct ones + corrected versions]
```

---

## Part 1 Summary

### Overall Accuracy

| Problem | Total Assertions | Correct | Incorrect | Accuracy Rate |
|---------|-----------------|---------|-----------|---------------|
| Problem 1: Count Valid Parentheses | [X] | [Y] | [Z] | [%] |
| Problem 2: Count Divisible Subarrays | [X] | [Y] | [Z] | [%] |
| **Combined** | [X] | [Y] | [Z] | [%] |

---

### Key Insights

1. **Common Issues Found:**
   - [List any patterns in incorrect assertions]
   - [e.g., "LLM struggled with edge cases involving special characters"]

2. **LLM Strengths:**
   - [What did the LLM do well?]
   - [e.g., "Generated clear boundary condition checks"]

3. **Manual Corrections Needed:**
   - [What types of corrections were most common?]
   - [e.g., "Added checks for division by zero"]

---

**End of Part 1**

Next: Proceed to Part 2 using the final correct specifications listed above.
