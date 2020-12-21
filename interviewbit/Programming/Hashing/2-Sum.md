# 2 Sum

    Given an array of integers, find two numbers such that they add up to
    a specific target number.

    The function twoSum should return indices of the two numbers such that they add
    up to the target, where index1 < index2. Please note that your returned answers
    (both index1 and index2 ) are not zero-based.
    Put both these numbers in order in an array and return the array from your
    function ( Looking at the function signature will make things clearer ). Note
    that, if no pair exists, return empty list.

    If multiple solutions exist, output the one where index2 is minimum. If there
    are multiple solutions with the minimum index2, choose the one with minimum
    index1 out of them.

---

## Approach:

Use hashmap to record each of the number that we examine. If we have a (target
- num) in the record, we can conclude that there exist two sum.

O(n) in time and space complexity.

---

Python:

```python

class Solution:

    def twoSum(self, nums, target):

        d = dict()

        for i, num in enumerate(nums):

            if target - num in d:
                return [d[target - num], i]
            if num not in d:
                d[num] = i

        return []
```

