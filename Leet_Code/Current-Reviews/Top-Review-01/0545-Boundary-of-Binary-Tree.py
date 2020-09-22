# 545 Boundary of Binary Tree

class Solution:
    def boundary(self, root):
        def traverseLeft(node):
            if not node or not (node.left and node.right):
                return
            lBound.append(node.val)
            if node.left:
                traverseLeft(node.left)
            else:
                traverseLeft(node.right)

        def traverseInorder(node):
            if not node:
                return
            traverseInorder(node.left)
            if not (node.left and node.right):
                lBound.append(node.val)
            traverseInorder(node.right)

        def traverseRight(node):
            if not node and not (node.left and node.right):
                return
            rBound.append(node.val)
            if node.right:
                traverseRight(node.right)
            else:
                traverseLeft(node.left)

        if not root:
            return []

        lBound, rBound = [root.val], []
        self.traverseLeft(root.left)
        self.traverseInorder(root.left)
        self.traverseInorder(root.right)
        self.traverseRight(root.right)

        return lBound + rBound[::-1]
