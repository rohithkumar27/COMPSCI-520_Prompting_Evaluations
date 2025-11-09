# How to View Your Combined Coverage Report

## 📊 **Your Comprehensive HTML Report is Ready!**

### **Location:**
```
reports/COMBINED_COVERAGE_REPORT.html
```

### **How to Open:**

**Option 1: Double-click the file**
- Navigate to the `reports` folder
- Double-click `COMBINED_COVERAGE_REPORT.html`
- It will open in your default browser

**Option 2: Right-click and open with browser**
- Right-click the file
- Select "Open with"
- Choose your preferred browser (Chrome, Firefox, Edge, etc.)

**Option 3: From command line**
```bash
start reports/COMBINED_COVERAGE_REPORT.html
```

## 📋 **What's in the Report:**

### **1. Summary Dashboard (Top Section)**
- 📊 Total Tests across all models
- ✅ Total Tests Passed
- 📈 Average Coverage percentage
- 🤖 Number of Models Analyzed

### **2. Individual Model Sections**

Each model has its own section with:

#### **Model Statistics:**
- Tests Passed/Total
- Pass Rate %
- Average Coverage %
- Total Assertions

#### **Detailed Table for Each Problem:**

| Column | Description |
|--------|-------------|
| **Problem** | Problem identifier (humaneval_0, humaneval_1, etc.) |
| **Status** | ✅ PASSED or ❌ FAILED |
| **Tests** | Number of assertions/test cases |
| **Line Coverage** | Visual bar showing % of lines covered |
| **Branch Coverage** | Visual bar showing % of branches covered |
| **Statements** | Total executable statements |
| **Notes** | Quick insights (e.g., "Perfect coverage", "Test failed", "5 lines missed") |

### **3. Visual Features:**

- **Color-coded status badges:**
  - 🟢 Green = PASSED
  - 🔴 Red = FAILED

- **Coverage bars:**
  - 🟢 Green (80-100%) = High coverage
  - 🟡 Yellow (50-79%) = Medium coverage
  - 🔴 Red (0-49%) = Low coverage

- **Interactive elements:**
  - Hover over rows for highlighting
  - Responsive design for different screen sizes

## 📊 **Models Included:**

1. **GROQ Chain of Thought**
2. **GROQ Step Chain of Thought**
3. **Gemini Chain of Thought**
4. **Gemini Step Chain of Thought**

## 🎯 **What You Can Learn:**

- Which model performs best overall
- Which problems are most challenging
- Coverage quality for each solution
- Specific test failures and their locations
- Comparison between Chain of Thought vs Step Chain of Thought strategies

## 💡 **Tips:**

- **Print the report** for presentations (File → Print in browser)
- **Take screenshots** of specific sections for your assignment
- **Compare models** side-by-side using the tables
- **Identify patterns** in failures across models

**Your comprehensive HTML report is ready to view!** 🎉