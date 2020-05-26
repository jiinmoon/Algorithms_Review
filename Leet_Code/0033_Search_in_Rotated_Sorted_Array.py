""" 33. Search in Rotated Sorted Array

Question:

    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to you beforehand. Given a target value to search, return its index if
    found. Else, return -1.

+++

Solution:

    The fact that array is rotated does not change that part of the array is
    still in sorted order - dividing the array into equal halves, lower or upper
    half will still be in sorted order. If so, then we can still apply
    divide-and-conquer principle.

"""

class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
