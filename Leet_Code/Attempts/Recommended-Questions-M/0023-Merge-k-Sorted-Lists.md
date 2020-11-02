# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

In general, merging K sorted lists can be expressed as a repeated operations of
the merging two sorted lists until single list is left. We realize that at each
iteration, we are reducing the size of the merging by half which indicates that
the overall time complexity is based of log of k which is O(log(k) * n).

---

Python:

```python

class Solution:
    def mergeKSortedLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            temp = list()
            while lists:
                temp.append(self.mergeTwoSortedLists(lists.pop(), lists.pop()))
            lists = temp
        return lists[0]

    def mergeTwoSortedLists(self, l1, l2):
        if not (l1 or l2):
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
