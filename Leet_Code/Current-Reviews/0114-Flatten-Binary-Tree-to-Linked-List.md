# 114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

---

Iterate to right; for every node, move over left subtree to right. But, there
may already be right subtree for current node. Thus, we first traverse to find
the rightmost node to left subtree and save the current node's right subtree to
rightmost node's right.

O(n) in time complexity and O(1) in space.

---

Python:

```python

class Solution:

    def flatten(self, root):

        if not root:
            return

        while root:

            if root.left:

                rightMost = root.left
                while rightMost.right:
                    rightMost = rightMost.right

                rightMost.right = root.right
                root.right = root.left
                root.left = None

            root = root.right
```
