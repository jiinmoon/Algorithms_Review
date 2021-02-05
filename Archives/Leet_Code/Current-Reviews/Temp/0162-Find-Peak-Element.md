# 162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the
array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

---

#### 1. Iterative search.

Scan across the nums to find first element that is strictly greater than nums
to its left and right. O(n) in time complexity.

#### 2. Binary search.

We can use binary search to reduce our size of search. O(log(n)) in time
complexity.

---

Python:

```python

class Solution162:

    def findPeakElement(self, nums):

        l, r = 0, len(nums) - 1

        while l < r:
            
            m = l + (r - l) // 2

            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1

        return l

```
