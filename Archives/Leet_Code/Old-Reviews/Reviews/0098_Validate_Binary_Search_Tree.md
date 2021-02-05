98 Validate Binary Search Tree
==============================

Question:
---------

Given a binary tree, determine if it is a valid binary search tree.

Solutions:
----------

We cannot simply apply the definition at each node - we need to remember that
it is a recursive definition. At each node, the value has to be less than the
"maximum" value and greater than "minium" which needs to be tracked as we move
from left and right.

Codes:
------

Python:

```python
class Solution:
    def isValidBST(self, root):
        
        def checkBST(node, minVal, maxVal):
            if not node:
                return True
            if minVal >= node.val or maxVal <= node.val:
                return False
            return self.checkBST(root.left, minVal, root.val) and \
                    self.checkBST(root.right, root.val, maxVal)

        return checkBST(root, float('-inf'), float('inf'))
```

Go:

```go
import "math"

func isValidBST(root *TreeNode) bool {
    return checkBST(root, math.MinInt64, math.MaxInt64)
}

func checkBST(node *TreeNode, min int, max int) bool {
    if root == nil {
        return true
    }
    if root.Val <= min || root.Val >= max {
        return false
    }
    return checkBST(root.Left, min, root.Val) && checkBST(root.Right, root.Val, max)
}
```

---

**Source:**

LeetCode: [Validate-Binary-Search-Tree](https://leetcode.com/problems/validate-binary-search-tree/)
