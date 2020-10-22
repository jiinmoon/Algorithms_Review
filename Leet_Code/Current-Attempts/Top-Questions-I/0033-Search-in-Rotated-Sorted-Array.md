# 33 Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer
target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e.,
[0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

---

Even though the array is rotated, it does not change the fact that it is still
in partially sorted order. The question is which half of the array is sorted
- and if we can find whether lower or upper half is sorted, we can ask the
  question of whether the target value lies within the range.

Thus, the solution would be in O(log(n)) in time complexity as we can still
apply modified version of the binary search algorithm.

---

Python:

```python

class Solution:
    def searchRotatedSortedArray(self, nums, target):
        if not nums:
            return -1

        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
```
