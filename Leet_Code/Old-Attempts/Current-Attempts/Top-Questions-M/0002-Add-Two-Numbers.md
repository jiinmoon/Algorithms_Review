# 2 Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

Until we exhaust all the nodes from both of the list, we iterate on both and
add sum of each digit while creating each node.

---

Python:

```python

class Solution:
    def addTwoNumbers(self, l1, l2):
        if not (l1 or l2):
            return l1 or l2

        dummy = prev = ListNode(None)
        carrySum = 0

        while l1 or l2 or carry:
            if l1:
                carrySum += l1.val
                l1 = l1.next
            if l2:
                carrySum += l2.val
                l2 = l2.next
            prev.next = ListNode(carrySum % 10)
            carrySum //= 10
            prev = prev.next

        return dummy.next
```
