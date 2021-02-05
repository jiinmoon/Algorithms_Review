# 297 Serialize and Deserialize Binary Tree
#
# Utilize any tree traversal - use same to restore.

class Solution:
    def serialize(self, root):
        def helper(node):
            if not node:
                res.append("null")
                return
            res.append(int(node.val))
            helper(node.left)
            helper(node.right)

        res = list()
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper():
            if not data:
                return
            curr = TreeNode(int(data.pop()))
            curr.left = helper()
            curr.right = helper()
            return curr

        data = data.split(",")[::-1]
        return helper()

