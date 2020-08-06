""" 189. Rotate Array """

class Solution:
    def rotate(self, nums, k):
        def reverse(nums):
            return nums[::-1]
        k = k % len(nums)
        nums = nums[::-1]
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])

