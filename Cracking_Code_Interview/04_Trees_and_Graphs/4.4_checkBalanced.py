""" 4.4 Check Balanced


Question:

    Implement a function to check if a binary tree is balanced. For the purposes
    of this question, a balanced tree is defined to be a tree such that the
    heights of the two subtrees of any node never differ by more than one.

---

The first approach would most likely to be for each node that we visit, we check
the heights of left and right subtrees then compare. But we realize that this
top-down approach would be rather redundant. If we are at root and checking the
heights of left and right subtree, why not compare them on the way up?

Thus, we change it to bottom-up approach where from the leaves, we return its
heights upto the node. While computing for the heights, if at any node we found
inbalance, we can report it.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def _checkHeight(self, root):
        if not root: return None

        leftHeight = self._checkHeight(root.left)
        if leftHeight == -1: return -1
        rightHeight = self._checkHeight(root.right)
        if rightHeight == -1: return -1

        heightDiff = abs(leftHeight - rightHeight)
        if heightDiff > 1:
            return -1 # unbalanced; pass it up
        else:
            return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root):
        return self._checkHeight(root) != Integer.

