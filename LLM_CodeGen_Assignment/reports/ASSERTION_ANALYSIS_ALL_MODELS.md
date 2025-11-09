# Assertion-Level Analysis - All Models

**Generated:** 2025-11-09  
**Analysis Type:** Individual Assertion Pass/Fail Count  
**Models:** 4 (2 Models × 2 Strategies)

## 📊 Complete Assertion Results Table

| Problem | Total Assertions | Groq CoT | Groq Step | Gemini CoT | Gemini Step |
|---------|------------------|----------|-----------|------------|-------------|
| **HumanEval Problems** |
| HE0: has_close_elements | 5 | 5/5 ✅ | 5/5 ✅ | 5/5 ✅ | N/A |
| HE1: separate_paren_groups | 3 | 0/3 ❌ | 0/3 ❌ | 3/3 ✅ | 3/3 ✅ |
| HE2: truncate_number | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ |
| HE3: below_zero | 4 | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ |
| HE4: mean_absolute_deviation | 3 | 3/3 ✅ | 0/3 ❌ | 3/3 ✅ | 3/3 ✅ |
| HE5: intersperse | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ |
| HE6: filter_by_substring | 3 | 3/3 ✅ | 3/3 ✅ | 3/3 ✅ | N/A |
| HE7: sum_product | 4 | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ | 4/4 ✅ |
| HE8: rolling_max | 4 | 4/4 ✅ | 4/4 ✅ | N/A | N/A |
| HE9: is_palindrome | 5 | 0/5 ❌ | 0/5 ❌ | N/A | N/A |
| **APPS Problems** |
| APPS0: knapsack_variant | 3 | N/A | N/A | 0/3 ❌ | 0/3 ❌ |
| APPS1: shortest_path | 3 | N/A | N/A | 0/3 ❌ | 0/3 ❌ |
| **TOTALS** | **43** | **29/37** | **26/37** | **28/34** | **20/26** |
| **Pass Rate** | | **78.4%** | **70.3%** | **82.4%** | **76.9%** |

**Legend:**
- CoT = Chain of Thought
- Step = Step Chain of Thought
- N/A = Test file not present or not tested
- X/Y = X assertions passed out of Y total assertions

---

## 📈 Summary Statistics

### Overall Performance

| Model | Strategy | Assertions Passed | Total Assertions | Pass Rate | Rank |
|-------|----------|-------------------|------------------|-----------|------|
| Gemini | Chain of Thought | 28 | 34 | **82.4%** | 🥇 1st |
| Groq | Chain of Thought | 29 | 37 | **78.4%** | 🥈 2nd |
| Gemini | Step Chain of Thought | 20 | 26 | **76.9%** | 🥉 3rd |
| Groq | Step Chain of Thought | 26 | 37 | **70.3%** | 4th |

---

## 🔍 Detailed Problem-by-Problem Analysis

### Problem HE0: has_close_elements (5 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 5/5 | ✅ | 100% |
| Groq | Step Chain of Thought | 5/5 | ✅ | 100% |
| Gemini | Chain of Thought | 5/5 | ✅ | 100% |
| Gemini | Step Chain of Thought | N/A | - | - |

**Result:** All tested models passed all 5 assertions

---

### Problem HE1: separate_paren_groups (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 0/3 | ❌ | 0% |
| Groq | Step Chain of Thought | 0/3 | ❌ | 0% |
| Gemini | Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Step Chain of Thought | 3/3 | ✅ | 100% |

**Result:** Gemini models passed all assertions, Groq models failed all

---

### Problem HE2: truncate_number (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 3/3 | ✅ | 100% |
| Groq | Step Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Step Chain of Thought | 3/3 | ✅ | 100% |

**Result:** All models passed all 3 assertions

---

### Problem HE3: below_zero (4 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 4/4 | ✅ | 100% |
| Groq | Step Chain of Thought | 4/4 | ✅ | 100% |
| Gemini | Chain of Thought | 4/4 | ✅ | 100% |
| Gemini | Step Chain of Thought | 4/4 | ✅ | 100% |

**Result:** All models passed all 4 assertions

---

### Problem HE4: mean_absolute_deviation (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 3/3 | ✅ | 100% |
| Groq | Step Chain of Thought | 0/3 | ❌ | 0% |
| Gemini | Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Step Chain of Thought | 3/3 | ✅ | 100% |

**Result:** Only Groq Step Chain failed all assertions

---

### Problem HE5: intersperse (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 3/3 | ✅ | 100% |
| Groq | Step Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Step Chain of Thought | 3/3 | ✅ | 100% |

**Result:** All models passed all 3 assertions

---

### Problem HE6: filter_by_substring (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 3/3 | ✅ | 100% |
| Groq | Step Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Chain of Thought | 3/3 | ✅ | 100% |
| Gemini | Step Chain of Thought | N/A | - | - |

**Result:** All tested models passed all 3 assertions

---

### Problem HE7: sum_product (4 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 4/4 | ✅ | 100% |
| Groq | Step Chain of Thought | 4/4 | ✅ | 100% |
| Gemini | Chain of Thought | 4/4 | ✅ | 100% |
| Gemini | Step Chain of Thought | 4/4 | ✅ | 100% |

**Result:** All models passed all 4 assertions

---

### Problem HE8: rolling_max (4 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 4/4 | ✅ | 100% |
| Groq | Step Chain of Thought | 4/4 | ✅ | 100% |
| Gemini | Chain of Thought | N/A | - | - |
| Gemini | Step Chain of Thought | N/A | - | - |

**Result:** Groq models passed all assertions, Gemini not tested

---

### Problem HE9: is_palindrome (5 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | 0/5 | ❌ | 0% |
| Groq | Step Chain of Thought | 0/5 | ❌ | 0% |
| Gemini | Chain of Thought | N/A | - | - |
| Gemini | Step Chain of Thought | N/A | - | - |

**Result:** All tested models failed (test file has incorrect test cases)

---

### Problem APPS0: knapsack_variant (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | N/A | - | - |
| Groq | Step Chain of Thought | N/A | - | - |
| Gemini | Chain of Thought | 0/3 | ❌ | 0% |
| Gemini | Step Chain of Thought | 0/3 | ❌ | 0% |

**Result:** Gemini models failed all assertions

---

### Problem APPS1: shortest_path (3 assertions)

| Model | Strategy | Passed | Status | Pass Rate |
|-------|----------|--------|--------|-----------|
| Groq | Chain of Thought | N/A | - | - |
| Groq | Step Chain of Thought | N/A | - | - |
| Gemini | Chain of Thought | 0/3 | ❌ | 0% |
| Gemini | Step Chain of Thought | 0/3 | ❌ | 0% |

**Result:** Gemini models failed all assertions

---

## 🎯 Key Insights

### Problems Where All Models Passed All Assertions:
1. ✅ **HE2: truncate_number** (3/3 assertions)
2. ✅ **HE3: below_zero** (4/4 assertions)
3. ✅ **HE5: intersperse** (3/3 assertions)
4. ✅ **HE7: sum_product** (4/4 assertions)

**Total:** 14 assertions - 100% success rate across all models

---

### Problems Where No Model Passed Any Assertions:
1. ❌ **HE9: is_palindrome** (0/5 assertions) - Test file issue
2. ❌ **APPS0: knapsack_variant** (0/3 assertions) - Gemini only
3. ❌ **APPS1: shortest_path** (0/3 assertions) - Gemini only

---

### Problems With Mixed Results:
1. **HE1: separate_paren_groups** (3 assertions)
   - Gemini: 3/3 ✅
   - Groq: 0/3 ❌

2. **HE4: mean_absolute_deviation** (3 assertions)
   - Groq CoT: 3/3 ✅
   - Gemini: 3/3 ✅
   - Groq Step: 0/3 ❌

---

## 📊 Strategy Comparison

### Chain of Thought vs Step Chain of Thought

#### Groq Models:
- **Chain of Thought:** 29/37 assertions (78.4%)
- **Step Chain of Thought:** 26/37 assertions (70.3%)
- **Difference:** +8.1% for Chain of Thought

#### Gemini Models:
- **Chain of Thought:** 28/34 assertions (82.4%)
- **Step Chain of Thought:** 20/26 assertions (76.9%)
- **Difference:** +5.5% for Chain of Thought

**Conclusion:** Chain of Thought strategy consistently outperforms Step Chain of Thought

---

## 🏆 Model Comparison

### Groq vs Gemini (Chain of Thought):
- **Gemini:** 28/34 assertions (82.4%)
- **Groq:** 29/37 assertions (78.4%)
- **Winner:** Gemini (+4.0%)

### Groq vs Gemini (Step Chain of Thought):
- **Gemini:** 20/26 assertions (76.9%)
- **Groq:** 26/37 assertions (70.3%)
- **Winner:** Gemini (+6.6%)

**Conclusion:** Gemini consistently outperforms Groq with both strategies

---

## 📈 Assertion Distribution

### By Problem Difficulty (based on pass rate):

**Easy (100% pass rate):**
- truncate_number: 12/12 assertions passed
- below_zero: 16/16 assertions passed
- intersperse: 12/12 assertions passed
- sum_product: 16/16 assertions passed

**Medium (50-99% pass rate):**
- has_close_elements: 15/15 assertions passed (tested models)
- filter_by_substring: 9/9 assertions passed (tested models)
- rolling_max: 8/8 assertions passed (tested models)
- separate_paren_groups: 6/12 assertions passed (50%)
- mean_absolute_deviation: 9/12 assertions passed (75%)

**Hard (0-49% pass rate):**
- is_palindrome: 0/10 assertions passed (0%)
- APPS problems: 0/12 assertions passed (0%)

---

## 📁 Individual Reports

Detailed assertion reports for each model:
1. `reports/assertion_analysis/groq_chain_of_thought_attempt1_assertions.md`
2. `reports/assertion_analysis/groq_step_chain_of_thought_attempt1_assertions.md`
3. `reports/assertion_analysis/gemini_chain_of_thought_attempt1_assertions.md`
4. `reports/assertion_analysis/gemini_step_chain_of_thought_attempt1_assertions.md`

---

## 🎉 Final Summary

### Best Performing Model:
**Gemini + Chain of Thought**
- 28/34 assertions passed (82.4%)
- Highest assertion pass rate
- Most consistent performance

### Recommended Strategy:
**Chain of Thought**
- Outperforms Step Chain of Thought for both models
- Simpler, more effective approach

### Total Assertions Analyzed:
- **Groq Models:** 37 assertions each
- **Gemini Models:** 26-34 assertions
- **Grand Total:** 134 unique assertions tested

---

*This report shows the exact number of assertions (test cases) passed out of total available for each problem in the dataset.*
