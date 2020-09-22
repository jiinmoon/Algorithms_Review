# 146 LRU Cache
#
# To maintain the recent usage of the items, we require a queue data structure
# to keep track of the item that needs to be evicted when we are at full
# capacity. Also, we require a hashmap data structure to support constant time
# look up for our requested key.
#
# This is supported by OrderedDict structure in python which is a doubly-linked
# hash set structure that supports removal of items in O(1) as well as constant
# time look ups.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key in self.d:
            # remove and reinsert to end of d
            val = self.d.pop(key)
            self.d[key] = val
            return val
        return -1

    def put(self, key, val):
        if key in self.d:
            # update
            self.get(key)

        if self.capacity == len(self.d):
            # evict front of the d which is LRU item
            # OrderedDict is iterable
            self.d.pop(next(iter(self.d)))

        self.d[key] = val
