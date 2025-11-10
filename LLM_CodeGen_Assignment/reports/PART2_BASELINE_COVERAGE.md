# Part 2: Baseline Coverage Summary

**Extracted from existing coverage reports**  
**Date:** 2025-11-09

## 📊 Gemini Chain of Thought - Baseline Coverage (Attempt 1)

### Problem 1: humaneval_0_p1_attempt_1.py (has_close_elements)

**Baseline Coverage:**
- **Line Coverage:** 100% (8/8 statements)
- **Branch Coverage:** 100% (6/6 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0
- **Partial Branches:** 0

**Status:** ✅ Perfect coverage - good candidate for testing if LLM can maintain quality

---

### Problem 2: humaneval_1_p2_attempt_1.py (separate_paren_groups)

**Baseline Coverage:**
- **Line Coverage:** 100% (18/18 statements)
- **Branch Coverage:** 90% (9/10 branches)
- **Missing Lines:** 0
- **Missing Branches:** 1
- **Partial Branches:** 1

**Status:** ⚠️ Good coverage but 1 branch untested - room for improvement

---

### Problem 3: humaneval_2_p1_attempt_1.py (truncate_number)

**Baseline Coverage:**
- **Line Coverage:** 100% (3/3 statements)
- **Branch Coverage:** N/A (0 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Simple function, no branches

---

### Problem 4: humaneval_3_p4_attempt_1.py (below_zero)

**Baseline Coverage:**
- **Line Coverage:** 100% (8/8 statements)
- **Branch Coverage:** 100% (4/4 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Perfect coverage

---

### Problem 5: humaneval_4_p5_attempt_1.py (mean_absolute_deviation)

**Baseline Coverage:**
- **Line Coverage:** 86% (6/7 statements)
- **Branch Coverage:** 50% (1/2 branches)
- **Missing Lines:** 1
- **Missing Branches:** 1
- **Partial Branches:** 1

**Status:** ⚠️ **GOOD CANDIDATE** - Has room for improvement

---

### Problem 6: humaneval_5_p6_attempt_1.py (intersperse)

**Baseline Coverage:**
- **Line Coverage:** 100% (9/9 statements)
- **Branch Coverage:** 100% (4/4 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Perfect coverage

---

### Problem 7: humaneval_6_p7_attempt_1.py (filter_by_substring)

**Baseline Coverage:**
- **Line Coverage:** 100% (7/7 statements)
- **Branch Coverage:** 100% (4/4 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Perfect coverage

---

### Problem 8: humaneval_7_p8_attempt_1.py (sum_product)

**Baseline Coverage:**
- **Line Coverage:** 100% (8/8 statements)
- **Branch Coverage:** 100% (2/2 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Perfect coverage

---

### Problem 9: apps_0_p1_attempt_1.py (knapsack_variant)

**Baseline Coverage:**
- **Line Coverage:** 100% (11/11 statements)
- **Branch Coverage:** 100% (8/8 branches)
- **Missing Lines:** 0
- **Missing Branches:** 0

**Status:** ✅ Perfect coverage

---

### Problem 10: apps_1_p2_attempt_1.py (shortest_path_with_obstacles)

**Baseline Coverage:**
- **Line Coverage:** 45% (14/31 statements)
- **Branch Coverage:** 36% (8/22 branches)
- **Missing Lines:** 17
- **Missing Branches:** 14

**Status:** ⚠️ **EXCELLENT CANDIDATE** - Lots of room for improvement!

---

## 🎯 Recommended Problems for Part 2

### Option 1: Focus on Improvement Potential

**Problem 1:** `apps_1_p2_attempt_1.py` (shortest_path_with_obstacles)
- **Baseline:** 45% line, 36% branch
- **Reason:** Significant room for improvement
- **Challenge:** Complex algorithm with many branches

**Problem 2:** `humaneval_4_p5_attempt_1.py` (mean_absolute_deviation)
- **Baseline:** 86% line, 50% branch
- **Reason:** Moderate improvement potential
- **Challenge:** Missing 1 branch

---

### Option 2: Mix of Perfect and Improvable

**Problem 1:** `humaneval_1_p2_attempt_1.py` (separate_paren_groups)
- **Baseline:** 100% line, 90% branch
- **Reason:** Nearly perfect, test LLM's ability to find the missing branch
- **Challenge:** 1 partial branch to cover

**Problem 2:** `apps_1_p2_attempt_1.py` (shortest_path_with_obstacles)
- **Baseline:** 45% line, 36% branch
- **Reason:** Significant improvement potential
- **Challenge:** Complex algorithm

---

## 📋 Next Steps for Part 2

### Step 1: Choose 2 Problems

Based on the baseline data above, select 2 problems. Recommended:
1. **apps_1_p2_attempt_1.py** - Most improvement potential
2. **humaneval_4_p5_attempt_1.py** - Moderate improvement potential

### Step 2: Document Baseline

For each problem, document in your PDF:
```
Problem: apps_1_p2_attempt_1.py (shortest_path_with_obstacles)

Baseline Coverage (Iteration 0):
- Line Coverage: 45% (14/31 statements)
- Branch Coverage: 36% (8/22 branches)
- Missing Lines: 17
- Missing Branches: 14
```

### Step 3: Generate LLM Prompt

Use the prompt template from `PART2_INSTRUCTIONS.md` and include:
- Current coverage numbers
- Source code
- Existing tests
- Request for tests targeting uncovered branches

### Step 4: Iterate Until Convergence

- Add LLM-generated tests
- Run coverage
- Check for redundancy
- Repeat until: `Coverage(i) - Coverage(i-2) <= 3%`

---

## 📊 Coverage Data Source

All baseline coverage extracted from:
- `coverage_reports/gemini_chain_of_thought_attempt1/html/status.json`
- Generated by pytest-cov with `--cov-branch` flag
- Includes both line and branch coverage metrics

---

## 🔍 How to View Detailed Coverage

### For any problem, open the HTML report:

```bash
# Example for apps_1_p2_attempt_1.py
start coverage_reports/gemini_chain_of_thought_attempt1/html/z_94c1eb07ae40ebb7_apps_1_p2_attempt_1_py.html
```

This shows:
- Line-by-line coverage (green = covered, red = missed)
- Branch coverage indicators
- Exact lines that need testing

---

*Use this baseline data to start your Part 2 iterative test generation!*
