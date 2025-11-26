# Exercise 3: Quick Start Guide

## What You Need to Do

### Part 1: Generate and Evaluate Specifications (5 pts)

**Goal:** Get an LLM to generate formal specifications, then evaluate and correct them.

#### Step-by-Step:

1. **Open the workflow document:**
   - File: `EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md`
   - This has the EXACT prompts to copy to your LLM

2. **For Problem 1 (Count Valid Parentheses):**
   - Copy the prompt from Section 1.3
   - Paste it into ChatGPT/Claude/Gemini
   - Save the LLM's response

3. **For Problem 2 (Count Divisible Subarrays):**
   - Copy the prompt from Section 2.3
   - Paste it into ChatGPT/Claude/Gemini
   - Save the LLM's response

4. **Evaluate the assertions:**
   - For each assertion, mark it ✅ Correct or ❌ Incorrect
   - Check for:
     - Does it call the function? (❌ Incorrect)
     - Does it use print/append/etc? (❌ Incorrect)
     - Is the logic sound? (if not, ❌ Incorrect)

5. **Calculate accuracy:**
   - Accuracy = (# Correct) / (Total Generated)

6. **Fix incorrect assertions:**
   - For each incorrect one, explain the problem
   - Write a corrected version

7. **Fill in the template:**
   - File: `EXERCISE3_PART1_COMPLETED_TEMPLATE.md`
   - Paste all your work there

---

### Part 2: Generate Tests from Specifications (5 pts)

**Goal:** Use the correct specifications to generate test cases, then compare coverage.

#### Step-by-Step:

1. **Create a new LLM prompt:**
   - Include your final correct specifications
   - Ask the LLM to generate test cases based on them

2. **Run the generated tests:**
   - Add them to your test suite
   - Run with pytest

3. **Measure coverage:**
   - Use pytest-cov or coverage.py
   - Compare with Exercise 2 results

4. **Document findings:**
   - Did coverage improve?
   - If not, explain why (case-specific)

---

## Files You'll Work With

### Input Files (Read These):
- `EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md` - Exact prompts to use
- `datasets/apps_tough_problems.py` - Problem descriptions

### Output Files (Fill These In):
- `EXERCISE3_PART1_COMPLETED_TEMPLATE.md` - Your Part 1 work
- `generated/spec_guided/test_apps_2_spec_guided.py` - Generated tests
- `generated/spec_guided/test_apps_3_spec_guided.py` - Generated tests

### Final Deliverable:
- One PDF with all your work
- GitHub repo link

---

## Example Workflow

### 1. Copy Prompt to LLM

From `EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md`, copy this:

```
Problem description: 
Given a string containing '(', ')', and '?'...
[full prompt]
```

### 2. LLM Responds

```python
# Specification 1: Empty string returns 1
assert res == 1 if s == "" else res >= 0

# Specification 2: Odd length returns 0
assert res == 0 if len(s) % 2 != 0 else res >= 0

# Specification 3: Starts with ')' returns 0
assert res == 0 if len(s) > 0 and s[0] == ')' else res >= 0
```

### 3. You Evaluate

| # | Status | Reason |
|---|--------|--------|
| 1 | ✅ | Correct logic, no side effects |
| 2 | ✅ | Correct logic, no side effects |
| 3 | ✅ | Correct logic, no side effects |

Accuracy: 3/3 = 100%

### 4. You Document

Fill in the template with:
- The prompt you used
- The LLM's raw output
- Your evaluation table
- Accuracy calculation
- Any corrections needed
- Final correct specifications

---

## Common Mistakes to Avoid

### ❌ Don't Do This:

1. **Calling the function in assertions:**
   ```python
   assert res == count_valid_parentheses_sequences(s)  # WRONG!
   ```

2. **Using side effects:**
   ```python
   assert (print(res) or True) and res >= 0  # WRONG!
   ```

3. **Skipping evaluation:**
   - Don't just accept all LLM output as correct
   - Actually check each assertion

4. **Not explaining corrections:**
   - If you mark something incorrect, explain why
   - Show the corrected version

### ✅ Do This:

1. **Pure logic assertions:**
   ```python
   assert res == 1 if s == "" else res >= 0  # GOOD!
   ```

2. **Thorough evaluation:**
   - Check each assertion carefully
   - Look for edge cases

3. **Clear documentation:**
   - Show your work
   - Explain your reasoning

---

## Time Estimate

- Part 1: 1-2 hours
  - 15 min: Copy prompts, get LLM responses
  - 30 min: Evaluate assertions
  - 30 min: Correct and document
  - 15 min: Fill in template

- Part 2: 1-2 hours
  - 30 min: Generate test cases
  - 30 min: Run coverage analysis
  - 30 min: Compare and document

**Total: 2-4 hours**

---

## Checklist

### Part 1:
- [ ] Copied Problem 1 prompt to LLM
- [ ] Saved Problem 1 LLM output
- [ ] Evaluated Problem 1 assertions
- [ ] Calculated Problem 1 accuracy
- [ ] Corrected Problem 1 incorrect assertions
- [ ] Listed Problem 1 final specifications
- [ ] Copied Problem 2 prompt to LLM
- [ ] Saved Problem 2 LLM output
- [ ] Evaluated Problem 2 assertions
- [ ] Calculated Problem 2 accuracy
- [ ] Corrected Problem 2 incorrect assertions
- [ ] Listed Problem 2 final specifications
- [ ] Filled in completed template

### Part 2:
- [ ] Generated test cases from specifications
- [ ] Ran tests successfully
- [ ] Measured coverage
- [ ] Compared with Exercise 2
- [ ] Documented insights
- [ ] Created final PDF

### Submission:
- [ ] PDF includes all required sections
- [ ] GitHub repo is updated
- [ ] Submitted to GradeScope

---

## Need Help?

1. **Stuck on evaluation?**
   - Check the "Tips for Evaluation" section in the workflow doc
   - Look for the common issues list

2. **LLM not generating good specs?**
   - Make sure you copied the EXACT prompt
   - Try a different LLM (ChatGPT vs Claude vs Gemini)

3. **Coverage not improving?**
   - That's okay! Explain why in your case-specific insight
   - Example: "Specs target same edge cases as Exercise 2"

---

**Good luck! Remember: The goal is to explore how specifications guide testing, not necessarily to achieve higher coverage.**
