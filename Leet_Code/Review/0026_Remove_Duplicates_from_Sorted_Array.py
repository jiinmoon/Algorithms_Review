""" 26. Remove Duplicates from Sorted Array

Question:

    Remove duplicate elements from the sorted array and return new length.

+++

Solution:

    Since the array is already sorted, the duplicates has to appear next to one
    another. Here, we will maintain an insert pointer to indicate where we
    should insert newly encountered, non-duplicate elements.

"""

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return None
        i = 0
        for j, num in enumerate(nums[1:]):
            if nums[i] != num:
                i += 1
                nums[i] = num
        return i + 1

