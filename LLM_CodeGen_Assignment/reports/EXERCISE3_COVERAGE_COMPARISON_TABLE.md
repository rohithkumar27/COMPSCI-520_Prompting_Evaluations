# Exercise 3: Coverage Comparison Table

## Baseline (Exercise 2) vs. Spec-Guided (Exercise 3)

---

## Summary Comparison Table

| Problem | Approach | # Tests | Stmt % | Branch % | Stmts Covered | Branches Covered | Change |
|---------|----------|---------|--------|----------|---------------|------------------|--------|
| **APPS/2: Count Valid Parentheses** | Baseline (Ex2) | 20 | 95% | 93% | 46/48 | 28/30 | - |
| **APPS/2: Count Valid Parentheses** | Spec-Guided (Ex3) | 24 | **97%** | **97%** | 47/48 | 29/30 | **+2% stmt, +4% branch** ✅ |
| | | | | | | | |
| **APPS/3: Count Divisible Subarrays** | Baseline (Ex2) | 17 | 94% | 92% | 23/24 | 11/12 | - |
| **APPS/3: Count Divisible Subarrays** | Spec-Guided (Ex3) | 22 | **94%** | **92%** | 23/24 | 11/12 | **No change** |

---

## Detailed Comparison: Problem 1 (APPS/2)

### Count Valid Parentheses Sequences

| Metric | Baseline (Exercise 2) | Spec-Guided (Exercise 3) | Improvement |
|--------|----------------------|--------------------------|-------------|
| **Test Count** | 20 | 24 | +4 tests (+20%) |
| **Tests Passed** | 18/20 (90%) | 23/24 (96%) | +6% pass rate |
| **Statement Coverage** | 95% | **97%** | **+2%** ✅ |
| **Statements Covered** | 46/48 | 47/48 | +1 statement |
| **Statements Missed** | 2 | 1 | -1 statement |
| **Branch Coverage** | 93% | **97%** | **+4%** ✅ |
| **Branches Covered** | 28/30 | 29/30 | +1 branch |
| **Partial Branches** | 2 | 1 | -1 partial |

### Visual Comparison

```
Statement Coverage:
Baseline (Ex2):  ███████████████████████████████████████████████░░  95%
Spec-Guided:     ████████████████████████████████████████████████░  97% (+2%)

Branch Coverage:
Baseline (Ex2):  ███████████████████████████████████████████████░░  93%
Spec-Guided:     ████████████████████████████████████████████████░  97% (+4%)
```

### Why Did Coverage Improve?

1. **More systematic wildcard testing:**
   - Spec 7 generated tests for all-wildcard strings: `"??"`, `"????"`
   - These hit additional branches in the wildcard handling logic

2. **Additional edge case variations:**
   - `test_wildcard_at_start()` - Tests '?' at position 0
   - `test_wildcard_at_end()` - Tests '?' at last position
   - More comprehensive testing of boundary conditions

3. **Better DP state coverage:**
   - Spec-guided tests explored more combinations of the DP state space
   - Covered one additional branch in the dynamic programming logic

---

## Detailed Comparison: Problem 2 (APPS/3)

### Count Divisible Subarrays

| Metric | Baseline (Exercise 2) | Spec-Guided (Exercise 3) | Improvement |
|--------|----------------------|--------------------------|-------------|
| **Test Count** | 17 | 22 | +5 tests (+29%) |
| **Tests Passed** | 17/17 (100%) | 22/22 (100%) | No change |
| **Statement Coverage** | 94% | **94%** | **No change** |
| **Statements Covered** | 23/24 | 23/24 | No change |
| **Statements Missed** | 1 | 1 | No change |
| **Branch Coverage** | 92% | **92%** | **No change** |
| **Branches Covered** | 11/12 | 11/12 | No change |
| **Partial Branches** | 1 | 1 | No change |

### Visual Comparison

```
Statement Coverage:
Baseline (Ex2):  ██████████████████████████████████████████████░░░  94%
Spec-Guided:     ██████████████████████████████████████████████░░░  94% (same)

Branch Coverage:
Baseline (Ex2):  ████████████████████████████████████████████░░░░░  92%
Spec-Guided:     ████████████████████████████████████████████░░░░░  92% (same)
```

### Why Didn't Coverage Improve?

1. **Specifications target same edge cases:**
   - Empty array (Spec 1) → Already tested in Ex2
   - k=0 case (Spec 2) → Already tested in Ex2
   - k=1 case (Spec 3) → Already tested in Ex2
   - All zeros (Spec 7) → Already tested in Ex2

2. **Missing line is implementation-specific:**
   - Line 61 (the uncovered statement) is in the main loop's modular arithmetic
   - Requires very specific numeric patterns to trigger
   - Neither coverage-driven nor specification-driven approaches reached it

3. **Coverage ceiling reached:**
   - Both approaches converged to the same 94%/92% coverage
   - The remaining 6%/8% requires deep implementation knowledge

---

## Side-by-Side Comparison

### Coverage Metrics

| Problem | Baseline Stmt % | Spec-Guided Stmt % | Baseline Branch % | Spec-Guided Branch % |
|---------|----------------|-------------------|------------------|---------------------|
| **APPS/2** | 95% | **97%** ✅ | 93% | **97%** ✅ |
| **APPS/3** | 94% | 94% | 92% | 92% |
| **Average** | **94.5%** | **95.5%** | **92.5%** | **94.5%** |

### Test Efficiency

| Problem | Baseline Tests | Spec-Guided Tests | Coverage per Test (Baseline) | Coverage per Test (Spec-Guided) |
|---------|---------------|------------------|------------------------------|--------------------------------|
| **APPS/2** | 20 | 24 | 4.75% stmt/test | 4.04% stmt/test |
| **APPS/3** | 17 | 22 | 5.53% stmt/test | 4.27% stmt/test |

**Note:** Spec-guided tests have slightly lower efficiency per test, but provide better documentation and maintainability.

---

## Convergence Analysis

### Problem 1: Count Valid Parentheses

| Iteration | Approach | Tests | Stmt % | Branch % | Improvement |
|-----------|----------|-------|--------|----------|-------------|
| Baseline (Iter 0) | Manual | 8 | 71% | 63% | - |
| Iteration 1 | Coverage-driven | 15 | 92% | 90% | +21% stmt, +27% branch |
| Iteration 2 | Coverage-driven | 20 | 95% | 93% | +3% stmt, +3% branch |
| **Exercise 3** | **Spec-guided** | **24** | **97%** | **97%** | **+2% stmt, +4% branch** ✅ |

**Conclusion:** Spec-guided testing pushed coverage beyond the Exercise 2 plateau.

---

### Problem 2: Count Divisible Subarrays

| Iteration | Approach | Tests | Stmt % | Branch % | Improvement |
|-----------|----------|-------|--------|----------|-------------|
| Baseline (Iter 0) | Manual | 8 | 69% | 58% | - |
| Iteration 1 | Coverage-driven | 14 | 94% | 92% | +25% stmt, +34% branch |
| Iteration 2 | Coverage-driven | 17 | 94% | 92% | 0% (converged) |
| **Exercise 3** | **Spec-guided** | **22** | **94%** | **92%** | **0% (same ceiling)** |

**Conclusion:** Both approaches converged to the same coverage ceiling.

---

## Key Insights

### 1. Specification-Guided Testing Can Improve Coverage

**Problem 1 (APPS/2):** +2% statement, +4% branch coverage
- Formal specifications identified edge cases missed by coverage-driven testing
- Systematic wildcard testing revealed additional branches
- More comprehensive DP state exploration

### 2. Coverage May Plateau Regardless of Approach

**Problem 2 (APPS/3):** No change in coverage
- Both approaches identified the same edge cases
- Remaining uncovered code is implementation-specific
- Requires deep algorithmic knowledge to reach

### 3. More Tests ≠ More Coverage

- Spec-guided: 24 tests (APPS/2), 22 tests (APPS/3)
- Baseline: 20 tests (APPS/2), 17 tests (APPS/3)
- **+4-5 more tests, but only +0-2% coverage improvement**

### 4. Value Beyond Coverage

Spec-guided tests provide:
- ✅ Better documentation (linked to specifications)
- ✅ Clearer test intent
- ✅ Easier maintenance
- ✅ Formal verification of requirements
- ✅ Regression testing confidence

---

## Recommendations

### When to Use Specification-Guided Testing

✅ **Use when:**
- Requirements are well-defined
- Formal specifications can be derived
- Documentation is important
- Long-term maintenance is expected
- Behavioral correctness is critical

### When to Use Coverage-Driven Testing

✅ **Use when:**
- Implementation is complex
- Edge cases are not obvious
- Quick iteration is needed
- Implementation-specific bugs are a concern

### Best Practice: Use Both

1. **Start with specifications** to define the contract
2. **Generate spec-guided tests** to verify requirements
3. **Analyze coverage** to find implementation gaps
4. **Add targeted tests** for uncovered branches
5. **Iterate** until coverage goals are met

---

## Final Comparison Table (For PDF Submission)

| Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % | Insight |
|---------|------------|------------|--------------|--------------|---------|
| **APPS/2: Count Valid Parentheses** | 95% | **97%** | 93% | **97%** | Spec-guided testing improved coverage by identifying additional wildcard edge cases not covered by baseline tests. The +2% statement and +4% branch improvement came from more systematic testing of '?' character combinations. |
| **APPS/3: Count Divisible Subarrays** | 94% | **94%** | 92% | **92%** | Coverage did not improve because specification-guided tests target the same edge cases (empty array, k=0, k=1, all zeros) already covered in Exercise 2. The remaining 6% uncovered code is in the main loop's modular arithmetic, which requires very specific numeric patterns that neither approach reaches. |

---

## HTML Coverage Reports

- **Problem 1 (APPS/2):** `coverage_reports/spec_guided_apps2/index.html`
- **Problem 2 (APPS/3):** `coverage_reports/spec_guided_apps3/index.html`

---

**End of Coverage Comparison**
