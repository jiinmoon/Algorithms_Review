""" 102. Binary Tree Level Order Traversal

Question:

    Given a binary tree, retur nthe level order traversal of its nodes values.

"""

class Solution:
    def levelOrder(self, root):
        # BFS.
        if not root:
            return []

        result = []
        queue = [ root ]
        while queue:
            m = len(queue)
            result.append(queue.copy())
            for _ in range(queue):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
