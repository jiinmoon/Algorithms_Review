""" 116. Populating Next Right Pointers in Each node

Question:

    Given a perfect binary tree where all leaves are on the same level, and
    every parent has two children, populate each next pointer to point to its
    next right node.

"""

class Solution:
    def connect(self, root):
        if not root:
            return

        queue = [ root ]
        while queue:
            nextDepth = []
            while queue:
                curr = queue.pop(0)
                curr.next = queue[0] if queue else None
                # this is perfect binary tree; gurantee'd two children.
                if curr.left:
                    nextDepth.append(curr.left)
                    nextDepth.append(curr.right)
            queue = nextDepth
        return root

