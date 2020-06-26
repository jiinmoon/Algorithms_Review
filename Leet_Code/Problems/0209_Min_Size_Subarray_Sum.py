""" 209. Min Size Subarry Sum

Question:

    Given an array of n positive integers and a positive integer s, find the
    minimal length of a contiguous subarray of which the sum >= s.

+++

Solution:

    Simply, we iterate on the array, while computing the current sum. When the
    current sum value goes over the given integer s, then we know that we have a
    candidate for minimal length subarray sum. Thus, we start to take the value
    from the left side, until current sum >= s.

"""

class Solution:
    def minSizeSubarraySum(self, nums, s):
        currSum = left = 0
        minLenThusFar = float('-inf')
        for right in range(len(nums)):
            # build current sum.
            currSum += nums[right]
            # if currSum >= s, start to take value away from left.
            while currSum >= s:
                minLenThusFar = min(minLenThusFar, r - l + 1)
                currSum -= nums[left]
                left += 1
        return minLenThusFar if minLenThusFar > 0 else 0
