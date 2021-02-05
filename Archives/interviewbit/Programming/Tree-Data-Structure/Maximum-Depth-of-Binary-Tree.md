# Maximum Depth of Binary Tree

    Given a binary tree, find its maximum depth.

    The maximum depth of a binary tree is the number of nodes along the longest
    path from the root node down to the farthest leaf node.

---

## Approach:

Recursively traverse down to the leaf nodes; starting on, we return maximum of
heights returned from left and right subtrees.

---

Python:

```python

class Solution:

    def maxDepth(self, root):

        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```
