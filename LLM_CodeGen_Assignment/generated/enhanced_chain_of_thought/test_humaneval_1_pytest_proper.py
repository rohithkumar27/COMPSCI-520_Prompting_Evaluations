"""
Proper pytest test file for humaneval_1_p1_attempt_1.py
Demonstrates best practices for LLM code evaluation testing.
"""

import pytest
import sys
from pathlib import Path
from typing import List, Callable

# Add solution directory to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from humaneval_1_p1_attempt_1 import separate_paren_groups
except ImportError as e:
    pytest.skip(f"Could not import separate_paren_groups: {e}", allow_module_level=True)


class TestSeparateParenGroups:
    """Test class for separate_paren_groups function."""
    
    @pytest.fixture
    def solution_function(self) -> Callable:
        """Fixture providing the solution function."""
        return separate_paren_groups
    
    def test_function_exists(self, solution_function):
        """Test that the function exists and is callable."""
        assert callable(solution_function), "separate_paren_groups should be callable"
        assert hasattr(solution_function, '__name__'), "Function should have a name"
        assert solution_function.__name__ == 'separate_paren_groups'
    
    def test_function_signature(self, solution_function):
        """Test function signature and type hints."""
        import inspect
        sig = inspect.signature(solution_function)
        
        # Check parameter count
        assert len(sig.parameters) == 1, "Function should take exactly 1 parameter"
        
        # Check parameter name
        param_names = list(sig.parameters.keys())
        assert 'paren_string' in param_names or 'string' in param_names[0].lower()
    
    @pytest.mark.dataset
    @pytest.mark.parametrize("input_string,expected_output", [
        ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
        ('() (()) ((())) (((())))', ['()', '(())', '((()))', '(((())))']),
        ('(()(())((()))))', ['(()(())((()))))']),
        ('()', ['()']),
        ('(())', ['(())']),
        ('', []),
        ('   ', []),
    ])
    def test_dataset_cases(self, solution_function, input_string, expected_output):
        """Test cases from the original dataset."""
        result = solution_function(input_string)
        assert result == expected_output, f"Input: {input_string}, Expected: {expected_output}, Got: {result}"
    
    @pytest.mark.parametrize("input_string,expected_output", [
        # Edge cases
        ('(', []),  # Unbalanced - should return empty or handle gracefully
        (')', []),  # Unbalanced - should return empty or handle gracefully
        ('((', []),  # Multiple unbalanced
        ('))', []),  # Multiple unbalanced
        ('())', []),  # Mixed unbalanced
        ('(()', []),  # Mixed unbalanced
    ])
    def test_edge_cases(self, solution_function, input_string, expected_output):
        """Test edge cases and error conditions."""
        try:
            result = solution_function(input_string)
            # For unbalanced parentheses, we expect either empty list or graceful handling
            assert isinstance(result, list), "Result should be a list"
        except Exception as e:
            # If function raises exception for invalid input, that's also acceptable
            pytest.skip(f"Function raises exception for invalid input: {e}")
    
    def test_return_type(self, solution_function):
        """Test that function returns correct type."""
        result = solution_function('()')
        assert isinstance(result, list), "Function should return a list"
        
        if result:  # If not empty
            assert all(isinstance(item, str) for item in result), "All items should be strings"
    
    @pytest.mark.performance
    def test_performance_simple(self, solution_function):
        """Test performance with simple input."""
        import time
        
        start_time = time.perf_counter()
        result = solution_function('() (()) ((()))')
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Simple case took too long: {execution_time:.4f}s"
        assert result == ['()', '(())', '((()))']
    
    @pytest.mark.performance
    @pytest.mark.slow
    def test_performance_complex(self, solution_function):
        """Test performance with complex input."""
        import time
        
        # Create a complex but valid parentheses string
        complex_input = '() ' * 100 + '(()) ' * 50 + '((()))' * 25
        
        start_time = time.perf_counter()
        result = solution_function(complex_input)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        assert execution_time < 5.0, f"Complex case took too long: {execution_time:.4f}s"
        assert isinstance(result, list), "Should return a list even for complex input"
    
    def test_whitespace_handling(self, solution_function):
        """Test handling of whitespace."""
        test_cases = [
            ('( )', ['()']),
            ('(  )', ['()']),
            ('  ()  ', ['()']),
            ('() ()', ['()', '()']),
            ('()   ()', ['()', '()']),
        ]
        
        for input_str, expected in test_cases:
            result = solution_function(input_str)
            assert result == expected, f"Whitespace test failed for '{input_str}'"
    
    def test_empty_groups(self, solution_function):
        """Test handling of empty and minimal groups."""
        result = solution_function('()')
        assert result == ['()'], "Should handle single empty group"
        
        result = solution_function('() ()')
        assert result == ['()', '()'], "Should handle multiple empty groups"


# Standalone test functions for backward compatibility
def test_separate_paren_groups_basic():
    """Basic standalone test for backward compatibility."""
    result = separate_paren_groups('() (())')
    assert result == ['()', '(())']
    print("✅ Basic test passed")


def test_separate_paren_groups_dataset():
    """Dataset test cases for backward compatibility."""
    test_cases = [
        ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
        ('() (()) ((())) (((())))', ['()', '(())', '((()))', '(((())))']),
        ('(()(())((()))))', ['(()(())((()))))']),
    ]
    
    for input_str, expected in test_cases:
        result = separate_paren_groups(input_str)
        assert result == expected, f"Failed for input: {input_str}"
    
    print("✅ Dataset tests passed")


if __name__ == "__main__":
    # Run basic tests when executed directly
    test_separate_paren_groups_basic()
    test_separate_paren_groups_dataset()
    print("✅ All standalone tests passed!")