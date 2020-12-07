# 23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

---

#### (1) Brute Force; collect all values and sort.

Naive solution would be to collect all the values from the lists, then build up
a new sorted list. Since each lists are sorted already, we do not have to
employ sorting algorithm but merging in sorted manner. It would be O(m * n) in
time complexity where m is the number of lists.

#### (2) Repeated pairing then merging.

At each iteration, we pair up lists. By doing so, we can reduce the amount to
sort by half each time. Hence, we can reduce the time to merge by O(log(m) * n)
as number of lists to merge reduces by half each time.

---

Python: repeated pariing then merging.

```python

class Solution23:

    def mergeKLists(self, lists):

        while len(lists) > 1:
            temp = list()
            while lists:
                l1 = lists.pop()
                l2 = lists.pop() if lists else None
                temp.append(self.mergeTwoLists(l1, l2))
            lists = temp

        return lists[0] if lists else None

    def mergeTwoLists(self, l1, l2):
        
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
