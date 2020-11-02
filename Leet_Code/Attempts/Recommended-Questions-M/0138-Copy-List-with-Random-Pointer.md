# 138 Copy List with Random Pointer

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each
node is represented as a pair of [val, random\_index] where:

val: an integer representing Node.val
random\_index: the index of the node (range from 0 to n-1) where random pointer
points to, or null if it does not point to any node.

---

The problem is that the random pointer can point at any other node in the given
list. We solve this problem by creating a hashmap where key is the original
node and the value would be the clone. Thus, we first identify whether the
clone of the random node is in the hashmap, and then rewire the pointers. The
algorithm should complete in O(n).

---

Python:

```python

class Solution:
    def copyListWithRandomPointer(self, head):
        d = dict()
        curr = head
        while curr:
            if curr not in d:
                d[curr] = ListNode(curr.val, None, None)
            if curr.next:
                if curr.next not in d:
                    d[curr.next] = ListNode(curr.next.val, None, None)
                d[curr].next = d[curr.next]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = ListNode(curr.random.val, None, None)
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]
```
