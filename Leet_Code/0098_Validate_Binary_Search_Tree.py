""" 98. Validate Binary Search Tree

Question:

    Given a binary tree, check whether it is a valid binary search tree.

+++

Solution:

    The definition of the binary search is recursive - which means that we
    cannot simply check against the parent's value against the childrens; but
    also consider their max and mins of the ancestors.

"""

class Solution:
    def isValidBST(self, root):
        def checkBST(node, minVal, maxVal):
            if not node:
                return True
            if node.val <= minVal or node.val >= maxVal:
                return False
            return checkBST(node.left, minVal, node.val) and \
                    checkBST(node.right, node.val, maxVal)
        return checkBST(root, float('-inf'), float('inf'))
