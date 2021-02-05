# 445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative
integers. The most significant digit comes first and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists
is not allowed.

---

Reversing the linked lists so that we can work on the least significant digit to
most significant digit is ideal approach, but we cannot modify the input lists.
Hence, we simply traverse on both lists to convert them into the integer
format. Then add two integers together. The end result is then convert back
into the linked list format - working from least to most significant digit, we
should create the list in reversed fashion.

The time complexity should be O(n + m).

---

Python:

```python

class Solution:
    def addTwoNumbers(self, l1, l2):
        def helper(head):
            result = 0
            while head:
                result = result * 10 + head.val
                head = head.next
            return result

        result = helper(l1) + helper(l2)
        # exceptional case here
        if not result:
            return ListNode(0)

        prev = None
        while result:
            node = ListNode(result % 10)
            node.next = prev
            prev = node
            result //= 10

        return prev
```
