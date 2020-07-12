""" 81. Search in Rotated Sorted Array II

Question:

    Suppose an array sorted in ascending order is rotated at some pivot
    unknown. Given a target value to search, return True if found; else, return
    False. The array may contain duplicates.

+++

Solution:

    Previously, when we did not have duplicaes, we had to check whcih side
    divided into the mid was in the increasing order and check the boundaries
    to see whether the target value could potentially lie within.

    But duplicate values makes it so that we now have a possibilitiy that the
    chosen lo, mid, or high values can be `flat`. If we do not take care of
    this, then the algorithm can get stuck here. Hence, we first check to see
    whether lower or upper side of array is in order and check for their
    condition. And if neither is case, then it must be that either lo == mid or
    mid == high and deal with it appropriately by moving. If both are flat,
    then we will have to check both sides.

    This will have runtime of O(n).

"""

class Solution:
    def search(self, nums, target):
        return self.binSearch(nums, 0, len(nums)-1, target)

    def binSearch(self, nums, lo, hi, target):
        if lo > hi:
            return False
        
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return True

        # check which half of array is in sorted order.
        if nums[lo] < nums[mid]:
            # bottom half is sorted; check whether target is in range.
            if nums[lo] <= target and target < nums[mid]:
                return self.binSearch(nums, lo, mid-1, target)
            return self.binSearch(nums, mid+1, hi, target)
        
        if nums[mid] < nums[high]:
            if nums[mid] < target and target < nums[hi]:
                return self.binSearch(nums, mid+1, hi, target)
            return self.binSearch(nums, lo, mid-1, target)

        # check for flatness on lower half or upper half.
        if nums[lo] == nums[mid] and nums[mid] != nums[hi]:
            # lower half is flat. move on to upper half.
            return self.binSearch(nums, mid+1, hi, target)
        if nums[mid] == nums[hi] and nums[mid] != nums[lo]:
            return self.binSearch(nums, lo, mid-1, target)

        # both flat - check both cases.
        if self.binSearch(nums, lo, mid-1, target):
            return True
        return  self.binSearch(nums, mid+1, hi, target)


