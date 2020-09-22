# 102 Binary Tree Level Order Traversal

class Solution:
    def levelOrderTraversal(self, root):
        if not root:
            return []

        q = [ root ]
        res = list()
        while q:
            res.append(q.copy())
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp

        return res
