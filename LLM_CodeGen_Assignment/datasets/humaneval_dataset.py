"""
Comprehensive HumanEval Dataset: 30 Problems
- 10 Easy Problems (Basic operations, simple logic)
- 10 Medium Problems (Algorithms, data structures)  
- 10 Hard Problems (Complex algorithms, optimization)
"""

HUMANEVAL_PROBLEMS = [
    # ========== EASY PROBLEMS (1-10) ==========
    {
        "task_id": "Easy/0",
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([1.0, 2.0, 3.0], 0.5) == False\n    assert candidate([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True\n\ncheck(has_close_elements)"
    },
    {
        "task_id": "Easy/1",
        "difficulty": "Easy", 
        "prompt": "from typing import List\n\n\ndef separate_paren_groups(paren_string: str) -> List[str]:\n    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\n    separate those group and return the list of those. Separate groups are balanced (each open brace is properly closed)\n    and not nested within each other\n    Input: '( ) (( )) (( )( ))'\n    Output: ['()', '(())', '(()())']\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']\n    assert candidate('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']\n    assert candidate('(()(())((())))') == ['(()(())((())))'] \n\ncheck(separate_paren_groups)"
    },
    {

        "task_id": "Easy/2",
        "difficulty": "Easy",
        "prompt": "\n\ndef truncate_number(number: float) -> float:\n    \"\"\" Given a positive floating point number, it can be decomposed into\n    and integer part (largest integer smaller than given number) and decimals\n    (leftover part always smaller than 1).\n\n    Return the decimal part of the number.\n    >>> truncate_number(3.5)\n    0.5\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate(3.5) == 0.5\n    assert abs(candidate(1.33) - 0.33) < 1e-6\n    assert abs(candidate(123.456) - 0.456) < 1e-6\n\ncheck(truncate_number)"
    },
    {
        "task_id": "Easy/3",
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef below_zero(operations: List[int]) -> bool:\n    \"\"\" You're given a list of deposit and withdrawal operations on a bank account that starts with\n    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and\n    at that point function should return True. Otherwise it should return False.\n    >>> below_zero([1, 2, 3])\n    False\n    >>> below_zero([1, 2, -4, 5])\n    True\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([]) == False\n    assert candidate([1, 2, -3, 1, 2, -3]) == False\n    assert candidate([1, 2, -4, 5, 6]) == True\n    assert candidate([1, 2, -4, 5]) == True\n\ncheck(below_zero)"
    },
    {
        "task_id": "Easy/4",
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef mean_absolute_deviation(numbers: List[float]) -> float:\n    \"\"\" For a given list of input numbers, calculate Mean Absolute Deviation\n    around the mean of this dataset.\n    Mean Absolute Deviation is the average absolute difference between each\n    element and a centerpoint (mean in this case):\n    MAD = average | x - x_mean |\n    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])\n    1.0\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 1.2) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) - 1.5) < 1e-6\n\ncheck(mean_absolute_deviation)"
    },
    # More Easy Problems
    {
        "task_id": "Easy/5",
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef intersperse(numbers: List[int], delimeter: int) -> List[int]:\n    \"\"\" Insert a number 'delimeter' between every two consecutive elements of input list `numbers'\n    >>> intersperse([], 4)\n    []\n    >>> intersperse([1, 2, 3], 4)\n    [1, 4, 2, 4, 3]\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([], 7) == []\n    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]\n    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]\n\ncheck(intersperse)"
    },
    {
        "task_id": "Easy/6", 
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef filter_by_substring(strings: List[str], substring: str) -> List[str]:\n    \"\"\" Filter an input list of strings only for ones that contain given substring\n    >>> filter_by_substring([], 'a')\n    []\n    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')\n    ['abc', 'bacd', 'array']\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([], 'john') == []\n    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']\n    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']\n\ncheck(filter_by_substring)"
    },
    {
        "task_id": "Easy/7",
        "difficulty": "Easy",
        "prompt": "from typing import List, Tuple\n\n\ndef sum_product(numbers: List[int]) -> Tuple[int, int]:\n    \"\"\" For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.\n    Empty sum should be equal to 0 and empty product should be equal to 1.\n    >>> sum_product([])\n    (0, 1)\n    >>> sum_product([1, 2, 3, 4])\n    (10, 24)\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([]) == (0, 1)\n    assert candidate([1, 1, 1]) == (3, 1)\n    assert candidate([100, 0]) == (100, 0)\n    assert candidate([3, 5, 7]) == (15, 105)\n\ncheck(sum_product)"
    },
    {
        "task_id": "Easy/8",
        "difficulty": "Easy",
        "prompt": "from typing import List\n\n\ndef rolling_max(numbers: List[int]) -> List[int]:\n    \"\"\" From a given list of integers, generate a list of rolling maximum element found until given moment\n    in the sequence.\n    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])\n    [1, 2, 3, 3, 3, 4, 4]\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate([]) == []\n    assert candidate([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]\n    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]\n    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]\n\ncheck(rolling_max)"
    },
    {
        "task_id": "Easy/9",
        "difficulty": "Easy",
        "prompt": "def is_palindrome(string: str) -> bool:\n    \"\"\" Test if given string is a palindrome \"\"\"\n    return string == string[::-1]\n\ndef make_palindrome(string: str) -> str:\n    \"\"\" Find the shortest palindrome that begins with a supplied string.\n    Algorithm idea is simple:\n    - Find the longest postfix of supplied string that is a palindrome.\n    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.\n    >>> make_palindrome('')\n    ''\n    >>> make_palindrome('cat')\n    'catac'\n    >>> make_palindrome('cata')\n    'catac'\n    \"\"\"\n",
        "test": "def check(candidate):\n    assert candidate('') == ''\n    assert candidate('x') == 'x'\n    assert candidate('xyz') == 'xyzyx'\n    assert candidate('xyx') == 'xyx'\n    assert candidate('jerry') == 'jerryrrej'\n\ncheck(make_palindrome)"
    },

    # ========== MEDIUM PROBLEMS (10-19) ==========
    
]