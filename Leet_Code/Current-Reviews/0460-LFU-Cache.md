460 LRU Cache
=============

Design and implement a data structure for Least Frequently Used (LFU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

---

As our main data structure, we can maintain a hashmap that can store key and
value. And we also need to mapping between the key and its frequency. When we
read `put` description carefull, there can be a "tie" as well - meaning that we
also need a timestamp of the elements. So, we will also maintain another
hashmap where we are going to store key and (frequency, timestamp) tuples.

When capacity is met, we need to find not only the least frequenctly used and
also the oldest.

---

Python:

```python
import heapq

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time = 0           # timestamp; when items was placed or updated
        self.m = dict()         # main struct; { k : v }
        self.freqTimes = dict() # { k : (freq, time) }
        self.pq = []            # [(freq, time, key)]; update when new key
        self update = set()     # keys to update (get/put since last new key)

    def get(self, k):
        # update new timestamp
        self.time += 1
        if key not in self.m:
            return -1
        # if key in the map, update its frequency and time
        freq, _ = self.freqTimes[k]
        self.freqTimes[k] = (freq + 1, self.time)
        # add key to update list for later
        self.update.add(k)
        return self.m[k]

    def put(self, key, val):
        if self.capacity <= 0:
            return
        self.time += 1
        if key in self.m:
            # if key already been inserted before
            # update frequenct, time and update list
            f, _ = self.freqTimes[key]
            self.freqTimes[key] = (f + 1, self.time)
            self.update.add(key)
        else:
            # otherwise, we need to insert
            # but have capacity been reached? if so, LFU item needs to go
            if len(self.m) >= self.capacity:
                while self.pq and self.pq[0][2] in self.update:
                    # priority queue contains (f, t, k)
                    _, _, k = heapq.heappop(self.pq)
                    f, t = self.freqTimes[k]
                    heapq.heappush(self.pq, (f, t, k))
                    self.update.remove(k)
                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.pq)
                self.m.pop(k)
                self.freqTimes.pop(k)
            self.freqTimes[key] = (0, self.time)
            heapq.heappush(self.pq, (0, self.time, key))
        self.map[key] = val
```
