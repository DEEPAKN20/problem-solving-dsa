Linked Lists in DSA — Complete Notes (Python)

Herbert

Table of Contents

# 1\. Introduction

## 1.1 What is a Linked List?

A **linked list** is a linear data structure where elements ("nodes") are not stored in contiguous memory. Instead, each node stores its data plus a **reference (pointer)** to the next node. The list is accessed through a reference to the **head** (first node).

class Node:  
def \__init_\_(self, data):  
self.data = data  
self.next = None

## 1.2 Why Linked Lists? Array vs Linked List

| Property                 | Array / Python list            | Linked List                          |
| ------------------------ | ------------------------------ | ------------------------------------ |
| Memory layout            | Contiguous                     | Scattered, connected via pointers    |
| Random access a\[i\]     | O(1)                           | O(n)                                 |
| Insert/Delete at front   | O(n) (shift elements)          | O(1)                                 |
| Insert/Delete at end     | O(1) amortized (dynamic array) | O(1) if tail pointer kept, else O(n) |
| Insert/Delete in middle  | O(n) (shift)                   | O(n) to find + O(1) to link          |
| Extra memory per element | None                           | One (or two) pointers per node       |
| Cache locality           | Good                           | Poor                                 |
| Dynamic resizing         | Amortized cost                 | Naturally dynamic, no resizing cost  |

**Use a linked list when:** frequent insertions/deletions at the front or in the middle are needed, size is unknown/highly variable, and random access isn't required.

**Use an array/list when:** you need fast random access, better cache performance, or lower memory overhead.

## 1.3 Types of Linked Lists

1. **Singly Linked List (SLL)** — each node points to the next only; traversal is one-directional.
2. **Doubly Linked List (DLL)** — each node has next and prev; traversal both directions.
3. **Circular Linked List** — the last node points back to the head instead of None. Can be singly or doubly circular.
4. **Circular Doubly Linked List** — combination of the above; used in structures like the LRU cache and OS process scheduling.

# 2\. Singly Linked List — Full Implementation

class Node:  
\__slots__= ("data", "next") # saves memory; no \__dict__ per node  
<br/>def \__init_\_(self, data):  
self.data = data  
self.next = None  
<br/><br/>class SinglyLinkedList:  
def \__init_\_(self):  
self.head = None  
self.size = 0 # keep a counter -> O(1) length queries  
<br/>\# ---------- Basic utilities ----------  
def is_empty(self):  
return self.head is None  
<br/>def \__len_\_(self):  
return self.size  
<br/>def \__iter_\_(self):  
curr = self.head  
while curr:  
yield curr.data  
curr = curr.next  
<br/>def \__repr_\_(self):  
return " -> ".join(str(x) for x in self) + " -> None"  
<br/>\# ---------- Insertion ----------  
def insert_at_head(self, data):  
"""O(1)"""  
node = Node(data)  
node.next = self.head  
self.head = node  
self.size += 1  
<br/>def insert_at_tail(self, data):  
"""O(n) without tail pointer, O(1) with one"""  
node = Node(data)  
if self.is_empty():  
self.head = node  
else:  
curr = self.head  
while curr.next:  
curr = curr.next  
curr.next = node  
self.size += 1  
<br/>def insert_at_index(self, index, data):  
"""O(n): insert before position \`index\` (0-based)"""  
if index &lt; 0 or index &gt; self.size:  
raise IndexError("Index out of bounds")  
if index == 0:  
return self.insert_at_head(data)  
node = Node(data)  
prev = self.head  
for _in range(index - 1):  
prev = prev.next  
node.next = prev.next  
prev.next = node  
self.size += 1  
<br/>def insert_after_value(self, target, data):  
"""O(n): insert right after the first node containing \`target\`"""  
curr = self.head  
while curr and curr.data != target:  
curr = curr.next  
if curr is None:  
raise ValueError(f"{target} not found")  
node = Node(data)  
node.next = curr.next  
curr.next = node  
self.size += 1  
<br/>\# ---------- Deletion ----------  
def delete_at_head(self):  
"""O(1)"""  
if self.is_empty():  
raise IndexError("delete from empty list")  
data = self.head.data  
self.head = self.head.next  
self.size -= 1  
return data  
<br/>def delete_at_tail(self):  
"""O(n)"""  
if self.is_empty():  
raise IndexError("delete from empty list")  
if self.head.next is None:  
data = self.head.data  
self.head = None  
self.size -= 1  
return data  
curr = self.head  
while curr.next.next:  
curr = curr.next  
data = curr.next.data  
curr.next = None  
self.size -= 1  
return data  
<br/>def delete_by_value(self, value):  
"""O(n): delete first node matching \`value\`"""  
if self.is_empty():  
return False  
if self.head.data == value:  
self.head = self.head.next  
self.size -= 1  
return True  
prev, curr = self.head, self.head.next  
while curr:  
if curr.data == value:  
prev.next = curr.next  
self.size -= 1  
return True  
prev, curr = curr, curr.next  
return False  
<br/>def delete_at_index(self, index):  
"""O(n)"""  
if index &lt; 0 or index &gt;= self.size:  
raise IndexError("Index out of bounds")  
if index == 0:  
return self.delete_at_head()  
prev = self.head  
for _in range(index - 1):  
prev = prev.next  
data = prev.next.data  
prev.next = prev.next.next  
self.size -= 1  
return data  
<br/>\# ---------- Search / traversal ----------  
def search(self, value):  
"""O(n): returns index or -1"""  
idx = 0  
curr = self.head  
while curr:  
if curr.data == value:  
return idx  
curr = curr.next  
idx += 1  
return -1  
<br/>def get(self, index):  
"""O(n): value at index"""  
if index &lt; 0 or index &gt;= self.size:  
raise IndexError("Index out of bounds")  
curr = self.head  
for_ in range(index):  
curr = curr.next  
return curr.data  
<br/>def reverse(self):  
"""O(n) time, O(1) space — iterative reversal"""  
prev = None  
curr = self.head  
while curr:  
nxt = curr.next  
curr.next = prev  
prev = curr  
curr = nxt  
self.head = prev

### 2.1 Complexity summary — Singly Linked List

| Operation                      | Time | Space             |
| ------------------------------ | ---- | ----------------- |
| Access by index                | O(n) | O(1)              |
| Search by value                | O(n) | O(1)              |
| Insert at head                 | O(1) | O(1)              |
| Insert at tail (no tail ptr)   | O(n) | O(1)              |
| Insert at tail (tail ptr kept) | O(1) | O(1)              |
| Insert at index / after node   | O(n) | O(1)              |
| Delete at head                 | O(1) | O(1)              |
| Delete at tail                 | O(n) | O(1)              |
| Delete by value / index        | O(n) | O(1)              |
| Reverse (iterative)            | O(n) | O(1)              |
| Reverse (recursive)            | O(n) | O(n) — call stack |
| Traverse / print               | O(n) | O(1)              |

# 3\. Doubly Linked List — Full Implementation

Each node keeps both prev and next, allowing O(1) deletion given a node reference (no need to find the predecessor) and O(1) insertion before a known node.

class DNode:  
\__slots__= ("data", "prev", "next")  
<br/>def \__init_\_(self, data):  
self.data = data  
self.prev = None  
self.next = None  
<br/><br/>class DoublyLinkedList:  
def \__init_\_(self):  
self.head = None  
self.tail = None  
self.size = 0  
<br/>def is_empty(self):  
return self.head is None  
<br/>def \__len_\_(self):  
return self.size  
<br/>def \__iter_\_(self):  
curr = self.head  
while curr:  
yield curr.data  
curr = curr.next  
<br/>def insert_at_head(self, data):  
"""O(1)"""  
node = DNode(data)  
if self.is_empty():  
self.head = self.tail = node  
else:  
node.next = self.head  
self.head.prev = node  
self.head = node  
self.size += 1  
<br/>def insert_at_tail(self, data):  
"""O(1) — because we maintain a tail pointer"""  
node = DNode(data)  
if self.is_empty():  
self.head = self.tail = node  
else:  
node.prev = self.tail  
self.tail.next = node  
self.tail = node  
self.size += 1  
<br/>def delete_node(self, node):  
"""O(1) given a direct reference to the node — the big DLL advantage"""  
if node.prev:  
node.prev.next = node.next  
else:  
self.head = node.next  
if node.next:  
node.next.prev = node.prev  
else:  
self.tail = node.prev  
node.prev = node.next = None  
self.size -= 1  
<br/>def delete_by_value(self, value):  
"""O(n) to find, O(1) to unlink"""  
curr = self.head  
while curr:  
if curr.data == value:  
self.delete_node(curr)  
return True  
curr = curr.next  
return False  
<br/>def reverse(self):  
"""O(n): swap next/prev at every node, then swap head/tail"""  
curr = self.head  
while curr:  
curr.prev, curr.next = curr.next, curr.prev  
curr = curr.prev # this is the OLD next, since we just swapped  
self.head, self.tail = self.tail, self.head

### 3.1 Complexity summary — Doubly Linked List

| Operation                         | Time | Space |
| --------------------------------- | ---- | ----- |
| Insert at head/tail               | O(1) | O(1)  |
| Delete given node reference       | O(1) | O(1)  |
| Delete by value (search + delete) | O(n) | O(1)  |
| Access/search by index/value      | O(n) | O(1)  |
| Reverse                           | O(n) | O(1)  |
| Traverse forward or backward      | O(n) | O(1)  |

Trade-off vs SLL: DLL uses extra memory (one more pointer/node) but gives O(1) deletion given a node and backward traversal — essential for structures like **LRU caches** and **text editor undo/redo**.

# 4\. Circular Linked List

Last node's next points to head (singly) — or in a circular DLL, head.prev == tail and tail.next == head.

class CircularLinkedList:  
def \__init_\_(self):  
self.head = None  
self.size = 0  
<br/>def insert_at_tail(self, data):  
node = Node(data)  
if self.head is None:  
self.head = node  
node.next = self.head # points to itself  
else:  
curr = self.head  
while curr.next != self.head:  
curr = curr.next  
curr.next = node  
node.next = self.head  
self.size += 1  
<br/>def traverse(self):  
"""O(n): must stop when we loop back to head"""  
result = \[\]  
if self.head is None:  
return result  
curr = self.head  
while True:  
result.append(curr.data)  
curr = curr.next  
if curr == self.head:  
break  
return result  
<br/>def delete_by_value(self, value):  
if self.head is None:  
return False  
prev, curr = None, self.head  
while True:  
if curr.data == value:  
if prev is None: # deleting head  
if curr.next == self.head: # only one node  
self.head = None  
else:  
last = self.head  
while last.next != self.head:  
last = last.next  
last.next = curr.next  
self.head = curr.next  
else:  
prev.next = curr.next  
self.size -= 1  
return True  
prev, curr = curr, curr.next  
if curr == self.head:  
return False

**Use cases:** round-robin CPU scheduling, playlist "repeat all", multiplayer turn rotation, Josephus problem.

**Complexity:** same asymptotics as SLL for most operations (O(1) head insert, O(n) search/insert-at-tail without a tail pointer), but every traversal needs an explicit stopping condition since there's no None terminator.

# 5\. Classic Linked List Algorithms

### 5.1 Reverse a Linked List

**Iterative — O(n) time, O(1) space** (shown in section 2). This is the standard/expected solution.

**Recursive — O(n) time, O(n) space** (call stack):

def reverse_recursive(head):  
if head is None or head.next is None:  
return head  
new_head = reverse_recursive(head.next)  
head.next.next = head  
head.next = None  
return new_head

### 5.2 Detect a Cycle — Floyd's Cycle Detection ("Tortoise and Hare")

**O(n) time, O(1) space.**

def has_cycle(head):  
slow = fast = head  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
if slow is fast:  
return True  
return False

_Why it works:_ the fast pointer moves 2 steps, the slow pointer 1 step. If there's a cycle, the gap between them shrinks by 1 each iteration, so they must eventually meet inside the loop. If there's no cycle, fast hits None first.

### 5.3 Find the Start of the Cycle

**O(n) time, O(1) space.**

def detect_cycle_start(head):  
slow = fast = head  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
if slow is fast: # cycle found  
ptr = head  
while ptr is not slow:  
ptr = ptr.next  
slow = slow.next  
return ptr # start of the cycle  
return None

_Why it works:_ let the distance from head to the cycle start be a, and the meeting point be b steps into the cycle. Mathematically, moving a second pointer from head and the slow pointer from the meeting point, both at speed 1, causes them to meet exactly at the cycle's start after a steps.

### 5.4 Find the Middle Node — Slow/Fast Pointers

**O(n) time, O(1) space.**

def find_middle(head):  
slow = fast = head  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
return slow # for even length, this is the SECOND middle node

### 5.5 Merge Two Sorted Linked Lists

**O(n + m) time, O(1) extra space (excluding output structure).**

def merge_two_sorted(l1, l2):  
dummy = Node(None)  
tail = dummy  
while l1 and l2:  
if l1.data <= l2.data:  
tail.next, l1 = l1, l1.next  
else:  
tail.next, l2 = l2, l2.next  
tail = tail.next  
tail.next = l1 if l1 else l2  
return dummy.next

_Pattern note:_ the **dummy head** trick avoids special-casing the first insertion — used constantly in linked-list problems.

### 5.6 Merge Sort a Linked List

Linked lists sort best with **merge sort** (O(n log n)) because splitting doesn't require random access, unlike quicksort's partitioning.

def sort_list(head):  
if head is None or head.next is None:  
return head  
<br/>\# 1. split into halves using slow/fast pointers  
slow, fast = head, head.next  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
mid, slow.next = slow.next, None  
<br/>\# 2. recursively sort each half  
left = sort_list(head)  
right = sort_list(mid)  
<br/>\# 3. merge  
return merge_two_sorted(left, right)

**Complexity:** O(n log n) time, O(log n) space (recursion stack).

### 5.7 Remove the N-th Node From the End

**One pass, O(n) time, O(1) space** using two pointers separated by n.

def remove_nth_from_end(head, n):  
dummy = Node(None)  
dummy.next = head  
fast = slow = dummy  
for_ in range(n):  
fast = fast.next  
while fast.next:  
fast = fast.next  
slow = slow.next  
slow.next = slow.next.next  
return dummy.next

### 5.8 Detect Intersection of Two Linked Lists

**O(n + m) time, O(1) space** — the elegant two-pointer switch:

def get_intersection_node(headA, headB):  
a, b = headA, headB  
while a is not b:  
a = a.next if a else headB  
b = b.next if b else headA  
return a # intersection node, or None if no intersection

_Why it works:_ both pointers travel lenA + lenB total steps and switch lists once exhausted, so they align at the intersection (or both reach None simultaneously if there's none).

### 5.9 Check if a Linked List is a Palindrome

**O(n) time, O(1) space** (reverse the second half in place):

def is_palindrome(head):  
if head is None or head.next is None:  
return True  
<br/>\# find middle  
slow = fast = head  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
<br/>\# reverse second half  
prev = None  
curr = slow  
while curr:  
curr.next, prev, curr = prev, curr, curr.next  
<br/>\# compare both halves  
left, right = head, prev  
result = True  
while right: # right half is shorter or equal  
if left.data != right.data:  
result = False  
break  
left, right = left.next, right.next  
return result

### 5.10 Reorder List (L0 -> Ln -> L1 -> Ln-1 -> …)

**O(n) time, O(1) space** — combine "find middle" + "reverse" + "merge alternately":

def reorder_list(head):  
if not head or not head.next:  
return  
\# 1. find middle  
slow = fast = head  
while fast and fast.next:  
slow = slow.next  
fast = fast.next.next  
\# 2. reverse second half  
second = slow.next  
slow.next = None  
prev = None  
while second:  
second.next, prev, second = prev, second, second.next  
\# 3. merge two halves alternately  
first, second = head, prev  
while second:  
first.next, first = second, first.next  
second.next, second = first, second.next

### 5.11 Add Two Numbers Represented as Linked Lists (digits reversed order)

**O(max(n, m)) time, O(max(n, m)) space** for the result:

def add_two_numbers(l1, l2):  
dummy = Node(None)  
curr = dummy  
carry = 0  
while l1 or l2 or carry:  
s = (l1.data if l1 else 0) + (l2.data if l2 else 0) + carry  
carry, digit = divmod(s, 10)  
curr.next = Node(digit)  
curr = curr.next  
l1 = l1.next if l1 else None  
l2 = l2.next if l2 else None  
return dummy.next

### 5.12 Rotate a Linked List by K Places

**O(n) time, O(1) space:**

def rotate_right(head, k):  
if not head or not head.next:  
return head  
\# get length and connect tail to head (make it circular temporarily)  
length = 1  
tail = head  
while tail.next:  
tail = tail.next  
length += 1  
tail.next = head  
<br/>k %= length  
steps_to_new_tail = length - k  
new_tail = head  
for_ in range(steps_to_new_tail - 1):  
new_tail = new_tail.next  
new_head = new_tail.next  
new_tail.next = None  
return new_head

### 5.13 Clone a Linked List with a Random Pointer

Each node has next and an extra random pointer to any node in the list (or None).

**Optimal O(n) time, O(1) extra space** (interleaving trick):

class RandomNode:  
def \__init_\_(self, data):  
self.data = data  
self.next = None  
self.random = None  
<br/>def copy_random_list(head):  
if not head:  
return None  
\# 1. interleave copied nodes: A -> A' -> B -> B' -> ...  
curr = head  
while curr:  
copy = RandomNode(curr.data)  
copy.next = curr.next  
curr.next = copy  
curr = copy.next  
<br/>\# 2. assign random pointers for the copies  
curr = head  
while curr:  
if curr.random:  
curr.next.random = curr.random.next  
curr = curr.next.next  
<br/>\# 3. detach the copied list from the original  
curr = head  
dummy = RandomNode(None)  
copy_curr = dummy  
while curr:  
copy_curr.next = curr.next  
curr.next = curr.next.next  
curr = curr.next  
copy_curr = copy_curr.next  
return dummy.next

_(A simpler O(n) time / O(n) space version uses a hash map from original node -> copy node.)_

### 5.14 Flatten a Multilevel Doubly Linked List

Nodes may have an extra child pointer to a separate doubly linked sub-list.

**O(n) time, O(d) space** where d = max nesting depth (stack for iterative DFS):

def flatten(head):  
if not head:  
return head  
stack = \[\]  
curr = head  
while curr:  
if curr.child:  
if curr.next:  
stack.append(curr.next)  
curr.next = curr.child  
curr.next.prev = curr  
curr.child = None  
if not curr.next and stack:  
nxt = stack.pop()  
curr.next = nxt  
nxt.prev = curr  
curr = curr.next  
return head

### 5.15 Remove Duplicates

**From a sorted list — O(n) time, O(1) space:**

def remove_duplicates_sorted(head):  
curr = head  
while curr and curr.next:  
if curr.data == curr.next.data:  
curr.next = curr.next.next  
else:  
curr = curr.next  
return head

**From an unsorted list — O(n) time, O(n) space (hash set):**

def remove_duplicates_unsorted(head):  
seen = set()  
prev, curr = None, head  
while curr:  
if curr.data in seen:  
prev.next = curr.next  
else:  
seen.add(curr.data)  
prev = curr  
curr = curr.next  
return head

**From an unsorted list, O(1) extra space (no hash set) — O(n^2) time:**

def remove_duplicates_no_extra_space(head):  
curr = head  
while curr:  
runner = curr  
while runner.next:  
if runner.next.data == curr.data:  
runner.next = runner.next.next  
else:  
runner = runner.next  
curr = curr.next  
return head

### 5.16 Josephus Problem (Circular Linked List application)

**O(n \* k) time naively, O(n log n) with better data structures; O(1) extra space with a circular list:**

def josephus(n, k):  
"""Returns the position (1-indexed) of the survivor among n people,  
counting off every k-th person, using a circular linked list."""  
head = Node(1)  
curr = head  
for i in range(2, n + 1):  
curr.next = Node(i)  
curr = curr.next  
curr.next = head # make circular  
<br/>curr = head  
while curr.next != curr:  
for _ in range(k - 1):  
curr = curr.next  
curr.next = curr.next.next # eliminate next node  
return curr.data

# 6\. LRU Cache — Doubly Linked List + Hash Map (classic interview problem)

Combines a **doubly linked list** (O(1) insert/remove given a node) with a **dict** (O(1) lookup) to get O(1) get and put.

class LRUCache:  
class \_Node:  
\__slots__= ("key", "value", "prev", "next")  
def \__init_\_(self, key=0, value=0):  
self.key, self.value = key, value  
self.prev = self.next = None  
<br/>def \__init_\_(self, capacity):  
self.capacity = capacity  
self.map = {}  
\# sentinel head/tail simplify edge cases  
self.head = self.\_Node()  
self.tail = self.\_Node()  
self.head.next = self.tail  
self.tail.prev = self.head  
<br/>def \_remove(self, node):  
node.prev.next = node.next  
node.next.prev = node.prev  
<br/>def \_add_to_front(self, node):  
node.next = self.head.next  
node.prev = self.head  
self.head.next.prev = node  
self.head.next = node  
<br/>def get(self, key):  
if key not in self.map:  
return -1  
node = self.map\[key\]  
self.\_remove(node)  
self.\_add_to_front(node)  
return node.value  
<br/>def put(self, key, value):  
if key in self.map:  
self.\_remove(self.map\[key\])  
node = self.\_Node(key, value)  
self.map\[key\] = node  
self.\_add_to_front(node)  
if len(self.map) > self.capacity:  
lru = self.tail.prev  
self.\_remove(lru)  
del self.map\[lru.key\]

**Complexity:** get and put are both **O(1)** time; **O(capacity)** space.

# 7\. Linked List vs Python's Built-in Structures

| Structure               | When to prefer it over a hand-rolled linked list                                                                                                      |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| list                    | Need random access, iteration speed, cache locality — almost always faster in practice due to C-level implementation                                  |
| collections.deque       | Need O(1) appends/pops from **both ends** — internally a doubly linked list of blocks; use this instead of writing your own DLL for queue/stack needs |
| collections.OrderedDict | Need LRU-like behavior without writing a DLL by hand (move_to_end, popitem(last=False))                                                               |

In real Python code, you rarely hand-roll a linked list for production use — deque and list are implemented in C and outperform pure-Python linked lists. Linked lists are taught because they build pointer-manipulation intuition and appear frequently in interviews, and they matter directly when implementing **other** structures (adjacency lists in graphs, hash-map chaining, LRU caches, skip lists).

# 8\. General Complexity Master Table

| Operation                                | Array / list | Singly Linked List           | Doubly Linked List           |
| ---------------------------------------- | ------------ | ---------------------------- | ---------------------------- |
| Access by index                          | O(1)         | O(n)                         | O(n)                         |
| Search                                   | O(n)         | O(n)                         | O(n)                         |
| Insert at front                          | O(n)         | O(1)                         | O(1)                         |
| Insert at end (tail ptr)                 | O(1)\*       | O(1)                         | O(1)                         |
| Insert at end (no tail ptr)              | O(1)\*       | O(n)                         | O(1) (has tail ptr)          |
| Insert/Delete in middle (position known) | O(n)         | O(n) to reach + O(1) to link | O(n) to reach + O(1) to link |
| Delete given direct node reference       | O(n)         | O(n) (need predecessor)      | O(1)                         |
| Delete at front                          | O(n)         | O(1)                         | O(1)                         |
| Reverse                                  | O(n)         | O(n)                         | O(n)                         |
| Extra memory / element                   | 0            | 1 pointer                    | 2 pointers                   |

\*Amortized, due to dynamic array over-allocation.

# 9\. Common Pitfalls in Python Linked List Code

1. **Losing the head reference** — always keep self.head (and self.tail if used) updated on every insert/delete.
2. **Off-by-one in index-based insert/delete** — decide clearly whether index means "insert before" or "insert after" and stay consistent.
3. **Forgetting to null out .next/.prev** on deleted nodes — usually harmless for garbage collection in CPython (reference counting handles it), but important if the node might be reused or if you're avoiding accidental cycles.
4. **Two-pointer bugs** — always check both fast and fast.next before advancing fast by two.
5. **Circular lists** — comparing with is (identity) rather than == (equality) when checking "have I returned to head" avoids issues if node data can repeat.
6. **Recursive reversal / traversal** on very long lists can hit Python's recursion limit (~1000 by default) — prefer iterative solutions for lists that might be large, or raise sys.setrecursionlimit() cautiously.
7. **Using == vs is for nodes**: when comparing _nodes_ (not data) for identity — e.g., in cycle detection or intersection — always use is.

# 10\. Practice Problem Checklist (roughly increasing difficulty)

1. Reverse a linked list (iterative + recursive)
2. Find the middle node
3. Detect a cycle (Floyd's)
4. Find the start of a cycle
5. Merge two sorted lists
6. Remove N-th node from end
7. Palindrome linked list
8. Intersection of two linked lists
9. Remove duplicates (sorted and unsorted)
10. Add two numbers (linked list digits)
11. Reorder list
12. Rotate list by k
13. Sort a linked list (merge sort)
14. Flatten a multilevel doubly linked list
15. Copy a list with random pointers
16. Design an LRU cache
17. Josephus problem using a circular linked list
18. Reverse nodes in k-group (advanced — reverse every k nodes)

### Bonus: Reverse Nodes in K-Group

**O(n) time, O(n/k) space (recursion) or O(1) iterative:**

def reverse_k_group(head, k):  
node = head  
count = 0  
while node and count < k:  
node = node.next  
count += 1  
if count < k:  
return head # fewer than k nodes left, leave as-is  
<br/>prev = reverse_k_group(node, k) # recursively handle the rest first  
curr = head  
for _ in range(k):  
nxt = curr.next  
curr.next = prev  
prev = curr  
curr = nxt  
return prev

# 11\. Quick Reference — Which Pattern to Reach For

| Problem signal                                                   | Technique                                                     |
| ---------------------------------------------------------------- | ------------------------------------------------------------- |
| "Find the middle" / "detect a cycle"                             | Slow/fast (tortoise-hare) pointers                            |
| "Remove k-th from end" / "keep a fixed gap"                      | Two pointers with a gap of k                                  |
| "Merge / build a new list without special-casing the first node" | Dummy head node                                               |
| "Reverse all or part of a list"                                  | Iterative pointer-rewiring (prev, curr, next)                 |
| "Sort a linked list"                                             | Merge sort (splitting via slow/fast, no random access needed) |
| "O(1) deletion given a node"                                     | Doubly linked list                                            |
| "Most-recently-used ordering"                                    | Doubly linked list + hash map (LRU cache)                     |
| "Clone with extra pointers"                                      | Interleaving trick or hash map                                |
| "Round-robin / circular counting"                                | Circular linked list                                          |