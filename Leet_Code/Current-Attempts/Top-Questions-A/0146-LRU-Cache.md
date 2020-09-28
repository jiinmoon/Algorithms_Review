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

Follow up:

Could you do get and put in O(1) time complexity?
 
---

To create most efficient LRU Cache, we require two data structures. One,
a queue is required such that we can maintain the order of the least recently
used items. Second, a hashmap is required so that we can retrieve the item in
a constant time.

We can support both in a single data structure - a hashmap that is implemented
with a doubly linked list. As a hashmap, retrieval of the value for the key is
supported with O(1). And also as a doubly linked list, we can easily remove as
needed. In Python, `OrderedDict` is such a data structure that we can use
instead of using two data structures.

---

Python:

```python

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key in self.d:
            val = self.d.pop(key)
            self.d[key] = val
            return val
        return -1

    def put(self, key, val):
        if key in self.d:
            self.get(key)

        if self.capacity == len(self.d):
            self.d.pop(next(iter(self.d)))

        self.d[key] = val
```
