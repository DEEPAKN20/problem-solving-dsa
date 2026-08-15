# Arrays in DSA — Complete Notes (Python)

---

## 1. What is an Array?

An array is a **collection of elements stored in contiguous memory locations**, all of the same type, accessed using an **index**.

**Key properties:**
- Fixed size (in classic arrays like C/Java) — Python's `list` is dynamic
- Elements accessed in **O(1)** time via index
- Elements stored contiguously → cache-friendly, fast iteration

### Array vs Python `list`
| Feature | C/Java array | Python `list` |
|---|---|---|
| Size | Fixed | Dynamic (auto-resizes) |
| Type | Homogeneous | Can hold mixed types |
| Memory | Contiguous, fixed-size elements | Contiguous array of *pointers* to objects |
| Resizing | Not possible | Automatic (over-allocates ~1.125x when full) |

Python also has a stricter `array` module (`import array`) for homogeneous, memory-efficient arrays, and `numpy.ndarray` for numerical computing (fixed-type, contiguous, vectorized — this is what real array-based DSA performance looks like).

```python
# Python list (most common in DSA prep)
arr = [10, 20, 30, 40]

# array module — homogeneous, more memory-efficient
from array import array
a = array('i', [10, 20, 30])   # 'i' = signed int

# numpy — used heavily in quant/finance work
import numpy as np
np_arr = np.array([10, 20, 30])
```

---

## 2. Memory Model

```
Index:      0     1     2     3
Value:     [10]  [20]  [30]  [40]
Address:  1000  1004  1008  1012   (assuming 4 bytes/int, contiguous)
```

Address of element at index `i` = `base_address + i * size_of_element`
→ This formula is *why* array access is **O(1)** — no traversal needed, just arithmetic.

In Python, a `list` stores **references (pointers)** to objects, not the raw values themselves — so indexing is still O(1), but there's an extra dereference step.

---

## 3. Basic Operations & Time Complexity

| Operation | Description | Time Complexity |
|---|---|---|
| Access `arr[i]` | Get element by index | O(1) |
| Update `arr[i] = x` | Set element by index | O(1) |
| Traverse | Visit every element | O(n) |
| Search (unsorted) | Find a value | O(n) |
| Search (sorted, binary search) | Find a value | O(log n) |
| Insert at end | `append()` | O(1) amortized |
| Insert at index `i` | `insert(i, x)` | O(n) — shifts elements |
| Delete at end | `pop()` | O(1) |
| Delete at index `i` | `pop(i)` / `del arr[i]` | O(n) — shifts elements |
| Delete by value | `remove(x)` | O(n) — search + shift |

```python
arr = [1, 2, 3, 4, 5]

arr[2]             # access -> 3            O(1)
arr[2] = 99        # update -> [1,2,99,4,5]  O(1)
arr.append(6)      # [1,2,99,4,5,6]          O(1) amortized
arr.insert(1, 100) # insert at index 1       O(n)
arr.pop()          # remove last             O(1)
arr.pop(0)         # remove first            O(n)
arr.remove(99)     # remove by value         O(n)
```

### Why is `append()` "amortized" O(1)?
Python lists over-allocate memory. When capacity is exceeded, it allocates a **new, larger block** (roughly 1.125x growth) and copies all elements — an O(n) operation — but this happens rarely enough that the *average* cost per append across many operations is O(1).

---

## 4. 1D Array — Core Patterns

### 4.1 Traversal
```python
arr = [4, 2, 7, 1, 9]
for i in range(len(arr)):
    print(arr[i])

for val in arr:        # pythonic
    print(val)
```

### 4.2 Linear Search — O(n)
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### 4.3 Binary Search — O(log n) — requires SORTED array
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
Python also has the `bisect` module for production-grade binary search:
```python
import bisect
bisect.bisect_left(arr, target)   # insertion point (leftmost)
```

### 4.4 Reversal
```python
arr = [1, 2, 3, 4, 5]
arr.reverse()          # in-place, O(n)
arr = arr[::-1]        # new list, O(n)

# manual two-pointer reversal (interview favorite)
def reverse(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
```

### 4.5 Rotation
```python
def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

def rotate_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]
```

---

## 5. Two-Pointer Technique

Used when scanning from both ends or tracking a pair — reduces O(n²) brute force to O(n).

```python
# Example: Check if array has a pair summing to target (sorted array)
def has_pair_with_sum(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1
    return False
```

**Common two-pointer problems:** pair sum, container with most water, remove duplicates from sorted array, merge two sorted arrays, trapping rain water.

---

## 6. Sliding Window Technique

Used for contiguous subarray problems — avoids recomputation by "sliding" the window instead of restarting.

```python
# Max sum of subarray of size k — O(n)
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

**Variable-size window example — smallest subarray with sum ≥ target:**
```python
def min_subarray_len(target, arr):
    l = 0
    total = 0
    min_len = float('inf')
    for r in range(len(arr)):
        total += arr[r]
        while total >= target:
            min_len = min(min_len, r - l + 1)
            total -= arr[l]
            l += 1
    return min_len if min_len != float('inf') else 0
```

---

## 7. Prefix Sum Technique

Precompute cumulative sums to answer range-sum queries in O(1) after O(n) preprocessing.

```python
def build_prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def range_sum(prefix, l, r):   # sum of arr[l..r] inclusive
    return prefix[r + 1] - prefix[l]
```

**Use cases:** range sum queries, subarray sum equals K (with hashmap), equilibrium index.

```python
# Subarray sum equals K — O(n) using prefix sum + hashmap
def subarray_sum_equals_k(arr, k):
    count = 0
    prefix_sum = 0
    seen = {0: 1}
    for num in arr:
        prefix_sum += num
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
```

---

## 8. Kadane's Algorithm — Maximum Subarray Sum (O(n))

Classic DP-on-array technique — very common interview question.

```python
def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
```

**Intuition:** at each index, decide whether to extend the previous subarray or start fresh — because a negative running sum only hurts future sums.

---

## 9. 2D Arrays (Matrices)

```python
# Creating a 2D array (careful: don't use [[0]*cols]*rows — shares references!)
rows, cols = 3, 4
matrix = [[0] * cols for _ in range(rows)]

# Traversal
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])

# Transpose
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Using numpy (preferred for numeric/matrix-heavy work — relevant for quant)
import numpy as np
m = np.zeros((rows, cols))
m.T          # transpose, O(1) view
m @ m.T      # matrix multiplication
```

**Common 2D array problems:** matrix rotation (90°), spiral traversal, search in row/column sorted matrix, set matrix zeroes, island counting (DFS/BFS on grid).

```python
# Rotate matrix 90 degrees clockwise, in-place
def rotate_matrix(matrix):
    n = len(matrix)
    # transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for row in matrix:
        row.reverse()
```

---

## 10. Sorting & Arrays

Arrays are the underlying structure for almost all sorting algorithms. Know the trade-offs:

| Algorithm | Time (avg) | Time (worst) | Space | Stable? |
|---|---|---|---|---|
| Bubble Sort | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(1) | No |
| Python `sorted()`/`.sort()` (Timsort) | O(n log n) | O(n log n) | O(n) | Yes |

```python
# Quick sort — key interview implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

## 11. Advanced Array Techniques

### 11.1 Dutch National Flag Problem (3-way partition, O(n), O(1) space)
Sort an array of 0s, 1s, 2s without extra space.
```python
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1; mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
```

### 11.2 Monotonic Stack (used heavily with arrays)
Solves "next greater element", "stock span", "largest rectangle in histogram".
```python
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []   # stores indices
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
```

### 11.3 Kth largest/smallest — Quickselect, O(n) average
```python
import random

def quickselect(arr, k):   # k-th smallest (1-indexed)
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))
```
(Heap-based approach: `heapq.nlargest(k, arr)` / `heapq.nsmallest(k, arr)` — simpler in practice.)

### 11.4 In-place tricks (O(1) extra space)
- **Cyclic sort** — for arrays containing 1..n: place each number at its correct index in one pass. Used for "find missing number", "find duplicate".
- **Marking via sign/index** — mark visited indices negative to detect duplicates/missing values without a hash set.

```python
# Find the missing number in [1..n] using cyclic sort — O(n) time, O(1) space
def find_missing(arr):
    i = 0
    n = len(arr)
    while i < n:
        correct = arr[i] - 1
        if 0 <= correct < n and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1
```

### 11.5 Difference Array (range update in O(1))
Useful when you need to apply many `add value to range [l, r]` operations efficiently.
```python
def range_update(n, updates):
    diff = [0] * (n + 1)
    for l, r, val in updates:
        diff[l] += val
        diff[r + 1] -= val
    result = [0] * n
    result[0] = diff[0]
    for i in range(1, n):
        result[i] = result[i - 1] + diff[i]
    return result
```

---

## 12. Space-Time Trade-off Summary

| Technique | Time | Space | Typical use |
|---|---|---|---|
| Brute force (nested loop) | O(n²) | O(1) | Baseline for pair/subarray problems |
| Two pointers | O(n) | O(1) | Sorted array pair/window problems |
| Sliding window | O(n) | O(1) | Contiguous subarray problems |
| Prefix sum | O(n) preprocess, O(1) query | O(n) | Range sum queries |
| Hashmap + prefix sum | O(n) | O(n) | Subarray sum = K |
| Sorting first | O(n log n) | O(1)–O(n) | Many array problems simplify after sorting |
| Cyclic sort / in-place marking | O(n) | O(1) | Missing/duplicate number problems |

---

## 13. Common Interview Problem List (practice roadmap)

**Easy:**
1. Find max/min in array
2. Reverse an array
3. Check if array is sorted
4. Remove duplicates from sorted array
5. Move zeroes to end
6. Second largest element

**Medium:**
7. Kadane's algorithm (max subarray sum)
8. Product of array except self
9. Rotate array by k
10. Merge intervals
11. Container with most water
12. 3Sum
13. Subarray sum equals K
14. Find missing/duplicate number in 1..n
15. Sort colors (Dutch flag)

**Hard:**
16. Trapping rain water
17. Median of two sorted arrays
18. Largest rectangle in histogram
19. Sliding window maximum (deque-based, O(n))
20. Next permutation

```python
# Sliding window maximum using deque — O(n)
from collections import deque

def sliding_window_max(arr, k):
    dq = deque()   # stores indices, values in decreasing order
    result = []
    for i, num in enumerate(arr):
        while dq and arr[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
```

---

## 14. Quick Reference — Python List Method Complexities

| Method | Complexity |
|---|---|
| `len(arr)` | O(1) |
| `arr[i]` | O(1) |
| `arr.append(x)` | O(1) amortized |
| `arr.pop()` | O(1) |
| `arr.pop(0)` | O(n) |
| `arr.insert(i, x)` | O(n) |
| `x in arr` | O(n) |
| `arr.sort()` | O(n log n) |
| `arr[::-1]` | O(n) |
| `arr.count(x)` | O(n) |
| `min(arr)`/`max(arr)` | O(n) |
| `sum(arr)` | O(n) |

---

## 15. Notes for Your Track (Quant Dev / Researcher prep)

- Interview rounds at firms like Tower Research, AlphaGrep, iRage often start with **array + two-pointer + sliding window** problems as warm-ups before moving to harder DS/algo or probability questions.
- For performance-sensitive contexts (which matters a lot in quant), get comfortable with **numpy vectorized operations** as the "next level" beyond plain Python lists — avoiding explicit loops matters both for interviews and for real trading-system code.
- Practice platforms: LeetCode (Array tag, ~200+ problems), and time yourself — array problems are usually meant to be solved in 15–20 minutes in interviews.

---

*End of notes. Next natural topics to study after this: Strings (many array techniques reuse directly), Hashing, and Linked Lists.*
