148 Sort List
=============

Question:
---------

Sort a linked list in O(n * log(n)) using constant space complexity.

Solutions:
----------

Since the singly linked list makes it difficult to traverse back and forth, the
best sorting algorithm that we should use here is the merge sort. We will
repeatedly find the mid node and split the linked list into two halves. This is
repeated until single element, and then we will merge the two lists back on up
the recursive calls.

Codes:
------

Python:

```python
class Solution:
    def merge(self, l1, l2):
        dummyHead = curr = ListNode(None)
        while l1 or l2:
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
            curr.next = temp
            curr = curr.next
        curr.next = l1 or l2
        return dummyHead.next

    def findMid(self, head):
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        return head2

    def sortList(self, head):
        # base case
        if not head or not head.next:
            return head
        # find mid and split
        head2 = self.findMid(head)
        lower = self.sortList(head)
        upper = self.sortList(head2)
        head = self.merge(lower, upper)
        return head
```

---

**Source:**

LeetCode: [Sort-List](https://leetcode.com/problems/sort-list/)
