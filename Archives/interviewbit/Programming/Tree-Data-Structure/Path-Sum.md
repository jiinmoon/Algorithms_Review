# Path Sum

    Given a binary tree and a sum, determine if the tree has a root-to-leaf path
    such that adding up all the values along the path equals the given sum.

---

## Approach:

Traverse down to the leaf nodes building the path sum. If the path sum has
reached 0, we have a valid path.

O(n) in time complexity.

---

Python:

```python

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        
        def helper(node, pathSum):

            if not node:
                return False

            pathSum += node.val
            if not (node.left or node.right):
                return pathSum == B

            else:
                left = helper(node.left, pathSum)
                if left: return left

                right = helper(node.right, pathSum)
                if right: return right

                return False
        
        return 1 if helper(A, 0) else 0
```
