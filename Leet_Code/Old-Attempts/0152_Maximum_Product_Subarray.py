""" 152. Maximum Product Subarray

Question:

    Given an integer array nums, find the contiguous subarray within an array
    which has the largest product.

+++

Solution:

    The main problem is that unlike maximum sum, we may encounter sequence of
    negatives that can still potentially produce the maximum product subarray.
    Hence, the candidates to consider would be not only the current value, but
    maximum product we seen thus far as well as minimum product.

"""

class Solution:
    def findMaxProduct(self, nums):
        result = maxThusFar = minThusFar = nums[0]
        for num in nums[1:]:
            candidates = [ num, maxThusFar * num, minThusFar * num ]
            maxThusFar = max(candidates)
            minThusFar = min(candidates)
            result = max(result, maxThusFar)
        return result
