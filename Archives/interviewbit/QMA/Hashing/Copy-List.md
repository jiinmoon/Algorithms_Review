# Copy List

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

---

Python:

```python

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        d, curr = dict(), head
        
        while curr:
            
            d[curr] = d.setdefault(curr, RandomListNode(curr.label))
            
            if curr.next:
                d[curr].next = d.setdefault(curr.next, RandomListNode(curr.next.label))
            
            if curr.random:
                d[curr].random = d.setdefault(curr.random, RandomListNode(curr.random.label))
            
            curr = curr.next
        
        return d[head]
```
