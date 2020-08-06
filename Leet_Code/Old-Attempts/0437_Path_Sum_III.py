""" 437. Path Sum III

Question:

    Given a binary tree, find the number of paths tha tsum to a given value.

+++

Solution:

    This is a much tricker question, where path does not have to begin at root
    nor end at the leaf. The naive approach would be to perform DFS at each node
    to see how far we can go - to see whether we can generate a path. This
    O(n^2) approach can be improved further using memoization technique, as we
    explore the paths, there is a chance that we have seen the values in
    previous iterations.

    Another approach is think about root to any node path sum. If there was a
    solution within this path, then it must be that there have been old
    root-to-node path sum that (current sum - old sum) which is the target.

"""

class Solution:
    def pathSumIII(self, root, target):
        pathCount = 0
        memo = { 0:1 }

        def backtrack(node, currPathSum):
            if not node: return
            currPathSum += node.val
            oldPathSum = currPathSum - target
            # how many times have we seen oldPathSum in this path?
            pathCount += memo.get(oldPathSum, 0)
            # update memor for next traversal.
            memo[currPathSum] = memo.get(currPathSum, 0) + 1
            # next.
            backtrrack(node.left, currPathSum)
            backtrack(node.right, currPathSum)
            # we are now on another branch at this point.
            # cannot have currPathSum since it is not there.
            memo[currPathSum] -= 1

        backtrack(root, 0)
        return pathCount
