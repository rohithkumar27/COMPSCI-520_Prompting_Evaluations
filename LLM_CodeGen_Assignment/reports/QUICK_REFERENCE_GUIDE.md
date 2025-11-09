# Quick Reference Guide - Test Analysis & Coverage

**Last Updated:** 2025-11-09

## 🚀 Quick Commands

### Run Detailed Analysis for Any Model
```bash
python detailed_test_case_analysis.py <model_name> 1
```

**Available Models:**
- `groq_chain_of_thought`
- `groq_step_chain_of_thought`
- `gemini_chain_of_thought`
- `gemini_step_chain_of_thought`
- `enhanced_chain_of_thought`

### View Coverage Reports
```bash
# Open HTML coverage report in browser
start coverage_reports\<model_name>_attempt1\html\index.html
```

### Verify All 10 Problems Exist
```bash
# Count test files
dir generated\<model_name>\test_*_attempt_1.py

# Should show 10 files
```

## 📊 Understanding Your Results

### Test Results Summary
When you run the analysis, you'll see:

```
Total Problems: 10
✅ Passed: 8 (80.0%)
❌ Failed: 2 (20.0%)
Total Test Cases: 37
```

**What this means:**
- 10 problems were tested
- 8 problems passed all their test cases
- 2 problems failed at least one test case
- 37 total assertions were checked

### Coverage Numbers Explained

```
Total Coverage: 33%
Statements: 174 (Missed: 116)
Branches: 54 (Partial: 0)
```

**Why 33%?**
- Only attempt 1 files are tested (100% coverage)
- Attempt 2 files are NOT tested (0% coverage)
- Attempt 3 files are NOT tested (0% coverage)
- Average: (100% + 0% + 0%) / 3 = 33%

**This is EXPECTED and CORRECT!**

### Per-File Coverage

```
Name                          Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
humaneval_0_p1_attempt_1.py      7      0      4      0   100%
```

**Column Meanings:**
- **Stmts**: Total executable statements
- **Miss**: Statements not executed
- **Branch**: Total branch points (if/else, loops)
- **BrPart**: Partially covered branches
- **Cover**: Coverage percentage

## ✅ Your Questions Answered

### Q1: "How many test cases per problem are passed?"

**Answer:** See the detailed report for each problem:

```
Problem 1 - has_close_elements
✅ Test Case 1: assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
✅ Test Case 2: assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
✅ Test Case 3: assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
✅ Test Case 4: assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
✅ Test Case 5: assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True

Result: 5/5 test cases passed ✅
```

### Q2: "Are all 10 problems of attempt 1 evaluated?"

**Answer:** YES! ✅

Verification:
```bash
$ dir generated\groq_chain_of_thought\test_*_attempt_1.py
10 files found

$ python detailed_test_case_analysis.py groq_chain_of_thought 1
Total Problems: 10
```

All 10 problems are evaluated with detailed results.

### Q3: "Why is branch coverage not shown in the report?"

**Answer:** Branch coverage IS shown! ✅

**Where to find it:**

1. **Terminal Output** - "Branch" column:
```
Name                          Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
humaneval_0_p1_attempt_1.py      7      0      4      0   100%
                                              ↑      ↑
                                         Branches  Partial
```

2. **HTML Report** - Visual indicators:
   - Open: `coverage_reports/<model_name>_attempt1/html/index.html`
   - Click on any file
   - See branch coverage with color coding

3. **Detailed Report** - Per-problem breakdown:
```
Problem 1: has_close_elements
Coverage: 100%
Branches: 4 (Partial: 0)
```

## 📁 Generated Reports

After running analysis, you'll find:

### 1. Console Output
Immediate summary in your terminal showing:
- All 10 problems
- Pass/fail status
- Test case counts
- Coverage summary

### 2. Detailed Markdown Report
**Location:** `reports/detailed_test_cases/<model_name>_attempt1_detailed.md`

**Contains:**
- Executive summary
- Coverage summary
- Detailed problem breakdown
- Individual test case results
- Failure reasons for failed tests

### 3. HTML Coverage Report
**Location:** `coverage_reports/<model_name>_attempt1/html/index.html`

**Features:**
- Interactive file browser
- Line-by-line coverage
- Branch coverage visualization
- Color-coded coverage indicators

## 🎯 Example: Complete Analysis Workflow

### Step 1: Run Analysis
```bash
python detailed_test_case_analysis.py groq_chain_of_thought 1
```

### Step 2: Review Console Output
```
======================================================================
📊 TEST RESULTS SUMMARY
======================================================================

Total Problems: 10
✅ Passed: 8 (80.0%)
❌ Failed: 2 (20.0%)

======================================================================
📝 DETAILED PROBLEM BREAKDOWN
======================================================================

✅ Problem 1 (HumanEval 0)
   Function: test_has_close_elements
   Test Cases: 5
   Coverage: 100% (Stmts: 7, Branches: 4)

❌ Problem 2 (HumanEval 1)
   Function: test_separate_paren_groups
   Test Cases: 3
   Coverage: 100% (Stmts: 5, Branches: 0)
   ⚠️  Failure: AssertionError: assert ['( )', '( )', '( )', '( )'] == ...

[... continues for all 10 problems ...]
```

### Step 3: Read Detailed Report
```bash
# Open in your editor
code reports\detailed_test_cases\groq_chain_of_thought_attempt1_detailed.md
```

### Step 4: View HTML Coverage
```bash
# Open in browser
start coverage_reports\groq_chain_of_thought_attempt1\html\index.html
```

## 📊 Interpreting Results

### High Pass Rate (80%+)
✅ Model is performing well
✅ Most problems solved correctly
✅ Good test case coverage

### Medium Pass Rate (50-80%)
⚠️ Some problems need attention
⚠️ Review failed test cases
⚠️ Check for edge cases

### Low Pass Rate (<50%)
❌ Model needs improvement
❌ Review prompting strategy
❌ Check problem understanding

## 🔧 Troubleshooting

### Issue: "No test files found"
**Solution:** Check if test files exist:
```bash
dir generated\<model_name>\test_*.py
```

### Issue: "Division by zero error"
**Solution:** No test files match the pattern. Check:
- File naming convention
- Attempt number (1, 2, or 3)
- Directory path

### Issue: "Can't see branch coverage"
**Solution:** Branch coverage IS there! Look for:
- "Branch" column in terminal output
- HTML report for visual indicators
- Detailed report for per-problem branches

## 📚 Additional Resources

### Documentation Files:
1. **Branch Coverage Explanation:** `reports/BRANCH_COVERAGE_EXPLANATION.md`
2. **All 10 Problems Confirmed:** `reports/ALL_10_PROBLEMS_CONFIRMED.md`
3. **This Guide:** `reports/QUICK_REFERENCE_GUIDE.md`

### Analysis Scripts:
1. **Detailed Test Case Analysis:** `detailed_test_case_analysis.py`
2. **Coverage Analysis:** `run_coverage_analysis.py`
3. **Model Reports:** `generate_model_reports.py`

## 🎉 Summary

✅ **All 10 problems ARE evaluated**  
✅ **Individual test cases ARE tracked**  
✅ **Branch coverage IS shown**  
✅ **Detailed reports ARE generated**  

Everything is working correctly! The 33% overall coverage is expected because only attempt 1 is tested.

---
**Need Help?** Run: `python detailed_test_case_analysis.py --help`
