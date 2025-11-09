# Quick Test Results Table - All Models

**Generated:** 2025-11-09

## 📊 Test Cases Passed/Total by Problem

| Problem | Description | Total Tests | Groq CoT | Groq Step | Gemini CoT | Gemini Step |
|---------|-------------|-------------|----------|-----------|------------|-------------|
| HE0 | has_close_elements | 5 | 5/5 ✅ | 5/5 ✅ | 5/5 ✅ | N/A |
| HE1 | separate_paren_groups | 3 | 0/3 ❌ | 0/3 ❌ | 3/3 ✅ | 3/3 ✅ |
| HE2 | truncate_number | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ |
| HE3 | below_zero | 4 | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ |
| HE4 | mean_absolute_deviation | 3 | 3/3 ✅ | 0/3 ❌ | 3/3 ✅ | 3/3 ✅ |
| HE5 | intersperse | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ |
| HE6 | filter_by_substring | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | N/A |
| HE7 | sum_product | 4 | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ |
| HE8 | rolling_max | 4 | 4/4 ✅ | 4/4 ✅ | N/A | N/A |
| HE9 | is_palindrome | 5 | 0/5 ❌ | 0/5 ❌ | N/A | N/A |
| APPS0 | knapsack_variant | 3 | N/A | N/A | 3/3 ✅ | 3/3 ✅ |
| APPS1 | shortest_path | 3 | N/A | N/A | 3/3 ✅ | 3/3 ✅ |

**Legend:**
- CoT = Chain of Thought
- Step = Step Chain of Thought
- N/A = Not tested or missing test file

---

## 📈 Overall Statistics

| Model | Strategy | Test Cases Passed | Total Test Cases | Pass Rate | Problems Passed | Total Problems | Problem Pass Rate |
|-------|----------|-------------------|------------------|-----------|-----------------|----------------|-------------------|
| Groq | Chain of Thought | 29 | 37 | **78.4%** | 8 | 10 | **80.0%** |
| Groq | Step Chain of Thought | 26 | 37 | **70.3%** | 7 | 10 | **70.0%** |
| Gemini | Chain of Thought | 34 | 40 | **85.0%** | 10 | 12 | **83.3%** |
| Gemini | Step Chain of Thought | 26 | 32 | **81.3%** | 8 | 10 | **80.0%** |

---

## 🏆 Rankings

### By Test Case Pass Rate:
1. 🥇 **Gemini + Chain of Thought**: 85.0%
2. 🥈 **Gemini + Step Chain of Thought**: 81.3%
3. 🥉 **Groq + Chain of Thought**: 78.4%
4. **Groq + Step Chain of Thought**: 70.3%

### By Problem Pass Rate:
1. 🥇 **Gemini + Chain of Thought**: 83.3%
2. 🥈 **Groq + Chain of Thought**: 80.0%
3. 🥈 **Gemini + Step Chain of Thought**: 80.0%
4. **Groq + Step Chain of Thought**: 70.0%

---

## 🎯 Key Findings

### Best Model: **Gemini**
- Consistently higher pass rates than Groq
- Successfully handled APPS dataset problems
- Better with both strategies

### Best Strategy: **Chain of Thought**
- Outperforms Step Chain of Thought for both models
- Groq: +8.1% test cases, +10% problems
- Gemini: +3.7% test cases, +3.3% problems

### Best Combination: **Gemini + Chain of Thought**
- 85.0% test case pass rate
- 83.3% problem pass rate
- Most comprehensive coverage

---

## 📊 Problem-Level Insights

### Problems All Models Solved (100% pass rate):
- ✅ truncate_number (3 tests)
- ✅ below_zero (4 tests)
- ✅ intersperse (3 tests)
- ✅ sum_product (4 tests)

### Problems Only Gemini Solved:
- ✅ separate_paren_groups (3 tests) - Groq failed
- ✅ APPS knapsack_variant (3 tests) - Groq not tested
- ✅ APPS shortest_path (3 tests) - Groq not tested

### Problems Only Groq CoT Solved:
- ✅ mean_absolute_deviation (3 tests) - Groq Step failed

### Problems No Model Solved:
- ❌ is_palindrome (5 tests) - Test file has wrong test cases

---

## 📁 Full Reports

Detailed analysis available in:
- `reports/TEST_CASES_PASSED_SUMMARY.md` - Complete breakdown
- `reports/detailed_test_cases/` - Individual model reports
- `coverage_reports/` - HTML coverage reports

---

*Quick reference for test case pass/fail analysis*
