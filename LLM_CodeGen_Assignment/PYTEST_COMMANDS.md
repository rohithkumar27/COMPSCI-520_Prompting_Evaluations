# Pytest Coverage Commands for LLM Model Evaluation

## Quick Start - Run All Models

```bash
# Run the automated script for all models
python run_coverage_analysis.py
```

## Individual Model Commands

### 1. GROQ Chain of Thought
```bash
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-report=html:coverage_reports/groq_chain_of_thought/html --cov-report=term-missing -v
```

### 2. GROQ Step Chain of Thought  
```bash
pytest generated/groq_step_chain_of_thought/ --cov=generated/groq_step_chain_of_thought --cov-report=html:coverage_reports/groq_step_chain_of_thought/html --cov-report=term-missing -v
```

### 3. Gemini Chain of Thought
```bash
pytest generated/gemini_chain_of_thought/ --cov=generated/gemini_chain_of_thought --cov-report=html:coverage_reports/gemini_chain_of_thought/html --cov-report=term-missing -v
```

### 4. Gemini Step Chain of Thought
```bash
pytest generated/gemini_step_chain_of_thought/ --cov=generated/gemini_step_chain_of_thought --cov-report=html:coverage_reports/gemini_step_chain_of_thought/html --cov-report=term-missing -v
```

### 5. Enhanced Chain of Thought
```bash
pytest generated/enhanced_chain_of_thought/ --cov=generated/enhanced_chain_of_thought --cov-report=html:coverage_reports/enhanced_chain_of_thought/html --cov-report=term-missing -v
```

### 6. Enhanced Step Chain of Thought
```bash
pytest generated/enhanced_step_chain_of_thought/ --cov=generated/enhanced_step_chain_of_thought --cov-report=html:coverage_reports/enhanced_step_chain_of_thought/html --cov-report=term-missing -v
```

### 7. Enhanced Gemini Chain of Thought
```bash
pytest generated/enhanced_gemini_chain_of_thought/ --cov=generated/enhanced_gemini_chain_of_thought --cov-report=html:coverage_reports/enhanced_gemini_chain_of_thought/html --cov-report=term-missing -v
```

### 8. Enhanced Gemini Step Chain of Thought
```bash
pytest generated/enhanced_gemini_step_chain_of_thought/ --cov=generated/enhanced_gemini_step_chain_of_thought --cov-report=html:coverage_reports/enhanced_gemini_step_chain_of_thought/html --cov-report=term-missing -v
```

### 9. Innovative Multi Agent
```bash
pytest generated/innovative_multi_agent/ --cov=generated/innovative_multi_agent --cov-report=html:coverage_reports/innovative_multi_agent/html --cov-report=term-missing -v
```

### 10. Multi Modal Simple
```bash
pytest generated/multi_modal_simple/ --cov=generated/multi_modal_simple --cov-report=html:coverage_reports/multi_modal_simple/html --cov-report=term-missing -v
```

## Command Explanation

- `pytest generated/MODEL_NAME/` - Run tests in specific model directory
- `--cov=generated/MODEL_NAME` - Measure coverage for that directory
- `--cov-report=html:path` - Generate HTML coverage report
- `--cov-report=term-missing` - Show missing lines in terminal
- `--cov-report=xml:path` - Generate XML report (for CI/CD)
- `--cov-report=json:path` - Generate JSON report (for analysis)
- `--cov-branch` - Include branch coverage
- `-v` - Verbose output showing each test
- `--tb=short` - Short traceback format

## Output Files

After running, you'll get:
- **HTML Report**: `coverage_reports/MODEL_NAME/html/index.html` (open in browser)
- **XML Report**: `coverage_reports/MODEL_NAME/coverage.xml` (for CI/CD)
- **JSON Report**: `coverage_reports/MODEL_NAME/coverage.json` (for analysis)
- **Terminal Output**: Pass/fail status and coverage percentage

## Advanced Usage

### Run with specific test patterns
```bash
pytest generated/groq_chain_of_thought/test_humaneval*.py --cov=generated/groq_chain_of_thought --cov-report=html -v
```

### Run with minimum coverage threshold
```bash
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-fail-under=80 --cov-report=html -v
```

### Run tests in parallel (if pytest-xdist installed)
```bash
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-report=html -v -n auto
```

### Generate only specific report types
```bash
# Only HTML report
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-report=html:reports/groq_html -v

# Only terminal report
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-report=term-missing -v

# Multiple formats
pytest generated/groq_chain_of_thought/ --cov=generated/groq_chain_of_thought --cov-report=html --cov-report=xml --cov-report=json -v
```

## Viewing Results

1. **Terminal Output**: Shows test results and coverage percentage immediately
2. **HTML Reports**: Open `coverage_reports/MODEL_NAME/html/index.html` in your browser for detailed visual coverage
3. **Compare Models**: Look at coverage percentages across different models to see which performs best