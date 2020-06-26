""" Rotate Array

Solution:

    There are many ways to approach this problem, but simplest would be to
    reverse the array three times.

"""

class Solution:
    def rotate(self, nums, k):

        def reverse(nums):
            return nums[::-1]

        k = k % len(nums)
        nums.reverse()
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
