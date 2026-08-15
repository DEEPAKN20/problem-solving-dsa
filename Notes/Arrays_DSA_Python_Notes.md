# Arrays in DSA — Complete Notes (Python)

---

## 1. What is an Array?

An **array** is a collection of elements, stored in **contiguous memory locations**, where each element can be accessed directly using an **index**.

Key properties:
- **Fixed type** (in true arrays — all elements same type)
- **Contiguous memory** → allows O(1) random access
- **Indexed from 0** (in Python, C, Java, etc.)

### Why Arrays Matter
Arrays are the foundation for almost every other data structure — strings, stacks, queues, hash tables (buckets), heaps, and matrices are all built on arrays.

---

## 2. Arrays in Python — Important Nuance

Python does **not** have a "true" fixed-type array as the default. What we normally use is:

```python
arr = [1, 2, 3, 4, 5]   # This is a Python LIST
```

A Python `list` is actually a **dynamic array** — resizable, and can hold mixed types. Internally, it's implemented as an array of *pointers* to objects, not raw values.

If you want a real, memory-efficient, single-type array, Python provides:

```python
import array
a = array.array('i', [1, 2, 3, 4])   # 'i' = signed int type code
```

And for numerical/matrix work, **NumPy** arrays are the industry standard:

```python
import numpy as np
a = np.array([1, 2, 3, 4])
```

| Feature | `list` | `array.array` | `numpy.array` |
|---|---|---|---|
| Type | Mixed types allowed | Single type only | Single type only |
| Speed | Slower | Faster than list | Fastest (vectorized) |
| Memory | High (pointers) | Lower | Lowest |
| Use case | General purpose | Simple typed arrays | Numerical/scientific computing |

> For DSA problem-solving and interviews, `list` is what you'll use 95% of the time.

---

## 3. Memory Representation

```
Index:   0    1    2    3    4
Value:  [10, 20, 30, 40, 50]
Address: 100  104  108  112  116   (if int = 4 bytes)
```

Formula for accessing element at index `i`:
```
address(arr[i]) = base_address + i * size_of_element
```

This is why **array access is O(1)** — it's pure arithmetic, not a search.

---

## 4. Basic Operations & Their Time Complexity

| Operation | Python Syntax | Time Complexity |
|---|---|---|
| Access by index | `arr[i]` | O(1) |
| Update | `arr[i] = x` | O(1) |
| Append (end) | `arr.append(x)` | O(1) amortized |
| Insert (middle) | `arr.insert(i, x)` | O(n) |
| Delete (end) | `arr.pop()` | O(1) |
| Delete (middle) | `arr.pop(i)` / `del arr[i]` | O(n) |
| Search (unsorted) | `x in arr` / linear scan | O(n) |
| Search (sorted) | Binary search | O(log n) |
| Traverse | `for x in arr` | O(n) |
| Slice | `arr[a:b]` | O(k), k = slice length |

### Why append is O(1) amortized
Python lists **over-allocate** memory. When capacity is exceeded, it creates a new, larger array (roughly 1.125× growth factor) and copies old elements over. Most appends are O(1); occasionally one costs O(n) — averaged out, it's O(1) amortized.

---

## 5. Basic Array Code Patterns in Python

### Traversal
```python
arr = [10, 20, 30, 40]
for i in range(len(arr)):
    print(arr[i])

# Pythonic way
for val in arr:
    print(val)
```

### Insertion at a position
```python
arr.insert(2, 99)   # insert 99 at index 2
```

### Deletion
```python
arr.remove(99)     # removes first occurrence of value 99
del arr[0]         # removes element at index 0
arr.pop()          # removes last element
```

### Linear Search
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Binary Search (array must be sorted)
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```
**Time complexity:** O(log n) | **Space:** O(1)

---

## 6. Multi-Dimensional Arrays

### 2D Array (Matrix)
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])   # 6 → row 1, col 2
```

### Creating a 2D array safely
```python
# WRONG — all rows point to the SAME list object
bad = [[0] * 3] * 3

# CORRECT
good = [[0] * 3 for _ in range(3)]
```
This is a classic Python gotcha — `[[0]*n]*m` creates `m` references to the *same* inner list, so modifying one row affects all rows.

### Traversing a 2D array
```python
for row in matrix:
    for val in row:
        print(val, end=' ')
```

---

## 7. Core Array Techniques (Used constantly in interviews & competitive coding)

### A. Two Pointer Technique
Used when array is sorted or you need to compare elements from both ends.

```python
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True
```
**Common uses:** pair sum in sorted array, reversing array, removing duplicates.

### B. Sliding Window Technique
Used for subarray problems (max/min sum, longest substring, etc.) — avoids recomputation.

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```
**Time:** O(n) instead of brute force O(n·k)

### C. Prefix Sum
Precompute cumulative sums to answer range-sum queries in O(1).

```python
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, l, r):   # sum of arr[l..r] inclusive
    return prefix[r + 1] - prefix[l]
```

### D. Kadane's Algorithm (Maximum Subarray Sum)
```python
def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```
**Time:** O(n) | **Space:** O(1) — classic DP-on-array pattern.

### E. Dutch National Flag Algorithm (3-way partition)
Sort an array of 0s, 1s, 2s in-place in one pass.
```python
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
```

### F. Kth Largest/Smallest — using heaps
```python
import heapq

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]
```

### G. Cyclic Sort (for arrays containing 1..n)
Useful for "find missing number" / "find duplicate" problems in O(n) time, O(1) space.
```python
def cyclic_sort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    return arr
```

---

## 8. Common Array Problems (Practice List)

**Easy**
- Reverse an array
- Find max/min element
- Find second largest element
- Move all zeros to the end
- Check if array is sorted

**Medium**
- Maximum subarray sum (Kadane's)
- Merge two sorted arrays
- Find the missing number (1 to n)
- Rotate array by k positions
- Find duplicate in array of n+1 integers
- Product of array except self
- Container with most water (two pointers)

**Hard**
- Trapping Rain Water
- Median of two sorted arrays
- Next Permutation
- Subarray sum equals K (using prefix sum + hashmap)
- Sliding window maximum (using deque)

### Example: Rotate Array by k
```python
def rotate(arr, k):
    n = len(arr)
    k %= n
    arr[:] = arr[-k:] + arr[:-k]
    return arr
```

### Example: Move Zeros to End (in-place, stable)
```python
def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr
```

### Example: Product of Array Except Self (no division)
```python
def product_except_self(arr):
    n = len(arr)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= arr[i]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= arr[i]
    return res
```
**Time:** O(n) | **Space:** O(1) extra (excluding output array)

---

## 9. Sorting Algorithms on Arrays (Quick Reference)

| Algorithm | Best | Average | Worst | Space | Stable? |
|---|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Python `sort()` (Timsort) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

Python's built-in sort:
```python
arr.sort()             # in-place, ascending
arr.sort(reverse=True) # descending
sorted_arr = sorted(arr)  # returns a new list
arr.sort(key=lambda x: -x)  # custom key
```

---

## 10. Advanced Concepts

### A. Dynamic Arrays — How Resizing Really Works
When a Python list exceeds its allocated capacity:
1. A new array of larger size is allocated (growth pattern ~1.125x + constant)
2. All existing elements are copied to the new array
3. Old array is discarded

This is why `append()` is **amortized O(1)** but a single call can occasionally be O(n).

### B. Arrays vs Linked Lists

| Aspect | Array | Linked List |
|---|---|---|
| Access | O(1) | O(n) |
| Insertion (middle) | O(n) | O(1) if node known |
| Memory | Contiguous | Scattered (pointers) |
| Cache performance | Better (locality) | Worse |
| Fixed size (raw array) | Yes (in low-level langs) | No |

### C. Space-Time Tradeoffs
Many array problems can be solved either:
- **O(n) time, O(1) space** (in-place, using array itself as scratch space — e.g., cyclic sort)
- **O(n) time, O(n) space** (using extra hashmap/set for O(1) lookups)

Interviewers often ask you to optimize from O(n) space to O(1) space.

### D. Amortized Analysis
Important concept: even though a single operation might take O(n), when **averaged over many operations**, the cost is O(1). This applies to Python list `append()`.

### E. In-place vs Out-of-place
- **In-place**: modifies the original array, O(1) extra space (e.g., reversing with two pointers)
- **Out-of-place**: creates a new array/copy, O(n) extra space (e.g., `arr[::-1]`)

```python
# In-place reverse
def reverse_inplace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Out-of-place reverse
reversed_arr = arr[::-1]
```

---

## 11. Useful Python-Specific Array Tricks

```python
# List comprehension
squares = [x**2 for x in range(10)]

# Enumerate (index + value)
for i, val in enumerate(arr):
    print(i, val)

# Zip two arrays together
for a, b in zip(arr1, arr2):
    print(a, b)

# Flatten a 2D array
flat = [x for row in matrix for x in row]

# Find max with index
idx = arr.index(max(arr))

# Remove duplicates but preserve order
seen = set()
result = [x for x in arr if not (x in seen or seen.add(x))]

# Count frequency
from collections import Counter
freq = Counter(arr)
```

---

## 12. Quick Summary Table — When to Use What

| Problem Type | Technique |
|---|---|
| Pair with given sum (sorted array) | Two pointers |
| Subarray/substring with constraint | Sliding window |
| Range sum queries | Prefix sum |
| Max/min subarray sum | Kadane's algorithm |
| Numbers in range [1, n] | Cyclic sort |
| Kth largest/smallest | Heap |
| Sort 0s, 1s, 2s | Dutch National Flag |
| Need O(1) lookups | Hash set/map alongside array |

---

## 13. Suggested Practice Order

1. Traversal, insertion, deletion, search
2. Two pointer problems
3. Sliding window problems
4. Prefix sum problems
5. Kadane's algorithm and variations
6. Sorting-based array problems
7. 2D array / matrix problems
8. Advanced: trapping rain water, next permutation, median of two sorted arrays

---

*Good next step: practice 3–5 problems from each section on LeetCode/GeeksforGeeks, tagged "Array," starting Easy → Medium → Hard.*
