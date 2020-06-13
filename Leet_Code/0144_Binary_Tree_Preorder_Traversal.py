""" 144. Binary Tree Preorder Traversal """

class Solution:
    def preorderTraversal(self, root):
        # recursive solution is trivial; iterative approach using DFS.
        if not root:
            return []
        result = list()
        stack = [ root ]
        while stack:
            currNode = stack.pop()
            result.append(currNode.val)
            # iterative process; right node will pop later than left!
            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return result
