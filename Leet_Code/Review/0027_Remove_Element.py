""" 27. Remove Element

Question:

    Given an array, remove all occurrences of a target, and return its new
    length.

+++

Solution:

    We still use same strategy as question 26, where we have utilized a insert
    pointer. So long as the element that is being scanned currently is not same
    as the target, we can safely move over, and increment the insert pointer.

"""

class Solution:
    def removeElement(self, nums, target):
        if not nums:
            return None
        i = 0
        for j in range(len(nums)):
            if nums[j] != target:
                nums[i] = nums[j]
                i += 1
        return i

