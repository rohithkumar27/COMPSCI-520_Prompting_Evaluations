# Groq solution using chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/9
# Difficulty: Easy

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
