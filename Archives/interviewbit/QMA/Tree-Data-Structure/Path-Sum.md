# Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

---

Compute pathSum down to the leaf node; if pathSum has reached the target value,
we can return true; otherwise, continue to explore down to the leaf node.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def hasPathSum(self, root, target):

        def _traverse(node, pathSum):
            
            if not node:
                return False

            pathSum -= node.val
            if not (node.left or node.right or pathSum):
                return True

            return _traverse(node.left, pathSum), _traverse(node.right, pathSum)

        return 1 if _traverse(root, 0) else 0

```


