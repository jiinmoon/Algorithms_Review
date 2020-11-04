# 543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

---

Using bottom up recursion, we traverse down all the way to the leaf node. From
here, we start to compute the length of the path. Then, at each node, the
maximum path length can be computed as a sum of the returned value from left
and right childs. Time complexity should be O(n).

---

Python:

```python

class Solution:
    def diameterOfBinaryTree(self, root):
        def helper(node):
            if not node: return -1
            # + 1 for offset leaf -1
            leftPathLen = helper(node.left) + 1
            rightPathLen = helper(node.right) + 1
            self.result = max(self.result, leftPathLen + rightPathLen)
            return max(leftPathLen, rightPathLen)

        self.result = 0
        helper(root)
        return self.result
```
