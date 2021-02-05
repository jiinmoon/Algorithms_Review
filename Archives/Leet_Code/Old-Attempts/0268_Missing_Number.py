""" 268. Missing Number

Question:

    Given an array containing n distinct numbers taken from 0, 1, 2, .., n, find
    the one that is missing from the array.

"""

class Solution:
    def missingNumber(self, nums):
        numSum = sum(nums)
        expectedSum = sum([for i in range(len(nums) + 1)])
        return expectedSum - numSum
