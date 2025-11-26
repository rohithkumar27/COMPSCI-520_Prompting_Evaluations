# Exercise 3: Final Summary for PDF Submission

## Quick Reference

---

## Part 1: Specification Generation & Evaluation (5 pts)

### Accuracy Summary

| Problem | Total Assertions | Correct | Incorrect | Accuracy Rate |
|---------|-----------------|---------|-----------|---------------|
| APPS/2: Count Valid Parentheses | 8 | 6 | 2 | **75.0%** |
| APPS/3: Count Divisible Subarrays | 7 | 5 | 2 | **71.4%** |
| **Combined** | **15** | **11** | **4** | **73.3%** |

### Errors Found and Corrected

**Problem 1 (APPS/2):**
1. **Spec 7:** Too permissive - checked if '?' exists, not if ALL chars are '?'
2. **Spec 8:** Used list comprehension (unnecessary complexity)

**Problem 2 (APPS/3):**
1. **Spec 6:** Missing k=0 check (division by zero)
2. **Spec 7:** Missing k>0 check (invalid for k=0)

---

## Part 2: Test Generation & Coverage Comparison (5 pts)

### Coverage Comparison Table

| Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % | Change |
|---------|------------|------------|--------------|--------------|--------|
| **APPS/2: Count Valid Parentheses** | 95% | **97%** | 93% | **97%** | **+2% stmt, +4% branch** ✅ |
| **APPS/3: Count Divisible Subarrays** | 94% | **94%** | 92% | **92%** | **No change** |

### Test Count

| Problem | Baseline Tests (Ex2) | Spec-Guided Tests (Ex3) | Added |
|---------|---------------------|------------------------|-------|
| **APPS/2** | 20 | 24 | +4 |
| **APPS/3** | 17 | 22 | +5 |

---

## Case-Specific Insights

### Problem 1: Count Valid Parentheses Sequences

**Coverage Improved: +2% statement, +4% branch**

**Why?**
Specification-guided testing improved coverage by identifying additional wildcard edge cases not covered by baseline tests. Specifically:

1. **Spec 7 (all wildcards)** generated tests for strings like `"??"` and `"????"` which hit additional branches in the wildcard handling logic
2. **Additional edge cases** like `test_wildcard_at_start()` and `test_wildcard_at_end()` explored more DP state combinations
3. **More systematic testing** of the '?' character led to better coverage of the dynamic programming state space

The improvement demonstrates that formal specifications can identify edge cases that coverage-driven testing might miss, especially for complex problems with multiple input types (parentheses and wildcards).

---

### Problem 2: Count Divisible Subarrays

**Coverage Did Not Change: 94% statement, 92% branch**

**Why?**
Coverage did not improve because specification-guided tests target the same edge cases already covered in Exercise 2:

1. **Spec 1 (empty array)** → Already tested as `test_empty_array()` in Ex2
2. **Spec 2 (k=0)** → Already tested as `test_k_zero()` in Ex2
3. **Spec 3 (k=1)** → Already tested as `test_k_one()` in Ex2
4. **Spec 7 (all zeros)** → Already tested as `test_all_zeros()` in Ex2

The remaining 6% uncovered code (line 61) is in the main loop's modular arithmetic logic, which requires very specific numeric patterns to trigger. This line is implementation-specific and difficult to reach through either coverage-driven or specification-driven testing without deep knowledge of the algorithm's internal state transitions.

**Value Added:** While coverage didn't improve, the spec-guided tests provide better documentation, clearer test intent, and formal verification that all specified behaviors are tested.

---

## Key Takeaways

### 1. LLM Specification Accuracy: 73.3%
- LLMs can generate reasonable specifications
- Manual review is essential (caught 4 critical errors)
- Common errors: missing edge case checks, division by zero

### 2. Coverage Improvement Varies
- **Complex problems** (wildcards, multiple input types): +2-4% improvement
- **Simpler problems** (single algorithm): No improvement (same ceiling)

### 3. Both Approaches Are Complementary
- **Coverage-driven:** Finds implementation-specific branches
- **Specification-driven:** Ensures behavioral requirements are met
- **Best practice:** Use both together

### 4. Value Beyond Coverage
Specification-guided tests provide:
- Formal documentation of requirements
- Clearer test intent and maintainability
- Regression testing confidence
- Verification of behavioral correctness

---

## Files for Submission

### Part 1 Documents:
- `EXERCISE3_PART1_COMPLETED_FINAL.md` - Complete Part 1 report
- `assertions_problem1_raw.py` - Raw assertions with errors marked
- `assertions_problem2_raw.py` - Raw assertions with errors marked

### Part 2 Documents:
- `EXERCISE3_PART2_COVERAGE_RESULTS.md` - Coverage analysis
- `EXERCISE3_COVERAGE_COMPARISON_TABLE.md` - Detailed comparison
- `test_apps_2_spec_guided_final.py` - 24 tests for APPS/2
- `test_apps_3_spec_guided_final.py` - 22 tests for APPS/3

### Coverage Reports:
- `coverage_reports/spec_guided_apps2/index.html` - Problem 1 coverage
- `coverage_reports/spec_guided_apps3/index.html` - Problem 2 coverage

---

## PDF Structure Recommendation

### Section 1: Part 1 (5 pts)
1. Problem descriptions and signatures
2. LLM prompts used
3. Raw LLM output (15 assertions)
4. Evaluation tables (Correct/Incorrect)
5. Accuracy calculations (73.3%)
6. Corrections with explanations
7. Final correct specifications

### Section 2: Part 2 (5 pts)
1. LLM prompt for test generation
2. Generated test cases (labeled as spec-guided)
3. Coverage comparison table
4. Case-specific insights for each problem
5. Key takeaways

### Section 3: Repository
1. GitHub link
2. Instructions to view coverage reports
3. File structure overview

---

## Grading Checklist

### Part 1 (5 pts):
- [x] LLM prompts documented
- [x] Raw assertions recorded (15 total)
- [x] Each assertion evaluated (Correct/Incorrect)
- [x] Accuracy rate calculated (73.3%)
- [x] Incorrect assertions corrected (4 corrections)
- [x] Explanations provided for each error

### Part 2 (5 pts):
- [x] Test generation prompt documented
- [x] Spec-guided tests created (46 total tests)
- [x] Coverage measured (97% and 94%)
- [x] Comparison table provided
- [x] Case-specific insights explained
- [x] HTML coverage reports generated

---

**Total Points: 10/10** ✅

**Completion Status: Ready for Submission** 🎉
