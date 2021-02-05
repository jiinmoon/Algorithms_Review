# 206. Reverse Linked List

Reverse a singly linked list.

---

Python: Iterative.

```python

class Solution206:

    def reverseList(self, head):

        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
```

Python: Recursive.

```python

class Solution206:

    def reverseList(self, head):

        if not (head and head.next):
            return head

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return prev
```
