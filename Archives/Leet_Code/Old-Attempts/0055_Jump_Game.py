""" 55. Jump Game

Question:

    Given an array of non-negative integers, you are initially positioned at the
    first index of the array.

    Each element in the array represents your max jump length at that position.

    Determine if you are able to reach the last index.

+++

Solution:

    We can simply iterate on the array to see whether we can reach the end. That
    is, the max jump position reachable is determined by the current value and
    the index.

"""

class Solution:
    def canJump(self, nums):
        m = len(nums)
        currPos = m - 1
        for i in range(m-1, -1, -1):
            if i + nums[i] >= currPos:
                currPos = i
        return not currPos
