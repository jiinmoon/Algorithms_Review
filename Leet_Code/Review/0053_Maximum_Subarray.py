""" 53. Maximum Subarray

Question:

    Given an integer nums, find the contiguous subarray (containing at least
    one number) which has the largest sum and return its sum.
    
+++

Solution:

    The naive approach would be to explore all possible contiguous subarraies
    to find the largest sum. However, we can simply iterate while maintaining
    a largestThusFar and compare against the current sum. Current growing 
    contiguous subarray can either grow further by adding the current value, or
    start a new subarray.

"""

class Solution:
    def maxSubarray(self, nums):
        if not nums:
            return 0
        largestThusFar = float('-inf')
        currSum = 0
        for num in nums:
            currSum = max(currSum + num, num)
            largestThusFar = max(curSum, largestThusFar)
        return largestThusFar

