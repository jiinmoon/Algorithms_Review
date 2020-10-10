# 1 Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Naive solution involves a nested loop for comparing every element against one
another to check whether two selected elements equal to the target value. Even
with an improvement of updating inner loop's index to not select the duplicated
elements of the outer loop, it will still remain at O(n^2) in time complexity.

Different approach that can slightly improve the time complexity to O(n
* log(n)) is first we sort the given array. By sorting, we have
  a directionality on selecting the values - starting from either ends of the
  list of the integers, if their sum is less than the target, than smaller
  value (left) should increase; otherwise, the bigger value (right) should
  decrease. O(n * log(n)) derives from the lower bound of the comparison based
  sorting.

To further improve upon this, we look to trade our space complexity. We use
hashmap to store the previously seen elements so that we do not have to
constantly compare, but check against the hashmap in O(1). Overall, this will
be linear time and space complexity.

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target-num] = i
        return []
```
