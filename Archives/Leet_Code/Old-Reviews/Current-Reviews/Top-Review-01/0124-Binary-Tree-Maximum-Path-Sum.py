# 124 Binary Tree Maximum Path Sum
#
# We recursively traverse down to the leaf and start to compute the max path
# sum that include the current node or without.
#
# if the path goes through the current node and connects to the other side, it
# has to include the downward path from left and right as well as node itself
# - otherwise, it is the maximum of either previous path sums.
#
# the current max path sum downward is the max of left and right plus itself.

class Solution:
    def maxPathSum(self, root):
        def helper(node):
            if not node:
                return float('-inf'), 0

            lInclude, lDown = helper(node.left)
            rInclude, rDown = helper(node.right)

            currInclude = max(node.val + max(0, lDown) + max(0, rDown), lInclude, rInclude)
            currDown = node.val + max(0, lDown, rDown) 

            return currInclude, currDown

        return helper(root)[0]
