# 1 Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Naive approach would be to use nested loop to compare every element against
itself. This would be O(n^2) in time complexity but does not require additional
space.

Slight improvement can be made by sorting the given list of integers as sorting
gives directionality, and makes the comparison against the target value to
select for next value in smart manner - but the overall complexity is still
bounded by the sorting algorithm used, O(n * log(n)).

If we want to achieve the linear time complexity, we need additional O(n) space
used to record the previously seen elements such that for each element that we
encounter, we can checked against our record in O(1) to see whether it makes up
for the target value.

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()

        for i, num in enumerate(nums):
            if num in d:
                return [ d[num], i ]
            d[target - num] = i

        return []
```
