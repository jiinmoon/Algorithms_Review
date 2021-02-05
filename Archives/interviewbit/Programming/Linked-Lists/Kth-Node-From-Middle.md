# Kth Node From Middle

    Given a linked list A of length N and an integer B.

    You need to find the value of the Bth node from the middle towards the
    beginning of the Linked List A.

    If no such element exists, then return -1.

    NOTE:

    Position of middle node is: (N/2)+1, where N is the total number of nodes in
    the list.

---

## Approach:

First, compute the length of the given linked list inorder to find the mid
point. Then, we have to iterate up to (N // 2) - B steps forward to find the
Kth node from middle.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def kthFromMiddle(self, head, B):
        
        def length(node):
            result = 0
            while node:
                length += 1
                node = node.next
            return result

        N = length(head)

        if B > N // 2:
            return -1
        B = (N // 2) - B

        for _ in range(B):
            if not head:
                return -1
            head = head.next

        return head.val
```
