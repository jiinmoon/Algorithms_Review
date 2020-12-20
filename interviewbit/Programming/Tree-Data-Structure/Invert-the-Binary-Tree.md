# Invert the Binary Tree

    Given a binary tree, invert the binary tree and return it.


## Approach:

We recursively traverse down to the bottom, then start returning each of the
node. While we do so, we exchange left and right subtrees. Or we can do
bottom down where we save the pointers for current node's left and right, and
exchange them on the way down.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def invertTree(self, root):

        if not root:
            return None

        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        return root

```
