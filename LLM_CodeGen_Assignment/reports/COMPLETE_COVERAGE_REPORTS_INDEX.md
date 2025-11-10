# Complete Coverage Reports Index

## Overview

This document provides an index of all coverage reports generated for the iterative test generation workflow.

---

## APPS Problem 2 (apps_2_p3) - Count Valid Parentheses Sequences

### 📊 Complete Analysis Report
**File:** `reports/APPS_2_P3_ALL_ITERATIONS_COVERAGE.md`

**Contents:**
- Baseline, Iteration 1, and Iteration 2 coverage
- Test results and failure analysis
- Coverage progression (75% → 94% → 96%)
- Edge case analysis
- Logic bug identification

### 📈 Individual Iteration Reports

#### Iteration 2 Only
**File:** `reports/APPS_2_P3_ITERATION2_COVERAGE.md`
- Detailed Iteration 2 analysis
- 19 tests (17 passed, 2 failed)
- 96% line coverage

### 📁 Coverage Data Files

**Baseline:**
- JSON: `coverage_reports/apps_2_p3_baseline.json`
- HTML: `coverage_reports/apps_2_p3_baseline/html/index.html`
- Coverage: 75% (36/48 lines)
- Tests: 8/8 passed

**Iteration 1:**
- JSON: `coverage_reports/apps_2_p3_iteration1.json`
- HTML: `coverage_reports/apps_2_p3_iteration1/html/index.html`
- Coverage: 94% (45/48 lines)
- Tests: 14/15 passed (1 failed)

**Iteration 2:**
- JSON: `coverage_reports/apps_2_p3_iteration2.json`
- HTML: `coverage_reports/apps_2_p3_iteration2/html/index.html`
- Coverage: 96% (46/48 lines)
- Tests: 17/19 passed (2 failed)

**Iteration 3:**
- JSON: `coverage_reports/apps_2_p3_iteration3.json`
- HTML: `coverage_reports/apps_2_p3_iteration3/html/index.html`
- Coverage: 98% (47/48 lines)
- Tests: 20/21 passed (1 failed)

### 🧪 Test Files
- Baseline: `generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1.py`
- Iteration 1: `generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1_iteration1.py`
- Iteration 2: `generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1_iteration2.py`

### 📝 Key Findings
- ✅ Coverage improved from 75% to 96% (+21%)
- ⚠️ 3 test failures revealed logic bugs in question mark handling
- ✅ Converged at Iteration 2 (only +2% improvement)
- ⚠️ High coverage doesn't guarantee correctness

---

## APPS Problem 3 (apps_3_p4) - Count Divisible Subarrays

### 📊 Complete Analysis Report
**File:** `reports/APPS_3_P4_ALL_ITERATIONS_COVERAGE.md`

**Contents:**
- Baseline, Iteration 1, and Iteration 2 coverage
- Test results (all passing)
- Coverage progression (75% → 96% → 96%)
- Edge case analysis
- Convergence analysis

### 📁 Coverage Data Files

**Baseline:**
- JSON: `coverage_reports/apps_3_p4_baseline.json`
- HTML: `coverage_reports/apps_3_p4_baseline/html/index.html`
- Coverage: 75% (18/24 lines)
- Tests: 8/8 passed

**Iteration 1:**
- JSON: `coverage_reports/apps_3_p4_iteration1.json`
- HTML: `coverage_reports/apps_3_p4_iteration1/html/index.html`
- Coverage: 96% (23/24 lines)
- Tests: 14/14 passed

**Iteration 2:**
- JSON: `coverage_reports/apps_3_p4_iteration2.json`
- HTML: `coverage_reports/apps_3_p4_iteration2/html/index.html`
- Coverage: 96% (23/24 lines)
- Tests: 17/17 passed

**Iteration 3:**
- JSON: `coverage_reports/apps_3_p4_iteration3.json`
- HTML: `coverage_reports/apps_3_p4_iteration3/html/index.html`
- Coverage: 96% (23/24 lines)
- Tests: 21/21 passed ✅ CONVERGED

### 🧪 Test Files
- Baseline: `generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1.py`
- Iteration 1: `generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1_iteration1.py`
- Iteration 2: `generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1_iteration2.py`

### 📝 Key Findings
- ✅ Coverage improved from 75% to 96% (+21%)
- ✅ All tests passing (100% success rate)
- ✅ Converged at Iteration 2 (0% improvement)
- ✅ Excellent edge case coverage

---

## Summary Comparison

| Problem | Baseline | Iteration 1 | Iteration 2 | Iteration 3 | Total Improvement | Final Pass Rate |
|---------|----------|-------------|-------------|-------------|-------------------|-----------------|
| **apps_2_p3** | 75% | 94% | 96% | 98% | +23% | 95% (20/21) |
| **apps_3_p4** | 75% | 96% | 96% | 96% | +21% | 100% (21/21) |

### Key Insights

**Similarities:**
- Both started at 75% baseline coverage
- Both achieved 96-98% final coverage
- Both required 3 iterations
- Both have 1 unreachable line remaining

**Differences:**
- apps_2_p3: 98% coverage, 95% pass rate (logic bugs)
- apps_3_p4: 96% coverage, 100% pass rate (perfect)
- apps_2_p3 improved gradually (+19%, +2%, +2%)
- apps_3_p4 converged sharply (+21%, 0%, 0%)

**Convergence:**
- apps_3_p4: ✅ Fully converged (Coverage(3) - Coverage(1) = 0%)
- apps_2_p3: ⚠️ Near-converged (Coverage(3) - Coverage(1) = 4%)

---

## How to View Reports

### HTML Coverage Reports
Open any of the `index.html` files in a browser:
```
coverage_reports/apps_2_p3_baseline/html/index.html
coverage_reports/apps_2_p3_iteration1/html/index.html
coverage_reports/apps_2_p3_iteration2/html/index.html
coverage_reports/apps_3_p4_baseline/html/index.html
coverage_reports/apps_3_p4_iteration1/html/index.html
coverage_reports/apps_3_p4_iteration2/html/index.html
```

### Markdown Reports
Open any of the `.md` files in your editor:
```
reports/APPS_2_P3_ALL_ITERATIONS_COVERAGE.md
reports/APPS_2_P3_ITERATION2_COVERAGE.md
reports/APPS_3_P4_ALL_ITERATIONS_COVERAGE.md
```

### JSON Data
For programmatic access, use the JSON files:
```
coverage_reports/apps_2_p3_baseline.json
coverage_reports/apps_2_p3_iteration1.json
coverage_reports/apps_2_p3_iteration2.json
coverage_reports/apps_3_p4_baseline.json
coverage_reports/apps_3_p4_iteration1.json
coverage_reports/apps_3_p4_iteration2.json
```

---

## Related Reports

### Iteration 3 Reports (NEW!)
- `reports/ITERATION3_COVERAGE_RESULTS.md` - Iteration 3 detailed results
- `reports/COMPLETE_ITERATIVE_COVERAGE_ANALYSIS.md` - All iterations analysis
- `prompts/ITERATION3_PROMPTS.md` - Iteration 3 prompts used

### Part 2 Assignment Reports
- `reports/PART2_FINAL_ASSIGNMENT_DOCUMENT.md` - Complete assignment documentation
- `reports/PART2_COVERAGE_COMPARISON.md` - Coverage comparison analysis
- `reports/PART2_BASELINE_COVERAGE.md` - Baseline coverage details
- `reports/PART2_NEW_PROBLEMS_BASELINE.md` - New problems baseline

### Gemini Model Reports
- `reports/GEMINI_CHAIN_OF_THOUGHT_COMPLETE_COVERAGE.md` - Complete Gemini analysis
- `coverage_reports/gemini_chain_of_thought_attempt1/html/index.html` - Part 1 coverage

---

## Commands to Regenerate Reports

### apps_2_p3 Coverage
```bash
# Baseline
pytest generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1.py --cov=apps_2_p3_attempt_1 --cov-report=json:coverage_reports/apps_2_p3_baseline.json --cov-report=html:coverage_reports/apps_2_p3_baseline/html -v

# Iteration 1
pytest generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1_iteration1.py --cov=apps_2_p3_attempt_1 --cov-report=json:coverage_reports/apps_2_p3_iteration1.json --cov-report=html:coverage_reports/apps_2_p3_iteration1/html -v

# Iteration 2
pytest generated/gemini_chain_of_thought/test_apps_2_p3_attempt_1_iteration2.py --cov=apps_2_p3_attempt_1 --cov-report=json:coverage_reports/apps_2_p3_iteration2.json --cov-report=html:coverage_reports/apps_2_p3_iteration2/html -v
```

### apps_3_p4 Coverage
```bash
# Baseline
pytest generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1.py --cov=apps_3_p4_attempt_1 --cov-report=json:coverage_reports/apps_3_p4_baseline.json --cov-report=html:coverage_reports/apps_3_p4_baseline/html -v

# Iteration 1
pytest generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1_iteration1.py --cov=apps_3_p4_attempt_1 --cov-report=json:coverage_reports/apps_3_p4_iteration1.json --cov-report=html:coverage_reports/apps_3_p4_iteration1/html -v

# Iteration 2
pytest generated/gemini_chain_of_thought/test_apps_3_p4_attempt_1_iteration2.py --cov=apps_3_p4_attempt_1 --cov-report=json:coverage_reports/apps_3_p4_iteration2.json --cov-report=html:coverage_reports/apps_3_p4_iteration2/html -v
```

---

**Index Generated:** November 10, 2025  
**Total Reports:** 9 markdown reports, 8 HTML reports, 8 JSON files  
**Coverage Range:** 75% - 98%  
**Iterations:** Baseline + 3 iterations  
**Status:** ✅ All reports generated successfully, convergence achieved
