""" 213. House Robber II

Solution:

    This time, the houses are arranged in the circle; but this does not change
    the set up very much as we only have to iterate on the circle twice. First
    time, we skip the first house; second time, we simply stop before the last
    house.

"""

class Solution:
    def rob(self, nums):
        n = len(nums)
        if not n:
            return 0
        # tricky exception; remember this is a circle.
        if n <= 3:
            return max(nums)

        def findMax(houses):
            # instead of DP array, we simply maintain profits from previous.
            prev, curr = 0, 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return max(prev, curr)

        return max(findMax(nums[1:]), findMax(nums[:-1]))
