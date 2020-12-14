# Valid Binary Search Tree

Given a root of binary tree, check whether it is valid BST.

---

Recursively check for each node to be within the range of minmum and maximum
value. Min value is updated when we move to right, and max value is updated
when we move to left.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isValidBST(self, root):

        def _check(node, minVal, maxVal):

            if not node:
                return True

            if node.val <= minVal or node.val >= maxVal:
                return False

            return _check(node.left, minVal, node.val) and _check(node.right, node.val, maxVal)

        return 1 if _check(root, float('-inf'), float('inf') else 0

```
