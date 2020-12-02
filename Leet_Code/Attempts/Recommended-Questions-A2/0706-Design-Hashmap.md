# 706. Design Hashmap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

```
put(key, value) : Insert a (key, value) pair into the HashMap. If the value
already exists in the HashMap, update the value.

get(key): Returns the value to which the specified key is mapped, or -1 if this
map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.
```

---

Simple design of a hashmap would be to use array of linked lists. We first hash
the key and map it to an array index. Here, if a boundary is known, then we do
not need to create a nested structure of array of linked lists as we can avoid
hash collisions. For example, if the key values are bounded between 0 and
1000000, then we can create an array of size 1000000. However, let us assume
this is not feasible.

Then, to the mapped index indicated by hashed key, we search the linked list
for the key, value pair. If the key exists, we can update it when we put or
retrieve it when we get. If the key does not exist, we cannot get nor remove
but can put by appending to existing list.

The efficiency of the hashmap depends upon the hash function used and size of
the array. Typically, we can achieve O(1) but in actuality, it is bounded by
O(n/k) where n is the number of keys and k is the size of array. 

Here are few implementation notes for Python:

(1) List is not ideal to substitute actual linked list - will incurr O(n)
shifting if a value is to be removed from the list. i.e. using (`del
self.d[hash(key)]`).

(2) key is already an int; do not necessarily require `hash()`.

---

Python: Array of Linked-List approach;

```python

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Solution706:
    SIZE = 1024

    def __init__(self):
        self.q = [None] * self.SIZE

    def put(self, key, val):
        h = hash(key) % self.SIZE

        # bucket is empty
        if self.q[h] == None:
            self.q[h] = ListNode(key, val)
        else:
            # two cases; key is in the bucket or not
            curr = self.q[h]
            # iterate to end; if key is found update else append to end
            while curr:
                if curr.key == key:
                    curr.val = val
                    return
                if not curr.next:
                    curr.next = ListNode(key, val)
                    return
                curr = curr.next

    def get(self, key):
        h = hash(key) % self.SIZE

        if self.q[h] != None:
            curr = self.q[h]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return -1

    def remove(self, key):
        h = hash(key) % self.SIZE
        
        # exceptional cases:
        # bucket is empty or it is head of the list
        if self.q[h] == None:
            return

        prev = curr = self.q[h]
        if curr.key == key:
            self.q[h] = curr.next
        else:
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                prev, curr = curr, curr.next
```
