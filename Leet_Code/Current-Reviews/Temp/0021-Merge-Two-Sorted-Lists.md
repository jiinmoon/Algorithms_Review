# 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list
should be made by splicing together the nodes of the first two lists.

---

We can merge two lists in a single iteration by comparing two nodes and
appending smaller node to our resulting list. The exceptional cases to watch
out for would be uneven lists given to us. This would be O(max(m, n)) in time
complexity and O(m + n) in space complexity.

---

Python:

```python

class Solution21:

    def mergeTwo(self, l1, l2):

        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 or l2

        return dummy.next

```
