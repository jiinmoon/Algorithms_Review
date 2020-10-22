# 1120 Maximum Average Subtree

To find the maximum average value starting from any node and its subtree, we
traverse the trees while counting the number of nodes within the node's subtree
and the sum of all the nodes thus far - starting from bottom up fashion.

---

Python:

```python

class Solution:
    def maxAverageSubtree(self, root):
        def helper(node):
            if not node: return 0, 0

            lsum, lcount = helper(node.left)
            rsum, rcount = helper(node.right)
            currSum = node.val + lsum + rsum
            currCount = lcount + rcount + 1
            self.result = max(self.result, currSum // currCount)

            return currSum, currCount
       
        self.result = 0
        helper(root)

        return self.result
```
