124 Binary Tree Maximum Path Sum
================================

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

---

The problem is that we cannot simply perform a traversal that only considers
going downwards to the leaf - we also need to consider all the returned values
of the children as well.

So, we design a recursive traversal that at each node, we compute the maximum
path sum that either includes the current node on its path (through left and
right children), or simply passes through the nodes' children to either left or
right.

---

Python:

```python

class Solution:
    def maxPathSum(self, root):
        def helper(node):
            # node.val can be negative
            if not node: return float('-inf'), 0

            lWith, lDown = helper(node.left)
            rWith, rDown = helper(node.right)

            # "with" means max of path that either includes current and/or move
            # down to left or right; or max path sum found on previous "with"s.
            currWith = max(node.val + max(0, lDown) + max(0, rDown), lWith, rWith)

            # "down" means simple max path sum downwards from curr to left or right
            currDown = node.val + max(0, lDown, rDown)

            return currWith, currDown

        return helper(node)[0]
```

