# Complete Coverage Table - All Iterations

## Master Coverage Table

### Both Problems - All Metrics - All Iterations

| Problem | Iteration | Tests | Line Coverage | Branch Coverage | Missing Lines | Missing Branches | Pass Rate | Line Δ | Branch Δ |
|---------|-----------|-------|---------------|-----------------|---------------|------------------|-----------|--------|----------|
| **apps_2_p3** | Baseline | 8 | 75% (36/48) | 71% (19/30) | 12 | 11 | 100% (8/8) | - | - |
| | Iteration 1 | 15 | 94% (45/48) | 92% (27/30) | 3 | 3 | 93% (14/15) | +19% | +21% |
| | Iteration 2 | 19 | 96% (46/48) | 95% (28/30) | 2 | 2 | 89% (17/19) | +2% | +3% |
| | **Iteration 3** | **21** | **98% (47/48)** | **97% (29/30)** | **1** | **1** | **95% (20/21)** | **+2%** | **+2%** |
| | **TOTAL GAIN** | **+13** | **+23%** | **+26%** | **-11** | **-10** | **-5%** | - | - |
| **apps_3_p4** | Baseline | 8 | 75% (18/24) | 69% (7/12) | 6 | 5 | 100% (8/8) | - | - |
| | Iteration 1 | 14 | 96% (23/24) | 94% (11/12) | 1 | 1 | 100% (14/14) | +21% | +25% |
| | Iteration 2 | 17 | 96% (23/24) | 94% (11/12) | 1 | 1 | 100% (17/17) | 0% | 0% |
| | **Iteration 3** | **21** | **96% (23/24)** | **94% (11/12)** | **1** | **1** | **100% (21/21)** | **0%** | **0%** |
| | **TOTAL GAIN** | **+13** | **+21%** | **+25%** | **-5** | **-4** | **0%** | - | - |

---

## Simplified Table (For Report)

### Coverage Progression Summary

| Problem | Metric | Baseline | Iter 1 | Iter 2 | Iter 3 | Total Gain |
|---------|--------|----------|--------|--------|--------|------------|
| **apps_2_p3** | Line Coverage | 75% | 94% | 96% | **98%** | **+23%** |
| | Branch Coverage | 71% | 92% | 95% | **97%** | **+26%** |
| | Tests | 8 | 15 | 19 | **21** | **+13** |
| | Pass Rate | 100% | 93% | 89% | **95%** | **-5%** |
| **apps_3_p4** | Line Coverage | 75% | 96% | 96% | **96%** | **+21%** |
| | Branch Coverage | 69% | 94% | 94% | **94%** | **+25%** |
| | Tests | 8 | 14 | 17 | **21** | **+13** |
| | Pass Rate | 100% | 100% | 100% | **100%** | **0%** |

---

## Visual Comparison

### Line Coverage Progression

```
apps_2_p3:  75% ████████████████░░░░░░░░ (Baseline)
            94% ███████████████████████░░ (Iteration 1) +19%
            96% ████████████████████████░ (Iteration 2) +2%
            98% ████████████████████████▓ (Iteration 3) +2%

apps_3_p4:  75% ████████████████░░░░░░░░ (Baseline)
            96% ████████████████████████░ (Iteration 1) +21%
            96% ████████████████████████░ (Iteration 2) 0% ← CONVERGED
            96% ████████████████████████░ (Iteration 3) 0% ← CONFIRMED
```

### Branch Coverage Progression

```
apps_2_p3:  71% ███████████████░░░░░░░░░ (Baseline)
            92% ███████████████████████░░ (Iteration 1) +21%
            95% ████████████████████████░ (Iteration 2) +3%
            97% ████████████████████████▓ (Iteration 3) +2%

apps_3_p4:  69% ██████████████░░░░░░░░░░ (Baseline)
            94% ████████████████████████░ (Iteration 1) +25%
            94% ████████████████████████░ (Iteration 2) 0% ← CONVERGED
            94% ████████████████████████░ (Iteration 3) 0% ← CONFIRMED
```

---

## Convergence Analysis Table

### Convergence Check (Coverage(i) - Coverage(i-2) ≤ 3%)

| Problem | Metric | Iter 2 vs Baseline | Iter 3 vs Iter 1 | Converged? |
|---------|--------|-------------------|------------------|------------|
| **apps_2_p3** | Line | 96% - 75% = 21% | 98% - 94% = 4% | ⚠️ Near (4% > 3%) |
| | Branch | 95% - 71% = 24% | 97% - 92% = 5% | ⚠️ Near (5% > 3%) |
| **apps_3_p4** | Line | 96% - 75% = 21% | 96% - 96% = 0% | ✅ Yes (0% ≤ 3%) |
| | Branch | 94% - 69% = 25% | 94% - 94% = 0% | ✅ Yes (0% ≤ 3%) |

---

## Detailed Breakdown by Iteration

### Baseline (Iteration 0)

| Problem | Line Cov | Branch Cov | Tests | Pass Rate | Strategy |
|---------|----------|------------|-------|-----------|----------|
| apps_2_p3 | 75% (36/48) | 71% (19/30) | 8 | 100% | Redundant tests |
| apps_3_p4 | 75% (18/24) | 69% (7/12) | 8 | 100% | Redundant tests |

**Issue:** Tests were similar, no edge case targeting, 0% improvement per test

### Iteration 1

| Problem | Line Cov | Branch Cov | Tests | Pass Rate | Strategy |
|---------|----------|------------|-------|-----------|----------|
| apps_2_p3 | 94% (45/48) | 92% (27/30) | 15 (+7) | 93% | Target major branches |
| apps_3_p4 | 96% (23/24) | 94% (11/12) | 14 (+6) | 100% | Target major branches |

**Success:** Covered most edge cases, +19-21% line, +21-25% branch

### Iteration 2

| Problem | Line Cov | Branch Cov | Tests | Pass Rate | Strategy |
|---------|----------|------------|-------|-----------|----------|
| apps_2_p3 | 96% (46/48) | 95% (28/30) | 19 (+4) | 89% | Target remaining gaps |
| apps_3_p4 | 96% (23/24) | 94% (11/12) | 17 (+3) | 100% | Target remaining gaps |

**Result:** Minimal improvement, apps_3_p4 converged (0%)

### Iteration 3

| Problem | Line Cov | Branch Cov | Tests | Pass Rate | Strategy |
|---------|----------|------------|-------|-----------|----------|
| apps_2_p3 | 98% (47/48) | 97% (29/30) | 21 (+2) | 95% | Target final lines |
| apps_3_p4 | 96% (23/24) | 94% (11/12) | 21 (+4) | 100% | Target final lines |

**Result:** apps_2_p3 +2%, apps_3_p4 0% (convergence confirmed)

---

## Efficiency Metrics

### Coverage Gain per Test

| Problem | Iteration | Tests Added | Line Gain | Branch Gain | Line Efficiency | Branch Efficiency |
|---------|-----------|-------------|-----------|-------------|-----------------|-------------------|
| **apps_2_p3** | Baseline | 8 | 0% | 0% | 0% per test | 0% per test |
| | Iteration 1 | 7 | +19% | +21% | 2.7% per test | 3.0% per test |
| | Iteration 2 | 4 | +2% | +3% | 0.5% per test | 0.75% per test |
| | Iteration 3 | 2 | +2% | +2% | 1.0% per test | 1.0% per test |
| **apps_3_p4** | Baseline | 8 | 0% | 0% | 0% per test | 0% per test |
| | Iteration 1 | 6 | +21% | +25% | 3.5% per test | 4.2% per test |
| | Iteration 2 | 3 | 0% | 0% | 0% per test | 0% per test |
| | Iteration 3 | 4 | 0% | 0% | 0% per test | 0% per test |

**Key Finding:** Iteration 1 was most efficient (2.7-4.2% per test), baseline was completely inefficient (0%)

---

## Missing Coverage Analysis

### What's Still Not Covered

| Problem | Missing Line | Missing Branch | Reason |
|---------|--------------|----------------|--------|
| **apps_2_p3** | Line 66: `return 0` in min_open validation | Branch for Line 66 | Likely unreachable due to validation loop logic |
| **apps_3_p4** | Line 61: `remainder += k` | Branch for Line 61 | Python 3's modulo handles negatives automatically |

**Conclusion:** Both missing lines appear to be unreachable code. 96-98% is the practical maximum.

---

## Statistical Summary

### Overall Performance

| Metric | apps_2_p3 | apps_3_p4 | Average |
|--------|-----------|-----------|---------|
| **Starting Line Coverage** | 75% | 75% | 75% |
| **Final Line Coverage** | 98% | 96% | 97% |
| **Starting Branch Coverage** | 71% | 69% | 70% |
| **Final Branch Coverage** | 97% | 94% | 95.5% |
| **Line Improvement** | +23% | +21% | +22% |
| **Branch Improvement** | +26% | +25% | +25.5% |
| **Tests Generated** | 21 | 21 | 21 |
| **Final Pass Rate** | 95% | 100% | 97.5% |
| **Iterations to Converge** | 3 (near) | 2 | 2.5 |

---

## Copy-Paste Table for Report

**Compact Version:**

```
| Problem | Baseline | Iter 1 | Iter 2 | Iter 3 | Gain |
|---------|----------|--------|--------|--------|------|
| apps_2_p3 (Line) | 75% | 94% | 96% | 98% | +23% |
| apps_2_p3 (Branch) | 71% | 92% | 95% | 97% | +26% |
| apps_3_p4 (Line) | 75% | 96% | 96% | 96% | +21% |
| apps_3_p4 (Branch) | 69% | 94% | 94% | 94% | +25% |
```

**Full Version:** See "Master Coverage Table" at the top of this document.

---

**Report Generated:** November 10, 2025  
**Problems:** 2 (apps_2_p3, apps_3_p4)  
**Iterations:** 4 (Baseline + 3 iterations)  
**Metrics:** Line and Branch Coverage  
**Status:** ✅ Complete analysis with all data
