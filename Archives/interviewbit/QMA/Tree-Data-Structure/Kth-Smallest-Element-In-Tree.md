# Kth Smallest Element in Tree

Given a binary search tree, write a function to find the kth smallest element
in the tree.

---

Perform inorder traversal; starting from leftmost node, we iterate K-th place
forward to return the smallest element.

O(h + k) in time complexity where h is height to traverse to leftmost node.

---

Python:

```python

class Solution:

    def kthsmallest(self, A, B):

        def traverse(node):

            if not node:
                return

            traverse(node.left)

            self.k -= 1

            if not self.k:
                self.result = node
                return

            traverse(node.right)

        self.k, self.result = B, None
        
        traverse(A)

        return self.result.val
```
