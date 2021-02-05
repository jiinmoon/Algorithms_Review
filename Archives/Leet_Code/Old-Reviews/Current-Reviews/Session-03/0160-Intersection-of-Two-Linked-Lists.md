160 Intersection of Two Linked Lists
====================================

Write a program to find the node at which the intersection of two singly linked
lists begins.

---

It is rather simply traverse on both of the linked lists as the same time until
two nodes are equal to each other. They are both either Null which indicates no
intersection, or intersecting node.

Time complexity should be of O(m + n).

---

Python:

```python

class Solution:
    def getIntersectionNode(self, A, B):
        if not (A and B):
            return None

        currA, currB = A, B
        while currA != currB:
            currA = B if not currA else currA.next
            currB = A if not currB else currB.next

        return currA
```
