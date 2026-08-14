# Big O Notation — Complete Notes (with Python Examples)

## 1. What Problem Does Big O Solve?

When you write code, you want to know: **"If my input gets bigger, how much slower will this get?"**

Big O answers this. It doesn't tell you exact seconds — it tells you the *growth pattern* of time (or memory) as input size `n` grows. This matters because:

- A laptop and a supercomputer both slow down as `n` grows — Big O describes the *shape* of that slowdown, not the raw speed.
- It lets you compare two different algorithms fairly, independent of hardware.

**Key idea:** Big O = "worst-case growth rate" of an algorithm, ignoring constants and lower-order terms.

---

## 2. The Core Rule of Thumb

Count how many times the "basic operation" (comparison, addition, print, etc.) runs, as a function of `n` (input size). Then simplify:

- **Drop constants:** `O(2n)` → `O(n)`
- **Drop lower-order terms:** `O(n² + n)` → `O(n²)`
- **Keep only the fastest-growing term**

Why drop constants? Because for *huge* `n`, the shape of growth matters way more than a fixed multiplier.

---

## 3. Common Big O Classes (Fastest → Slowest)

| Big O | Name | Growth feel |
|---|---|---|
| O(1) | Constant | Instant, doesn't care about n |
| O(log n) | Logarithmic | Very slow growth |
| O(n) | Linear | Grows exactly with n |
| O(n log n) | Linearithmic | Slightly worse than linear |
| O(n²) | Quadratic | Grows fast (nested loops) |
| O(n³) | Cubic | Grows faster still |
| O(2ⁿ) | Exponential | Explodes quickly |
| O(n!) | Factorial | Explodes almost instantly |

---

## 4. Each Class Explained with Python Code

### O(1) — Constant Time
No matter how big the input is, this takes the same time.

```python
def get_first_element(arr):
    return arr[0]   # always 1 step, whether arr has 5 or 5 million items
```

Dictionary/set lookups are also O(1) on average:
```python
d = {"a": 1, "b": 2}
print(d["a"])   # O(1) lookup
```

---

### O(log n) — Logarithmic Time
The problem size gets **cut in half** (or some fraction) every step. Classic example: **binary search**.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

Why O(log n)? Each iteration halves the search space. For `n = 1,000,000`, you only need about **20 steps** (log₂ 1,000,000 ≈ 20). That's the power of log time.

---

### O(n) — Linear Time
Runtime grows exactly in proportion to input size. One loop through the data.

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:          # runs n times
        if num > max_val:
            max_val = num
    return max_val
```

If `n` doubles, time roughly doubles.

---

### O(n log n) — Linearithmic Time
Common in efficient sorting algorithms (merge sort, quicksort average case, Python's built-in `sorted()`).

```python
arr = [5, 2, 8, 1, 9]
sorted_arr = sorted(arr)   # Python's Timsort is O(n log n)
```

Think of it as: "do an O(log n) thing, n times" — e.g., merge sort splits the array (log n levels) and merges at each level (n work per level).

---

### O(n²) — Quadratic Time
Nested loops over the same data. Very common trap for beginners.

```python
def has_duplicates(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):   # nested loop
            if arr[i] == arr[j]:
                return True
    return False
```

For `n = 1000`, that's roughly 1,000,000 operations. Bubble sort, selection sort, insertion sort are all O(n²).

---

### O(n³) — Cubic Time
Three nested loops — common in naive matrix multiplication.

```python
def matrix_multiply(A, B, n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):        # triple nested
                C[i][j] += A[i][k] * B[k][j]
    return C
```

---

### O(2ⁿ) — Exponential Time
Every additional input element **doubles** the work. Classic example: naive recursive Fibonacci.

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)   # branches into 2 calls each time
```

`fib(30)` is already slow. `fib(50)` would take forever. This is why we use memoization/dynamic programming to fix it.

---

### O(n!) — Factorial Time
Generating all permutations of a list.

```python
from itertools import permutations

def all_orderings(arr):
    return list(permutations(arr))   # n! possible orderings
```

For `n = 10`, that's 3,628,800 permutations. For `n = 20`, it's astronomically large. Avoid this unless `n` is tiny.

---

## 5. How to Analyze Your Own Code (Step-by-Step Method)

1. **Find the loops.** Each independent (non-nested) loop over `n` items → add O(n).
2. **Find nested loops.** Loop inside a loop → multiply: O(n) × O(n) = O(n²).
3. **Sequential blocks add, nested blocks multiply.**
   ```python
   for i in range(n):      # O(n)
       print(i)
   for j in range(n):      # O(n)
       print(j)
   # total: O(n) + O(n) = O(2n) → simplifies to O(n)
   ```
4. **Recursive calls:** count how many calls happen and how the problem shrinks each time.
5. **Drop constants and lower-order terms** at the end.

### Worked Example
```python
def example(arr):
    n = len(arr)
    print(arr[0])              # O(1)
    for x in arr:               # O(n)
        print(x)
    for i in range(n):          # O(n^2) — nested loop
        for j in range(n):
            print(i, j)
```
Total = O(1) + O(n) + O(n²) → drop lower-order terms → **O(n²)**

---

## 6. Big O vs Big Ω vs Big Θ (quick mention)

- **Big O (O)** — *upper bound*: worst case. "It will never be slower than this."
- **Big Omega (Ω)** — *lower bound*: best case. "It will never be faster than this."
- **Big Theta (Θ)** — *tight bound*: average/typical case when best = worst.

In everyday conversation, "Big O" is almost always used loosely to mean "the typical/worst-case runtime," even when people technically mean Θ.

---

## 7. Space Complexity (Big O for Memory)

Big O also describes **memory usage**, not just time.

```python
def make_list(n):
    return [i for i in range(n)]   # O(n) space — creates n elements
```

```python
def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total   # O(1) space — only one variable used, regardless of n
```

---

## 8. Common Python Operations & Their Big O (cheat sheet)

| Operation | Big O |
|---|---|
| `list[i]` (indexing) | O(1) |
| `list.append(x)` | O(1) amortized |
| `list.insert(0, x)` | O(n) |
| `x in list` | O(n) |
| `x in set` / `x in dict` | O(1) average |
| `list.sort()` / `sorted()` | O(n log n) |
| `len(list)` | O(1) |
| `dict[key] = value` | O(1) average |
| slicing `list[a:b]` | O(b-a) |
| string concatenation in a loop | O(n²) if done naively |

**Beginner trap:** `x in list` is O(n) because Python checks each item one by one. `x in set`/`dict` is O(1) because it uses hashing. If you're checking membership repeatedly, **use a set, not a list**.

```python
# Slow: O(n) per check, O(n^2) overall if checking n times
names = ["a", "b", "c", ...]
if "z" in names: ...

# Fast: O(1) per check, O(n) overall
names_set = set(names)
if "z" in names_set: ...
```

---

## 9. Quick Growth Comparison (why it matters at scale)

For `n = 1,000`:

| Big O | Approx. operations |
|---|---|
| O(1) | 1 |
| O(log n) | ~10 |
| O(n) | 1,000 |
| O(n log n) | ~10,000 |
| O(n²) | 1,000,000 |
| O(2ⁿ) | astronomically large |

This is why an O(n²) algorithm can feel "fine" on small test data but crash or hang on real-world data.

---

## 10. Summary Cheat Sheet

- **O(1)** — dict/set lookup, array index access
- **O(log n)** — binary search, balanced tree operations
- **O(n)** — single loop, linear search
- **O(n log n)** — efficient sorting (`sorted()`, merge sort)
- **O(n²)** — nested loops, bubble/insertion/selection sort
- **O(2ⁿ)** — naive recursive algorithms without memoization
- **O(n!)** — brute-force permutations

**Golden rules:**
1. Count loops → nested = multiply, sequential = add.
2. Always simplify to the dominant term.
3. Prefer sets/dicts over lists for membership checks.
4. Watch for hidden nested loops (e.g., `x in list` inside a `for` loop = hidden O(n²)).
5. When in doubt, test with a **larger n** and see if runtime explodes — that reveals the true complexity.
