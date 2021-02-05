# 460 LFU Cache

Use the additional hashmap to store the frequency and time that it was updated.
Also, maintain a priority queue by first its frequency and then time, so that
we can evict the least frequent and oldest time.

---

Python:

```python

import heapq

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0
        self.q = list()
        self.updates = set()
        self.d = dict()
        self.ft = dict()

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
            f, _ = self.ft[key]
            self.ft[key] = (f, self.time)
            self.updates.add(key)
        else:
            if self.capacity == len(self.d):
                while self.pq and self.pq[0][2] in self.updates:
                    _, _, k = heappop(self.pq)
                    f, t = self.ft[k]
                    heappush(self.pq, (f, t, k))
                    self.updates.remove(k)
                _, _, k = heappop(self.pq)
                self.ft.pop(k)
                self.d.pop(k)
            self.ft[key] = (0, self.time)
            heappush(self.pq, (0, self.time, key))
        self.d[key] = val
```
