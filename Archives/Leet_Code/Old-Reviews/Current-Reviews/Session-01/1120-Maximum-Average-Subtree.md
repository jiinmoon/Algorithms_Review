1120 Maximum Average Subtree
============================

Given the root of a binary tree, find the maximum average value of any subtree
of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The
average value of a tree is the sum of its values, divided by the number of
nodes.)

---

Simply, we will iterate on the tree using dfs - at each node, we will retrieve
the total number of nodes and sum from its left and right subtree to compute
the current average. Maintain a global maximum average as we iterate on the
tree.

---

Python:

```python
class Solution:
    def maximumAverageSubtree(self, root):
        self.maxAvg = 0

        def dfs(node):
            if not node:
                return (0, 0)
            lNodeSum, lNodeCount = dfs(node.left)
            rNodeSum, rNodeCount = dfs(node.right)
            currNodeSum = lNodeSum + rNodeSum + node.val
            currNodeCount = lNodeCount + rNodeCount + 1
            currAvg = currNodeSum / currNodeCount
            self.maxAvg = max(self.maxAvg, currAvg)
            return (currNodeSum, currNodeCount)

        dfs(root)
        return self.maxAvg
```

