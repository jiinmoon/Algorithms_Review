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

This implementation requres a queue to maintain the orders of the items such
that we can update its position based on usage as well as hashmap for
retreiving values in constant time. We can implement this with queue and
hashmap, or with a hashset that is implemented with a doubly-linked list.

---

Python:

```python

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.c = capacity
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

        if self.c == len(self.d):
            self.d.pop(next(iter(self.d)))

        self.d[key] = val
```
