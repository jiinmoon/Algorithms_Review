# 238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

---

The problem is easier to visualize in a generalized example:

Suppose that we have been given a array nums [A, B, C, D]. Then, the end
resulting array should be [BCD, ACD, ABD, ABC]. To generate this array, lets
prepare an array where we have a cumulative products as we iterate on the nums
from left to right.

[1, A, AB, ABC]

From this position, we can reverse the process to create the resulting array as
we multiply each elements from right to left from the nums.

[BCD, A CD, AB D, ABC]

---

Python:

```python

class Solution:
    def productExceptSelf(self, nums):
        result = [1]
        for num in nums[:-1]:
            result.append(result[-1] * num)

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= temp
            temp *= nums[i]

        return result
```
