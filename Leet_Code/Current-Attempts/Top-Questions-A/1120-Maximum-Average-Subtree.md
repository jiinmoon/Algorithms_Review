# 1120 Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree
of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The
average value of a tree is the sum of its values, divided by the number of
nodes.)

---

We may perform a traversal on the tree; and from bottom up, we return the
current count of the nodes as well as sum of the nodes along the path.

---

Python:

```python

class Solution:
    def maxAverageSubtree(self, root):
        def helper(node):
            if not node:
                return 0, 0
            lcount, lsum = helper(node.left)
            rcount, rsum = helper(node.right)
            currCount = 1 + lcount + rcount
            currSum = node.val + lsum + rsum
            self.maxAvg = max(self.maxAvg, currSum / currCount)
            return currCount, currSum

        self.maxAvg = 0
        helper(root)
        return self.maxAvg
```
