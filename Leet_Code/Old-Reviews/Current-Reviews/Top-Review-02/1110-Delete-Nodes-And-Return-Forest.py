# 1110 Delete Nodes And Return Forest

class Solution:
    def deleteNode(self, root, toDelete):
        def helper(node, hasParent):
            if not node:
                return
            delete = node in toDelete
            if not hasParent and not delete:
                res.append(node)
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return node if not delete else None

        toDelete = set(toDelete)
        res = list()
        helper(root, False)
        return res
