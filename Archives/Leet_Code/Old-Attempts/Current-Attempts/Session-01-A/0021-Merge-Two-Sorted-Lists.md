# 21 Merge Two Sorted Lists

Simply traverse while appending the minimum of the two heads from the sorted
lists unto the new list. Time complexity is in O(m + n).

---

Python:

```python

class Solution:
    def mergeTwo(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            prev.next = temp
            prev = prev.next

        prev.next = l1 or l2

        return dummy.next
```
