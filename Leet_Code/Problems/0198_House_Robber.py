""" 198. House Robber

Question:

    Given a list of non-negative integers representing the amount of money each
    house, determine the maximum amount of money you can rob tonight without
    alerting the police.

+++

Solution:

    This problem is best approached by DP. Suppose that we are at any arbitary
    house at i, then what is the total profit that can be made upto this point?

    This depends on the choices that we could have made upto this point. At each
    house, we can either choose the rob the house, or skip it. Hence, the
    maximum profit made at each house i would be max between choosing robbing
    i-2th house + current house, or choosing to skip current and carry over
    i-1th house profit over.

"""

class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        m = len(nums)
        if m == 1:
            return nums[0]
        maxThusFar = [0] * m
        maxThusFar[0], maxThusFar[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, m):
            maxThusFar[i] = max(maxThusFar[i-2] + nums[i], maxThusFar[i-1])
        return maxThusFar[-1]
