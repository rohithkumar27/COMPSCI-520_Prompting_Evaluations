# Problem Dataset References

This document provides citations and references for all problems used in the code generation evaluation study.

## Dataset Overview

The evaluation dataset consists of 17 problems from multiple sources, categorized by difficulty:
- **Problems 1-10**: Basic HumanEval problems
- **Problems 11-15**: Tough algorithmic problems  
- **Problems 16-17**: Extremely challenging problems designed to test AI limits

---

## Problem References

### Problems 1-10: HumanEval Dataset

**Source**: Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. D. O., Kaplan, J., ... & Zaremba, W. (2021). *Evaluating large language models trained on code*. arXiv preprint arXiv:2107.03374.

**Dataset**: HumanEval - A collection of 164 handwritten programming problems with unit tests.

**Official Repository**: https://github.com/openai/human-eval

**Problems Used**:
1. **Problem/0**: `has_close_elements` - Check if numbers are within threshold
2. **Problem/1**: `separate_paren_groups` - Parse nested parentheses groups
3. **Problem/2**: `truncate_number` - Extract decimal part of float
4. **Problem/3**: `below_zero` - Detect negative bank balance
5. **Problem/4**: `mean_absolute_deviation` - Calculate MAD statistic
6. **Problem/5**: `intersperse` - Insert delimiter between list elements
7. **Problem/6**: `parse_nested_parens` - Find maximum nesting depth
8. **Problem/7**: `filter_by_substring` - Filter strings by substring
9. **Problem/8**: `sum_product` - Calculate sum and product of list
10. **Problem/9**: `rolling_max` - Generate rolling maximum sequence

**Citation Format**:
```
Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. D. O., Kaplan, J., ... & Zaremba, W. (2021). 
Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374.
```

---

### Problems 11-15: Tough Algorithmic Problems

**Source**: LeetCode - Online programming contest platform

**Problems Used**:

11. **Tough/0**: `find_median_sorted_arrays` 
    - **LeetCode Problem**: #4 - Median of Two Sorted Arrays
    - **Difficulty**: Hard
    - **URL**: https://leetcode.com/problems/median-of-two-sorted-arrays/
    - **Algorithm**: Binary search, O(log(m+n)) complexity

12. **Tough/1**: `longest_valid_parentheses`
    - **LeetCode Problem**: #32 - Longest Valid Parentheses  
    - **Difficulty**: Hard
    - **URL**: https://leetcode.com/problems/longest-valid-parentheses/
    - **Algorithm**: Stack-based parsing, dynamic programming

13. **Tough/2**: `trap_rain_water`
    - **LeetCode Problem**: #42 - Trapping Rain Water
    - **Difficulty**: Hard  
    - **URL**: https://leetcode.com/problems/trapping-rain-water/
    - **Algorithm**: Two-pointer technique, O(n) time complexity

14. **Tough/3**: `edit_distance`
    - **LeetCode Problem**: #72 - Edit Distance (Levenshtein Distance)
    - **Difficulty**: Hard
    - **URL**: https://leetcode.com/problems/edit-distance/
    - **Algorithm**: Dynamic programming, Wagner-Fischer algorithm

15. **Tough/4**: `max_sliding_window`
    - **LeetCode Problem**: #239 - Sliding Window Maximum
    - **Difficulty**: Hard
    - **URL**: https://leetcode.com/problems/sliding-window-maximum/
    - **Algorithm**: Deque-based optimization, O(n) time complexity

**Citation Format**:
```
LeetCode LLC. (2024). LeetCode - The World's Leading Online Programming Learning Platform. 
Retrieved from https://leetcode.com/
```

---

### Problems 16-17: Extremely Challenging Problems

**Source**: Custom problems designed for this research study

**Design Rationale**: These problems were specifically created to test the limits of current AI code generation capabilities by combining multiple complex requirements that are known to challenge large language models.

16. **Extreme/0**: `solve_traveling_salesman_with_constraints`
    - **Problem Type**: Constrained Traveling Salesman Problem (TSP)
    - **Complexity**: NP-hard optimization with multiple constraints
    - **Challenges**: Time windows, capacity constraints, multi-objective optimization
    - **Theoretical Background**: 
      - Applegate, D. L., Bixby, R. E., Chvátal, V., & Cook, W. J. (2006). *The traveling salesman problem: a computational study*. Princeton university press.
      - Cordeau, J. F., Desaulniers, G., Desrosiers, J., Solomon, M. M., & Soumis, F. (2002). VRP with time windows. *The vehicle routing problem*, 9, 157-193.

17. **Extreme/1**: `create_concurrent_lru_cache_with_ttl`
    - **Problem Type**: Concurrent data structure implementation
    - **Complexity**: Thread-safe LRU cache with time-based expiration
    - **Challenges**: Concurrency control, O(1) operations, memory management
    - **Theoretical Background**:
      - O'Neil, E. J., O'Neil, P. E., & Weikum, G. (1993). The LRU-K page replacement algorithm for database disk buffering. *ACM SIGMOD Record*, 22(2), 297-306.
      - Herlihy, M., & Shavit, N. (2020). *The art of multiprocessor programming*. Morgan Kaufmann.

**Citation Format**:
```
Custom problems designed for "Evaluating Prompting Strategies for AI Code Generation" research study (2024).
Problems specifically created to test the limits of large language model code generation capabilities.
```

---

## Problem Difficulty Classification

### Basic Problems (1-10)
- **Characteristics**: Single algorithmic concept, clear requirements
- **Average Lines of Code**: 5-15 lines
- **Key Skills**: Basic programming constructs, simple algorithms

### Tough Problems (11-15)  
- **Characteristics**: Advanced algorithms, optimization requirements
- **Average Lines of Code**: 15-30 lines
- **Key Skills**: Dynamic programming, graph algorithms, complex data structures

### Extreme Problems (16-17)
- **Characteristics**: Multiple interacting constraints, systems programming
- **Average Lines of Code**: 50-100+ lines  
- **Key Skills**: Concurrent programming, optimization, complex state management

---

## Usage in Research

These problems were selected to provide a comprehensive evaluation of AI code generation capabilities across different difficulty levels and problem types. The progression from basic HumanEval problems to extremely challenging custom problems allows for detailed analysis of where and why different prompting strategies succeed or fail.

**Research Questions Addressed**:
1. How do different prompting strategies perform across difficulty levels?
2. What types of problems cause specific strategies to fail?
3. Where are the current limits of AI code generation capabilities?

---

## Additional Resources

### HumanEval Dataset
- **Paper**: https://arxiv.org/abs/2107.03374
- **Code**: https://github.com/openai/human-eval
- **Leaderboard**: https://paperswithcode.com/dataset/humaneval

### LeetCode Problems
- **Platform**: https://leetcode.com/
- **Problem Archive**: https://leetcode.com/problemset/all/
- **Difficulty Distribution**: Easy (25%), Medium (50%), Hard (25%)

### Algorithmic References
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms* (3rd ed.). MIT press.
- Skiena, S. S. (2020). *The algorithm design manual* (3rd ed.). Springer.