# Check Subtree of Another
#
# Question:
#
# Given two binary trees, check if the first tree is subtree of the second one.
# A subtree of a tree T is a tree S consisting of a node in T and all of its
# descendants in T. The subtree corresponding to the root node is the entire
# tree; the subtree corresponding to any other node is called a proper subtree.
#
# ---
#
# Attempt:
#
# One approach to this problem is perform recursive traversal on the given tree
# S. At each node, we traverse downwards to confirm whether they are same
# - which confirms that T is a subtree of S. As we need to perform traversal on
# every single node again, the time complexity is O(m * n) where m and n are
# sizes of the given trees.
#
# To make improvement, we need to trade off our space. First, we create
# a string representation of both of the trees. Then, we check for substring
# match. This requires O(m + n) in space, but search process can complete in
# O(m + n) as well.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def isSame(self, p, q):
    if not (p and q):
        return p == q
    if p.val != q.val:
        return False
    return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

def isSubtreeRecur(self, S, T):
    if not S:
        return False
    return self.isSame(S, T) or self.isSubtree(S, T.left) or self.isSubtree(S, T.right)

def isSubtreeIter(self, S, T):
    def serialize(node, result):
        if not node:
            result.append("None")
            return
        result.append(str(node.val))
        serialize(node.left, result)
        serialize(node.right, result)

        serialS, serialT = [], []
        serialize(S, serialS)
        serialize(T, serialT)

        return serialS in serialT
