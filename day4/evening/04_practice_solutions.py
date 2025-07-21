"""
Hash Table Practice Solutions
============================

Complete solutions to the hash table practice exercises.
"""

from typing import List, Dict
from collections import defaultdict, Counter

def practice_problem_1_solution():
    """Character Frequency Counter - Solution"""
    def count_characters(s: str) -> Dict[str, int]:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    
    # Alternative solution using Counter
    def count_characters_counter(s: str) -> Dict[str, int]:
        return dict(Counter(s))
    
    # Test cases
    test_cases = [
        ("hello", {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
        ("aabbcc", {'a': 2, 'b': 2, 'c': 2}),
        ("", {}),
        ("a", {'a': 1})
    ]
    
    print("Problem 1: Character Frequency Counter - SOLUTION")
    for i, (input_str, expected) in enumerate(test_cases):
        result = count_characters(input_str)
        print(f"Test {i+1}: Input='{input_str}', Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_2_solution():
    """Find Missing Number - Solution"""
    def find_missing_number(nums: List[int]) -> int:
        # Hash table approach
        num_set = set(nums)
        n = len(nums)
        
        for i in range(n + 1):
            if i not in num_set:
                return i
        
        return -1  # Should never reach here
    
    # Alternative mathematical approach
    def find_missing_number_math(nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    # Test cases
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1)
    ]
    
    print("Problem 2: Find Missing Number - SOLUTION")
    for i, (nums, expected) in enumerate(test_cases):
        result = find_missing_number(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_3_solution():
    """Majority Element - Solution"""
    def find_majority_element(nums: List[int]) -> int:
        count = {}
        n = len(nums)
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num
        
        return -1  # Should never reach here given problem constraints
    
    # Alternative solution using Counter
    def find_majority_element_counter(nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common(1)[0][0]
    
    # Test cases
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 1, 2, 2, 2], 1)
    ]
    
    print("Problem 3: Majority Element - SOLUTION")
    for i, (nums, expected) in enumerate(test_cases):
        result = find_majority_element(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_4_solution():
    """Two Sum with Duplicates - Solution"""
    def two_sum_pairs(nums: List[int], target: int) -> List[tuple]:
        seen = set()
        pairs = set()
        
        for num in nums:
            complement = target - num
            if complement in seen:
                # Add pair in sorted order to avoid duplicates
                pair = tuple(sorted([num, complement]))
                pairs.add(pair)
            seen.add(num)
        
        return list(pairs)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 2, 4], 4, [(1, 3), (2, 2)]),
        ([1, 1, 1, 1], 2, [(1, 1)]),
        ([1, 2, 3, 4, 5], 10, []),
        ([5, 5, 5, 5], 10, [(5, 5)])
    ]
    
    print("Problem 4: Two Sum with Duplicates - SOLUTION")
    for i, (nums, target, expected) in enumerate(test_cases):
        result = two_sum_pairs(nums, target)
        result_set = set(result)
        expected_set = set(expected)
        print(f"Test {i+1}: Input={nums}, Target={target}")
        print(f"Expected={expected}, Got={result}")
        print("✓ Passed" if result_set == expected_set else "✗ Failed")
    print()

def practice_problem_5_solution():
    """Group Words by Length - Solution"""
    def group_by_length(words: List[str]) -> Dict[int, List[str]]:
        groups = defaultdict(list)
        
        for word in words:
            groups[len(word)].append(word)
        
        return dict(groups)
    
    # Test cases
    test_cases = [
        (["cat", "dog", "elephant", "mouse", "ant"], 
         {3: ["cat", "dog", "ant"], 5: ["mouse"], 8: ["elephant"]}),
        (["a", "bb", "ccc"], {1: ["a"], 2: ["bb"], 3: ["ccc"]}),
        ([], {}),
        (["hello", "world"], {5: ["hello", "world"]})
    ]
    
    print("Problem 5: Group Words by Length - SOLUTION")
    for i, (words, expected) in enumerate(test_cases):
        result = group_by_length(words)
        print(f"Test {i+1}: Input={words}")
        print(f"Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_6_solution():
    """First Non-Repeating Character - Solution"""
    def first_non_repeating_char(s: str) -> int:
        char_count = {}
        
        # Count frequencies
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find first character with count 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1
    
    # Test cases
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabbcc", -1),
        ("abcabc", -1),
        ("a", 0)
    ]
    
    print("Problem 6: First Non-Repeating Character - SOLUTION")
    for i, (s, expected) in enumerate(test_cases):
        result = first_non_repeating_char(s)
        print(f"Test {i+1}: Input='{s}', Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def practice_problem_7_solution():
    """Intersection of Multiple Arrays - Solution"""
    def find_intersection(arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return []
        
        # Start with the first array
        intersection = set(arrays[0])
        
        # Find intersection with each subsequent array
        for arr in arrays[1:]:
            intersection &= set(arr)
        
        return list(intersection)
    
    # Alternative approach using Counter
    def find_intersection_counter(arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return []
        
        element_count = Counter()
        
        # Count in how many arrays each element appears
        for arr in arrays:
            for num in set(arr):  # Use set to count each element once per array
                element_count[num] += 1
        
        # Return elements that appear in all arrays
        return [num for num, count in element_count.items() if count == len(arrays)]
    
    # Test cases
    test_cases = [
        ([[1, 2, 3], [2, 3, 4], [3, 4, 5]], [3]),
        ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 2, 3]),
        ([[1, 2], [3, 4]], []),
        ([[1]], [1])
    ]
    
    print("Problem 7: Intersection of Multiple Arrays - SOLUTION")
    for i, (arrays, expected) in enumerate(test_cases):
        result = find_intersection(arrays)
        result_set = set(result)
        expected_set = set(expected)
        print(f"Test {i+1}: Input={arrays}")
        print(f"Expected={expected}, Got={result}")
        print("✓ Passed" if result_set == expected_set else "✗ Failed")
    print()

def practice_problem_8_solution():
    """Longest Consecutive Sequence - Solution"""
    def longest_consecutive(nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current_length = 1
                current_num = num
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
    
    # Test cases
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 0, 1], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7)
    ]
    
    print("Problem 8: Longest Consecutive Sequence - SOLUTION")
    for i, (nums, expected) in enumerate(test_cases):
        result = longest_consecutive(nums)
        print(f"Test {i+1}: Input={nums}, Expected={expected}, Got={result}")
        print("✓ Passed" if result == expected else "✗ Failed")
    print()

def advanced_hash_table_problems():
    """Additional advanced hash table problems"""
    
    print("ADVANCED HASH TABLE PROBLEMS")
    print("=" * 40)
    
    # Problem: Design a data structure that supports insert, delete, and random access
    class RandomizedSet:
        def __init__(self):
            self.vals = []  # List to store values
            self.val_to_index = {}  # Hash map: value -> index in vals
        
        def insert(self, val: int) -> bool:
            if val in self.val_to_index:
                return False
            
            self.vals.append(val)
            self.val_to_index[val] = len(self.vals) - 1
            return True
        
        def remove(self, val: int) -> bool:
            if val not in self.val_to_index:
                return False
            
            # Move last element to the position of element to remove
            last_val = self.vals[-1]
            index_to_remove = self.val_to_index[val]
            
            self.vals[index_to_remove] = last_val
            self.val_to_index[last_val] = index_to_remove
            
            # Remove the last element
            self.vals.pop()
            del self.val_to_index[val]
            
            return True
        
        def get_random(self) -> int:
            import random
            return random.choice(self.vals)
    
    # Test RandomizedSet
    print("Advanced Problem: RandomizedSet")
    rs = RandomizedSet()
    print(f"Insert 1: {rs.insert(1)}")  # True
    print(f"Insert 2: {rs.insert(2)}")  # True
    print(f"Insert 1: {rs.insert(1)}")  # False (duplicate)
    print(f"Random: {rs.get_random()}")  # 1 or 2
    print(f"Remove 1: {rs.remove(1)}")  # True
    print(f"Remove 1: {rs.remove(1)}")  # False (doesn't exist)
    print()
    
    # Problem: LRU Cache
    class LRUCache:
        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = {}
            self.order = []  # Most recently used at the end
        
        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            
            # Move to end (most recently used)
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        
        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                # Update existing key
                self.cache[key] = value
                self.order.remove(key)
                self.order.append(key)
            else:
                # Add new key
                if len(self.cache) >= self.capacity:
                    # Remove least recently used
                    lru_key = self.order.pop(0)
                    del self.cache[lru_key]
                
                self.cache[key] = value
                self.order.append(key)
    
    # Test LRU Cache
    print("Advanced Problem: LRU Cache")
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"Get 1: {lru.get(1)}")  # 1
    lru.put(3, 3)  # Evicts key 2
    print(f"Get 2: {lru.get(2)}")  # -1 (not found)
    lru.put(4, 4)  # Evicts key 1
    print(f"Get 1: {lru.get(1)}")  # -1 (not found)
    print(f"Get 3: {lru.get(3)}")  # 3
    print(f"Get 4: {lru.get(4)}")  # 4
    print()

def run_all_solutions():
    """Run all practice problem solutions"""
    print("HASH TABLE PRACTICE SOLUTIONS")
    print("=" * 50)
    
    practice_problem_1_solution()
    practice_problem_2_solution()
    practice_problem_3_solution()
    practice_problem_4_solution()
    practice_problem_5_solution()
    practice_problem_6_solution()
    practice_problem_7_solution()
    practice_problem_8_solution()
    
    advanced_hash_table_problems()
    
    print("=" * 50)
    print("All solutions completed!")
    print("Key takeaways:")
    print("- Hash tables provide O(1) average time complexity")
    print("- Use dictionaries for counting, mapping, and caching")
    print("- Sets are useful for membership testing and uniqueness")
    print("- Consider space-time tradeoffs when using hash tables")
    print("- Hash tables are essential for many algorithm optimizations")

if __name__ == "__main__":
    run_all_solutions()
