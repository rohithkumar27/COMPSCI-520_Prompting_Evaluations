# Exercise 3 - Part 1: Complete Workflow Guide

## Overview
This document provides the exact prompts to use with an LLM and step-by-step instructions for Part 1.

---

## Problem 1: Count Valid Parentheses Sequences

### Step 1.1: Identify Function Signature

```python
def count_valid_parentheses_sequences(s: str) -> int
```

**Input:** `s` (string containing '(', ')', and '?')  
**Output:** `int` (count of valid ways, modulo 10^9 + 7)

---

### Step 1.2: Natural Language Problem Description

```
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
```

---

### Step 1.3: LLM Prompt (Copy this EXACTLY to your LLM)

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

### Step 1.4: Record LLM Output

**INSTRUCTIONS:** 
1. Copy the prompt above to ChatGPT/Claude/Gemini
2. Paste the LLM's response below
3. Keep the raw output exactly as generated

**LLM Output (paste here):**
```python
[You will paste the LLM's generated assertions here]
```

---

### Step 1.5: Evaluate Each Assertion

**INSTRUCTIONS:**
For each assertion the LLM generated, determine if it's Correct or Incorrect.

**Evaluation Criteria:**
- ✅ **Correct:** Logically sound, no side effects, properly expresses a specification
- ❌ **Incorrect:** Has logical errors, uses side effects, calls the function, or is malformed

**Evaluation Table:**

| # | Assertion | Status | Reason (if incorrect) |
|---|-----------|--------|----------------------|
| 1 | `[paste assertion 1]` | ✅/❌ | [explanation if incorrect] |
| 2 | `[paste assertion 2]` | ✅/❌ | [explanation if incorrect] |
| 3 | `[paste assertion 3]` | ✅/❌ | [explanation if incorrect] |
| 4 | `[paste assertion 4]` | ✅/❌ | [explanation if incorrect] |
| 5 | `[paste assertion 5]` | ✅/❌ | [explanation if incorrect] |

---

### Step 1.6: Compute Accuracy Rate

```
Total Assertions Generated: [count]
Correct Assertions: [count]
Incorrect Assertions: [count]

Accuracy Rate = [correct] / [total] = [percentage]%
```

---

### Step 1.7: Correct Incorrect Assertions

**INSTRUCTIONS:**
For each incorrect assertion, provide:
1. The original (incorrect) assertion
2. Explanation of what's wrong
3. Corrected version

**Example Format:**

#### Incorrect Assertion #1

**Original:**
```python
assert res == count_valid_parentheses_sequences(s)
```

**Problem:** Calls the function itself (self-reference), which violates the constraint.

**Corrected:**
```python
# Cannot be expressed as a pure assertion without calling the function
# This specification is removed
```

---

### Step 1.8: Final Correct Specifications

**INSTRUCTIONS:**
List only the correct specifications (original correct ones + corrected versions).
These will be used in Part 2.

```python
# Specification 1: [description]
assert [condition]

# Specification 2: [description]
assert [condition]

# ... etc
```

---

## Problem 2: Count Divisible Subarrays

### Step 2.1: Identify Function Signature

```python
def count_divisible_subarrays(arr: List[int], k: int) -> int
```

**Input:** 
- `arr` (list of integers)
- `k` (integer divisor)

**Output:** `int` (count of subarrays with sum divisible by k)

---

### Step 2.2: Natural Language Problem Description

```
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
```

---

### Step 2.3: LLM Prompt (Copy this EXACTLY to your LLM)

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

### Step 2.4: Record LLM Output

**INSTRUCTIONS:** 
1. Copy the prompt above to ChatGPT/Claude/Gemini
2. Paste the LLM's response below
3. Keep the raw output exactly as generated

**LLM Output (paste here):**
```python
[You will paste the LLM's generated assertions here]
```

---

### Step 2.5: Evaluate Each Assertion

**INSTRUCTIONS:**
For each assertion the LLM generated, determine if it's Correct or Incorrect.

**Evaluation Table:**

| # | Assertion | Status | Reason (if incorrect) |
|---|-----------|--------|----------------------|
| 1 | `[paste assertion 1]` | ✅/❌ | [explanation if incorrect] |
| 2 | `[paste assertion 2]` | ✅/❌ | [explanation if incorrect] |
| 3 | `[paste assertion 3]` | ✅/❌ | [explanation if incorrect] |
| 4 | `[paste assertion 4]` | ✅/❌ | [explanation if incorrect] |
| 5 | `[paste assertion 5]` | ✅/❌ | [explanation if incorrect] |

---

### Step 2.6: Compute Accuracy Rate

```
Total Assertions Generated: [count]
Correct Assertions: [count]
Incorrect Assertions: [count]

Accuracy Rate = [correct] / [total] = [percentage]%
```

---

### Step 2.7: Correct Incorrect Assertions

**INSTRUCTIONS:**
For each incorrect assertion, provide:
1. The original (incorrect) assertion
2. Explanation of what's wrong
3. Corrected version

---

### Step 2.8: Final Correct Specifications

**INSTRUCTIONS:**
List only the correct specifications (original correct ones + corrected versions).
These will be used in Part 2.

```python
# Specification 1: [description]
assert [condition]

# Specification 2: [description]
assert [condition]

# ... etc
```

---

## Summary Checklist for Part 1

- [ ] Problem 1: Copied exact prompt to LLM
- [ ] Problem 1: Recorded raw LLM output
- [ ] Problem 1: Evaluated each assertion (Correct/Incorrect)
- [ ] Problem 1: Computed accuracy rate
- [ ] Problem 1: Corrected all incorrect assertions
- [ ] Problem 1: Listed final correct specifications
- [ ] Problem 2: Copied exact prompt to LLM
- [ ] Problem 2: Recorded raw LLM output
- [ ] Problem 2: Evaluated each assertion (Correct/Incorrect)
- [ ] Problem 2: Computed accuracy rate
- [ ] Problem 2: Corrected all incorrect assertions
- [ ] Problem 2: Listed final correct specifications

---

## Next Steps

After completing Part 1, proceed to Part 2 where you will:
1. Use the final correct specifications to generate test cases
2. Run coverage analysis
3. Compare with Exercise 2 results

---

## Tips for Evaluation

### Common Issues to Watch For:

1. **Self-Reference:** Assertion calls the function being specified
   ```python
   # WRONG
   assert res == count_divisible_subarrays(arr, k)
   ```

2. **Side Effects:** Uses print, append, etc.
   ```python
   # WRONG
   assert (print(res) or True) and res >= 0
   ```

3. **Incomplete Logic:** Missing edge cases
   ```python
   # WRONG (doesn't handle k=0)
   assert res == 1 if len(arr) == 1 and arr[0] % k == 0 else res >= 0
   
   # CORRECT
   assert res == 1 if len(arr) == 1 and k != 0 and arr[0] % k == 0 else res >= 0
   ```

4. **Overly Complex:** Tries to reimplement the algorithm
   ```python
   # WRONG (too complex, essentially reimplements the function)
   assert res == sum(1 for i in range(len(arr)) for j in range(i, len(arr)) if sum(arr[i:j+1]) % k == 0)
   ```

5. **Incorrect Logic:** Misunderstands the problem
   ```python
   # WRONG (for parentheses problem - doesn't account for '?')
   assert res == 0 if s.count('(') == len(s) else res >= 0
   # Should check s.replace('?', '') instead
   ```

---

## Example Workflow (Abbreviated)

### You ask LLM:
"[paste the exact prompt from Step 1.3]"

### LLM responds:
```python
# Specification 1: Empty string returns 1
assert res == 1 if s == "" else res >= 0

# Specification 2: Odd length returns 0
assert res == 0 if len(s) % 2 != 0 else res >= 0
```

### You evaluate:
| # | Assertion | Status | Reason |
|---|-----------|--------|--------|
| 1 | `assert res == 1 if s == "" else res >= 0` | ✅ | Correct logic, no side effects |
| 2 | `assert res == 0 if len(s) % 2 != 0 else res >= 0` | ✅ | Correct logic, no side effects |

### You compute:
Accuracy Rate = 2/2 = 100%

### You list final specs:
```python
# Specification 1: Empty string returns 1
assert res == 1 if s == "" else res >= 0

# Specification 2: Odd length returns 0
assert res == 0 if len(s) % 2 != 0 else res >= 0
```

---

**End of Part 1 Workflow Guide**
