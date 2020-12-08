# 543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

---

First, we recursively traverse to bottom of the tree while computing their
distance. At each node, maximum path length span from left to right would be
sum of distance returned from left and right subtrees. We recursively return
their maximum as there can only be a single path upwards.

O(n) in time complexity and space.

---

Python:

```python

class Solution543:

    def diameterOfBinaryTree(self, root):

        def helper(node):
            nonlocal result

            if not node:
                return 0

            leftDist = helper(node.left)
            rightDist = helper(node.right)

            result = max(result, leftDist + rightDist)

            return max(leftDist, rightDist) + 1     # add current node to distance

        result = 0
        helper(root)

        return result
```
