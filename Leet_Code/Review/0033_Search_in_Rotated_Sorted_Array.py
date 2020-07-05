""" 33. Search in Rotated Sorted Array

Question:

    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to us. Given a taget value, search its index if found; else return -1. The
    algorithm should run in O(lg n).

+++

Solution:

    The fact that we know the time complexity gives away a lot of hint
    - mainly, when we think of logrithmic time scale, this has to do with
      divide-and-conquer strategy. In this case, we are searching for a number,
      thus binary search algorithm. However, the problem is that the array is
      rotated which makes us to believe that binary search is unusable, but
      this is not true.

    Even though the array is maybe rotated, but when you examine the lower half
    and upper half, at least one of them has to be in the order - and this
    implies that we can check for boundary conditions to see whether target
    values lies within or not, to make logical decision to move onto which part
    of the array to search next.

"""

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        m = len(nums)
        lo, hi = 0, m-1
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
