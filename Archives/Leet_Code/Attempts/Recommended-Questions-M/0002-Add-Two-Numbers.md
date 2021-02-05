# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

Since the number represented in the given linked list is in "reverse" order, we
can simply add up the values as we iterate on the both of the linked list while
they are present. For each iteration, we can use modulo operation of extract
the last digit and create the new list to append. The time complexity should be
linear for this algorithm.

---

Python:

```python

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not (l1 or l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry % 10)
            carry //= 10
            prev = prev.next

        return dummy.next
```
