# 53 Maximum Subarray

class Solution:
    def maxSubarray(self, nums):
        maxSum = float('-inf')
        currSum = 0
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum

