# 146 LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

```
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise
return -1.

void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
```

---

To support all the necessary operations as efficiently as possible, we require
two data structures: queue and hashmap. A queue is required to maintain the
order of the items such that we can identify the least-recently used items.
A hashmap is for quickly adding, removing and retrieving the item for the
matching key.

There is an ideal data structure that supports all the above features such as
Python's OrderedDict from collections library. This is a hashmap structure that
is implemented with a doubly linked list.

---

Python:

```python

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key not in self.d:
            return -1
        val = self.d.pop[key]
        self.d[key] = val
        return val

    def put(self, key, val):
        if key in self.d:
            self.get(key)
        if self.capacity == len(self.d):
            self.d.pop(next(iter(self.d)))
        self.d[key] = val
```
