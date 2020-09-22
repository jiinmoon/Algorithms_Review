# 53 Maximum Subarray
#
# We can maintain the maximum sum value as we iterate on the each element. The
# problem is the negative values that needs to be accounted for. For this, we
# maintain another variable that takes the maximum of itself plus the value or
# the value. This is account for the negative integers encountered  - and
# should the sum go negative, it will break the subarray and start from the new
# value.

class Solution:
    def maxSubarray(self, nums):
        currSum = float('inf')
        totalSum = 0
        for num in nums:
            currSum = max(currSum + num, num)
            totalSum = max(totalSum, currSum)
        return totalSum
