# Part 3: Short Answers (Quick Reference)

---

## Q1: What bugs were injected and why are they realistic?

### apps_2_p3 (2 bugs)

**Bug 1:** Changed `len(s) % 2 != 0` to `len(s) % 2 > 0` (Line 20)  
**Realistic because:** Off-by-one errors are extremely common. The operators seem equivalent for modulo 2, making it a subtle mistake that passes code review.

**Bug 2:** Changed `max_open < 0` to `max_open <= 0` (Line 52)  
**Realistic because:** Confusing `<` with `<=` is a classic boundary condition error, easy to introduce when implementing algorithms.

### apps_3_p4 (2 bugs)

**Bug 1:** Changed `n * (n + 1) // 2` to `n * (n - 1) // 2` (Line 22)  
**Realistic because:** Mathematical formula errors are common when writing formulas from memory. Easy to confuse `n+1` with `n-1`.

**Bug 2:** Changed `mod_count[0] = 1` to `mod_count[0] = 0` (Line 33)  
**Realistic because:** Initialization errors happen when developers don't understand why we start with 1 (empty prefix). Starting from 0 looks "natural" but is wrong.

---

## Q2: Did tests fail? Which test(s) caught bugs?

### Results: 1 out of 4 bugs caught (25%)

**apps_2_p3:**
- Bug 1: ❌ NOT CAUGHT (weak assertions: `assert result >= 0`)
- Bug 2: ❌ NOT CAUGHT (branch not covered)

**apps_3_p4:**
- Bug 1: ✅ CAUGHT by `test_k_one()` and `test_all_zeros()`
  - Used exact assertion: `assert result == 6`
  - Expected: 6, Got: 3 → Test FAILED
- Bug 2: ❌ NOT CAUGHT (no behavioral validation)

**Test that caught Bug 1:**
```python
def test_k_one():
    result = count_divisible_subarrays([1, 2, 3], 1)
    assert result == 6  # ✅ Exact assertion caught the bug
```

---

## Q3: Conclusion linking coverage ↔ fault detection

### Main Finding: Coverage ≠ Fault Detection

**Evidence:**
- Achieved 93% branch coverage on buggy code
- Only detected 25% of bugs (1 out of 4)
- Same coverage with different assertions: 25% → 100% detection

### The Coverage-Detection Gap

| Test Suite | Coverage | Assertions | Detection |
|------------|----------|------------|-----------|
| Iteration-3 | 94-97% | Weak (`>= 0`) | 25% |
| Custom | 94-97% | Strong (exact) | 100% |

### Why Coverage Alone Fails

**Example - Bug Covered But Not Detected:**
- apps_2_p3 Bug 1: Line covered ✅, both branches executed ✅
- But test used `assert result >= 0` (weak)
- Bug went undetected ❌

**Example - Bug Covered AND Detected:**
- apps_3_p4 Bug 1: Line covered ✅
- Test used `assert result == 6` (exact)
- Bug caught ✅ (got 3 instead of 6)

### The Winning Formula

```
High Coverage + Weak Assertions = 25% Detection ❌
High Coverage + Strong Assertions = 100% Detection ✅
```

### Conclusion

**Coverage is necessary but not sufficient:**
1. **Necessary:** Can't detect bugs in uncovered code
2. **Not sufficient:** Executing buggy code ≠ detecting the bug
3. **Assertion quality is critical:** Bridges the gap between coverage and detection

**Our experiment proves:** Branch coverage improvements (70% → 95%) covered the buggy code paths, but only tests with exact assertions actually detected the bugs. Coverage gets you to the bug, assertions catch it.

---

**Key Insight:** Coverage measures execution, not validation. You need BOTH high coverage AND exact assertions for effective bug detection.
