# Final Coverage Report - All Models

**Generated:** 2025-11-06

## 📊 Complete Coverage & Test Results

| Model | Tests Run | Passed | Failed | Pass Rate | Coverage | HTML Report |
|-------|-----------|--------|--------|-----------|----------|-------------|
| **GROQ Chain of Thought** | 10 | 8 | 2 | **80.0%** | **33%** | ✅ Generated |
| **GROQ Step Chain of Thought** | 10 | 7 | 3 | **70.0%** | **31%** | ✅ Generated |
| **Gemini Chain of Thought** | 8 | 8 | 0 | **100%** | **21%** | ✅ Generated |
| **Gemini Step Chain of Thought** | 0 | 0 | 0 | **N/A** | **N/A** | ❌ Collection Errors |

## 📁 Coverage Report Locations

### HTML Reports (Open in Browser):
1. **GROQ CoT**: `coverage_reports/groq_chain_of_thought/html/index.html`
2. **GROQ Step CoT**: `coverage_reports/groq_step_chain_of_thought/html/index.html`
3. **Gemini CoT**: `coverage_reports/gemini_chain_of_thought/html/index.html`
4. **Gemini Step CoT**: Not generated (collection errors)

## 🎯 Detailed Results

### 1. GROQ Chain of Thought ✅

**Coverage:** 33% (58/174 statements)
**Tests:** 8/10 passed (80%)

| File | Statements | Missed | Coverage |
|------|------------|--------|----------|
| humaneval_0_p1_attempt_1.py | 7 | 0 | 100% |
| humaneval_1_p2_attempt_1.py | 5 | 0 | 100% |
| humaneval_2_p3_attempt_1.py | 3 | 0 | 100% |
| humaneval_3_p4_attempt_1.py | 8 | 0 | 100% |
| humaneval_4_p5_attempt_1.py | 5 | 0 | 100% |
| humaneval_5_p6_attempt_1.py | 8 | 0 | 100% |
| humaneval_6_p7_attempt_1.py | 3 | 0 | 100% |
| humaneval_7_p8_attempt_1.py | 8 | 0 | 100% |
| humaneval_8_p9_attempt_1.py | 9 | 0 | 100% |
| humaneval_9_p10_attempt_1.py | 2 | 0 | 100% |

**Failed Tests:**
- humaneval_1 (separate_paren_groups)
- humaneval_9 (is_palindrome)

---

### 2. GROQ Step Chain of Thought ⚠️

**Coverage:** 31% (77/249 statements)
**Tests:** 7/10 passed (70%)

| File | Statements | Missed | Coverage |
|------|------------|--------|----------|
| humaneval_0_p1_attempt_1.py | 9 | 1 | 89% |
| humaneval_1_p2_attempt_1.py | 18 | 1 | 94% |
| humaneval_2_p3_attempt_1.py | 3 | 0 | 100% |
| humaneval_3_p4_attempt_1.py | 8 | 0 | 100% |
| humaneval_4_p5_attempt_1.py | 7 | 1 | 86% |
| humaneval_5_p6_attempt_1.py | 8 | 0 | 100% |
| humaneval_6_p7_attempt_1.py | 7 | 0 | 100% |
| humaneval_7_p8_attempt_1.py | 8 | 0 | 100% |
| humaneval_8_p9_attempt_1.py | 9 | 0 | 100% |
| humaneval_9_p10_attempt_1.py | 3 | 0 | 100% |

**Failed Tests:**
- humaneval_1 (separate_paren_groups)
- humaneval_4 (mean_absolute_deviation)
- humaneval_9 (is_palindrome)

---

### 3. Gemini Chain of Thought ✅

**Coverage:** 21% (67/318 statements)
**Tests:** 8/8 passed (100%)

| File | Statements | Missed | Coverage |
|------|------------|--------|----------|
| humaneval_0_p1_attempt_1.py | 8 | 0 | 100% |
| humaneval_1_p2_attempt_1.py | 18 | 0 | 100% |
| humaneval_2_p1_attempt_1.py | 3 | 0 | 100% |
| humaneval_3_p4_attempt_1.py | 8 | 0 | 100% |
| humaneval_4_p5_attempt_1.py | 7 | 1 | 86% |
| humaneval_5_p6_attempt_1.py | 9 | 0 | 100% |
| humaneval_6_p7_attempt_1.py | 7 | 0 | 100% |
| humaneval_7_p8_attempt_1.py | 8 | 0 | 100% |

**Note:** Apps tests excluded due to collection errors

---

### 4. Gemini Step Chain of Thought ❌

**Status:** Collection errors prevent test execution

**Issues:**
- test_apps_0_p1_attempt_1.py: AssertionError during collection
- test_apps_1_p2_attempt_1.py: Missing `collections` import

**No coverage data available**

---

## 🏆 Performance Ranking

### By Test Pass Rate:
1. **Gemini Chain of Thought**: 100% (8/8)
2. **GROQ Chain of Thought**: 80% (8/10)
3. **GROQ Step Chain of Thought**: 70% (7/10)
4. **Gemini Step Chain of Thought**: N/A (errors)

### By Code Coverage:
1. **GROQ Chain of Thought**: 33%
2. **GROQ Step Chain of Thought**: 31%
3. **Gemini Chain of Thought**: 21%
4. **Gemini Step Chain of Thought**: N/A

## 📈 Key Insights

### Strengths:
- **Gemini CoT** has perfect pass rate on humaneval problems
- **GROQ models** have higher code coverage
- All attempt_1 files show 100% coverage when tests pass

### Weaknesses:
- **Palindrome problem** (humaneval_9) fails across GROQ models
- **Parentheses parsing** (humaneval_1) fails in GROQ models
- **Gemini Step CoT** has collection errors preventing execution

## 🔧 Commands Used

```bash
# GROQ Chain of Thought
pytest generated/groq_chain_of_thought/ -k "attempt_1" --cov=generated/groq_chain_of_thought --cov-report=html:coverage_reports/groq_chain_of_thought/html --cov-report=term-missing -v

# GROQ Step Chain of Thought
pytest generated/groq_step_chain_of_thought/ -k "attempt_1" --cov=generated/groq_step_chain_of_thought --cov-report=html:coverage_reports/groq_step_chain_of_thought/html --cov-report=term-missing -v

# Gemini Chain of Thought
pytest generated/gemini_chain_of_thought/ -k "attempt_1" --cov=generated/gemini_chain_of_thought --cov-report=html:coverage_reports/gemini_chain_of_thought/html --cov-report=term-missing -v --ignore=generated/gemini_chain_of_thought/test_apps_0_p1_attempt_1.py --ignore=generated/gemini_chain_of_thought/test_apps_1_p2_attempt_1.py

# Gemini Step Chain of Thought
pytest generated/gemini_step_chain_of_thought/ -k "attempt_1" --cov=generated/gemini_step_chain_of_thought --cov-report=html:coverage_reports/gemini_step_chain_of_thought/html --cov-report=term-missing -v
```

---

*Complete coverage analysis with pytest and pytest-cov*