146 LRU Cache
=============

Question:
---------

Design and implement LRU Cache. It should support `get` and `put` operations.

The cache will be initilized with a positive capacity.

Can both operations happen in O(1)?

Solutions:
----------

LRU implies that when the cache is full, the least recently used item should be
evicted to make a room for the new item. Internally, we will use two data
structures - queue and map. The map will store our cache items - and allows us
to retrieve the value quickly with `get(key)` operation. Whenever an item is
put, or updated, we remove th item from the queue and reinsert to the queue.
When capacity is reached, we evict the first item in the queue.

The problem here is what datastructure to use for the queue. Since it needs to
be able to support remove in O(1), it would be good idea to use doubly-linked
list and have values stored as ListNodes. 

Codes:
------

Python: using `collections.deque`.

```python
from collections import deque

class InvalidCapacityException(Exception):
    pass

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

clas LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise InvalidCapacityException("Capacity cannot be below 0.")
        self.capacity = capacity
        self.map = dict()
        self.queue = deque()

    def _update(self, key):
        self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        if key not in self.map:
            return -1
        self._update(key)
        return self.map[key].value

    def put(self, key, value):
        # key already in the map
        # update map and refresh the value queue
        if key in self.map:
            self.map[key].value = value
            self._update(key)
            return
        # capacity is reached
        # delete lru item from queue and map
        if self.capacity == len(self.map):
            del self.map[self.queue.popleft()]
        # insert new item in map
        self.map[key] = Item(key, value)
        self.map.append(key)
```

---

**Source:**

LeetCode: [LRU-Cache](https://leetcode.com/problems/lru-cache/)
