# 238 Product of Array Except Self

The problem is easier if we abstract the details out and use example:

    Given [a, b, c, d], return [bcd, acd, abd, abc]

To achieve this, we first prepare another list where we have cumulative
products:

    [a, b, c, d] 
    [1, a, ab, abc]

Then, from right to left, multiply the new list with cumulative product.

    [1, a, ab, abc]         r = 1
    [1, a, abd, abc]        r = d
    [1, acd, abd, abc]      r = cd
    [bcd, acd, abd, abc]    r = bcd

---

Python:

```python

class Solution:
    def productExceptSelf(self, nums):
        products = [1]
        for num in nums[1:]
            products.append(products[-1] * num)

        r = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= r
            r *= nums[i]

        return products
```
