""" 236. LCA of a Binary Tree

Solution:

    To find the Lowest Common Ancestor, we would perform recursive traversal on
    the binary tree; and when we encounter either given nodes, we can return
    that node up. And at each node, this will happen on node's left and right
    subtree. And when we both have left and right subtrees returning a node,
    then we know that current node is the lowest common ancestor as two nodes
    have been found on both sides. Otherwise, we simply return whichever node
    that we have found.

"""

class Solution:
    def findLCA(self, root, p, q):
        # base case: root exists and is it p or q?
        if root in (None, p, q):
            return root
        left = self.findLCA(root.left)
        right = self.findLCA(root.right)
        return root if left and right else left or right
