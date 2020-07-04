""" 31. Next Permutation

Question:

    Given a sequence of integers, find its next logical permutation.

+++

Solution:

    The naive approach would be to simply generate all the permutations, and
    find the n+1 permutation. However, the there is a way to find the next
    permutation in better fashion.

    We start by noticing that the next permutation for the sequence of
    intergers which are ordered backwards has to be the reverse. This gives us
    an idea that we should first check for whether the array is in sorted
    order. If it is then we reverse the array. However, we may encounter an out
    of place element, this is the indicator where its next permutation would
    have this value decremented with next value that is lower than it within
    the range where we have found the out-of-place element.

    Thus, we have our algorithm. First, we iterate from behind to find the
    first out of place element (the array should be in decending order). If
    found, then we find its next greater value from behind again. Swap the two
    elements. Then reverse the array.

"""

class Solution:
    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        m = len(nums)
        i = m - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = m - 1
            while j > 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i+1)
