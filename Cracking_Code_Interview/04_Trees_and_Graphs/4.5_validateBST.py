""" 4.5 Validate BST


Question:

    Implement a function to check if a binary tree is a binary search tree.

---

This is a rather theoretical question on the BST - that what is the precise
definition of the BST and whether the given BT fits the description.

Remember that BST is also BT, which means that the recursive definition should
hold true for every node. When we mean by BST, it is a BT where for each parent
node, the values in the left-sbutree has all the values less than its parent,
and the values to the right-substree has all the values greater than its parent.

The first suboptimal way to check would be perform in-order traversal on the
given binary tree. Store the information on extra structure such as list, then
confirm whether the list is in order. While the idea is very simple and easy to
implement, in terms of both spatial and time complexity, it is suboptimal.

To improve upon, we have to return to the recursive definition of the BST. For
every node that we visit, we check whether its value is within the range that
conforms to be a BST. There is however a small pitfall in thinking that it is as
simple as confirming left child's value and right child's value to the current
node. For example, we can have a node down the line that is in prefect range
within its direct parent, but out of bounds for its grand parents.

Thus, we need to maintain min/max variable while going through the tree to check
the node. Whenever we are going in left subtree, we also has to check whether
the node is under max variable.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _checkBST(self, node, minimum, maximum):
        if not node: return True

        # check whether node is within bound.
        if (minimum and node.val <= minimum) or
            (maximum and node.val > maximum):
                return False

        # going left? max needs to be updated
        # vice versa on right
        if (!self._checkBST(node.left, minimum, node.val)) and
            (!self._checkBST(node.right, node.val, maximum)):
                return False

        return True

    def checkBST(self, root):
        return self._checkBST(root, None, None)

