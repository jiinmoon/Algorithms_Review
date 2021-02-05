""" 110. Balanced Binary Tree

Question:

    Given a binary tree, determine if it is height balanced.

"""

class Solution:
    def isBalanced(self, root):
        if not root:
            return True

        def checkBalance(node):
            if not node:
                return 0
            leftHeight = checkBalance(node.left)
            rightHeight = checkBalance(node.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight -
                    rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1

        return checkBalance(root) != -1
