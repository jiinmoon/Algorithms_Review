# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

---

The fact that the given array is in sorted order indicates that we may use the
binary search algorithm to our advantage. By using the modified binary search
algorithm, we try to find the index positions. Due to nature of divide and
conquer algorithm, the time complexity would be reduced to O(log n) as
required.

Here, we simply create a generic binary serach algorithm, but the search values
would be target value plus and minus the half the point. This will allow us to
not having to write two separate binary search algorithm to search leftmost and
rightmost positions of the target value.

---

Python:

```python

class Solution:
    def searchRange(self, nums, target):
        def helper(l, r, target):
            # end of search
            # in general, we serach as far left as possible
            if l > r:
                return l
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            # answer not found; repeat with updated pointers
            return helper(target, l, r)
        
        first = helper(0, len(nums) - 1, target - 0.5)
        last = helper(0, len(nums) - 1, target + 0.5)
        if first == last:
            return [-1, -1]
        return [first, last - 1]
```

