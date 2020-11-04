# 124. Binary Tree Max Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

---

We can first recursively traverse all the way down to the leaf of the tree.
From here, at each node, we return the max path sum found from its subtrees
that "includes the current node" or without the current node. This is because
we have a case where the path can "go through" the current node from left and
continue on down to the right. So, we need to maintain the path sums found thus
far from its left and right subtree, and compute the current sum that includes
and excludes the current.

Hence, at each node, we return "include" and "exclude" path sum. Then, these
values are examined for left and right. Then, current path sum that "includes"
the current sum would be the maximum sum that either includes the downward path
from left and right and current node value, OR either of the previous left or
right path sum that have included in the previous. The current sum that
"excludes" would be simply the current node value plus the maximum of the
either left or right path sum that have been excluded thus far.

Note the case of negative values - hence, use maximum.

This algorithm should complete in O(n).

---

Python:

```python

class Solution:
    def maxPathSum(self, root):
        def helper(node):
            # return include and exclude path sum
            if not node:
                return float('-inf'), 0
            lWith, lDown = helper(node.left)
            rWith, rDown = helper(node.right)
            currWith = max(node.val + max(0, lDown) + max(0, rDown), lWith, rWith)
            currDown = node.val + max(0, lDown, rDown)
            return currWith, currDown

        return helper(root)[0]
```
