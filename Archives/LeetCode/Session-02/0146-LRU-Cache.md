# 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:

```
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise
return -1.

void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
```

Follow up:

Could you do get and put in O(1) time complexity?

---

To implement such a structure in efficient manner, we require two aspect. One,
we require hashmap like structure so that we can easily update our values as
well as insert the key. And other is queue like structure to maintain the order
of our elements inserted so that we know which pair to evict once the capacity
has been reached.

Hence, the problem can be solved by using a dictionary and a queue implemented
with doubly linked list where we can insert pair of key to node in
a dictionary, and if need for evict arises, we can find the order in a queue.

---

Python: Using `OrderedDict` structure which maintains order of keys in
dictionary.

```python

from collections import OrderedDict

class Solution146:

    def __init__(self, capacity):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        if key not in self.d:
            return -1
        
        # update order
        val = self.d[key]
        del self.d[key]
        self.d[key] = val
        return val

    def put(self, key, val):
        if key in self.d:
            del self.d[key]

        elif self.capacity == len(self.d):
            del self.d[next(iter(self.d))]

        self.d[key] = val
```

Python: Implmenting Doubly Linked List + Using Dictionary.

```python

class ListNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev, self.next = None, None


class Solution146:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0 # size of list
        self.d = dict()
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.d:
            return -1

        # update order; bring paired node to front
        self._moveToFront(self.d[key])
        return self.d[key].value

    def put(self, key, value):
        if key not in self.d:
            if self.size == self.capacity:
                evictNode = self._removeLast()
                self.d.pop(evictNode.key)
                self.size -= 1
            self.size += 1
            self.d[key] = ListNode(key, value)
            self._add(self.d[key])
        else:
            self.d[key].value = value
            self._moveToFront(self.d[key])
    
    # adds new node to front of queue
    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    # moves existing node to front of queue
    def _moveToFront(self, node):
        self._remove(node)
        self._add(node)

    def _removeLast(self):
        node = self.tail.prev
        self._remove(node)
        return node
``` 
