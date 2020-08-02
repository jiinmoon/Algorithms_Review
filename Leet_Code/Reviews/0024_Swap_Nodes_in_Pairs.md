24 Swap Nodes in Pairs
======================

Question:
---------

Given a linked list, swap every two nodes and return its head.

Solutions:
----------

N/A.

Codes:
------

Python:

```python
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummyHead = prev = ListNode(None)
        while head and head.next:
            temp = head.next.next
            prev.next = head.next
            head.next.next = head
            prev = head
            head = temp
        prev.next = head
        return dummyHead.next
```

---

**Source:**

LeetCode:
[Swap-Nodes-in-Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
