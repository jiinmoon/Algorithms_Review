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

There are two components that we need to consider in order to achieve efficient
time complexity on both get and put operations. First, to achieve O(1) time
complexity in get and put, we need a hashmap structure that can retrieve the
value in constant time.

Problem is the evict operation of LRU item - to support LRU, we need
a structure that can maintain an order of the items such that we can remove and
add whilst maintaining order.

Naively, we can use two structure (queue and hashmap) to achieve this. But
evict operation will cost O(n) to search and update the LRU item. To resolve
this, we can implement hashmap with doubly linked list.

---

Python:

```python

from collections import OrderedDict

class LRUCache:
    def __init__(self, size):
        self.size = size
        self.d = OrderedDict()

    def get(self, key):
        if key in self.d:
            self.d[key] = self.d.pop(key)
            return self.d[key]
        return -1

    def put(self, key, val):
        if key in self.d:
            self.get(key)

        if len(self.d) > self.size:
            self.d.pop(next(iter(self.d)))

        self.d[key] = val
```
