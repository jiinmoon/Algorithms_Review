""" 4.6 Successor


Question:

    Write an algorithm to find the next node (in-order successor) of a given
    node in a BST. You may assume that each node has a link to its parent.

---

The question would have been a bit more complicated if we do not have a link to
its parent, but since we do we can think of few cases to how to handle this.

We may think that when we say in-order successor of a given node, we generally
understand as its right-child. But what if we have more than a single child, but
entire tree? Then we have to look for left-most child of the right subtree.

But what if the right subtree does not exist for the given node? Then, we will
have to visit up to the parents where we are on the first left subtree instead
of right subtree. This parent value would be the next successor.

If we do not have an access to parent node directly, then we have to perform a
traversal down the given node while keeping track of the parent that we are
going left of, instead of right; then return that parent's value.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _leftMostChild(self, node):
        if not node: return None
        while node.left:
            node = node.left
        return node

    def inorderSuccessor(self, node):
        if not node: return None

        # if right child is present, return leftmost child or right subtree.
        if node.right:
            return self._leftMostChild(node)
        else:
            # no right subtree.
            # move up until we are on the left side instead of right.
            q = node
            x = q.parent
            while x != None and x.left != q:
                q = x
                x = x.parent
            return x

