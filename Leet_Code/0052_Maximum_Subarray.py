""" 52. Maximum Subarray

Question:

    Given an integer array nums, find the contiguous subarray which has the
    largest sum and return its sum.

"""

class Solution:
    def maxSubarray(self, nums):
        maxThusFar = currMax = nums[0]
        for num in nums[1:]:
            currMax = max(currMax + num, num)
            maxThusFar = max(currMax. maxThusFar)
        return maxThusFar
