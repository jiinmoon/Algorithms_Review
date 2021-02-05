# 1120 Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree
of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The
average value of a tree is the sum of its values, divided by the number of
nodes.)

---

To find the maximum average value starting from any node and its subtree, we
traverse the trees while counting the number of nodes within the node's subtree
and the sum of all the nodes thus far - starting from bottom up fashion.

The time complexity of this algorithm should be of typical DFS traversal on the
binary tree, O(n).

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
