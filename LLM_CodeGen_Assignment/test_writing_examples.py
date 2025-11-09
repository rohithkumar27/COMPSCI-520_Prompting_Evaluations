"""
Examples of different ways to write test cases in Python.
"""

import pytest


# Example function to test
def add_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0


# ============================================================================
# APPROACH 1: Multiple Asserts in One Function (Current Approach)
# ============================================================================

def test_add_numbers_multiple_asserts():
    """Multiple test cases in one function - SIMPLE but has issues."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5
    # Problem: If first assert fails, others don't run!


# ============================================================================
# APPROACH 2: Separate Function for Each Test Case (BEST for clarity)
# ============================================================================

def test_add_numbers_positive():
    """Test adding positive numbers."""
    assert add_numbers(2, 3) == 5

def test_add_numbers_zero():
    """Test adding with zero."""
    assert add_numbers(0, 0) == 0

def test_add_numbers_negative():
    """Test adding negative numbers."""
    assert add_numbers(-1, 1) == 0

def test_add_numbers_mixed():
    """Test adding positive and negative."""
    assert add_numbers(10, -5) == 5


# ============================================================================
# APPROACH 3: Parameterized Tests (BEST for many similar test cases)
# ============================================================================

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (100, 200, 300),
])
def test_add_numbers_parametrized(a, b, expected):
    """Parameterized test - runs each case separately."""
    assert add_numbers(a, b) == expected


# ============================================================================
# APPROACH 4: Test Class Organization (BEST for complex testing)
# ============================================================================

class TestAddNumbers:
    """Test class for organizing related tests."""
    
    def test_positive_numbers(self):
        """Test positive number addition."""
        assert add_numbers(2, 3) == 5
        assert add_numbers(1, 1) == 2
    
    def test_edge_cases(self):
        """Test edge cases."""
        assert add_numbers(0, 0) == 0
        assert add_numbers(-1, 1) == 0
    
    def test_large_numbers(self):
        """Test with large numbers."""
        assert add_numbers(1000000, 2000000) == 3000000


# ============================================================================
# APPROACH 5: Fixtures and Setup (BEST for complex data)
# ============================================================================

@pytest.fixture
def sample_data():
    """Fixture providing test data."""
    return {
        'positive_cases': [(2, 3, 5), (1, 4, 5)],
        'negative_cases': [(-1, -1, -2), (-5, 3, -2)],
        'edge_cases': [(0, 0, 0), (0, 5, 5)]
    }

def test_with_fixtures(sample_data):
    """Test using fixtures for data."""
    for a, b, expected in sample_data['positive_cases']:
        assert add_numbers(a, b) == expected


# ============================================================================
# APPROACH 6: Subtests (Python 3.4+) - Run all even if some fail
# ============================================================================

import unittest

class TestWithSubtests(unittest.TestCase):
    def test_add_numbers_subtests(self):
        """Using subtests to run all cases even if some fail."""
        test_cases = [
            (2, 3, 5),
            (0, 0, 0),
            (-1, 1, 0),
            (10, -5, 5)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(add_numbers(a, b), expected)


# ============================================================================
# REAL-WORLD EXAMPLE: Testing the has_close_elements function
# ============================================================================

def has_close_elements(numbers, threshold):
    """Example function from your dataset."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False


# Current approach (what you have now)
def test_has_close_elements_current():
    """Current approach - multiple asserts in one function."""
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    # Problem: If first fails, others don't run


# Better approach - separate functions
def test_has_close_elements_no_close():
    """Test case where no elements are close."""
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_has_close():
    """Test case where elements are close."""
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_has_close_elements_edge_case():
    """Test edge case."""
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True


# Best approach - parameterized
@pytest.mark.parametrize("numbers,threshold,expected", [
    ([1.0, 2.0, 3.0], 0.5, False),
    ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3, True),
    ([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05, False),
    ([1.0, 2.0, 5.9, 4.0, 5.0], 0.95, True),
])
def test_has_close_elements_parametrized(numbers, threshold, expected):
    """Parameterized test - each case runs independently."""
    assert has_close_elements(numbers, threshold) == expected


if __name__ == "__main__":
    # Run with pytest for best results
    pytest.main([__file__, "-v"])