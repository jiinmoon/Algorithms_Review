# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Naive approach would be to perform brute force comparison of an element against
every other element. This nested loop approach will be O(n^2) in time
complexity but would not require any additional space.

Slight improvement in time complexity can be made by first sorting the given
array of integers, and then use two pointers starting from either ends to
search for the two values. This is O(n * log(n)) in time complexity however can
be more difficult to implement as we want to indicies from the original array.

Best approach would be to use the hash structure to store the previously seen
elements. Thus, by using O(n) space, we can reduce the time complexity down
to O(n) as well.

---

Python:

```python

class Solution1:

    def twoSum(self, nums, target):

        d = {}

        for i, num in enumerate(nums):
            if num in d:
                return [ d[num], i ]
            else:
                d[target - num] = i

        return []
```

