92 Reverse Linked List II
=========================

Question:
---------

Reverse a linked list from position m to n in a single pass.

Solutions:
----------

We traverse up to m nodes and start the reversing process on (m-n) nodes ahead.

Codes:
------

Python:

```python
class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m > n:
            return

        prev, curr = None, head
        while m:
            curr = curr.next
            m -= 1; n -= 1
        newHead, newTail = prev, curr

        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if newHead:
            newHead.next = prev
        else:
            head = prev

        newTail.next = curr

        return head
```

Same idea; a bit more compact.

```python
class Solution:
    def reverseBetween(self, head, m, n):
        dummyHead = prev = ListNode(None)
        n -= m
        while m:
            prev = prev.next
            m -= 1
        newHead, newTail = None, prev.next
        while n >= 0:
            temp = newTail.next
            newTail.next = newHead
            newHead = newTail
            newTail = temp
            n -= 1
        curr.next.next = temp
        curr.next = newHead
        return dummyHead.next
```
---

**Source:**

LeetCode:
[Reverse-Linked-List-II](https://leetcode.com/problems/reverse-linked-list-ii)
