# 146 LRU Cache

To determine which one to evict once at full capacity, we need a queue data
structure; and to be able to return the requested key value, a hashmap as well.

With Python, we have a OrderedDict structure which is a doubly-linked hash set
that can support both efficiently.

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
