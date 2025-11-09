"""
Working test file for humaneval_1_solution.py
"""

import pytest
from humaneval_1_solution import separate_paren_groups


def test_basic_functionality():
    """Test basic functionality."""
    result = separate_paren_groups('( ) (( )) (( )( ))')
    expected = ['()', '(())', '(()())']
    assert result == expected


def test_complex_nested():
    """Test complex nested parentheses."""
    result = separate_paren_groups('() (()) ((())) (((())))') 
    expected = ['()', '(())', '((()))', '(((())))']
    assert result == expected


def test_single_group():
    """Test single complex group."""
    result = separate_paren_groups('(()(())((())))') 
    expected = ['(()(())((())))']
    assert result == expected


def test_empty_string():
    """Test empty string."""
    result = separate_paren_groups('')
    expected = []
    assert result == expected


def test_invalid_characters():
    """Test invalid characters."""
    result = separate_paren_groups('(a)')
    expected = []
    assert result == expected


def test_unbalanced():
    """Test unbalanced parentheses."""
    result = separate_paren_groups('(()')
    expected = []
    assert result == expected