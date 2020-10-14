# 23 Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

Generalized merging k sorted lists can be approached as a repeated merging two
sorted list process. At each iteration, we pair two lists at a time. Then, in
every step, we reduce the size of our lists by half - meaning that we can
complete the algorithm in O(k * log(n)) time complexity.

---

Python:

```python

class Solution:
    def mergeTwo(self, l1, l2):
        if not (l1 or l2):
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

    def mergeK(self, lists):
        while len(lists) > 1:
            temp = list()
            while lists:
                l1, l2 = lists.pop(), lists.pop()
                temp.append(self.mergeTwo(l1, l2))
            lists = temp
        return lists[0] if lists else None
```
