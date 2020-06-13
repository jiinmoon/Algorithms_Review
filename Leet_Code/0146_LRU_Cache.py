""" 146. LRU Cache

Question:

    Design and implement a data struct for LRU cache, that supports get(key) and
    put(key, value) operations.

    get(key) - should retrieve the value; if not exist, return -1.

    get(key, value) - set or insert the value if the key is not laready present.
        if capacity is reached, it should evict least recently used item before
        inserting a new item.

    Cache is initialized with a set positive capacity.

    Can both operations supported in O(1) time complexity?

---

Solution:

    Use the hashmap structure beneath to support the cache, while using extra
    queue to record the how frequently the item is used. Everytime item is
    accessed, we remove/add the key back into the queue.

"""

# use deque for faster ops at either ends.
from collections import deque

class InvalidCapacityException(Exception):
    pass

class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise InvalidCapacityException("Capacity is set to {}".capacity)
        self.capacity = capacity
        self.keyMap = dict() # map
        self.lruCache = deque() # queue

    def get(self, key):
        if key not in self.keyMap:
            return -1
        self.lruCache.remove(key)
        self.lruCache.append(key)
        return self.keyMap[key].value

    def put(self, key, value):
        # key is already in keyMap; update value in map and queue.
        if key in self.keyMap:
            self.keyMap[key].value = value
            self.lruCache.remove(key)
            self.lruCache.append(key)
            return

        # capcity has been reached; delete LRU item.
        if self.capacity == len(self.keyMap):
            del self.keyMap[self.lruCache.popleft()]

        # add new key: value item in map.
        self.keyMap[key] = Item(key, value)
        self.lruCache.append(key)
