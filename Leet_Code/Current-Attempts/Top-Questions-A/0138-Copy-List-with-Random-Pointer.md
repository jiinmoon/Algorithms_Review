# 138 Copy List with Random Pointer

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.

---

We cannot simply traverse and copy the nodes since there is not only the next
pointer, but also random pointer that may point ahead into the list. To resolve
this, we create a hashmap of node to copied node. By doing so, we can check to
see whether current node's next and random nodes exist; if not, we create and
add to the hashmap.

---

Python:

```python

class Solution:
    def copyListWithRandom(self, head):
        if not head:
            return None

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
