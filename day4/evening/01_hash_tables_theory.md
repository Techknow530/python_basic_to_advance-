# Hash Tables and Dictionaries in Python

## What are Hash Tables?
Hash tables (dictionaries in Python) are data structures that store key-value pairs and provide average O(1) time complexity for insertion, deletion, and lookup operations.

## How Hash Tables Work:
1. **Hash Function**: Converts keys into array indices
2. **Collision Handling**: Manages cases where multiple keys hash to the same index
3. **Dynamic Resizing**: Expands/contracts based on load factor

## Python Dictionary Operations:

### Time Complexities:
- **Lookup**: O(1) average, O(n) worst case
- **Insertion**: O(1) average, O(n) worst case
- **Deletion**: O(1) average, O(n) worst case
- **Iteration**: O(n)

### Common Operations:
```python
# Creation
d = {}  # Empty dictionary
d = {"key": "value"}  # With initial data

# Access
value = d["key"]  # Raises KeyError if key doesn't exist
value = d.get("key", "default")  # Returns default if key doesn't exist

# Insertion/Update
d["key"] = "value"

# Deletion
del d["key"]  # Raises KeyError if key doesn't exist
value = d.pop("key", "default")  # Returns default if key doesn't exist

# Checking existence
if "key" in d:
    print("Key exists")

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)
```

## Why Hash Tables are Important:

### 1. Fast Lookups
- O(1) average time complexity
- Perfect for caching and memoization
- Excellent for counting and frequency analysis

### 2. Common Use Cases:
- **Caching**: Store computed results
- **Counting**: Count occurrences of items
- **Grouping**: Group items by categories
- **Mapping**: Create one-to-one or one-to-many relationships
- **Set Operations**: Fast membership testing

### 3. Problem-Solving Patterns:
- **Two-pointer technique**: Use hash table to store complements
- **Sliding window**: Track elements in current window
- **Frequency analysis**: Count character/word frequencies
- **Graph algorithms**: Store visited nodes

## Common LeetCode Patterns:

### 1. Complement Pattern (Two Sum)
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### 2. Counting Pattern
```python
def count_frequency(items):
    frequency = {}
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency
```

### 3. Grouping Pattern
```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

### 4. Caching Pattern (Memoization)
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

## Job Interview Benefits:
- **Fundamental Data Structure**: Essential for technical interviews
- **Algorithm Optimization**: Often key to improving time complexity
- **Real-world Applications**: Used in databases, caches, and more
- **Problem-solving Skills**: Many interview problems involve hash tables

## Common Interview Questions:
1. **Two Sum**: Find two numbers that add up to target
2. **Contains Duplicate**: Check if array has duplicates
3. **Valid Anagram**: Check if two strings are anagrams
4. **Group Anagrams**: Group strings that are anagrams
5. **Subarray Sum Equals K**: Find subarrays with given sum
6. **Longest Substring Without Repeating**: Find longest unique substring
7. **Top K Frequent Elements**: Find k most frequent elements

## Tips for Hash Table Problems:
1. **Think about what to store**: Keys vs values
2. **Consider edge cases**: Empty inputs, single elements
3. **Use appropriate methods**: `get()`, `setdefault()`, `defaultdict`
4. **Watch for collision handling**: Understand worst-case scenarios
5. **Memory vs time trade-offs**: Hash tables use extra space for speed

## Advanced Concepts:
- **Load Factor**: Ratio of stored elements to total capacity
- **Collision Resolution**: Chaining vs open addressing
- **Hash Functions**: Properties of good hash functions
- **Resizing**: When and how hash tables resize
- **Ordered Dictionaries**: Maintain insertion order (Python 3.7+)
