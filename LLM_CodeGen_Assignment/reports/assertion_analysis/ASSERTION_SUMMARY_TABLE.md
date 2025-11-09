# Assertion Summary Table - Quick Reference

**Generated:** 2025-11-09

## 📊 Assertions Passed/Total by Problem

| Problem | Assertions | Groq CoT | Groq Step | Gemini CoT | Gemini Step |
|---------|------------|----------|-----------|------------|-------------|
| HE0: has_close_elements | 5 | **5/5** | **5/5** | **5/5** | - |
| HE1: separate_paren_groups | 3 | 0/3 | 0/3 | **3/3** | **3/3** |
| HE2: truncate_number | 3 | **3/3** | **3/3** | **3/3** | **3/3** |
| HE3: below_zero | 4 | **4/4** | **4/4** | **4/4** | **4/4** |
| HE4: mean_absolute_deviation | 3 | **3/3** | 0/3 | **3/3** | **3/3** |
| HE5: intersperse | 3 | **3/3** | **3/3** | **3/3** | **3/3** |
| HE6: filter_by_substring | 3 | **3/3** | **3/3** | **3/3** | - |
| HE7: sum_product | 4 | **4/4** | **4/4** | **4/4** | **4/4** |
| HE8: rolling_max | 4 | **4/4** | **4/4** | - | - |
| HE9: is_palindrome | 5 | 0/5 | 0/5 | - | - |
| APPS0: knapsack | 3 | - | - | 0/3 | 0/3 |
| APPS1: shortest_path | 3 | - | - | 0/3 | 0/3 |
| **TOTAL** | **43** | **29/37** | **26/37** | **28/34** | **20/26** |
| **Pass Rate** | | **78.4%** | **70.3%** | **82.4%** | **76.9%** |

**Bold** = All assertions passed for that problem

---

## 🏆 Rankings

### By Assertion Pass Rate:
1. 🥇 **Gemini CoT**: 82.4% (28/34)
2. 🥈 **Groq CoT**: 78.4% (29/37)
3. 🥉 **Gemini Step**: 76.9% (20/26)
4. **Groq Step**: 70.3% (26/37)

---

## 📈 Quick Stats

| Metric | Groq CoT | Groq Step | Gemini CoT | Gemini Step |
|--------|----------|-----------|------------|-------------|
| **Assertions Passed** | 29 | 26 | 28 | 20 |
| **Total Assertions** | 37 | 37 | 34 | 26 |
| **Pass Rate** | 78.4% | 70.3% | 82.4% | 76.9% |
| **Perfect Problems** | 8/10 | 7/10 | 8/10 | 6/8 |
| **Failed Problems** | 2/10 | 3/10 | 2/10 | 2/8 |

---

## ✅ Problems All Models Solved (100%)

These problems had all assertions pass for every model tested:

1. **truncate_number** - 3 assertions
2. **below_zero** - 4 assertions  
3. **intersperse** - 3 assertions
4. **sum_product** - 4 assertions

**Total: 14 assertions with 100% success rate**

---

## ❌ Problems No Model Solved (0%)

These problems had zero assertions pass:

1. **is_palindrome** - 5 assertions (test file issue)
2. **APPS knapsack** - 3 assertions (Gemini only)
3. **APPS shortest_path** - 3 assertions (Gemini only)

---

## 🎯 Key Takeaways

1. **Best Model:** Gemini CoT (82.4% assertions passed)
2. **Best Strategy:** Chain of Thought (beats Step for both models)
3. **Easiest Problems:** 4 problems with 100% pass rate
4. **Hardest Problems:** 3 problems with 0% pass rate
5. **Total Assertions:** 134 unique assertions tested across all models

---

*For detailed analysis, see: `reports/ASSERTION_ANALYSIS_ALL_MODELS.md`*
