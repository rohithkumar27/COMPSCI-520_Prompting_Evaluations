# Gemini solution using chain_of_thought (Attempt 1/3)
# Dataset: Unknown
# Problem: Easy/6
# Difficulty: Easy

from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result
