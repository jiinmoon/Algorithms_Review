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

Java:

```java

class Solution {
    
    private int result = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        helper(root);
        return this.result;
    }

    public int helper(TreeNode node) {
        if (node == null) return 0;
        
        // ignore negative values;
        int leftSum = Math.max(0, helper(node.left));
        int rightSum = Math.max(0, helper(node.right));
        this.result = Math.max(this.result, node.val + leftSum + rightSum);
        int currSum = Math.max(Math.max(leftSum, rightSum) + node.val, 0);

        return currSum;
    }
}

```

Java:

```java

class Solution {
    
    static class Pair {
        private int with, down;

        public Pair(int with, int down) {
            this.with = with;
            this.down = down;
        }
    }

    public int mathPathSum(TreeNode root) {
        Pair result = helper(root);
        return result.with;
    }

    private Pair helper(TreeNode node) {
        if (node == null)
            return new Pair(Integer.MIN_VALUE, 0);

        Pair lPair = helper(node.left);
        Pair rPair = helper(node.right);
        int cWith = Math.max(
                        Math.max(
                            node.val + Math.max(0, lPair.down) + Math.max(0, rPair.down), 
                            lPair.with), 
                        rPair.with);
        int cDown = node.val + 
                        Math.max(
                            Math.max(0, lPair.down),
                            rPair.down);

        return new Pair(cWith, cDown);
    }
}

```

Python:

```python

class Solution:
    def maxPathSum(self, root):
        self.result = float('-inf')

        def helper(node):
            # return include and exclude path sum
            if not node:
                return 0
            l = max(0, helper(node.left))
            r = max(0, helper(node.right))
            self.result = max(self.result, l + r + node.val)
            currSum = max(max(l, r) + node.val, 0)
            return currSum
        
        helper(root)
        return self.result
```
