""" 35. Search Insert Position

Question:

    Given a sorted array and a target value, return the index if the target is
    found. If not, return the index where it would be if it were inserted in
    order.

"""

class Solution:
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
