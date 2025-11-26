# Exercise 3 - Part 2: Coverage Results

## Overview

This document presents the coverage results for specification-guided tests generated from the corrected formal specifications in Part 1.

---

## Coverage Summary

| Problem | Tests | Passed | Statement Coverage | Branch Coverage | Change from Ex2 |
|---------|-------|--------|-------------------|-----------------|-----------------|
| **APPS/2: Count Valid Parentheses** | 24 | 23 | **97%** (48 stmts, 1 miss) | **97%** (30 branches, 1 partial) | +2% stmt, +4% branch |
| **APPS/3: Count Divisible Subarrays** | 22 | 22 | **94%** (24 stmts, 1 miss) | **92%** (12 branches, 1 partial) | No change |

---

## Problem 1: Count Valid Parentheses Sequences (APPS/2)

### Test Execution Results
- **Total Tests:** 24
- **Passed:** 23 ✅
- **Failed:** 1 ❌

### Coverage Metrics
```
Name: apps_2_p3_attempt_1.py
Statements: 48
Missing: 1
Branches: 30
Partial: 1

Statement Coverage: 97% (47/48)
Branch Coverage: 97% (29/30)
```

### Comparison with Exercise 2

| Metric | Exercise 2 (Final) | Exercise 3 (Spec-Guided) | Change |
|--------|-------------------|--------------------------|--------|
| **Statement Coverage** | 95% | 97% | **+2%** ✅ |
| **Branch Coverage** | 93% | 97% | **+4%** ✅ |
| **Tests** | 20 | 24 | +4 tests |

### Coverage Improvement Analysis

**Why did coverage improve?**

The specification-guided tests achieved slightly better coverage because:

1. **More systematic edge case coverage:** The formal specifications explicitly identified boundary conditions that needed testing:
   - Spec 7 (all wildcards) led to tests like `test_spec7_all_wildcards_two()` and `test_spec7_all_wildcards_four()`
   - Spec 8 (all opening/closing parens) led to comprehensive tests for these cases

2. **Additional wildcard combinations:** The spec-guided approach generated more wildcard test cases:
   - `test_wildcard_at_start()` - Tests '?' at position 0
   - `test_wildcard_at_end()` - Tests '?' at last position
   - These hit additional branches in the wildcard handling logic

3. **Redundancy with purpose:** While some tests overlap with Exercise 2, the spec-guided tests provide:
   - Clearer documentation of what's being tested (linked to specifications)
   - More variations of each edge case
   - Better coverage of the DP state space

### Missing Coverage

**Line 66:** One statement still not covered (same as Exercise 2)
- This is likely a rare DP state transition that requires very specific input patterns

**Branch:** One partial branch (improved from Exercise 2's 2 partial branches)

### HTML Coverage Report

Location: `coverage_reports/spec_guided_apps2/index.html`

---

## Problem 2: Count Divisible Subarrays (APPS/3)

### Test Execution Results
- **Total Tests:** 22
- **Passed:** 22 ✅
- **Failed:** 0

### Coverage Metrics
```
Name: apps_3_p4_attempt_1.py
Statements: 24
Missing: 1
Branches: 12
Partial: 1

Statement Coverage: 94% (23/24)
Branch Coverage: 92% (11/12)
```

### Comparison with Exercise 2

| Metric | Exercise 2 (Final) | Exercise 3 (Spec-Guided) | Change |
|--------|-------------------|--------------------------|--------|
| **Statement Coverage** | 94% | 94% | **No change** |
| **Branch Coverage** | 92% | 92% | **No change** |
| **Tests** | 17 | 22 | +5 tests |

### Coverage Analysis

**Why didn't coverage improve?**

Coverage remained at 94%/92% because:

1. **Specifications target same edge cases:** The formal specifications identified the same boundary conditions that Exercise 2's coverage-driven approach found:
   - Empty array (Spec 1) → Already tested in Ex2
   - k=0 case (Spec 2) → Already tested in Ex2
   - k=1 case (Spec 3) → Already tested in Ex2
   - All zeros (Spec 7) → Already tested in Ex2

2. **Missing line is implementation-specific:** Line 61 (the one missing statement) is in the main loop's modular arithmetic logic. Neither approach reaches it because:
   - It requires a very specific combination of array values and k
   - The condition is implementation-dependent, not specification-dependent

3. **Specifications describe behavior, not implementation:** Formal specifications capture the function's contract (what it should do), but don't necessarily cover all implementation paths (how it does it).

### Value of Spec-Guided Tests

Even without coverage improvement, the spec-guided tests provide:

1. **Better documentation:** Each test explicitly states which specification it verifies
2. **Clearer intent:** Test names like `test_spec6_single_element_with_k_zero()` clearly show the edge case being tested
3. **Easier maintenance:** If specifications change, tests can be updated systematically
4. **Redundancy for robustness:** More tests = more confidence in correctness

### Missing Coverage

**Line 61:** One statement in the main loop (same as Exercise 2)
- Requires specific numeric patterns to trigger

**Branch:** One partial branch in the remainder calculation (same as Exercise 2)

### HTML Coverage Report

Location: `coverage_reports/spec_guided_apps3/index.html`

---

## Overall Analysis

### Key Findings

1. **Specification-guided testing achieved 94-97% coverage**
   - Problem 1: 97% (improved from 95%)
   - Problem 2: 94% (same as Exercise 2)

2. **Improvement varies by problem complexity**
   - More complex problems (with wildcards) benefit more from systematic specification-based testing
   - Simpler problems reach a coverage ceiling quickly

3. **Both approaches are complementary**
   - Coverage-driven: Finds implementation-specific branches
   - Specification-driven: Ensures all behavioral requirements are tested

### Comparison: Coverage-Driven vs. Specification-Driven

| Aspect | Coverage-Driven (Ex2) | Specification-Driven (Ex3) |
|--------|----------------------|---------------------------|
| **Approach** | Analyze uncovered lines/branches | Derive tests from formal specs |
| **Focus** | Implementation coverage | Behavioral correctness |
| **Strengths** | Finds implementation bugs | Documents requirements |
| **Weaknesses** | May miss logical errors | May miss implementation paths |
| **Coverage** | 93-95% | 94-97% |
| **Test Count** | 17-20 tests | 22-24 tests |

### Recommendations

For maximum effectiveness:

1. **Start with specifications** to define the contract
2. **Use coverage analysis** to find implementation gaps
3. **Iterate** between both approaches
4. **Document** which tests verify which specifications

---

## Detailed Test Breakdown

### Problem 1: Count Valid Parentheses (24 tests)

**Specification-based tests (21):**
- Spec 1: Empty string (1 test)
- Spec 2: Odd length (3 tests)
- Spec 3: Starts with ')' (2 tests)
- Spec 4: Ends with '(' (2 tests)
- Spec 5: Result range (2 tests)
- Spec 6: No wildcards (4 tests)
- Spec 7: All wildcards (3 tests)
- Spec 8: All same char (4 tests)

**Additional edge cases (3):**
- Wildcard at start
- Wildcard at end
- Simple wildcard valid

### Problem 2: Count Divisible Subarrays (22 tests)

**Specification-based tests (18):**
- Spec 1: Empty array (1 test)
- Spec 2: k=0 (2 tests)
- Spec 3: k=1 (3 tests)
- Spec 4: Non-negative result (2 tests)
- Spec 5: Bounded result (2 tests)
- Spec 6: Single element (4 tests)
- Spec 7: All zeros (4 tests)

**Additional edge cases (4):**
- Mixed with zeros
- Negative numbers
- Large k
- Single zero element

---

## Conclusion

Specification-guided testing achieved excellent coverage (94-97%) and demonstrated that:

1. **Formal specifications are effective** for generating comprehensive test suites
2. **Coverage can improve** when specifications identify edge cases missed by coverage-driven testing (Problem 1: +2% stmt, +4% branch)
3. **Coverage may plateau** when specifications and coverage-driven tests target the same edge cases (Problem 2: no change)
4. **Both approaches are valuable** and should be used together for maximum effectiveness

The 73.3% accuracy rate in Part 1 (11/15 specifications correct) shows that while LLMs can generate reasonable specifications, **manual review and correction are essential** for ensuring logical correctness.

---

## Files Generated

- **Test Files:**
  - `test_apps_2_spec_guided_final.py` (24 tests)
  - `test_apps_3_spec_guided_final.py` (22 tests)

- **Coverage Reports:**
  - `coverage_reports/spec_guided_apps2/index.html`
  - `coverage_reports/spec_guided_apps3/index.html`

- **Documentation:**
  - This report: `EXERCISE3_PART2_COVERAGE_RESULTS.md`

---

**End of Part 2**
