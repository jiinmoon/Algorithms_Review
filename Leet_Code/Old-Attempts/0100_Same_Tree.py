""" 100. Same Tree

Question:

    Given two binary trees, write a function to check if they are the same or
    not.

"""

class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)
