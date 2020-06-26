""" 80. Remove Duplicates from Sorted Array II

Question:

    Given a sorted array nums, remove the duplicates in place such that
    duplicates appeared at most twice and return the new length.

+++

Solution:

    The solution is not as intuitive as it looks - and probably feels like a
    trick. But we will use the insertion pointer method. Let us have an
    insertion pointer start at index 2, then we have another pointer scans ahead
    beginning from index 2.

    We check for whether the scan element is same as the element that is pointed
    at insertion pointer - 2. If it is the new element that we encounter, that
    we can safely swap with what is currently at insertion pointer now since
    this new value is not the third same element that we have encountered!

"""

class Solution:
    def removeDuplicates(self, nums):
        m = len(nums)
        if m < 3:
            return m
        i = 2
        for j in range(2, m):
            if nums[i - 2] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i
