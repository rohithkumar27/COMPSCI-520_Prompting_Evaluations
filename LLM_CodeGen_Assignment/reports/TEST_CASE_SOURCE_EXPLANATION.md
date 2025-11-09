# Test Case Source Explanation

**Generated:** 2025-11-09

## 📚 Where Test Cases Come From

### For APPS Problem: shortest_path_with_obstacles

**Source File:** `datasets/apps_tough_problems.py`

This file contains the **original test cases** from the APPS dataset. The test cases are defined in the dataset and then copied into the generated test files.

---

## 🔍 Example: APPS/1 - shortest_path_with_obstacles

### Original Dataset Definition

**Location:** `datasets/apps_tough_problems.py` (Line ~70-120)

```python
{
    "task_id": "APPS/1", 
    "difficulty": "Hard",
    "source": "APPS Dataset - Graph Algorithms",
    "prompt": """
def shortest_path_with_obstacles(grid, k):
    '''
    You are given a grid of size N x M where:
    - 0 represents an empty cell
    - 1 represents an obstacle
    - 2 represents the start position
    - 3 represents the end position
    
    Find the shortest path from start to end, considering you can remove at most K obstacles.
    Return the minimum number of steps, or -1 if impossible.
    '''
""",
    "test": """
def test_shortest_path():
    # Test case 1: Basic example
    grid1 = [
        [2, 1, 0, 0],
        [0, 1, 1, 0], 
        [0, 0, 1, 3]
    ]
    result = shortest_path_with_obstacles(grid1, 1)
    assert result == 5, f"Expected 5, got {result}"
    
    # Test case 2: No obstacles needed to remove
    grid2 = [
        [2, 0, 0],
        [0, 0, 0],
        [0, 0, 3]
    ]
    result = shortest_path_with_obstacles(grid2, 0)
    assert result == 4, f"Expected 4, got {result}"
    
    # Test case 3: Impossible even with K removals
    grid3 = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 3]
    ]
    result = shortest_path_with_obstacles(grid3, 1)
    assert result == -1, f"Expected -1, got {result}"
    
    print("All shortest path tests passed!")

test_shortest_path()
"""
}
```

---

## 📝 Test Cases Breakdown

### Test Case 1: Basic Example
```python
grid1 = [
    [2, 1, 0, 0],
    [0, 1, 1, 0], 
    [0, 0, 1, 3]
]
result = shortest_path_with_obstacles(grid1, 1)
assert result == 5, f"Expected 5, got {result}"
```

**Expected:** 5 steps  
**Description:** Can reach end by removing 1 obstacle

---

### Test Case 2: No Obstacles to Remove
```python
grid2 = [
    [2, 0, 0],
    [0, 0, 0],
    [0, 0, 3]
]
result = shortest_path_with_obstacles(grid2, 0)
assert result == 4, f"Expected 4, got {result}"
```

**Expected:** 4 steps  
**Description:** Clear path exists without removing obstacles

---

### Test Case 3: Impossible Case
```python
grid3 = [
    [2, 1, 1],
    [1, 1, 1],
    [1, 1, 3]
]
result = shortest_path_with_obstacles(grid3, 1)
assert result == -1, f"Expected -1, got {result}"
```

**Expected:** -1 (impossible)  
**Description:** Cannot reach end even with K=1 obstacle removals

---

## 🔄 How Test Cases Are Used

### Step 1: Dataset Definition
Test cases are defined in `datasets/apps_tough_problems.py`

### Step 2: Code Generation
When the LLM generates code, it receives:
1. The problem prompt
2. The test cases (as reference)

### Step 3: Test File Creation
The test cases are copied into generated test files like:
- `generated/gemini_chain_of_thought/test_apps_1_p2_attempt_1.py`
- `generated/gemini_step_chain_of_thought/test_apps_1_p2_attempt_1.py`

### Step 4: Execution
Pytest runs these test files to verify if the generated solution is correct.

---

## 📊 All APPS Problems in Dataset

The `datasets/apps_tough_problems.py` file contains **5 hard problems**:

| Task ID | Problem | Test Cases | Difficulty |
|---------|---------|------------|------------|
| APPS/0 | solve_knapsack_variant | 3 | Hard |
| APPS/1 | shortest_path_with_obstacles | 3 | Hard |
| APPS/2 | count_valid_parentheses_sequences | 4 | Hard |
| APPS/3 | count_divisible_subarrays | 3 | Hard |
| APPS/4 | tree_diameter_with_weights | 3 | Hard |

**Total:** 16 test cases across 5 problems

---

## 🎯 For HumanEval Problems

**Source File:** `datasets/humaneval_dataset.py`

HumanEval problems follow the same pattern:
1. Problem definition with prompt
2. Test cases defined in the dataset
3. Test cases copied to generated test files

---

## 📁 File Structure

```
project/
├── datasets/
│   ├── apps_tough_problems.py          ← Original test cases defined here
│   └── humaneval_dataset.py            ← HumanEval test cases
│
├── generated/
│   ├── gemini_chain_of_thought/
│   │   ├── apps_1_p2_attempt_1.py      ← Generated solution
│   │   └── test_apps_1_p2_attempt_1.py ← Test cases copied here
│   │
│   └── groq_chain_of_thought/
│       ├── apps_1_p2_attempt_1.py
│       └── test_apps_1_p2_attempt_1.py
│
└── reports/
    └── assertion_analysis/              ← Test results
```

---

## 🔍 How to Find Test Cases for Any Problem

### Method 1: Check Dataset File
```bash
# For APPS problems
cat datasets/apps_tough_problems.py

# For HumanEval problems  
cat datasets/humaneval_dataset.py
```

### Method 2: Check Generated Test File
```bash
# Example for APPS/1
cat generated/gemini_chain_of_thought/test_apps_1_p2_attempt_1.py
```

### Method 3: Search by Problem Name
```bash
# Search for specific problem
grep -r "shortest_path_with_obstacles" datasets/
```

---

## ✅ Summary

**For `test_shortest_path()` specifically:**

- **Source:** `datasets/apps_tough_problems.py` (APPS/1)
- **Total Test Cases:** 3 assertions
- **Test Case 1:** Basic example (expects 5)
- **Test Case 2:** No obstacles (expects 4)
- **Test Case 3:** Impossible case (expects -1)

**All test cases are defined in the dataset files and remain constant across all model attempts.**

---

*This ensures fair comparison - all models are tested against the exact same test cases from the dataset.*
