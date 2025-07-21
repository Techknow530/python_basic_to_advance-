"""
Hash Table Practice Exercises
============================

Practice problems to master hash table concepts.
Complete these exercises to build confidence.
"""

from typing import List, Dict
from collections import defaultdict, Counter

def practice_problem_1():
    """
    Character Frequency Counter
    
    Write a function that takes a string and returns a dictionary
    with the frequency of each character.
    
    Example:
    Input: "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    def count_characters(s: str) -> Dict[str, int]:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ("hello", {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
        ("aabbcc", {'a': 2, 'b': 2, 'c': 2}),
        ("", {}),
        ("a", {'a': 1})
    ]
    
    print("Problem 1: Character Frequency Counter")
    for i, (input_str, expected) in enumerate(test_cases):
        result = count_characters(input_str)
        print(f"Test {i+1}: Input='{input_str}', Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_2():
    """
    Find Missing Number
    
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
    find the one that is missing.
    
    Example:
    Input: [3, 0, 1]
    Output: 2
    """
    def find_missing_number(nums: List[int]) -> int:
        # TODO: Implement this function using hash table approach
        pass
    
    # Test cases
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1)
    ]
    
    print("Problem 2: Find Missing Number")
    for i, (nums, expected) in enumerate(test_cases):
        result = find_missing_number(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_3():
    """
    Majority Element
    
    Given an array of size n, find the majority element. The majority element
    is the element that appears more than ⌊n/2⌋ times.
    
    Example:
    Input: [3, 2, 3]
    Output: 3
    """
    def find_majority_element(nums: List[int]) -> int:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 1, 2, 2, 2], 1)
    ]
    
    print("Problem 3: Majority Element")
    for i, (nums, expected) in enumerate(test_cases):
        result = find_majority_element(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_4():
    """
    Two Sum with Duplicates
    
    Given an array of integers and a target, find all unique pairs that sum to target.
    
    Example:
    Input: [1, 2, 3, 2, 4], target = 4
    Output: [(1, 3), (2, 2)]
    """
    def two_sum_pairs(nums: List[int], target: int) -> List[tuple]:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 2, 4], 4, [(1, 3), (2, 2)]),
        ([1, 1, 1, 1], 2, [(1, 1)]),
        ([1, 2, 3, 4, 5], 10, []),
        ([5, 5, 5, 5], 10, [(5, 5)])
    ]
    
    print("Problem 4: Two Sum with Duplicates")
    for i, (nums, target, expected) in enumerate(test_cases):
        result = two_sum_pairs(nums, target)
        result_set = set(result)
        expected_set = set(expected)
        print(f"Test {i+1}: Input={nums}, Target={target}")
        print(f"Expected={expected}, Got={result}")
        print(f"✓ Passed" if result_set == expected_set else "✗ Failed")
    print()

def practice_problem_5():
    """
    Group Words by Length
    
    Given a list of words, group them by their length.
    
    Example:
    Input: ["cat", "dog", "elephant", "mouse", "ant"]
    Output: {3: ["cat", "dog", "ant"], 5: ["mouse"], 8: ["elephant"]}
    """
    def group_by_length(words: List[str]) -> Dict[int, List[str]]:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        (["cat", "dog", "elephant", "mouse", "ant"], 
         {3: ["cat", "dog", "ant"], 5: ["mouse"], 8: ["elephant"]}),
        (["a", "bb", "ccc"], {1: ["a"], 2: ["bb"], 3: ["ccc"]}),
        ([], {}),
        (["hello", "world"], {5: ["hello", "world"]})
    ]
    
    print("Problem 5: Group Words by Length")
    for i, (words, expected) in enumerate(test_cases):
        result = group_by_length(words)
        print(f"Test {i+1}: Input={words}")
        print(f"Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_6():
    """
    First Non-Repeating Character
    
    Given a string, find the first non-repeating character and return its index.
    If it doesn't exist, return -1.
    
    Example:
    Input: "leetcode"
    Output: 0 (character 'l' at index 0)
    """
    def first_non_repeating_char(s: str) -> int:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabbcc", -1),
        ("abcabc", -1),
        ("a", 0)
    ]
    
    print("Problem 6: First Non-Repeating Character")
    for i, (s, expected) in enumerate(test_cases):
        result = first_non_repeating_char(s)
        print(f"Test {i+1}: Input='{s}', Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_7():
    """
    Intersection of Multiple Arrays
    
    Given multiple arrays, find elements that appear in all arrays.
    
    Example:
    Input: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    Output: [3]
    """
    def find_intersection(arrays: List[List[int]]) -> List[int]:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ([[1, 2, 3], [2, 3, 4], [3, 4, 5]], [3]),
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 2, 3]),
        ([[1, 2], [3, 4]], []),
        ([[1]], [1])
    ]
    
    print("Problem 7: Intersection of Multiple Arrays")
    for i, (arrays, expected) in enumerate(test_cases):
        result = find_intersection(arrays)
        result_set = set(result)
        expected_set = set(expected)
        print(f"Test {i+1}: Input={arrays}")
        print(f"Expected={expected}, Got={result}")
        print(f"✓ Passed" if result_set == expected_set else "✗ Failed")
    print()

def practice_problem_8():
    """
    Longest Consecutive Sequence
    
    Given an unsorted array of integers, find the length of the longest
    consecutive elements sequence.
    
    Example:
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4 (sequence: [1, 2, 3, 4])
    """
    def longest_consecutive(nums: List[int]) -> int:
        # TODO: Implement this function
        pass
    
    # Test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 0, 1], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7)
    ]
    
    print("Problem 8: Longest Consecutive Sequence")
    for i, (nums, expected) in enumerate(test_cases):
        result = longest_consecutive(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print(f"✓ Passed" if result == expected else "✗ Failed")
    print()

def run_all_practice_problems():
    """Run all practice problems"""
    print("HASH TABLE PRACTICE PROBLEMS")
    print("=" * 50)
    print("Complete the TODO functions and run this script to test your solutions.\n")
    
    practice_problem_1()
    practice_problem_2()
    practice_problem_3()
    practice_problem_4()
    practice_problem_5()
    practice_problem_6()
    practice_problem_7()
    practice_problem_8()
    
    print("=" * 50)
    print("Practice complete! Check your solutions against the expected outputs.")
    print("Focus on understanding the hash table patterns used in each problem.")

if __name__ == "__main__":
    run_all_practice_problems()
