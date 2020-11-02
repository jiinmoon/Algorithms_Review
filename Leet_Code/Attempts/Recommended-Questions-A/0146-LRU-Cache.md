# 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

---

To keep track of the least recently used items, we require a data structure to
keep track of the order of the items. And to update the usage and new items, we
also require a hashmap like data structure. To implement this, we may use
a OrderedDict which is a hashset using the doubly linked list.

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
        val = self.d.pop(key)
        self.d[key] = val
        return val

    def put(self, key, val):
        if key in self.d:
            self.get(key)
        if self.capacity == len(self.d):
            self.d.pop(next(iter(self.d)))
        self.d[key] = val
```
