# 1120 Maximum Average Subtree

Recursively travel downwards - from leaf, we return the sum of all nodes path
and the count of the nodes thus far. Update the maximum average on each node.

---

Python:

```python

class Solution:
    def maxAverageSubtree(self, root):
        def helper(node):
            if not node:
                return 0, 0
            lCount, lSum = helper(node.left)
            rCount, rSum = helper(node.right)
            currCount = 1 + lCount + rCount
            currSum = node.val + lSum + rSum
            self.maxAvg = max(self.maxAvg, currSum / currCount)
            return currCount, currSum

        self.maxAvg = 0
        helper(root)
        return self.maxAvg
```
