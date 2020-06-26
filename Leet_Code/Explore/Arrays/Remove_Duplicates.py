""" Remove Duplicates from Sorted Array

Question:

    Given a sorted array nums, remove the duplicates in-place such that each
    element appear only once and return the new length.

    Do not allocate extra space for another array - modify given array in-place.

+++

Solution:

    The fact that the array is sorted implies that the duplicates will be
    neighbour to one another. Hence, we would utilize the two pointers. One
    pointer would be used to indicate the insert position within the array; the
    other is used to scan forward, skipping the duplicates to find the new value
    to insert into the insert position. Thus, this algorithm will be able to
    complete the given task within O(n) and without using extra space.

"""

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return None
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                nums[i] = nums[j]
                i += 1

