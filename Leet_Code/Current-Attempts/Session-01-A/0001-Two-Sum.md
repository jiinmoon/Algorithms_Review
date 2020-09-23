# 1 Two Sum

Naive approach involves comparison of every possible two element combination
within the array. O(n^2) time complexity for nested loop to consider every
other element for each element.

By using a hashmap structure to store the previously seen elements, we can
complete the algorithm in O(n).

---

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return[d[num], i]
            d[target-num] = i
        return []
```
