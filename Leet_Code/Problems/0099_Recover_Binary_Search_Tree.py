""" 99. Recover Binary Search Tree

Question:

    Two elements of a binary search tree are swapped by a mistake - recover the
    tree without changing the structure.

+++

Solution:

    We will simply traverse on the tree to find the two nodes which are out of
    place, then swap their values.

"""

class Solution:
    def recoverTree(self, root):
        faultyNodes = []

        # traverse and find two out of place nodes.
        # in-order traversal on BST should be sorted order.
        def findFaultyNodes(curr, last):
            # continue traversing on left.
            if curr.left:
                last = findFaultyNodes(curr.left, last)
            # out of order.
            if last.val > curr.val:
                # is it first one or second one?
                if faultyNodes:
                    faultyNodes[1] = curr
                else:
                    faultyNodes += [last, curr]
            last = curr
            if curr.right:
                last = findFaultyNodes(curr.right, last)
            return last

        findFaultyNodes(root, TreeNode(float('-inf')))
        first, second = faultyNodes[0], faultyNodes[1]
        first.val, second.val = second.val, first.val

