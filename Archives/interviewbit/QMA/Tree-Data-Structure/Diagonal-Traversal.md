# Diagonal Traversal

Consider lines of slope -1 passing between nodes.

Given a Binary Tree A containing N nodes, return all diagonal elements in
a binary tree belonging to same line.

---

We traverse to right while saving nodes to revisit in a queue.

O(n) in time complexity and O(h) in space complexity where h is the height of
the tree.

---

Python:

```python

from collections import deque

class Solution:

    def diagonalTraversal(self, root):

        queue = deque([root])
        result = []

        while queue:

            curr = queue.popleft()

            while curr:
                result.append(curr.val)
                if curr.left:
                    queue.append(curr)
                curr = curr.right

        return result

```
