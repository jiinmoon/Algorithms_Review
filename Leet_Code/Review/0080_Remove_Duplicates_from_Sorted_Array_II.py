""" 80. Remove Duplicates from Sorted Array II

Question:

    Given a sorted array nums, remove the duplicates in-place such that
    duplicates appeared at most twice and return the new length.

    Do not allicate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.

+++

Solution:

    We may use the two pointer method which has a pointer that marks the
    position for the insert, and another for scanning ahead. But as we are
    allowed to have upto two duplicates, our insert position should start at
    second position. And the scan pointer should check against not direct at
    the insert pointer, but two cells behind. This will automatically check for
    the duplicates.

"""

class Solution:
    def remove_duplicates(self, nums):
        ins = 2
        for scan in range(2, len(nums)):

