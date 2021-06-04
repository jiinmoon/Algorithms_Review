# 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting
and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

---

Naive linear time complexity approach here would be to perform a scan to find
the first position and last position of the given element in the array.

To improve upon this, we leverage on the fact that the array is in sorted
order. Hence, we can use modified binary search algorithm to find the left most
and right most position of the target value. We can improve upon this slightly
by writing concise single binary search algorithm instead of two by searching
for target value +/- 0.5 (in the case of Python; may need to rethink about this
strategy for other languages and how their numberical types are).

---

Python:

```python

class Solution34:
    
    def searchRange(self, nums, target):

        def search(l, r, target):

            if l > r:
                return l

            m = l + (r - l) * 0.5

            if nums[m] <= target:
                l = mid + 1
            else:
                r = mid - 1

            return search(l, r, target)

        first = search(0, len(nums) - 1, target - 0.5)
        last = search(0, len(nums) - 1, target + 0.5)
        
        if first == last:
            return [-1, -1]
        return [first, last + 1]
```
