""" 31. Next Permutation

Question:

    Implement next permutation, which rearranges numbers into the
    lexicographically next greater permutation of numbers.

+++

Solution:

    We see that once the segment is in decending order, then next permutation is
    the reverse of the segment. Thus, we should check for where in the given
    list of integers, the decending order is broken. If it is present, then the
    next permutation is the reverse of the segment starting from itself - but
    only with the value swapped to higher value.

"""

class Solution:
    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1; end -= 1

    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1)
