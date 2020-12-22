# LRU Cache

    Design and implement a data structure for LRU (Least Recently Used) cache. It
    should support the following operations: get and set.

        get(key) - Get the value (will always be positive) of the key if the key exists
        in the cache, otherwise return -1.

        set(key, value) - Set or insert the value if the key is not already present.
        When the cache reaches its capacity, it should invalidate the least recently
        used item before inserting the new item.

    The LRU Cache will be initialized with an integer corresponding to its
    capacity. Capacity indicates the maximum number of unique keys it can hold at
    a time.

    Definition of “least recently used” : An access to an item is defined as a get
    or a set operation of the item. “Least recently used” item is the one with the
    oldest access time.

---

## Approach:

To maintain an order, we require a queue data structure; but to easily look up
and update, we would need a hashamp. Hence, we combine both where we use
hashmap to maintain the (key, node) where node is the doubly linked list node
containing the target value. We need to use doubly linked list as we need to be
able to easily access both end of the list as well as update any arbitary node.

---

Python:

```python

class ListNode:

    def __init__(self, key=None, value=None):

        self.key = key
        self.value = value
        self.next, self.prev = None, None


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

        node = self.d[key]
        self._remove(node)
        self._addFront(node)

        return node.value


    def put(self, key, value):

        if key in self.d:

            node = self.d[key]
            node.value = value
            self._remove(node)
            self._addFront(node)

        else:
            
            if self.capacity == len(self.d):
                self._removeRear()
                del self.d[key]

            node = ListNode(key, value)
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
        self.head.next = node

    
    def _removeRear(self):
        
        node = self.tail.prev
        self._remove(node)
        return node


