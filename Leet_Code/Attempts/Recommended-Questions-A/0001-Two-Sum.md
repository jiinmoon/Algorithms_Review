# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Finding the two elements in the array that sums to target value can be
approached with a hashmap structure where we will record the previously
encountered elements. This algorithm will be O(n) in both time and space
complexity.

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        return []
```
