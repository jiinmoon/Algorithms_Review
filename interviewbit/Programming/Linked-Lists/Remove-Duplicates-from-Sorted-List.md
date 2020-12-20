# Remove Duplicates from Sorted List

    Given a sorted linked list, delete all duplicates such that each element appear
    only once.

---

## Approach:

Iterate forward while checking against the next node's value. If they are same,
we skip over that node - otherwise, continue to iterate forward.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def removeDuplciates(self, head):

        if not (head and head.next):
            return head

        curr = head
        while curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
            else:
                curr.next = curr.next.next

        return head
```
