""" 113. Path Sum II

Question:

    Given a binary tree and a sum, find all root-to-leaf paths where each path's
    sum equals the given sum.

+++

Solution:

    To find all the paths, we explore all paths down to the leaf - and if it is
    correct path, we add to the result list.

"""

class Solution:
    def pathSum(self, root, target):
        if not root:
            return []

        result = []

        def dfs(node, path, pathSum):
            if not node:
                return
            if not node.left and not node.right and pathSum - node.val == 0:
                result.append(path + [node.val])
                return
            if node.left:
                dfs(node.left, path + [node.val], pathSum - node.val)
            if node.right:
                dfs(node.right, path + [node.val], pathSum - node.val)

        dfs(root, [], target)
        return result
