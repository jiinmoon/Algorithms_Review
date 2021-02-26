# 34. Find First and Last Positions of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

---

Naive solution would be to scan forward to find the target value; then iterate
onwards to see its last value. This would be O(n) in worst case since there may
only be a single element repeated in the array.

Since the array is in sorted order, the intuitive approach would be to use
binary search - in particular, we can tweak the binary search algorithm to find
the left most and right most positions of the given target value (more on
wiki). This can achieve O(log n).

An improvement from above would be just perform a binary search - but search
for the value +/- 0.5 of the target value. This way, we only have to write
a single function to find the leftmost value.

---

Python: binary search method.

```python

class Solution34:

    def searchRange(self, nums, target):

        def binSearch(target, l, r):
            if l > r:
                return l

            mid = l + (r - l) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            return helper(target, l, r)

        first = binSearch(target - 0.5, 0, len(nums) - 1)
        last = binSearch(target + 0.5, 0, len(nums) - 1)

        if first == last:
            return [-1, -1]
        return [first, last - 1]
```
