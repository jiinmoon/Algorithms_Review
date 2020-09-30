# 460 LFU Cache

Design and implement a data structure for Least Frequently Used (LFU) cache. It
should support the following operations: get and put.

```
get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.
```

Note that the number of times an item is used is the number of calls to the get
and put functions for that item since it was inserted. This number is set to
zero when the item is removed.


 Follow up:
 Could you do both operations in O(1) time complexity?

---

We need a several combinations of data structure in order to properly support
these operations. Firstable, we notice that we not only have to record the
freqeuncy of each items' usage, but when there is a tie in frequency, we also
require to maintain the record of the time that it was created or accessed. To
resolve this, we use a hashmap of key to (frequency, timestamp) pair. Also, we
also need a way to quickly identify the evict item based first on the freqeuncy
next timestamp - for this, we use prioirity queue (or minheap). Whenever an
item is accessed, we do not have to update our pq right away; to support our
operations efficiently, we maintain a set of updated keys that we will use to
update our priority queue based on the previous record of frequency and
timestamps. Finally, we would also require hashmap that will actually store our
key - value.

---

Python:

```python

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.ft = dict()
        self.d = dict()
        self.updates = set()
        slef.pq = list()

    def get(self, key):
        self.time += 1
        if key in self.d:
            f, _ = self.ft[key]
            self.ft[key] = (f, self.time)
            self.updates.add(key)
            return self.d[key]
        return -1

    def put(self, key, val):
        self.time += 1
        if key in self.d:
            self.get(key)
        else:
            if self.capacity == len(self.d):
                while self.pq and self.pq[0][2] in self.updates:
                    _, _, updateKey = heappop(self.pq)
                    f, t = self.ft[key]
                    heappush(self.pq, (f, t, updateKey)
                    self.updates.remove(updateKey)
                _, _, removeKey = heappop(self.pq)
                self.d.pop(removeKey)
                self.ft.pop(removeKey)
            heappush(self.pq, (0, self.time, key))
            self.ft[key] = (0, self.time)
        self.d[key] = val
```
