""" 124. Binary Tree Maximum Path Sum

Question:

    Given a non-empty binary tree, find the maximum path sum.

+++

Solution:

    Here, the path is not simply from root to leaf, but any path along the
    parent to child connections. To compute this, we will break down what needs
    to happen at each node as we traverse.

    Firstable, at each node that we visit, we need to compute the maximum path
    sum. The max path sum should be a global variable that is maintained
    throughout, where at each node should be compared against the current path
    sum that is leftMax + rightMax + node.value.

    We need to compute the current max through the node - but we can have a
    previously computed max that is below 0 - due to having negative values in
    the nodes. Thus, it is necessary to compare the values against 0.

"""

class Solution:
    def maxPathSum(self, root):
        maxSum = [float('-inf')]

        def dfs(node):
            if not node:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            maxSum[0] = max(maxSum[0], leftSum + rightSum + node.val)
            currMax = max(leftSum, rightSum, 0) + node.val
            return max(currMax, 0)

        dfs(root)
        return maxSum[0]
