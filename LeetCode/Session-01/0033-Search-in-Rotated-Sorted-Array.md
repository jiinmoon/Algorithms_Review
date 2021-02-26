# 33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct
values).

Prior to being passed to your function, nums is rotated at an unknown pivot
index k (0 <= k < nums.length) such that the resulting array is [nums[k],
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
[4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.

---

The fact that the given array is still sorted - just shifted about unknown
pivot - allows for binary search algorithm. When we take the mid element, we
can still divide the array into two halves; and can check whether lower or
upper half is in sorted order to query whether the target falls within the
lower or upper half in the range.

Hence, overall time complexity would be O(log(n)).

---

Python: Modified Binary Search method.

```python

class Solution33:

    def searchRotatedArray(self, nums, target):

        lo, hi = 0, len(nums) - 1

        while lo <= hi:

            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid

            # is lower or upper half in sorted order?
            if nums[lo] <= nums[mid]:
                # lower half is in sorted order
                # then, is target in lower half?
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # upper half is in sorted order
                # is target in upper half?
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
```
