""" 145. BT Postorder Traversal

Question:

    Given a binary tree, return the postorder traversal of its nodes' values.

+++

Solution:

    Reminder: given tree [1, 2, 3, null, null, 4, 5], the post order on it
    should be [2, 4, 5, 3, 1].

    Maintain visited - it will be used to gauge when we visit the node the
    second time, meaning that we can safely add the node out of the loop and to
    the result.

"""

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        stack [ (root, False) ]
        while stack:
            curr, visited = stack.pop()
            if visited:
                result.append(curr.val)
                continue
            else:
                stack.append( (curr, True) )
                if curr.right:
                    stack.append( (curr.right, False) )
                if curr.left:
                    stack.append( (curr.left, False) )
        return result
