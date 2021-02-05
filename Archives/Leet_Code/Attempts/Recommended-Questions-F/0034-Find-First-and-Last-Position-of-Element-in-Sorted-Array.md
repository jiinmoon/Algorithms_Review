# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

---

Efficient algorithm for searching a value within a "sorted" array is binary
search - hence, we search for the value that is +/- 0.5 of the given value. If
the values are not found, then both indicies to left and right would be equal
to each other - in which case we return [-1, -1]. Since this is basically
a binary search algorithm, the time complexity should be O(log(n)).

---

Python:

```python

class Solution:
    def searchRange(self, nums, target):
        def binSearch(l, r, target):
            if l > r:
                return l
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
            return binSearch(l, r, target)

        first = binSearch(0, len(nums) - 1, target - 0.5)
        last = binSearch(0, len(nums) - 1, target + 0.5)
        if first == last:
            return [-1, -1]
        return [first, last-1]
```
