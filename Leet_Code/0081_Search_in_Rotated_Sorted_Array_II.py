""" 81. Search in Rotated Sorted Array II

Question:

    Same as before, but we have duplicates in the array.

+++

Solution:

    The problem with duplicates is that when we choose our mid value, we may
    pick a duplicate that gets us 'stuck'. We simply escape this by trying to
    move our pointers.

"""

class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            if nums[lo] < nums[mid]:
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1 # this is where we escape the duplicates.
        return False
