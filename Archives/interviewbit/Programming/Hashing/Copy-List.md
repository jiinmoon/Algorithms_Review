# Copy List

    A linked list is given such that each node contains an additional random
    pointer which could point to any node in the list or NULL.

    Return a deep copy of the list.

---

## Approach:

Use hashmap to store the node and copied nodes. The problem is the random
pointer which can point elsewhere in the list; hence, we check for its
existence, if not we create a copy to store in the hashmap.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def copyList(self, head):

        curr, d = head, dict()

        while curr:

            d.setdefault(curr, ListNode(curr.val))

            if curr.next:
                d[curr].next = d.setdefault(curr.next, ListNode(curr.next.val))

            if curr.random:
                d[curr].random = d.setdefault(curr.random, ListNode(curr.random.val))

            curr = curr.next

        return d[head]
```
