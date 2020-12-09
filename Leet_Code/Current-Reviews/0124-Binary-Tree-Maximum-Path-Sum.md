# 124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting
node to any node in the tree along the parent-child connections. The path must
contain at least one node and does not need to go through the root.

---

We recursively traverse to left and right subtrees down to the bottom. From
here one, we return the maximum path sum from left and right subtree while
recording the current maximum path sum. When we are returning, it should be
maximum path sum from either left or right as it should be linear path upwards.

This would be O(n) in both time and space complexity.

---

Java:

```java

class Solution124 {

    private int result = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root)
    {
        helper(root);

        return this.result;
    }

    private int helper(TreeNode node)
    {
        if (Objects.isNull(node))
            return 0;

        int leftSum = helper(node.left);
        int rightSum = helper(node.right);

        this.result = Math.max(this.result, leftSum + rightSum + node.val);

        return Math.max(Math.max(leftSum, rightSum) + node.val, 0);
    }
}

```

Python:

```python

class Solution124:

    def maxPathSum(self, root):
        
        result = float('-inf')

        def helper(node):
            nonlocal result

            if not node:
                return 0

            l, r = helper(node.left), helper(node.right)
            result = max(result, l + r + node.val)
            return max(max(l, r) + node.val, 0)

        helper(root)

        return result
```
