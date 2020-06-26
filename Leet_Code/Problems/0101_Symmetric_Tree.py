""" 101. Symmetric Tree

Question:

    Given a binary tree, check whether it is a mirror of itself.

"""

class Solution:
    def isSymmetric(self, root):
        if not root:
            return

        def checkSymmetric(p, q):
            if not p or not q:
                return p == q
            if p.val != q.val:
                return False
            return checkSymmetric(p.right, q.left) and \
                    checkSymmetric(p.left, q.right)

        return checkSymmetric(root.left, root.right)
