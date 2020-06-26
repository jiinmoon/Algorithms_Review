""" 75. Sort Colors

Question:

    Given an array with n objects colored red, white or blue, sort them in-place
    so that objects of the same color are adjacent, in the order of RWB.

"""

class Solution:
    def sortColors(self, nums):
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        redPointer = 0
        whitePointer = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                swap(redPointer, i)
                redPointer += 1
                if redPointer > whitePointer:
                    whitePointer += 1
            if nums[i] == 1:
                swap(whitePointer, i)
                whitePointer += 1

