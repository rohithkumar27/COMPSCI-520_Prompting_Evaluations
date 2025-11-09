"""
Basic test file for problem_1
Auto-generated for coverage analysis.
"""

import pytest
from test_humaneval_1_solution import *


def test_basic_functionality():
    """Basic test to ensure the solution can be imported and executed."""
    # This is a placeholder test - real tests should be provided
    # for meaningful coverage analysis
    assert True, "Solution imports successfully"


def test_function_exists():
    """Test that the main function exists and is callable."""
    # Try to find the main function in the solution
    import inspect
    import test_humaneval_1_solution as solution_module
    
    functions = [name for name, obj in inspect.getmembers(solution_module) 
                if inspect.isfunction(obj) and not name.startswith('_')]
    
    assert len(functions) > 0, "No functions found in solution"
    
    # Test that at least one function is callable
    main_func = getattr(solution_module, functions[0])
    assert callable(main_func), f"Function {functions[0]} is not callable"
