""" 35. Search Insert Position

Question:

    Given a sorted array and a target value, return index if found, else return
    where it should be.

+++

Solution:

    Binary search algorithm.

"""

class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        m = len(nums)
        lo, hi = 0, m-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
