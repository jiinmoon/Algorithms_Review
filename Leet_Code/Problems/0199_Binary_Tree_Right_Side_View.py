""" 199. Binary Tree Right Side View

Question:

    Given a binary tree, retur nthe values of the nodes you can see from right
    side.

+++

Solution:

    BFS.

"""

class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        result = []
        queue = [ root ]
        while queue:
            m = len(queue)
            result.append(queue[-1].val)
            for _ in range(m):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result
