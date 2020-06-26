""" 112. Path Sum

Question:

    Given a binary tree and a sum, determine if the tree has a root-to-leaf path
    such that adding up all the values along the path equals the given sum.

"""


class Solution:
    def hasPathSum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right and root.val == target:
            return True
        return self.hasPathSum(root.left, target - root.val) or \
                self.hasPathSum(root.right, target - root.val)
