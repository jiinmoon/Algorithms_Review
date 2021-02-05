# 98. Validate BST

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key.
The right subtree of a node contains only nodes with keys greater than the
node's key.
Both the left and right subtrees must also be binary search trees.

---

To determine whether the given binary tree fits the definition of BST, we apply
the criteria of the BST in recursive manner. However, we must note that when we
move down from the current node, the child value has to be compared against not
just the parent's value but absolute ancestor's min and max value as well.

---

Python:

```python

class Solution:
    def isValidBST(self, root):
        def helper(node, minVal, maxVal):
            if not node:
                return True
            if not (minVal < node.val < maxVal):
                return False
            return helper(node.left, minVal, node.val) and helper(node.right, node.val, maxVal)
        return helper(root, float('-inf'), float('inf'))
```
