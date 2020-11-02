# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

First naive approach that we can think of would be brute force to compare every
element against each other to check whether they would sum to target. Even with
the improvement of manipulating pointer such that we do not pick the previously
seen elements, it would still be of O(n^2) in time complexity but it would be
constant in space.

One improvement can be made to above algorithm which is sorting the given array
such that we now have a directionality when we are choosing the elements. By
using sorting and two pointer method, we can complete the search in linear time
complexity. However, due to sorting involved, the time complexity would still
be of O(n * log(n)) and space depends upon the sorting algorithm used.

If we are to seek further improvement, we may trade off space complexity to
speed up the algorithm to linear time complexity. By using extra space to
record the previously seen elements, we can complete the algorithm faster. For
this purpose, a hashmap is an ideal structure as we can look-up the previously
stored elements in O(1) time complexity.

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[num - target] = i
        return []
```
