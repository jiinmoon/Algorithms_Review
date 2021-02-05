# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Brute force approach is to consider every possible combinations of two elements
to check to see whether they would sum to target in O(n^2) time complexity. We
can reduce down to O(n * log(n)) by first soting the array and use two pointers
method. Best approach would be to use extra O(n) space to record the previously
examined elements in hashmap to complete the search in O(n).

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                retunr [d[num], i]
            d[target - num] = i
        return []
```
