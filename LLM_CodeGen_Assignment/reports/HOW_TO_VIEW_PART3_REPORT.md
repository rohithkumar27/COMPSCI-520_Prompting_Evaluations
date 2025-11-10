# 📊 How to View Part 3 HTML Report

## Quick Access

### **Option 1: Double-click the file**
1. Navigate to: `LLM_CodeGen_Assignment/reports/`
2. Double-click: `PART3_BUG_DETECTION_REPORT.html`
3. Opens in your default browser

### **Option 2: Command line (Windows)**
```bash
cd LLM_CodeGen_Assignment/reports
start PART3_BUG_DETECTION_REPORT.html
```

### **Option 3: From VS Code**
1. Right-click `PART3_BUG_DETECTION_REPORT.html`
2. Select "Open with Live Server" or "Open in Default Browser"

---

## What's in the Report?

### 📊 **Executive Summary**
- 4 bugs injected, 1 caught (25% detection)
- 93% branch coverage achieved
- 42 total tests executed

### 🔴 **Problem 1: apps_2_p3**
- 0/2 bugs caught (0%)
- Bug 1: Off-by-one error (covered but not detected)
- Bug 2: Wrong boundary condition (not covered)

### 🟡 **Problem 2: apps_3_p4**
- 1/2 bugs caught (50%)
- Bug 1: Formula error ✅ CAUGHT by test_k_one()
- Bug 2: Initialization error (covered but not detected)

### 🔑 **Key Findings**
1. Coverage ≠ Fault Detection
2. Assertion Quality Matters More
3. Branch Coverage Helps But Isn't Sufficient
4. The Coverage-Detection Gap

### 🎯 **Conclusion**
- High coverage + weak assertions = 25% detection
- High coverage + strong assertions = 100% detection
- Assertion quality is critical for bug detection

---

## Features

✅ **Interactive Design** - Hover effects and responsive layout  
✅ **Color-Coded Results** - Green (caught), Red (missed), Yellow (partial)  
✅ **Code Examples** - Shows actual buggy code and test assertions  
✅ **Detailed Analysis** - Why each bug was caught or missed  
✅ **Print-Friendly** - Can be printed or saved as PDF  

---

## File Location

```
LLM_CodeGen_Assignment/
└── reports/
    └── PART3_BUG_DETECTION_REPORT.html  ← Open this file
```

---

**Generated:** November 10, 2025  
**Purpose:** Part 3 Assignment Submission - Fault Detection Evaluation
