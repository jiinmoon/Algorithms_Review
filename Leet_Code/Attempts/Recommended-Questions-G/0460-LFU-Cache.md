# 460. LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache.

Implement the LFUCache class:

```
LFUCache(int capacity) Initializes the object with the capacity of the data
structure.

int get(int key) Gets the value of the key if the key exists in the cache.
Otherwise, returns -1.

void put(int key, int value) Sets or inserts the value if the key is not
already present. When the cache reaches its capacity, it should invalidate the
least frequently used item before inserting a new item. For this problem, when
there is a tie (i.e., two or more keys with the same frequency), the least
recently used key would be evicted.
```

Notice that the number of times an item is used is the number of calls to the
get and put functions for that item since it was inserted. This number is set
to zero when the item is removed.

Follow up:

Could you do both operations in O(1) time complexity?

---

We need to consider not only the frequency of the item usage, but also the
timestamp for when the item was updated. To support better time complexity, we
use pq to maintain the order for least frequently used + oldest item to evict.
And we only update the pq only when it is absolutely necessary.

---

Python:

```python

import heapq

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.d, self.ft, self.update = {}, {}, {}
        self.pq = list()

    def get(self, key):
        self.time += 1
        if key in self.d:
            f, _ = self.ft[key]
            self.ft[key] = (f + 1, self.time)
            self.update.add(key)
            return self.d[key]
        return -1

    def put(self, key, val):
        self.time += 1
        if key in self.d:
            self.get(key)
        else:
            if self.capacity == len(self.d):
                while self.update and pq[0][2] in self.update:
                    _, _, updateKey = heappop(self.pq)
                    f, t = self.ft[updatekey]
                    heappush(self.pq, (f, t, updateKey))
                    self.update.remove(updateKey)
                _, _, removeKey = heappop(self.pq)
                self.ft.pop(removeKey)
                self.d.pop(removeKey)
            self.ft[key] = (0, self.time)
            heappush(self.pq, (0, self.time, key))
        self.d[key] = val
```
