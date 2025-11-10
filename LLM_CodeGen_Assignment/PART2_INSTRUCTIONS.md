# Part 2: LLM-Assisted Test Generation & Coverage Improvement

## 📋 Assignment Requirements

For **2 representative problems**, you need to:
1. Use LLM to generate/improve tests to increase coverage
2. Run coverage with new tests
3. Document prompts, before/after coverage, and redundancy handling
4. Iterate until convergence (3 consecutive iterations with <3% improvement)

---

## 🚀 Quick Start Guide

### Step 1: Select 2 Problems

Choose 2 problems from your existing code. Recommended:

**Problem 1:** `humaneval_0_p1_attempt_1` (has_close_elements)
- File: `generated/groq_chain_of_thought/humaneval_0_p1_attempt_1.py`
- Test: `generated/groq_chain_of_thought/test_humaneval_0_p1_attempt_1.py`

**Problem 2:** `humaneval_1_p2_attempt_1` (separate_paren_groups)
- File: `generated/groq_chain_of_thought/humaneval_1_p2_attempt_1.py`
- Test: `generated/groq_chain_of_thought/test_humaneval_1_p2_attempt_1.py`

---

### Step 2: Get Baseline Coverage

```bash
# Problem 1
python -m pytest generated/groq_chain_of_thought/test_humaneval_0_p1_attempt_1.py \
  --cov=generated/groq_chain_of_thought/humaneval_0_p1_attempt_1.py \
  --cov-branch \
  --cov-report=term \
  --cov-report=html:coverage_reports/problem1_baseline

# Problem 2
python -m pytest generated/groq_chain_of_thought/test_humaneval_1_p2_attempt_1.py \
  --cov=generated/groq_chain_of_thought/humaneval_1_p2_attempt_1.py \
  --cov-branch \
  --cov-report=term \
  --cov-report=html:coverage_reports/problem2_baseline
```

**Record the baseline numbers:**
- Line coverage: X%
- Branch coverage: Y%
- Branches covered: A/B

---

### Step 3: Generate Prompt for LLM

Use this template:

```
I need you to generate additional unit tests to improve code coverage for the following Python function.

**Current Coverage:**
- Line Coverage: [X]%
- Branch Coverage: [Y]%
- Branches Covered: [A]/[B]

**Source Code:**
```python
[PASTE YOUR SOURCE CODE HERE]
```

**Existing Tests:**
```python
[PASTE YOUR EXISTING TESTS HERE]
```

**Task:**
Generate NEW test cases that:
1. Increase branch coverage by testing untested conditional paths
2. Test edge cases not covered by existing tests
3. Are NOT duplicates of existing tests
4. Focus on improving branch coverage specifically

**Requirements:**
- Generate 3-5 new test functions
- Each test should target a specific uncovered branch or edge case
- Use descriptive test names like `test_edge_case_empty_input()`
- Include assertions to verify behavior
- Do NOT duplicate existing test logic

**Output Format:**
Provide ONLY the new test functions (no explanations, just code).
```

---

### Step 4: Add Generated Tests

1. Copy the LLM-generated tests
2. Append them to your test file
3. Add a comment marking the iteration:

```python
# ===== Iteration 1 - LLM Generated Tests =====

def test_edge_case_1():
    # LLM generated test
    pass
```

---

### Step 5: Run Coverage Again

```bash
python -m pytest generated/groq_chain_of_thought/test_humaneval_0_p1_attempt_1.py \
  --cov=generated/groq_chain_of_thought/humaneval_0_p1_attempt_1.py \
  --cov-branch \
  --cov-report=term \
  --cov-report=html:coverage_reports/problem1_iteration1
```

**Record the new numbers:**
- Line coverage: X2%
- Branch coverage: Y2%
- Improvement: (Y2 - Y)%

---

### Step 6: Check for Redundancy

**Look for:**
- Duplicate test logic
- Tests that test the same branch
- Near-identical assertions

**De-duplication strategy:**
1. Compare new tests with existing tests
2. Remove exact duplicates
3. Merge similar tests if they test the same branch
4. Keep only tests that add unique coverage

**Document in your report:**
```
Redundancy Analysis - Iteration 1:
- Generated: 5 tests
- Duplicates found: 2 tests
- Removed: test_duplicate_1, test_duplicate_2
- Kept: 3 unique tests
- Reason: Tests X and Y tested the same branch condition
```

---

### Step 7: Repeat Until Convergence

**Convergence Criteria:**
```
Coverage(i) - Coverage(i-2) <= 3%
```

**Example:**
- Iteration 1: 75% branch coverage
- Iteration 2: 82% branch coverage (+7%)
- Iteration 3: 85% branch coverage (+3%)
- Iteration 4: 86% branch coverage (+1%)
- Iteration 5: 87% branch coverage (+1%)

**Check:** Coverage(5) - Coverage(3) = 87% - 85% = 2% ✅ CONVERGED

---

## 📊 Documentation Template for PDF

### Problem 1: [Problem Name]

#### Iteration 0 (Baseline)
**Coverage:**
- Line: 85%
- Branch: 75%
- Branches: 6/8

#### Iteration 1

**Prompt Used:**
```
[PASTE YOUR PROMPT HERE]
```

**Generated Tests:**
```python
def test_edge_case_empty_list():
    result = has_close_elements([], 0.5)
    assert result == False

def test_negative_threshold():
    result = has_close_elements([1.0, 2.0], -0.5)
    assert result == False
```

**Coverage After:**
- Line: 90% (+5%)
- Branch: 87.5% (+12.5%)
- Branches: 7/8

**Redundancy:**
- Generated: 4 tests
- Duplicates: 1 (test_empty_list was similar to existing test)
- Kept: 3 unique tests

**What Changed:**
- Added test for empty list edge case (covered branch 7)
- Added test for negative threshold (covered branch 8)
- Improved branch coverage by testing previously untested conditions

#### Iteration 2

[Repeat same format]

#### Convergence Analysis

**Coverage History:**
| Iteration | Line | Branch | Improvement |
|-----------|------|--------|-------------|
| 0 | 85% | 75% | Baseline |
| 1 | 90% | 87.5% | +12.5% |
| 2 | 92% | 90% | +2.5% |
| 3 | 93% | 91% | +1% |

**Convergence Check:**
- Coverage(3) - Coverage(1) = 91% - 87.5% = 3.5% (not converged)
- Coverage(4) - Coverage(2) = 92% - 90% = 2% ✅ CONVERGED

**Total Iterations:** 4
**Final Coverage:** 92% line, 92% branch
**Total Improvement:** +17% branch coverage

---

## 🎯 Why Branch Coverage > Line Coverage

**Branch Coverage is Better Because:**

1. **Tests Decision Points:** Branch coverage ensures all conditional paths (if/else) are tested
2. **Catches Logic Errors:** A line can execute but still have untested branches
3. **More Thorough:** 100% line coverage doesn't guarantee all code paths are tested

**Example:**
```python
def example(x):
    if x > 0:  # Line executed
        return "positive"
    else:
        return "negative"
```

- **Line Coverage:** 100% with just `example(5)` (all lines executed)
- **Branch Coverage:** 50% with just `example(5)` (only positive branch tested)

**Conclusion:** Branch coverage provides better quality assurance by ensuring all decision paths are tested.

---

## 📁 Files to Submit

1. **PDF Report** containing:
   - Prompts used for each iteration
   - Before/after coverage numbers
   - Redundancy analysis
   - Convergence analysis
   - Explanation of what changed

2. **Code Files:**
   - Updated test files with LLM-generated tests
   - Coverage reports (HTML)

---

## 🔧 Automated Workflow (Optional)

If you want to automate this process:

```bash
python llm_test_generation_workflow.py \
  generated/groq_chain_of_thought/humaneval_0_p1_attempt_1.py \
  generated/groq_chain_of_thought/test_humaneval_0_p1_attempt_1.py
```

This will:
1. Get baseline coverage
2. Generate prompts for each iteration
3. Wait for you to add LLM-generated tests
4. Run coverage and track improvements
5. Check for convergence
6. Generate detailed reports

---

## ✅ Checklist

- [ ] Select 2 representative problems
- [ ] Get baseline coverage for both
- [ ] Generate LLM prompts
- [ ] Add generated tests (iteration 1)
- [ ] Run coverage and document results
- [ ] Check for redundancy and de-duplicate
- [ ] Repeat until convergence (3 iterations with <3% improvement)
- [ ] Document all prompts in PDF
- [ ] Document before/after coverage numbers
- [ ] Explain what changed in each iteration
- [ ] Include redundancy analysis
- [ ] Show convergence calculation
- [ ] Explain why branch coverage > line coverage

---

*Good luck with Part 2!*
