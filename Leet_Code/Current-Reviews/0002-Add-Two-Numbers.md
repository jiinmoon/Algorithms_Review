# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

---

Since the numbers stored in linked lists are convinently in reversed order, we
may add current digits and build our resulting list as we iterate on both of
the lists. Time and space complexity would be O(max(n, m)) as we only have to
iterate as far out as the longest list.

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
            carry //= 10
            prev = prev.next

        return dummy.next
```
