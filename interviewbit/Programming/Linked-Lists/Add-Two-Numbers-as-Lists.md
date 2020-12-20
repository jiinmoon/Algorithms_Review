# Add Two Numbers as Lists

    You are given two linked lists representing two non-negative numbers. The
    digits are stored in reverse order and each of their nodes contain a single
    digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)


---

Python:

```python

class Solution:

    def addTwoNums(self, l1, l2):

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
