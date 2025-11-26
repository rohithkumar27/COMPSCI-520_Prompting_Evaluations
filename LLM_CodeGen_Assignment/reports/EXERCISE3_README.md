# Exercise 3: Specification-Guided Test Improvement

## Overview

This exercise explores how formal specifications, automatically generated from natural language problem statements, can guide test improvement.

**Deadline:** November 25, 11:59PM EST

---

## Document Guide

### 📋 Start Here:
1. **`EXERCISE3_QUICK_START_GUIDE.md`** - Read this first for overview
2. **`EXERCISE3_COPY_PASTE_PROMPTS.txt`** - Copy these prompts to your LLM

### 📝 Detailed Instructions:
3. **`EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md`** - Complete workflow with examples
4. **`EXERCISE3_PART1_COMPLETED_TEMPLATE.md`** - Fill this in with your work

### 📊 Reference:
5. **`EXERCISE3_SPECIFICATION_GUIDED_TESTING.md`** - Example completed document

---

## Quick Workflow

### Part 1: Generate and Evaluate Specifications (5 pts)

```
1. Open: EXERCISE3_COPY_PASTE_PROMPTS.txt
2. Copy Problem 1 prompt → Paste to LLM → Save response
3. Copy Problem 2 prompt → Paste to LLM → Save response
4. Evaluate each assertion (Correct/Incorrect)
5. Calculate accuracy rate
6. Correct incorrect assertions
7. Fill in: EXERCISE3_PART1_COMPLETED_TEMPLATE.md
```

**Time:** 1-2 hours

---

### Part 2: Generate Tests from Specifications (5 pts)

```
1. Use your final correct specifications
2. Ask LLM to generate test cases
3. Run tests and measure coverage
4. Compare with Exercise 2 results
5. Document insights (even if no improvement)
```

**Time:** 1-2 hours

---

## Files Structure

```
LLM_CodeGen_Assignment/
├── reports/
│   ├── EXERCISE3_README.md                          ← You are here
│   ├── EXERCISE3_QUICK_START_GUIDE.md               ← Start here
│   ├── EXERCISE3_COPY_PASTE_PROMPTS.txt             ← Copy these prompts
│   ├── EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md      ← Detailed guide
│   ├── EXERCISE3_PART1_COMPLETED_TEMPLATE.md        ← Fill this in
│   └── EXERCISE3_SPECIFICATION_GUIDED_TESTING.md    ← Example
│
├── generated/
│   ├── spec_guided/
│   │   ├── test_apps_2_spec_guided.py               ← Your tests
│   │   └── test_apps_3_spec_guided.py               ← Your tests
│   │
│   └── gemini_chain_of_thought/
│       ├── apps_2_p3_attempt_1.py                   ← Solution code
│       └── apps_3_p4_attempt_1.py                   ← Solution code
│
└── datasets/
    └── apps_tough_problems.py                       ← Problem descriptions
```

---

## What You'll Submit

### PDF Document (via GradeScope)

Must include:

#### Part 1 (5 pts):
- [ ] LLM prompts used (both problems)
- [ ] Raw LLM output (generated assertions)
- [ ] Evaluation table (Correct/Incorrect for each)
- [ ] Accuracy rate calculation
- [ ] Corrections for incorrect assertions
- [ ] Final correct specifications

#### Part 2 (5 pts):
- [ ] LLM prompt for test generation
- [ ] Generated test cases (labeled as spec-guided)
- [ ] Coverage comparison table:
  ```
  | Problem | Old Stmt % | New Stmt % | Old Branch % | New Branch % |
  ```
- [ ] Case-specific insights (why coverage changed or didn't)

#### Repository:
- [ ] GitHub link
- [ ] Source code
- [ ] Test files
- [ ] Coverage reports

---

## Key Points

### What Makes a Good Specification?

✅ **Good:**
```python
# Specification: Empty string returns 1
assert res == 1 if s == "" else res >= 0
```
- Pure logic
- No side effects
- Doesn't call the function
- Clear and testable

❌ **Bad:**
```python
# Calls the function (self-reference)
assert res == count_valid_parentheses_sequences(s)

# Uses side effects
assert (print(res) or True) and res >= 0

# Too complex (reimplements algorithm)
assert res == sum(1 for i in range(len(arr)) for j in range(i, len(arr)) 
                  if sum(arr[i:j+1]) % k == 0)
```

---

### Evaluation Criteria

Check each assertion for:

1. **No Self-Reference:** Doesn't call the function being specified
2. **No Side Effects:** No print, append, file I/O, random, timing
3. **Logical Correctness:** Accurately represents the specification
4. **Edge Case Handling:** Considers special cases (empty, zero, etc.)

---

### If Coverage Doesn't Improve

**That's okay!** You still get full credit if you:

1. Clearly explain why (case-specific)
2. Show that specs target same edge cases as Exercise 2
3. Discuss the value of specifications beyond coverage

**Example explanation:**
> "Coverage did not increase because the specification-guided tests target 
> the same edge case branches already covered in Exercise 2's Iteration 1. 
> Specifically, the empty string specification maps to test_empty_string() 
> from Exercise 2. This demonstrates that coverage-driven testing naturally 
> discovers the same edge cases that formal specifications identify."

---

## Common Questions

### Q: How many specifications should I generate?
**A:** About 5 per problem. If the LLM generates more, keep the distinct ones. If fewer, that's fine for simple methods.

### Q: What if the LLM generates incorrect assertions?
**A:** That's expected! Evaluate them, mark as incorrect, explain the issue, and provide corrected versions.

### Q: What if coverage doesn't improve in Part 2?
**A:** Provide a clear, case-specific explanation. You'll still get full credit.

### Q: Can I use the same problems from Exercise 2?
**A:** Yes! Use the two problems with weakest coverage from Exercise 2.

### Q: Which LLM should I use?
**A:** Any major LLM works: ChatGPT-4, Claude, Gemini, etc. Just document which one you used.

---

## Grading Rubric

### Part 1 (5 pts):
- Correct prompts used (1 pt)
- LLM output documented (1 pt)
- Thorough evaluation (1 pt)
- Accurate accuracy calculation (1 pt)
- Proper corrections (1 pt)

### Part 2 (5 pts):
- Test generation from specs (1 pt)
- Tests run successfully (1 pt)
- Coverage measured (1 pt)
- Comparison with Exercise 2 (1 pt)
- Clear insights/explanations (1 pt)

---

## Tips for Success

1. **Follow the prompts exactly** - Don't modify them
2. **Document everything** - Show your work
3. **Be thorough in evaluation** - Check each assertion carefully
4. **Explain your reasoning** - Especially for corrections
5. **Case-specific insights** - Don't give generic explanations

---

## Timeline

**Day 1 (Nov 24):**
- Morning: Complete Part 1 (2 hours)
- Afternoon: Complete Part 2 (2 hours)
- Evening: Create PDF, finalize repo

**Day 2 (Nov 25):**
- Morning: Review and polish
- Before 11:59 PM: Submit to GradeScope

---

## Need Help?

1. Check the example: `EXERCISE3_SPECIFICATION_GUIDED_TESTING.md`
2. Review the workflow: `EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md`
3. Use the template: `EXERCISE3_PART1_COMPLETED_TEMPLATE.md`

---

## Final Checklist

- [ ] Read Quick Start Guide
- [ ] Copy prompts to LLM
- [ ] Save LLM responses
- [ ] Evaluate assertions
- [ ] Calculate accuracy
- [ ] Correct incorrect assertions
- [ ] Generate test cases
- [ ] Run coverage analysis
- [ ] Compare with Exercise 2
- [ ] Document insights
- [ ] Create PDF
- [ ] Update GitHub repo
- [ ] Submit to GradeScope

---

**Good luck! Remember: This is about exploring the relationship between specifications and testing, not just achieving higher coverage.**
