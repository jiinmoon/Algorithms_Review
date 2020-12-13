# Sort Binary Linked List

Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of
only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.

---

The problem does not state that we cannot modify the node's values; hence we
simply count the numer of ones and repopulate the list.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def solve(self, A):

        length, ones = 0, 0 

        curr = A
        while curr:
            if curr.val = 1:
                ones += 1
            length += 1
            curr = curr.next

        curr = A
        for _ in range(length - ones):
            curr.val = 0
            curr = curr.next

        while curr:
            curr.val = 1
            curr = curr.next

        return A
```
