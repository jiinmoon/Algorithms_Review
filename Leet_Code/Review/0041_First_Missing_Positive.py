""" 41. First Missing Positive

Question:

    Given an unsorted integer array, find the smallest missing positive
    integer.

+++

Solution:

    The trick lies in understanding that the smallest missing positive integer
    has to be present within the length of the array. The smallest positive
    integer would lie outside of the range of length of the array if all the
    array is filled with integers from 1, len(array).
    
    Thus, this allows us to use array indicies as an indicator of the elements
    present within the array. The algorithm would be as follows: we iterate on
    the array, and if the element is within the range of array length, we mark
    the index indicated by the element and repeat the process.

"""

class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        # Mark.
        nums.append(0) # avoid zero indexing issue.
        for i, num in enumerate(nums):
            while num != 'X' and num > 0 and num < len(nums):
                nums[num], num = 'X', nums[num]
        # Find first non marked index.
        for i in range(1, len(nums)):
            if nums[i] != 'X':
                return i
        # All array is filled.
        return len(nums)
