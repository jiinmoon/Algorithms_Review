# 238 Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

---

The problem becomes easier to conceptualize once we create an abstraction.
Suppose following:

[A, B, C, D]

Then, the resulting array would become

[BCD, ACD, ABD, ABC]

To produce this final result, we create an array of cumulative products:

[1, A, AB, ABC]

Then, we repeat the process, but from right to left with original values
- right cumulative products.

---

Python:

```python

class Solution:
    def productExceptSelf(self, nums):
        products = [1]
        for num in nums:
            products.append(num * products[-1])

        r = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= r
            r *= nums[i]

        return products
```
