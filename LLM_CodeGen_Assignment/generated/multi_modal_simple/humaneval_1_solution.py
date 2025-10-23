# Multi-Modal Solution (Groq + Gemini)
# Problem: Easy/1
# Generated: 2025-10-22 20:12:22

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string.
    Separate groups are balanced (each open brace is properly closed) and
    not nested within each other (meaning only top-level, self-contained
    groups are extracted).

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
                        Spaces are ignored. Any other non-parenthesis characters
                        will cause the function to consider the input malformed
                        and return an empty list.

    Returns:
    List[str]: A list of separated paren groups.
               Returns an empty list if the input string is malformed
               (e.g., unbalanced parentheses, contains invalid characters
               other than '(', ')', or space).
    """
    groups = []
    stack = []
    # Use a list to build the current group string efficiently.
    # Appending to a list and then joining is generally faster than repeated string concatenation.
    current_group_chars = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group_chars.append(char)
        elif char == ')':
            # If a closing parenthesis is encountered and the stack is empty,
            # it means there's an unmatched closing parenthesis, indicating malformed input.
            if not stack:
                return []
            
            stack.pop()
            current_group_chars.append(char)
            
            # If the stack becomes empty after popping, it signifies that
            # a complete top-level parenthesis group has been found.
            if not stack:
                groups.append("".join(current_group_chars))
                current_group_chars = []  # Reset for the next group
        elif char == ' ':
            # As per the example, spaces are ignored and should not be part of the output groups.
            pass
        else:
            # Any character that is not an opening parenthesis, closing parenthesis, or space
            # is considered an invalid character, making the input malformed.
            return []
            
    # After iterating through the entire string, if the stack is not empty,
    # it means there are unmatched opening parentheses, indicating malformed input.
    if stack:
        return []
        
    # All groups are balanced and extracted.
    return groups