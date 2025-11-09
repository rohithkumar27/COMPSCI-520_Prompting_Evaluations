# Complete Model Test Summary

**Generated:** 2025-11-06

## 📊 Overall Model Performance Comparison

| Model | Test Files | Passed | Failed | Pass Rate | Total Test Cases | Avg Tests/File |
|-------|------------|--------|--------|-----------|------------------|----------------|
| **GROQ Chain of Thought** | 10 | 8 | 2 | **66.7%** | 45 | 3.8 |
| **GROQ Step Chain of Thought** | 10 | 7 | 3 | **53.8%** | 48 | 3.7 |
| **Gemini Chain of Thought** | 8 | - | - | **ERROR** | - | - |
| **Gemini Step Chain of Thought** | 0 | - | - | **NO TESTS** | - | - |

## 🎯 Detailed Results

### 1. GROQ Chain of Thought ✅

**Performance:** 66.7% pass rate (8/12 files passed)

| Problem | Test File | Status | Test Cases |
|---------|-----------|--------|------------|
| humaneval_0 | test_humaneval_0_p1_attempt_1.py | ✅ PASSED | 5 |
| humaneval_1 | test_humaneval_1_p2_attempt_1.py | ❌ FAILED | 3 |
| humaneval_2 | test_humaneval_2_p3_attempt_1.py | ✅ PASSED | 3 |
| humaneval_3 | test_humaneval_3_p4_attempt_1.py | ✅ PASSED | 4 |
| humaneval_4 | test_humaneval_4_p5_attempt_1.py | ✅ PASSED | 3 |
| humaneval_5 | test_humaneval_5_p6_attempt_1.py | ✅ PASSED | 3 |
| humaneval_6 | test_humaneval_6_p7_attempt_1.py | ✅ PASSED | 3 |
| humaneval_7 | test_humaneval_7_p8_attempt_1.py | ✅ PASSED | 4 |
| humaneval_8 | test_humaneval_8_p9_attempt_1.py | ✅ PASSED | 4 |
| humaneval_9 | test_humaneval_9_p10_attempt_1.py | ❌ FAILED | 5 |

**Failed Problems:**
- `humaneval_1` - separate_paren_groups (parsing issue)
- `humaneval_9` - is_palindrome (return type mismatch)

---

### 2. GROQ Step Chain of Thought ⚠️

**Performance:** 53.8% pass rate (7/13 files passed)

| Problem | Test File | Status | Test Cases |
|---------|-----------|--------|------------|
| humaneval_0 | test_humaneval_0_p1_attempt_1.py | ✅ PASSED | 5 |
| humaneval_1 | test_humaneval_1_p2_attempt_1.py | ❌ FAILED | 3 |
| humaneval_2 | test_humaneval_2_p3_attempt_1.py | ✅ PASSED | 3 |
| humaneval_3 | test_humaneval_3_p4_attempt_1.py | ✅ PASSED | 4 |
| humaneval_4 | test_humaneval_4_p5_attempt_1.py | ❌ FAILED | 3 |
| humaneval_5 | test_humaneval_5_p6_attempt_1.py | ✅ PASSED | 3 |
| humaneval_6 | test_humaneval_6_p7_attempt_1.py | ✅ PASSED | 3 |
| humaneval_7 | test_humaneval_7_p8_attempt_1.py | ✅ PASSED | 4 |
| humaneval_8 | test_humaneval_8_p9_attempt_1.py | ✅ PASSED | 4 |
| humaneval_9 | test_humaneval_9_p10_attempt_1.py | ❌ FAILED | 5 |

**Failed Problems:**
- `humaneval_1` - separate_paren_groups (returns empty strings)
- `humaneval_4` - mean_absolute_deviation (calculation error)
- `humaneval_9` - is_palindrome (return type mismatch)

---

### 3. Gemini Chain of Thought ❌

**Performance:** Collection errors - tests cannot run

**Issues:**
- `test_apps_0_p1_attempt_1.py` - AssertionError during collection (Expected 14, got None)
- `test_apps_1_p2_attempt_1.py` - NameError: 'deque' not defined (missing import)

**Status:** Tests have syntax/import errors that prevent execution

---

### 4. Gemini Step Chain of Thought ❌

**Performance:** No test files found

**Status:** No attempt_1 test files exist in this directory

---

## 📈 Key Insights

### Best Performing Model
🏆 **GROQ Chain of Thought** - 66.7% pass rate with 8/10 successful implementations

### Most Challenging Problems
❌ **humaneval_9 (is_palindrome)** - Failed in both GROQ models
❌ **humaneval_1 (separate_paren_groups)** - Failed in both GROQ models

### Most Successful Problems
✅ **humaneval_0, 2, 3, 5, 6, 7, 8** - Passed in both GROQ models

## 🔧 Commands Used

```bash
# GROQ Chain of Thought
python detailed_test_analysis.py --directory groq_chain_of_thought

# GROQ Step Chain of Thought  
python detailed_test_analysis.py --directory groq_step_chain_of_thought

# Gemini Chain of Thought
pytest generated/gemini_chain_of_thought/ -k "attempt_1" -v --tb=line --no-cov

# Gemini Step Chain of Thought
python detailed_test_analysis.py --directory gemini_step_chain_of_thought
```

## 📊 Summary Statistics

- **Total Models Tested:** 4
- **Fully Functional:** 2 (GROQ models)
- **With Errors:** 1 (Gemini CoT)
- **No Tests:** 1 (Gemini Step CoT)
- **Total Test Cases (GROQ only):** 93
- **Total Passed (GROQ only):** 60 (64.5%)
- **Total Failed (GROQ only):** 33 (35.5%)

---

*Report generated from pytest analysis and detailed test case breakdown*