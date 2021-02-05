# 23 Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

Generallized merge k sorted lists algorithm would be a repeatition of merging
two lists until we exahust all the given lists. Since at each iteration, we
are reducing the size of the lists to merge by half, we only require to perform
log(k) merge two process. Hence, the overall time complexity should be O(n
* log(k)) instead of k.

---

Python

```python

class Solution:
    def mergeK(self, lists):
        while len(lists) > 1:
            temp = list()
            while lists:
                temp.append(self.mergeTwo(lists.pop(), lists.pop())
            lists = temp
            
        return lists[0] if lists else None

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
```
