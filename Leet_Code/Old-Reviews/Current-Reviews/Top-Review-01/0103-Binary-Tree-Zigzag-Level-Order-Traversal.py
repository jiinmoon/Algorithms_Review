# 103 Binary Tree Zigzag Level Order Traversal

class Solution:
    def zigzagTraversal(self, root):
        if not root:
            return []

        res = list()
        q = [root]
        flip = False

        while q:
            if flip:
                res.append([node.val for node in q[::-1]])
            else:
                res.append([node.val for node in q])
            flip = not flip
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp

        return res
