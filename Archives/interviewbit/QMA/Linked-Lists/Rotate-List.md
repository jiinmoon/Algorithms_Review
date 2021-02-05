# Rotate List

Given a list, rotate the list to the right by k places, where k is
non-negative.

---

To move the list to right by k, we need to find the k-th node from behind.
However, k can be unexpectedly large thus we must first take the length of the
array and apply modulo.

Then, we move the fast runner forward by k-th place. And move two runners at
same pace. Slow runner will be placed at new tail end of the rotated list and
fast runner at the end of the list. We conjoin fast runner to the head, then
set the new tail's next as None.

O(n) in time complexity.

---

Python:

```python

class Solution:
    
    def length(self, head):

        result = 0

        while head:
            head = head.next
            result += 1

        return result


    def rotateRight(self, A, B):

        newHead = newTail = A

        B %= length(A)

        for _ in range(B):
            newHead = newHead.next

        while newHead.next:
            newHead = newHead.next
            newTail = newTail.next

        newHead.next = head
        newHead = newTail.next
        newTail.next = None

        return newHead
```
