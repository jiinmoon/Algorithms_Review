""" 162. Find Peak Element

Question:

    A peak element is an element that is greater than its neighbors. The given
    array may contain multiple of such element; find index of any one.

+++

Solution:

    Since we do not have to find all peak elements, we do not really need to
    scan all the areas; instead, we can try to find the trend between two points
    i and i + 1. As the nums[i] != nums[i+1], we are either rising or
    decreasing. Hence, we follow the increasing trend as far as possible.

"""

class Solution:
    def findPeakElement(self, nums):
        if not nums or len(nums) < 1:
            return 0
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid+1]:
                # decreasing trend.
                hi = mid
            else:
                lo = mid + 1
        return lo

