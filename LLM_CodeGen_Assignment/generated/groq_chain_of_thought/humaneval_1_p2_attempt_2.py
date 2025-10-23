# Groq solution using chain_of_thought (Attempt 2/3)
# Dataset: Unknown
# Problem: Easy/1
# Difficulty: Easy

from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = re.findall(r'\([^()]+\)', paren_string)
    return groups
