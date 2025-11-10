# LLM Prompt Template for Iterative Test Generation

## Prompt Template for Coverage-Driven Test Generation

```
You are a test generation expert. Your task is to generate additional test cases that improve code coverage by targeting uncovered branches and edge cases.

## Current Situation

**Source Code:**
```python
[INSERT SOURCE CODE HERE]
```

**Existing Tests:**
```python
[INSERT EXISTING TEST CODE HERE]
```

**Current Coverage:**
- Line Coverage: [X]%
- Branch Coverage: [Y]%
- Missing Lines: [LIST MISSING LINE NUMBERS]
- Uncovered Branches: [DESCRIBE UNCOVERED BRANCHES]

## Your Task

Generate NEW test cases that:
1. Target the uncovered branches and missing lines
2. Test edge cases not covered by existing tests
3. Follow the same format as existing tests
4. Are concise and focused

## Uncovered Code Paths to Target

[DESCRIBE SPECIFIC BRANCHES/CONDITIONS NOT COVERED]

For example:
- Empty input edge case (line X)
- k=0 edge case (line Y)
- k=1 special case (line Z)
- Odd length string (line W)
- Negative remainder handling (line V)

## Output Format

Provide ONLY the new test functions in this format:

```python
def test_[descriptive_name]():
    # Test [specific edge case]
    [test code]
    assert [condition]
```

## Requirements

- Each test should target a DIFFERENT uncovered branch
- Tests should be independent and self-contained
- Use descriptive test names that indicate what edge case is being tested
- Include a brief comment explaining what branch/edge case the test covers
- Do NOT duplicate existing test logic

Generate 3-5 new targeted test cases.
```

## Example Usage for apps_3_p4_attempt_1 (Count Divisible Subarrays)

### Iteration 1 Prompt:

```
You are a test generation expert. Your task is to generate additional test cases that improve code coverage by targeting uncovered branches and edge cases.

## Current Situation

**Source Code:**
```python
def count_divisible_subarrays(arr: List[int], k: int) -> int:
    # Edge case: empty array
    if not arr:
        return 0
    
    # Edge case: k is 0 or 1
    if k == 0:
        return 0
    
    if k == 1:
        n = len(arr)
        return n * (n + 1) // 2
    
    # Edge case: single element
    if len(arr) == 1:
        return 1 if arr[0] % k == 0 else 0
    
    # Main logic with prefix sums...
```

**Existing Tests (8 tests):**
All test normal arrays with positive/negative numbers and various k values.
All follow the same code path through the main logic.

**Current Coverage:**
- Line Coverage: 69% (24 statements, 6 missed)
- Branch Coverage: 58% (12 branches, 5 partial)
- Missing Lines: 21-23, 26-28, 31-33
- Uncovered Branches: 
  - Empty array check (line 21)
  - k==0 check (line 26)
  - k==1 check (line 29)
  - Single element check (line 34)
  - Negative remainder handling (line 49)

## Your Task

Generate NEW test cases that target these specific uncovered branches:

1. **Empty array edge case** (line 21): Test with arr=[]
2. **k=0 edge case** (line 26): Test with k=0
3. **k=1 edge case** (line 29): Test with k=1 (all subarrays divisible)
4. **Single element array** (line 34): Test with arr=[5], k=5
5. **Negative remainder** (line 49): Test with negative numbers that produce negative remainders

## Output Format

Provide ONLY the new test functions targeting these edge cases.
```

---

## Example Usage for apps_2_p3_attempt_1 (Count Valid Parentheses)

### Iteration 1 Prompt:

```
You are a test generation expert. Your task is to generate additional test cases that improve code coverage by targeting uncovered branches and edge cases.

## Current Situation

**Source Code:**
```python
def count_valid_parentheses_sequences(s: str) -> int:
    # Edge case: empty string
    if not s:
        return 1
    
    # Edge case: odd length can't be valid
    if len(s) % 2 != 0:
        return 0
    
    # Edge case: starts with ')'
    if s[0] == ')':
        return 0
    
    # Edge case: ends with '('
    if s[-1] == '(':
        return 0
    
    # Main logic with DP...
```

**Existing Tests (8 tests):**
All test valid even-length strings with balanced parentheses.
All follow the same code path through the main logic.

**Current Coverage:**
- Line Coverage: 71% (48 statements, 12 missed)
- Branch Coverage: 63% (30 branches, 11 partial)
- Missing Lines: 21-23, 26-28, 31-33, 36-38
- Uncovered Branches:
  - Empty string check (line 21)
  - Odd length check (line 26)
  - Starts with ')' check (line 31)
  - Ends with '(' check (line 36)
  - Question mark '?' handling (line 75)

## Your Task

Generate NEW test cases that target these specific uncovered branches:

1. **Empty string edge case** (line 21): Test with s=""
2. **Odd length edge case** (line 26): Test with s="(((" (odd length)
3. **Starts with ')' edge case** (line 31): Test with s="))(("
4. **Ends with '(' edge case** (line 36): Test with s="(()("
5. **Question mark handling** (line 75): Test with s="(?)" or s="????"

## Output Format

Provide ONLY the new test functions targeting these edge cases.
```

---

## Convergence Criteria

Stop iterating when:
```
Coverage(iteration_i) - Coverage(iteration_i-2) <= 3%
```

This indicates diminishing returns and convergence.

---

## Benefits of This Approach

1. **Targeted**: Focuses on specific uncovered branches
2. **Efficient**: Avoids redundant tests
3. **Measurable**: Clear coverage improvement metrics
4. **Iterative**: Can repeat until convergence
5. **Explainable**: Each test has a clear purpose

