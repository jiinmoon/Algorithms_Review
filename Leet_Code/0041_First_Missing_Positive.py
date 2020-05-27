""" 41. First Missing Positive

Question:

    Given an unsorted integer array, find the smallest missing positive integer.

+++

Solution:

    The first missing positive by definition has to be within the length of the
    array. Then, we may utilize the indicies of the array as an indicator of
    elements present within the array.

"""

class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        nums.append(0) # avoid zero index.
        for i, num in enumerate(nums):
            while num != 'X' and num > 0 and num < len(nums):
                nums[num], num = 'X', nums[num]

        for i in range(1, len(nums)):
            if nums[i] != 'X':
                return i

        return len(nums)
