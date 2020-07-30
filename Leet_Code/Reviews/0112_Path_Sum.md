112 Path Sum
============

Question:
---------

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Solutions:
----------

We will traverse down the given binary tree until we have reached the leaf
node - and we will maintain the new sum where we will take away the current
node's value. If the current node is leaftnode and sum is 0, then we know that
it is the path and binary tree does have a path. This is a linear time
algorithm O(n) as we are exploring all paths.

Codes:
------

Python:

```python
class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        sum -= root.val
        if not sum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, sum) or \
                self.hasPathSum(root.right, sum)

```

---

**Source:**

LeetCode: [Path-Sum](https://leetcode.com/problems/path-sum)
