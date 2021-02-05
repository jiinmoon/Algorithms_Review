# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

We iterate on both of the given lists so long as there are digits to add them
and create a new node to represent the new digit. However, since the numbers
can overflow, we use carry variable to **carry** over the values if the sum of
two previous values are to carry over to the next digit.

O(n) in both time and space.

---

Python:

```python

class Solution2:

    def addTwoNumbers(self, l1, l2):
        if not (l1 and l2):
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
            prev = prev.next
            carry //= 10

        return dummy.next
```

