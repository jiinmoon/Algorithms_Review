# K reverse linked list




---

## Approach:

We iterate upto K steps whilst reversing. If we have more nodes left over, we
recurse.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reverseKGroup(self, head, k):

        if not (head and head.next):
            return head

        prev = head

        for _ in range(k):
            if not prev:
                return head
            prev = prev.next

        prev = self.reverseKGroup(prev, k)

        for _ in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
```
