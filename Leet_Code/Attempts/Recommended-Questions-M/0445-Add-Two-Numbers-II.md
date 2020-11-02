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

One method would be to reverse both of the lists first, then add up the two
numbers as we build it forward (and reverse the end resulting list as well).

However, since the reversing method is not available to us, we would simply
iterate on both of the lists to extract two numbers. Then, iterate on forward
using modulo operation to build on the resulting list.

---

Python:

```python

class Solution:
    def listToInt(self, head):
        result = 0
        while head:
            result *= 10 + head.val
            head = head.next
        return result

    def addTwoNumbers(self, l1, l2):
        if not (l1 or l2):
            return l1 or l2

        result = self.listToInt(l1) + self.listToInt(l2)
        if not result:
            return ListNode(0)
        
        # end result should be in reversed order when we build it
        prev = None
        while result:
            result, curr = divmod(result, 10)
            newNode = ListNode(curr)
            newNode.next = prev
            prev = newNode

        return prev
```

