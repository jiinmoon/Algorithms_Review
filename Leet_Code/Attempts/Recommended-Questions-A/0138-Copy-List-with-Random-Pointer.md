# 138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

---

We can efficiently create a deep copy of the given list using the hashmap - and
by doing so, we can avoid the problem of dealing the node that does not exist
yet which is pointed by the random variable.

---

Python:

```python

class Solution:
    def copyList(self, head):
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
