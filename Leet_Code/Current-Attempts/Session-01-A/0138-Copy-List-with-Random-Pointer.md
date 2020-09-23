# 138 Copy List with Random Pointer

Use hashmap to store the all nodes copied to account for the random pointer.

---

Python:

```python

class Solution:
    def copyList(self, head):
        d = dict()
        curr = head

        while curr:
            if curr not in d:
                d[curr] = Node(curr.val, None, None)
            if curr.next:
                if curr.next not in d:
                    d[curr.next] = Node(curr.next.val, None, None)
                d[curr].next = d[curr.next]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val, None, None)
                d[curr].random = d[curr.random]
            curr = curr.next

        return d[head]
```
