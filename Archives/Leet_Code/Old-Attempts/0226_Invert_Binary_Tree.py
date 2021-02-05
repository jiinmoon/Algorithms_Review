""" 226. Invert Binary Tree """

class Solution:
    def invertTree(self, root):
        # at each node, we receive left and right childs.
        # then, attach them to current node's left and right swapped.
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
