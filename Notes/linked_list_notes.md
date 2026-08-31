# Linked Lists in DSA — Complete Notes (Python)

---

## 1. What is a Linked List?

A **Linked List** is a linear data structure where elements (called **nodes**) are not stored in contiguous memory. Instead, each node stores:
1. **Data** — the value
2. **Pointer/Reference** — address of the next node (and previous, for doubly linked lists)

```
[10 | *] -> [20 | *] -> [30 | *] -> [40 | None]
 head
```

Compare this to an **array**, where elements sit next to each other in memory and are accessed via an index.

### Why use a Linked List instead of an Array?

| Feature | Array | Linked List |
|---|---|---|
| Memory layout | Contiguous | Scattered (linked via pointers) |
| Access by index | O(1) | O(n) |
| Insertion/Deletion at start | O(n) (shift elements) | O(1) |
| Insertion/Deletion at end | O(1) amortized (dynamic array) | O(1) if tail pointer kept, else O(n) |
| Insertion/Deletion in middle | O(n) | O(n) to find + O(1) to link |
| Memory overhead | Low | Higher (extra pointer per node) |
| Cache locality | Good | Poor |
| Fixed size | Yes (static array) | No, grows dynamically |

**Use Linked Lists when:** frequent insertions/deletions at the ends or middle, unknown/variable size, no need for random access.
**Use Arrays when:** frequent random access by index, memory efficiency and cache performance matter.

---

## 2. Types of Linked Lists

### 2.1 Singly Linked List (SLL)
Each node points only to the **next** node.
```
head -> [A] -> [B] -> [C] -> None
```

### 2.2 Doubly Linked List (DLL)
Each node points to both **next** and **previous** nodes.
```
None <- [A] <-> [B] <-> [C] -> None
        head              tail
```

### 2.3 Circular Linked List (CLL)
The last node points back to the first node (can be singly or doubly circular).
```
        +-------------------------+
        v                         |
head -> [A] -> [B] -> [C] --------+
```

---

## 3. Node Structure in Python

```python
class Node:
    """A single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class DNode:
    """A single node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

---

## 4. Singly Linked List — Full Implementation

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # ---------- Traversal ----------
    def traverse(self):
        """O(n) time, O(1) space"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __str__(self):
        return " -> ".join(map(str, self.traverse())) + " -> None"

    def __len__(self):
        return self.size

    # ---------- Insertion ----------
    def insert_at_head(self, data):
        """O(1) time"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, data):
        """O(n) time without a tail pointer, O(1) with one"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_position(self, data, position):
        """O(n) time, O(1) space. position is 0-indexed."""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")
        if position == 0:
            return self.insert_at_head(data)

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    # ---------- Deletion ----------
    def delete_at_head(self):
        """O(1) time"""
        if not self.head:
            raise IndexError("List is empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def delete_at_tail(self):
        """O(n) time"""
        if not self.head:
            raise IndexError("List is empty")
        if not self.head.next:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data

        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        self.size -= 1
        return data

    def delete_by_value(self, value):
        """O(n) time — deletes first occurrence"""
        if not self.head:
            raise IndexError("List is empty")
        if self.head.data == value:
            return self.delete_at_head()

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return value
            current = current.next
        raise ValueError(f"{value} not found in list")

    # ---------- Search ----------
    def search(self, value):
        """O(n) time, O(1) space — returns index or -1"""
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, position):
        """O(n) time — access by index (linked lists have no O(1) random access)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")
        current = self.head
        for _ in range(position):
            current = current.next
        return current.data
```

---

## 5. Complexity Cheat Sheet — Singly Linked List

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| Access by index | O(n) | O(1) |
| Search by value | O(n) | O(1) |
| Insert at head | O(1) | O(1) |
| Insert at tail (no tail ptr) | O(n) | O(1) |
| Insert at tail (with tail ptr) | O(1) | O(1) |
| Insert at given position | O(n) | O(1) |
| Delete at head | O(1) | O(1) |
| Delete at tail | O(n) | O(1) |
| Delete by value | O(n) | O(1) |
| Reverse entire list | O(n) | O(1) iterative / O(n) recursive (call stack) |
| Detect cycle (Floyd's) | O(n) | O(1) |
| Merge two sorted lists | O(n + m) | O(1) |

**Doubly Linked List** improves *delete-at-tail* to O(1) if a tail pointer is maintained (since you can walk backward from `prev`), at the cost of extra memory per node for the `prev` pointer.

---

## 6. Visual Walkthroughs of Core Operations

### Insert at Head
```
Before:  head -> [20] -> [30] -> None
Insert 10:
  new_node(10).next = head   ->  [10] -> [20] -> [30] -> None
  head = new_node
After:   head -> [10] -> [20] -> [30] -> None
```

### Insert in Middle (position 2, value 99)
```
Before:  head -> [A] -> [B] -> [C] -> None
                        ^current (after 1 step from head, position-1 = 1)
Step 1: new_node.next = current.next   (99 -> C)
Step 2: current.next = new_node        (B -> 99)
After:   head -> [A] -> [B] -> [99] -> [C] -> None
```

### Delete by Value
```
Before:  head -> [A] -> [B] -> [C] -> None
Delete B:
  current(A).next = current.next.next   (A.next skips B, points to C)
After:   head -> [A] -> [C] -> None       (B is garbage collected)
```

---

## 7. Reversing a Linked List (Very Common Interview Question)

### Iterative — O(n) time, O(1) space
```python
def reverse_iterative(head):
    prev = None
    current = head
    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse the pointer
        prev = current              # move prev forward
        current = next_node         # move current forward
    return prev  # new head
```

Visual:
```
None <- [A]    [B] -> [C] -> None      (step 1: A reversed)
None <- [A] <- [B]    [C] -> None      (step 2: B reversed)
None <- [A] <- [B] <- [C]              (step 3: C reversed, new head = C)
```

### Recursive — O(n) time, O(n) space (call stack)
```python
def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

---

## 8. Detecting a Cycle — Floyd's Tortoise and Hare

O(n) time, O(1) space. Two pointers move at different speeds; if they meet, a cycle exists.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        if slow == fast:
            return True
    return False
```

### Finding the Start of the Cycle
```python
def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # no cycle

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # node where cycle begins
```
*Why it works:* Let distance from head to cycle start = `a`, cycle start to meeting point = `b`, remaining cycle length = `c`. When slow and fast meet, resetting one pointer to head and moving both at the same speed makes them meet exactly at the cycle start — a property derived from `2(a+b) = a+b+n(b+c)`.

---

## 9. Finding the Middle Node — Slow/Fast Pointer

O(n) time, O(1) space, single pass.
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # middle node (2nd middle if even length)
```

---

## 10. Merging Two Sorted Linked Lists

O(n + m) time, O(1) extra space (in-place relinking).
```python
def merge_two_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
```

---

## 11. Removing the Nth Node From the End

O(n) time (single pass), O(1) space — using a two-pointer gap technique.
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n):        # move fast n steps ahead
        fast = fast.next

    while fast.next:          # move both until fast hits the end
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next   # skip the target node
    return dummy.next
```

---

## 12. Palindrome Linked List Check

O(n) time, O(1) space — find middle, reverse second half, compare.
```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    second_half = reverse_iterative(slow)

    # Step 3: compare both halves
    first_half = head
    result = True
    while second_half:
        if first_half.data != second_half.data:
            result = False
            break
        first_half = first_half.next
        second_half = second_half.next

    return result
```

---

## 13. Intersection of Two Linked Lists

O(n + m) time, O(1) space — two pointers switch heads after reaching the end.
```python
def get_intersection(headA, headB):
    p1, p2 = headA, headB
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1  # intersection node or None
```
*Why it works:* both pointers travel `lenA + lenB` total steps, so they align at the intersection point (or both reach `None` simultaneously if no intersection).

---

## 14. Sorting a Linked List — Merge Sort

O(n log n) time, O(log n) space (recursion stack) — the standard optimal sort for linked lists since random access (needed by quicksort's partitioning/array sort) is unavailable, but O(1) splitting via slow/fast pointers works well with merge sort's divide-and-conquer.

```python
def merge_sort(head):
    if not head or not head.next:
        return head

    # Split into halves
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)
    return merge_two_sorted(left, right)
```

---

## 15. Doubly Linked List — Full Implementation

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data):
        """O(1)"""
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_tail(self, data):
        """O(1) — tail pointer maintained"""
        new_node = DNode(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_at_tail(self):
        """O(1) — the key advantage over SLL"""
        if not self.tail:
            raise IndexError("List is empty")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def delete_node(self, node):
        """O(1) if you already have a reference to the node (e.g. from a hashmap)"""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

    def traverse_forward(self):
        result, current = [], self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def traverse_backward(self):
        result, current = [], self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
```

**Key insight — why DLL matters in real systems:** O(1) deletion given a node reference is exactly why DLLs power **LRU Caches** (combined with a hashmap of key -> node).

---

## 16. Circular Linked List Implementation

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def traverse(self):
        if not self.head:
            return []
        result = [self.head.data]
        current = self.head.next
        while current != self.head:
            result.append(current.data)
            current = current.next
        return result
```

**Use cases:** round-robin CPU scheduling, circular buffers, multiplayer turn-based games (Josephus Problem).

### Josephus Problem (classic CLL application)
```python
def josephus(n, k):
    """Returns the position of the survivor (0-indexed) using a circular list simulation."""
    circle = CircularLinkedList()
    for i in range(n):
        circle.insert_at_tail(i)

    current = circle.head
    prev = None
    # find node before head to complete the circle traversal
    while current.next != circle.head:
        current = current.next
    prev = current
    current = circle.head

    count = n
    while count > 1:
        for _ in range(k - 1):
            prev = current
            current = current.next
        prev.next = current.next
        current = current.next
        count -= 1
    return current.data
```

---

## 17. LRU Cache — DLL + HashMap (O(1) get and put)

A capstone application combining a doubly linked list with a dictionary.

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> DNode
        self.head = DNode(0)  # dummy head (most recently used side)
        self.tail = DNode(0)  # dummy tail (least recently used side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """O(1)"""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_at_front(node)
        return node.data[1]

    def put(self, key, value):
        """O(1)"""
        if key in self.cache:
            self._remove(self.cache[key])
        node = DNode((key, value))
        self.cache[key] = node
        self._insert_at_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.data[0]]
```

---

## 18. Clone a Linked List with Random Pointers

O(n) time, O(1) extra space (excluding output) — the interleaving trick.

```python
class RandomNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone_random_list(head):
    if not head:
        return None

    # Step 1: interleave cloned nodes: A -> A' -> B -> B' -> ...
    current = head
    while current:
        clone = RandomNode(current.data)
        clone.next = current.next
        current.next = clone
        current = clone.next

    # Step 2: assign random pointers to clones
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: detach clone list from original
    current = head
    clone_head = head.next
    while current:
        clone = current.next
        current.next = clone.next
        clone.next = clone.next.next if clone.next else None
        current = current.next

    return clone_head
```

---

## 19. Flattening a Multilevel Linked List

Common variant where nodes may have a `child` pointer to a separate sub-list. O(n) time, O(n) space (stack) using an iterative DFS-style approach.

```python
class MultiNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

def flatten(head):
    if not head:
        return head
    stack = [head]
    prev = None

    while stack:
        current = stack.pop()
        if prev:
            prev.next = current
            current.prev = prev
        if current.next:
            stack.append(current.next)
        if current.child:
            stack.append(current.child)
            current.child = None
        prev = current

    return head
```

---

## 20. Array-Based (Dynamic) Alternative — Where Linked Lists Lose

Python's built-in `list` is a **dynamic array**, not a linked list. It offers O(1) amortized append and O(1) index access, which is why in practice `collections.deque` (a doubly linked list of blocks, implemented in C) is preferred over hand-rolled linked lists for queue-like behavior:

```python
from collections import deque

dq = deque()
dq.append(10)        # O(1) — insert at tail
dq.appendleft(5)      # O(1) — insert at head
dq.pop()               # O(1) — delete at tail
dq.popleft()           # O(1) — delete at head
```

**Practical rule of thumb:** in interviews, implement linked lists manually with `Node` classes to demonstrate understanding. In production Python code, prefer `deque` for queue/stack-like linked-list behavior unless you specifically need custom node-level control (e.g., building an LRU cache from scratch, or a custom skip list / graph adjacency structure).

---

## 21. Common Patterns Summary Table

| Pattern | Used For | Complexity |
|---|---|---|
| Two pointers (slow/fast) | Middle node, cycle detection, palindrome | O(n) time, O(1) space |
| Dummy head node | Simplifies edge cases (deleting head, merging) | O(1) extra |
| Reverse (iterative) | In-place reversal, palindrome check | O(n) time, O(1) space |
| Recursion | Reverse, merge sort, deep problems | O(n) time, O(n) space (stack) |
| Multiple pointers with gap | Nth node from end | O(n) time, O(1) space |
| Interleaving | Clone with random pointer | O(n) time, O(1) extra space |
| HashMap + DLL | O(1) LRU cache | O(n) space |
| Merge sort | Sorting linked lists optimally | O(n log n) time |

---

## 22. Practice Problem List (Roughly Easy -> Hard)

1. Reverse a linked list (iterative + recursive)
2. Find the middle of a linked list
3. Detect a cycle in a linked list
4. Find the start node of a cycle
5. Merge two sorted linked lists
6. Remove duplicates from a sorted linked list
7. Remove the Nth node from the end
8. Check if a linked list is a palindrome
9. Find the intersection point of two linked lists
10. Add two numbers represented as linked lists (digit-by-digit addition)
11. Flatten a multilevel doubly linked list
12. Clone a linked list with random pointers
13. Sort a linked list using merge sort
14. Reverse a linked list in groups of k
15. Rotate a linked list by k positions
16. Implement an LRU cache using DLL + HashMap
17. Design a skip list (advanced — probabilistic multi-level linked list, O(log n) search)
18. Flatten a binary tree to a linked list (in-place)
19. Convert a binary search tree to a sorted doubly linked list

---

## 23. Quick Reference: Big-O Summary (All Structures)

| Structure | Access | Search | Insert Head | Insert Tail | Delete Head | Delete Tail (with node ref) |
|---|---|---|---|---|---|---|
| Array (static) | O(1) | O(n) | O(n) | O(1)/full | O(n) | O(1) |
| Dynamic Array (`list`) | O(1) | O(n) | O(n) | O(1) amortized | O(n) | O(1) |
| Singly Linked List | O(n) | O(n) | O(1) | O(1)* | O(1) | O(n) |
| Doubly Linked List | O(n) | O(n) | O(1) | O(1) | O(1) | O(1) |
| Circular Linked List | O(n) | O(n) | O(1) | O(n)/O(1)* | O(1) | O(n) |

`*` assumes a tail pointer is maintained.

---

## 24. Key Takeaways

- Linked lists trade **random access** for **efficient insertion/deletion** at known positions.
- The **two-pointer (slow/fast)** technique is the single most reusable idea across linked list problems — master it first.
- A **dummy node** eliminates most head-related edge cases and should be your default habit for insert/delete/merge problems.
- **Doubly linked lists** are what make O(1) arbitrary deletion possible — this is the backbone of LRU caches, browser history, and text editor undo/redo stacks.
- In real Python code, prefer `collections.deque` over a hand-written linked list unless the problem specifically requires custom node manipulation (interviews, or specialized structures like LRU caches/skip lists).
