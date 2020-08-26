146 LRU Cache
=============

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

```
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
```

The cache is initialized with a positive capacity.

Follow up:

Could you do both operations in O(1) time complexity?

---

Cache can be designed with a hashmap structure, with separate queue for
maintaining the order of the least recently used unit.

If the language supports a Doubly Linked Hast Set structure, that is a hashmap
but also supports ordered traversal and removal in O(1), we can use it instead
as well (such as OrderedDict in Python).

---

Python: OrderedDict approach.

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.m = OrderedDict()

    def update(self, key):
        val = self.m[key]
        del self.m[key]
        self.m[key] = val

    def get(self, key):
        if key in self.m:
            return self.m[key]
        return -1

    def put(self, key, val):
        if key in self.m:
            self.update(key)
        elif self.c == len(self.m):
            removed = next(iter(self.m))
            del self.m[removed]
        self.m[key] = val
```

Python: Queue + HashMap approach.

```python
from collections import deque

class InvalidCapacityError(Exception):
    pass

class Item:
    def __init__(self, k, v):
        self.k = k
        self.v = v

class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise InvalidCapacityError("Capacity <= 0")
        self.capacity = capaicty
        self.m = dict()
        self.q = deque()

    def update(self, k):
        self.q.remove(k)
        self.q.append(k)

    def get(self, k):
        if k not in self.m:
            return -1
        self.update(k)
        return self.m[k].v

    def put(self, k, v):
        if k in self.m:
            self.m[k].v = v
            self.update(k)
            return
        # delete lru item
        if self.capacity == len(self.m):
            del self.m[self.q.popleft()]
        self.m[k] = Item(k, v) 
        self.q.append(k)
```

