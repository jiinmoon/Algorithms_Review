""" 27. Remove ELement

Question:

    Given an array nums and a value val, remove all instances of that value
    in-place and return the new length.

"""

class Solution:
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
