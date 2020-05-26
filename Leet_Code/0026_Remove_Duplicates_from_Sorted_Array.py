""" 26. Remove Duplicates from Sorted Array

Question:

    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

"""

class Solution:
    def removeDuplicates(self, nums):
        m = len(nums)
        if not nums or m < 2:
            return m
        i = 0
        for j in range(1, m):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

