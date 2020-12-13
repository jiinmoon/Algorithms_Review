# K reverse linked list

Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K 

---

Recursively find K segments; start returning nodes where we have the start of
the each K-segment and reversing them.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def reverseList(self, A, B):

        prev = A
        for _ in range(B):
            if not prev:
                return A
            prev = prev.next

        prev = self.reverseList(prev, B)

        for _ in range(B):
            temp = A.next
            A.next = prev
            prev = A
            A = temp

        return prev
```
