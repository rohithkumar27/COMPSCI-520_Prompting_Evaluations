# Groq solution using chain_of_thought (Attempt 3/3)
# Dataset: Unknown
# Problem: Easy/1
# Difficulty: Easy

from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    # Find all balanced groups of parentheses in the input string
    groups = re.findall(r'\([^()]+\)', paren_string)
    
    # Return the list of groups
    return groups
