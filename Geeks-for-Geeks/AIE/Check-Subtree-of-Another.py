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
# One appraoch to this problem is perform recursive traversal on the given tree
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

class 
