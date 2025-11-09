# Branch Coverage Explanation

**Generated:** 2025-11-09

## ✅ Branch Coverage IS Being Generated!

Your pytest configuration is correctly set up to generate branch coverage. Here's what you need to know:

## 📊 Understanding the Coverage Report

### What the Numbers Mean

When you run pytest with coverage, you see columns like this:

```
Name                                    Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------------------
humaneval_0_p1_attempt_1.py                7      0      4      0   100%
humaneval_1_p2_attempt_1.py                5      0      0      0   100%
```

**Column Definitions:**
- **Stmts**: Total number of executable statements
- **Miss**: Number of statements not executed
- **Branch**: Total number of branch points (if/else, loops, etc.)
- **BrPart**: Partially covered branches (one path taken, other not)
- **Cover**: Overall coverage percentage

### Branch Coverage Examples

#### Example 1: Function with Branches (4 branches)
```python
def has_close_elements(numbers, threshold):
    for i in range(len(numbers)):           # Branch 1: loop entry
        for j in range(i + 1, len(numbers)): # Branch 2: nested loop entry
            if abs(numbers[i] - numbers[j]) < threshold:  # Branch 3: if True
                return True                  # Branch 4: if False
    return False
```
**Coverage:** Stmts: 7, Branches: 4

#### Example 2: Simple Function (0 branches)
```python
def truncate_number(number):
    return number % 1
```
**Coverage:** Stmts: 3, Branches: 0 (no if/else or loops)

## 🎯 Why Overall Coverage is 33%

The **33% overall coverage** is because:

1. **Only Attempt 1 files are tested** - You're running tests with `-k "attempt_1"`
2. **Attempts 2 and 3 are NOT executed** - These files have 0% coverage
3. **Coverage includes ALL files** in the directory

### Breakdown:
- **Attempt 1 files:** 100% coverage (all executed)
- **Attempt 2 files:** 0% coverage (not tested)
- **Attempt 3 files:** 0% coverage (not tested)
- **Average:** (100% + 0% + 0%) / 3 = 33%

## 📈 How to See Branch Coverage Details

### 1. Terminal Output
When you run pytest, branch coverage shows in the terminal:
```bash
pytest generated/groq_chain_of_thought/ -k "attempt_1" \
  --cov=generated/groq_chain_of_thought \
  --cov-branch \
  --cov-report=term
```

Look for the "Branch" and "BrPart" columns in the output.

### 2. HTML Report (RECOMMENDED)
The HTML report shows branch coverage visually:

```bash
# Open this file in your browser:
coverage_reports/groq_chain_of_thought_attempt1/html/index.html
```

**What you'll see:**
- Green highlighting: Code executed
- Red highlighting: Code not executed
- Yellow highlighting: Partial branch coverage
- Branch indicators: Shows which branches were taken

### 3. Detailed View
Click on any file in the HTML report to see:
- Line-by-line coverage
- Branch coverage indicators (e.g., "2 of 4 branches taken")
- Which specific branches were missed

## 🔍 Example: Viewing Branch Coverage in HTML

1. Open `coverage_reports/groq_chain_of_thought_attempt1/html/index.html`
2. Click on a file like `humaneval_0_p1_attempt_1.py`
3. Look for annotations like:
   - `branch 0 taken` - This branch was executed
   - `branch 1 not taken` - This branch was NOT executed
   - Yellow highlighting - Partial branch coverage

## ✅ All 10 Problems ARE Evaluated

Your test run shows:
```
✅ Problem 1 (HumanEval 0) - PASSED - 5 test cases
❌ Problem 2 (HumanEval 1) - FAILED - 3 test cases
✅ Problem 3 (HumanEval 2) - PASSED - 3 test cases
✅ Problem 4 (HumanEval 3) - PASSED - 4 test cases
✅ Problem 5 (HumanEval 4) - PASSED - 3 test cases
✅ Problem 6 (HumanEval 5) - PASSED - 3 test cases
✅ Problem 7 (HumanEval 6) - PASSED - 3 test cases
✅ Problem 8 (HumanEval 7) - PASSED - 4 test cases
✅ Problem 9 (HumanEval 8) - PASSED - 4 test cases
❌ Problem 10 (HumanEval 9) - FAILED - 5 test cases
```

**Total:** 10 problems, 37 test cases, 8 passed (80%), 2 failed (20%)

## 📝 Individual Test Case Results

Each problem has multiple test cases (assertions). For example:

**Problem 1 - has_close_elements (5 test cases):**
1. ✅ `assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False`
2. ✅ `assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True`
3. ✅ `assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True`
4. ✅ `assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False`
5. ✅ `assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True`

All 5 test cases passed! ✅

## 🛠️ How to Run Analysis

### Quick Analysis (Console Output)
```bash
python detailed_test_case_analysis.py groq_chain_of_thought 1
```

### Generate Full Report
```bash
python detailed_test_case_analysis.py groq_chain_of_thought 1
# Report saved to: reports/detailed_test_cases/groq_chain_of_thought_attempt1_detailed.md
```

### View HTML Coverage Report
```bash
# Windows
start coverage_reports/groq_chain_of_thought_attempt1/html/index.html

# Or just open the file in your browser
```

## 🎯 Summary

1. ✅ **Branch coverage IS working** - It's shown in the "Branch" column
2. ✅ **All 10 problems ARE evaluated** - Each problem has 3-5 test cases
3. ✅ **Individual test cases ARE tracked** - See detailed report for each assertion
4. ⚠️ **33% coverage is expected** - Because only attempt 1 is tested (attempts 2 & 3 are 0%)

## 📊 To Get 100% Coverage

If you want to see 100% coverage, test only attempt 1 files:

```bash
pytest generated/groq_chain_of_thought/ \
  -k "attempt_1" \
  --cov=generated/groq_chain_of_thought \
  --cov-branch \
  --cov-report=term \
  --cov-report=html:coverage_reports/groq_chain_of_thought_attempt1/html
```

The individual files will show 100% coverage, but the total will be 33% because it includes all attempts.

## 🔗 Related Reports

- **Detailed Test Case Analysis:** `reports/detailed_test_cases/groq_chain_of_thought_attempt1_detailed.md`
- **HTML Coverage Report:** `coverage_reports/groq_chain_of_thought_attempt1/html/index.html`
- **Model Comparison:** `reports/model_analysis/MODEL_COMPARISON_SUMMARY.md`

---
*Your pytest configuration is correct and branch coverage is working as expected!*
