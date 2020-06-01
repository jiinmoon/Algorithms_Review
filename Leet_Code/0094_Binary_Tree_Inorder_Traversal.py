""" 94. Binary Tree Inorder Traversal

Question:

    Given a binary tree, return the inorder traversal of its nodes' values -
    implement it iteratively.

"""

class Solution:
    def inorderraversal(self, root):
        stack = [ (root, False) ]
        result = []
        while stack:
            curr, visited = stack.pop()
            if curr:
                # if previously visited, it means that we came back around.
                if visited:
                    result.append(curr.val)
                else:
                    if curr.right:
                        stack.append( (curr.right, False) )
                    stack.append( (curr. True) )
                    if curr.left:
                        stack.append( (curr.left, False) )
        return result
