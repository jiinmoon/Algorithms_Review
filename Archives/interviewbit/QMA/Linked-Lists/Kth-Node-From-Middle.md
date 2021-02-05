# Kth Node From Middle

Given a linked list A of length N and an integer B.

You need to find the value of the Bth node from the middle towards the
beginning of the Linked List A.

If no such element exists, then return -1.

NOTE:

Position of middle node is: (N/2)+1, where N is the total number of nodes in
the list.

---

Finding node that is Bth from middle of the point is finding the node that is
(length of list // 2) - B. Hence, we iterate once to find the length, compute
the step and iterate forward while we can. O(n) in time complexity.

---

Python:

```python

class Solution:

    def solve(self, A, B):

        def length(head):
            result = 0
            while head:
                head = head.next
                result += 1
            return result

        N = length(A)

        if B > N // 2:
            return -1

        for _ in range(N // 2 - B):
            if not A:
                return -1
            A = A.next

        return A.val
```
