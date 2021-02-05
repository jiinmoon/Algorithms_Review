41 First Missing Positive
=========================

Question:
---------

Given an unsorted integer array, find the first missing positive integer.

Solutions:
----------

By definition, the first missing postivie integer has to be less than the
length of the given integer array. Thus, we examine the array for positive
values that are within the range of the array, and place them in their correct
places. Now, when we iterate for second time, the index where its value does
not match will be the first missing positive value. This will be an O(n)
algorithm.

Codes:
------

Python:

```python
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1

        nums.append(0) # avoid zero index issue

        for i, num in enumerate(nums):
            while num != 'x' and num > 0 and num < len(nums):
                nums[num], num = 'x', nums[num]

        for i in range(1, len(nums)):
            if nums[i] != 'x':
                return i
        
        return len(nums) # array all occupied. 
```

---

**Source:**

LeetCode:
[First-Missing-Positive](https://leetcode.com/problems/first-missing-positive)
