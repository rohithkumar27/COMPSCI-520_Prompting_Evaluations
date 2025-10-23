# Groq solution using step_chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/9
# Difficulty: Easy

from typing import List

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:  # edge case: empty string
        return ''

    rev_str = string[::-1]  # reverse the input string
    for i in range(len(string)):  # find the longest palindromic suffix
        if string[i:] == string[i:][::-1]:
            return string + rev_str[i:]  # append the reverse of the prefix

    return string + rev_str  # if no palindromic suffix found, append the whole reverse
