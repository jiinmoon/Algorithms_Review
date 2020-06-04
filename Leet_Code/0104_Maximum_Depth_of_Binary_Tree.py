""" 104. Maximum Depth of Binary Tree

Question:

    Given a binary Tree, find its maximum depth.

"""

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
