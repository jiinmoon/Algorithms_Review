""" 103. Binary Tree ZigZag Level Order Traversal

Question:

    Given a binary tree, return the zigzag level order traversal of its noes'
    values.

"""

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [ root ]
        flip = False
        while queue:
            m = len(queue)
            if flip:
                result.append(queue.copy()[::-1])
            else:
                result.append(queue.copy())
            flip = ~flip
            for _ in range(m):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
