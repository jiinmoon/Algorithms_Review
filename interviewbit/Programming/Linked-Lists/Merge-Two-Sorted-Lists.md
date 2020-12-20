# Merge Two Sorted Lists

    Merge two sorted linked lists and return it as a new list.
    The new list should be made by splicing together the nodes of the first two
    lists, and should also be sorted.

---

Python:

```python

class Solution:

    def mergeTwo(self, l1, l2):
        
        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)

        while l1 and l2:

            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = 2l
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2

        return dummy.next
```

