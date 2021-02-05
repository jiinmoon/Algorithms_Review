110 Balanced Binary Tree
========================

Question:
---------

Given a binary tree, determine if it is height-balanced.

Solutions:
----------

We may repeatedly call `height()` on each node's children as we traverse down
and compare them, but this is highly inefficient. The better approach would be
to start returning the heights from leaf to up, comparing them.


Codes:
------

Python:

```python
class Solution:
    def isBalanced(self, root):
        if not root:
            return True

        def checkBalance(node):
            if not node:
                return 0 # base height
            # find children heights
            leftHeight = checkBalance(node.left)
            rightHeight = checkBalance(node.right)
            # return error if imbalanced
            if leftHeight < 0 or rightHeight < 0 or \
                abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1 # next height
```

---

**Source:**

LeetCode:
[Balanced-Binary-Tree](https://leetcode.com/problems/balanced-binary-tree)
