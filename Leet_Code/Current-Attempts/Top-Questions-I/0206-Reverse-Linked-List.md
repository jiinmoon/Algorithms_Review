# 206 Reverse Linked List

Reverse a singly linked list.

---

It is much easier to visualize the sample nodes and go through the steps.
Remember to create a prev node at the start.

---

Python:

```python

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
```
