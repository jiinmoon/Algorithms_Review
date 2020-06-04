""" 111. Minimum Depth of Binary Tree

Question:

    Given a binary Tree, find its minimum depth.

+++

Solution:

    We use BFS to find the shortest path to the closest leaf node.

"""

class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        queue = [ root ]
        depth = 0

        while queue:
            depth += 1
            m = len(queue)
            for _ in range(m):
                curr = queue.pop(0)
                if not curr.left and not curr.right:
                    return depth
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

