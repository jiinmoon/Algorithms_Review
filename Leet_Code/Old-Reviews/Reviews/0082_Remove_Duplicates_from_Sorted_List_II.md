82 Remove Duplicates from Sorted List II
========================================

Question:
---------

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Solutions:
----------

For every new value that we encounter, we check to see whether duplicate exist.
If it does, then we move forward until non-duplicate value is found and fix the
pointers.

Codes:
------

Python:

```python
class Solution:
    def deleteDuplicates(self, head):
        # head may contain duplicates
        dummyHead = ListNode(None)
        dummyHead.next = head
        prev, curr = dummyHead, dummyHead.next
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.val
                while curr and curr.val == temp:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummHead.next
```

---

**Source:**

LeetCode: [Remove-Duplicates-from-Sorted-List-II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)
