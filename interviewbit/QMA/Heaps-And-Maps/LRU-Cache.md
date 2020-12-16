# LRU Cache

Design LRU Cache.

---

We require queue and hashmap to efficiently identify LRU item to remove and
update. To update the LRU item whenever it is used or added, we require
a flexible queue that supports fast update at either ends as well as middle.
Thus, we use hashmap + doubly linked list.

---

Python:

```python

class Node:

    def __init__(self, key=None, val=None):

        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.d = dict()
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def get(self, key):
        
        if key not in self.d:
            return -1
        
        # update node as recently used; move to front of queue
        node = self.d[key]
        self._remove(node)
        self._addFront(node)
        return node.val

    def put(self, key, val):

        if key in self.d:
            node = self.d[key]
            node.val = val
            self._remove(node)
            self._addFront(node)
        else:
            # evict least recently used unit
            if self.capacity == len(self.d):
                self._removeRear()
                del self.d[key]
            node = ListNode(key, val)
            self.d[key] = node
            self._addFront(node)

    def _remove(self, node):
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next

    def _addFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head = node

    def _removeRear(self):
        node = self.tail.prev
        self._remove(node)
        return node
```
