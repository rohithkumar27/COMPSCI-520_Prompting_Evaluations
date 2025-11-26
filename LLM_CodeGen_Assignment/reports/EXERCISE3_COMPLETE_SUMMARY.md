# Exercise 3: Complete Summary & Action Plan

## 🎯 Your Mission

Generate formal specifications from problem descriptions, evaluate them, and use them to guide test generation.

---

## 📚 Documents Created for You

### 1. **EXERCISE3_README.md** - Start Here
- Overview of the entire exercise
- File structure
- What to submit
- Grading rubric

### 2. **EXERCISE3_QUICK_START_GUIDE.md** - Quick Reference
- Step-by-step checklist
- Time estimates
- Common mistakes to avoid

### 3. **EXERCISE3_COPY_PASTE_PROMPTS.txt** - The Prompts
- **USE THIS FILE!**
- Copy these exact prompts to your LLM
- One for each problem

### 4. **EXERCISE3_PART1_PROMPTS_AND_WORKFLOW.md** - Detailed Guide
- Complete workflow with examples
- Evaluation criteria
- Tips for success

### 5. **EXERCISE3_PART1_COMPLETED_TEMPLATE.md** - Your Workspace
- **FILL THIS IN!**
- Template for all your work
- Will become your PDF submission

### 6. **EXERCISE3_VISUAL_WORKFLOW.md** - Visual Guide
- Flowcharts and diagrams
- Decision trees
- Timeline

### 7. **EXERCISE3_SPECIFICATION_GUIDED_TESTING.md** - Example
- Complete example submission
- Shows what a finished document looks like

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Open the Prompts File
```
File: EXERCISE3_COPY_PASTE_PROMPTS.txt
```

### Step 2: Copy First Prompt
```
Copy everything from:
"Problem description: Given a string containing..."
to
"```python"
```

### Step 3: Paste to LLM
- Open ChatGPT, Claude, or Gemini
- Paste the prompt
- Hit Enter

### Step 4: Save Response
- Copy the LLM's output
- Save it somewhere

### Step 5: Repeat for Problem 2
- Copy the second prompt
- Paste to LLM
- Save response

**You now have the raw material for Part 1!**

---

## 📝 Part 1 Workflow (2 Hours)

### What You're Doing:
Evaluating whether the LLM-generated assertions are correct.

### How to Evaluate Each Assertion:

```python
# Example assertion from LLM:
assert res == 1 if s == "" else res >= 0
```

**Ask yourself:**
1. ❓ Does it call the function? → If YES: ❌ Incorrect
2. ❓ Does it use print/append/etc? → If YES: ❌ Incorrect
3. ❓ Is the logic correct? → If NO: ❌ Incorrect
4. ✅ If all checks pass: ✅ Correct

### Fill in the Table:

| # | Assertion | Status | Reason |
|---|-----------|--------|--------|
| 1 | `assert res == 1 if s == "" else res >= 0` | ✅ | Correct logic |
| 2 | `assert res == count_valid_parentheses_sequences(s)` | ❌ | Calls function |

### Calculate Accuracy:
```
Correct: 4
Total: 5
Accuracy = 4/5 = 80%
```

### Fix Incorrect Ones:
For each ❌, explain what's wrong and provide a corrected version.

---

## 🧪 Part 2 Workflow (2 Hours)

### What You're Doing:
Using the correct specifications to generate test cases.

### Step 1: Create New Prompt

```
Based on these formal specifications, generate test cases:

Specification 1: Empty string returns 1
Specification 2: Odd length returns 0
[... list all your correct specs ...]

Generate test functions that verify each specification.
Each test should:
- Have a descriptive name
- Test one specification
- Include an assertion

Format:
def test_spec1_empty_string():
    """Specification 1: Empty string returns 1"""
    result = count_valid_parentheses_sequences("")
    assert result == 1
```

### Step 2: Run Tests

```bash
cd LLM_CodeGen_Assignment/generated/spec_guided
python test_apps_2_spec_guided.py
python test_apps_3_spec_guided.py
```

### Step 3: Measure Coverage

```bash
pytest test_apps_2_spec_guided.py --cov=../gemini_chain_of_thought/apps_2_p3_attempt_1 --cov-report=term
pytest test_apps_3_spec_guided.py --cov=../gemini_chain_of_thought/apps_3_p4_attempt_1 --cov-report=term
```

### Step 4: Compare

| Problem | Ex2 Stmt % | Ex3 Stmt % | Ex2 Branch % | Ex3 Branch % |
|---------|------------|------------|--------------|--------------|
| APPS/2  | 95%        | ?%         | 93%          | ?%           |
| APPS/3  | 94%        | ?%         | 92%          | ?%           |

### Step 5: Explain

If coverage didn't improve:
> "Coverage did not increase because the specification-guided tests 
> target the same edge cases already covered in Exercise 2. For example,
> the empty string specification maps directly to test_empty_string() 
> from Exercise 2's Iteration 1."

---

## 📦 What to Submit

### PDF Document (via GradeScope)

Must include these sections:

#### Part 1:
1. **Problem 1 & 2 Signatures**
2. **Natural Language Descriptions**
3. **LLM Prompts Used** (copy from EXERCISE3_COPY_PASTE_PROMPTS.txt)
4. **Raw LLM Output** (paste exactly what LLM generated)
5. **Evaluation Tables** (Correct/Incorrect for each assertion)
6. **Accuracy Rates** (calculated for each problem)
7. **Corrections** (for any incorrect assertions)
8. **Final Correct Specifications** (list of all correct ones)

#### Part 2:
1. **LLM Prompt for Test Generation**
2. **Generated Test Cases** (labeled as spec-guided)
3. **Coverage Comparison Table**
4. **Case-Specific Insights** (why coverage changed or didn't)

#### Repository:
1. **GitHub Link**
2. **All source code**
3. **Test files**
4. **Coverage reports**

---

## ✅ Pre-Submission Checklist

### Part 1:
- [ ] Used exact prompts from EXERCISE3_COPY_PASTE_PROMPTS.txt
- [ ] Documented raw LLM output (not modified)
- [ ] Evaluated each assertion (✅ or ❌)
- [ ] Calculated accuracy rate correctly
- [ ] Explained all incorrect assertions
- [ ] Provided corrected versions
- [ ] Listed final correct specifications

### Part 2:
- [ ] Generated tests from specifications
- [ ] Tests run successfully
- [ ] Measured coverage (statement & branch)
- [ ] Compared with Exercise 2 results
- [ ] Provided case-specific insights
- [ ] Explained why coverage changed/didn't change

### Submission:
- [ ] PDF has all required sections
- [ ] GitHub repo is updated
- [ ] Coverage reports are included
- [ ] Submitted before 11:59 PM EST on Nov 25

---

## 🎓 Grading Criteria

### Part 1 (5 points):
- ✅ Correct prompts used (1 pt)
- ✅ LLM output documented (1 pt)
- ✅ Thorough evaluation (1 pt)
- ✅ Accurate accuracy calculation (1 pt)
- ✅ Proper corrections (1 pt)

### Part 2 (5 points):
- ✅ Test generation from specs (1 pt)
- ✅ Tests run successfully (1 pt)
- ✅ Coverage measured (1 pt)
- ✅ Comparison with Exercise 2 (1 pt)
- ✅ Clear insights/explanations (1 pt)

---

## 💡 Pro Tips

### 1. Don't Modify the Prompts
Use the exact prompts from EXERCISE3_COPY_PASTE_PROMPTS.txt. Don't add or remove anything.

### 2. Document Everything
Show your work. Include:
- Raw LLM output (before any edits)
- Your evaluation reasoning
- Your corrections

### 3. Be Specific in Insights
Don't say: "Coverage didn't improve much."
Do say: "Coverage remained at 95% because spec 1 (empty string) maps to test_empty_string() from Exercise 2, which already covered line 21."

### 4. It's Okay if Coverage Doesn't Improve
You get full credit if you explain why. The exercise is about exploring the relationship between specifications and testing.

### 5. Use the Template
EXERCISE3_PART1_COMPLETED_TEMPLATE.md has all the sections you need. Just fill it in.

---

## 🆘 Troubleshooting

### Problem: LLM generates assertions that call the function
**Solution:** Mark them as incorrect, explain the issue, and either correct them or note they can't be expressed without calling the function.

### Problem: Not sure if an assertion is correct
**Solution:** Check:
1. Does it call the function? (bad)
2. Does it use side effects? (bad)
3. Is the logic sound? (good)

### Problem: Coverage didn't improve
**Solution:** That's fine! Explain why in your case-specific insight. You'll still get full credit.

### Problem: Tests are failing
**Solution:** Debug them. Make sure:
1. Imports are correct
2. Function names match
3. Test logic is sound

---

## 📅 Recommended Timeline

### Today (Nov 24):
- **Morning:** Complete Part 1 (2 hours)
- **Afternoon:** Complete Part 2 (2 hours)
- **Evening:** Create PDF, update repo (1 hour)

### Tomorrow (Nov 25):
- **Morning:** Review and polish (1 hour)
- **Before 11:59 PM:** Submit to GradeScope

---

## 🎯 Success Metrics

You'll know you're done when:

✅ You have LLM output for both problems  
✅ You've evaluated every assertion  
✅ You've calculated accuracy rates  
✅ You've corrected all incorrect assertions  
✅ You've generated test cases  
✅ You've measured coverage  
✅ You've compared with Exercise 2  
✅ You've documented insights  
✅ You've created a PDF  
✅ You've updated GitHub  
✅ You've submitted to GradeScope  

---

## 📞 Final Notes

- **Deadline:** November 25, 11:59 PM EST (sharp!)
- **Submission:** GradeScope only
- **Format:** PDF + GitHub link
- **Questions:** Contact TA Mingzhe Li (mingzhel@umass.edu)

---

**You have everything you need! Follow the workflow, use the templates, and you'll complete Exercise 3 successfully. Good luck! 🚀**
