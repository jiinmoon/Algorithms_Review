""" 114. Flatten Binary Tree to Linked List

Question:

    Given a binary tree, flatten it to a linked list in-place.

+++

Solution:

    We will traverse to our right, and think about each cases.

    1. node has a right child.

        We can continue to traverse on right.

    2. node has a left child.

        The left subtree should be attached to the right, setting left to be
        None. But this creates a problem if the right already exists. Thus, when
        we check for right child above, we should save the pointer to stack so
        that we can revisit.

    3. otherwise, we can continue to traverse.

"""

class Solution:
    def flatten(self, root):
        stack = []
        while root or stack:
            # case 1: right child?
            if root.right:
                stack.append(root.right)
            # case 2: left child?
            if root.left:
                # we have saved pointer to right previously.
                # safe to move over left subtree to right.
                root.right = root.left
                root.left= None
            root = stack.pop() if stack else root.right
