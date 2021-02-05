# 21 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list
should be made by splicing together the nodes of the first two lists.

---

Merging two sorted linked lists can be done by simply iterating over the two
linked lists, comparing their first nodes. Then, append the smaller node to the
new list, and advance.

The exceptional case here that we need to be mindful is that two lists can be
of different lengths. Hence, if one of the list becomes exhuasted, we append
the whichever is leftover to the end of the new list.

Time complexity should be of O(m + n).

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
