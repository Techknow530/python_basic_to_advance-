"""
Hash Tables / Dictionaries - LeetCode Style Problems
===================================================

This file contains common hash table problems that frequently appear in
technical interviews and competitive programming.
"""

from typing import List, Dict, Optional, Tuple
from collections import defaultdict, Counter
import string

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    LeetCode 1: Two Sum
    
    Given an array of integers nums and an integer target, return indices of 
    the two numbers such that they add up to target.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    
    return []  # No solution found

def contains_duplicate(nums: List[int]) -> bool:
    """
    LeetCode 217: Contains Duplicate
    
    Given an integer array nums, return true if any value appears at least 
    twice in the array.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def valid_anagram(s: str, t: str) -> bool:
    """
    LeetCode 242: Valid Anagram
    
    Given two strings s and t, return true if t is an anagram of s.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - limited character set
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    LeetCode 49: Group Anagrams
    
    Given an array of strings strs, group the anagrams together.
    
    Time Complexity: O(n * m * log(m)) where n is number of strings, m is avg length
    Space Complexity: O(n * m)
    """
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort characters to create a key
        sorted_chars = ''.join(sorted(s))
        anagram_groups[sorted_chars].append(s)
    
    return list(anagram_groups.values())

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 347: Top K Frequent Elements
    
    Given an integer array nums and an integer k, return the k most frequent elements.
    
    Time Complexity: O(n + k*log(n))
    Space Complexity: O(n)
    """
    # Count frequencies
    frequency = Counter(nums)
    
    # Sort by frequency (descending) and take first k
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

def first_unique_character(s: str) -> int:
    """
    LeetCode 387: First Unique Character in a String
    
    Given a string s, find the first non-repeating character and return its index.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - limited character set
    """
    char_count = {}
    
    # Count all characters
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    """
    LeetCode 560: Subarray Sum Equals K
    
    Given an array of integers nums and an integer k, return the total number 
    of continuous subarrays whose sum equals to k.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = 0
    prefix_sum = 0
    sum_frequency = {0: 1}  # Initialize with 0 sum occurring once
    
    for num in nums:
        prefix_sum += num
        
        # Check if (prefix_sum - k) exists in our map
        if prefix_sum - k in sum_frequency:
            count += sum_frequency[prefix_sum - k]
        
        # Add current prefix_sum to map
        sum_frequency[prefix_sum] = sum_frequency.get(prefix_sum, 0) + 1
    
    return count

def longest_substring_without_repeating(s: str) -> int:
    """
    LeetCode 3: Longest Substring Without Repeating Characters
    
    Given a string s, find the length of the longest substring without repeating characters.
    
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is charset size
    """
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            # Move start to after the repeated character
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

def ransom_note(ransom_note: str, magazine: str) -> bool:
    """
    LeetCode 383: Ransom Note
    
    Given two strings ransomNote and magazine, return true if ransomNote can be 
    constructed by using the letters from magazine.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1) - limited character set
    """
    char_count = {}
    
    # Count characters in magazine
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if we can construct ransom note
    for char in ransom_note:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

def isomorphic_strings(s: str, t: str) -> bool:
    """
    LeetCode 205: Isomorphic Strings
    
    Given two strings s and t, determine if they are isomorphic.
    
    Time Complexity: O(n)
    Space Complexity: O(1) - limited character set
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        char_s, char_t = s[i], t[i]
        
        # Check s -> t mapping
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check t -> s mapping
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True

def find_all_anagrams(s: str, p: str) -> List[int]:
    """
    LeetCode 438: Find All Anagrams in a String
    
    Given two strings s and p, return an array of all the start indices of p's 
    anagrams in s.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1) - limited character set
    """
    if len(p) > len(s):
        return []
    
    result = []
    p_count = Counter(p)
    window_count = Counter()
    
    # Initialize window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    # Check first window
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        old_char = s[i - len(p)]
        window_count[old_char] -= 1
        if window_count[old_char] == 0:
            del window_count[old_char]
        
        # Check if current window is anagram
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def word_pattern(pattern: str, s: str) -> bool:
    """
    LeetCode 290: Word Pattern
    
    Given a pattern and a string s, find if s follows the same pattern.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    words = s.split()
    
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for i in range(len(pattern)):
        char, word = pattern[i], words[i]
        
        # Check char -> word mapping
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        # Check word -> char mapping
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

def intersection_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    LeetCode 349: Intersection of Two Arrays
    
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    
    Time Complexity: O(n + m)
    Space Complexity: O(min(n, m))
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

def happy_number(n: int) -> bool:
    """
    LeetCode 202: Happy Number
    
    A happy number is a number defined by the following process:
    - Replace the number by the sum of the squares of its digits.
    - Repeat until the number equals 1 (happy) or loops endlessly in a cycle.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1

def four_sum_ii(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    """
    LeetCode 454: 4Sum II
    
    Given four integer arrays nums1, nums2, nums3, and nums4, return the number 
    of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.
    
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    count = 0
    sum_count = defaultdict(int)
    
    # Store all possible sums of nums1 and nums2
    for a in nums1:
        for b in nums2:
            sum_count[a + b] += 1
    
    # Check if complement exists in nums3 and nums4
    for c in nums3:
        for d in nums4:
            complement = -(c + d)
            count += sum_count[complement]
    
    return count

# Test functions
def test_hash_table_problems():
    """Test all hash table problems with sample inputs"""
    print("Testing Hash Table Problems")
    print("=" * 40)
    
    # Test Two Sum
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))
    
    # Test Contains Duplicate
    print("2. Contains Duplicate:", contains_duplicate([1, 2, 3, 1]))
    
    # Test Valid Anagram
    print("3. Valid Anagram:", valid_anagram("anagram", "nagaram"))
    
    # Test Group Anagrams
    print("4. Group Anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    
    # Test Top K Frequent
    print("5. Top K Frequent:", top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    
    # Test First Unique Character
    print("6. First Unique Character:", first_unique_character("leetcode"))
    
    # Test Subarray Sum Equals K
    print("7. Subarray Sum Equals K:", subarray_sum_equals_k([1, 1, 1], 2))
    
    # Test Longest Substring Without Repeating
    print("8. Longest Substring:", longest_substring_without_repeating("abcabcbb"))
    
    # Test Ransom Note
    print("9. Ransom Note:", ransom_note("a", "b"))
    
    # Test Isomorphic Strings
    print("10. Isomorphic Strings:", isomorphic_strings("egg", "add"))
    
    # Test Find All Anagrams
    print("11. Find All Anagrams:", find_all_anagrams("abab", "ab"))
    
    # Test Word Pattern
    print("12. Word Pattern:", word_pattern("abba", "dog cat cat dog"))
    
    # Test Intersection of Arrays
    print("13. Intersection:", intersection_of_arrays([1, 2, 2, 1], [2, 2]))
    
    # Test Happy Number
    print("14. Happy Number:", happy_number(19))
    
    # Test 4Sum II
    print("15. 4Sum II:", four_sum_ii([1, 2], [-2, -1], [-1, 2], [0, 2]))

if __name__ == "__main__":
    test_hash_table_problems()
