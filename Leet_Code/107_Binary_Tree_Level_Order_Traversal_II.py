""" 107. Binary Tree Level Order Traversal II

Question:

    Given a binary tree, return the bottom-up leve order traversal of its nodes'
    values.

"""

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        result = []
        queue = [ root ]
        while queue:
            m = len(queue)
            result.append(queue.copy())
            for _ in range(m):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result[::-1]
