# 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should
be made by splicing together the nodes of the first two lists.

---

We can merge two linked lists in sorted manner by examining the first nodes
from each of the list, and splice the smaller node to the new list. This would
be O(m + n) in time complexity, but no additional space as we are reusing the
given linked lists.

---

Python:

```python

class Solution21:

    def mergeTwo(self, l1, l2):

        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2

        return dummy.next
```
