238 Product of Array Except Self
================================

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

---

Let's view this problem as follows:

nums = [a, b, c, d, e]

Suppose that we have these values, then the product of array except itself at
each index would be:

products = [bcde, acde, abde, abce, abcd]

To acheive this, we will first prepare a cumulative product array:

[1, a, ab, abc, abcd]

Then, going to right to left, we continuously multiply the values from original
nums:

[ 1 * bcde, a * cde, ab * de, abc * e, abcd * 1]

So, the right term grows 1, e, de, cde, bcde which combined with the
cumuilative product array gives the answer.

---

Python:

```python
class Solution:
    def productExceptSelf(self, nums):
        # cumulative products from left to right
        products = [1]
        for i in range(1, len(nums)):
            products.append(nums[i-1] * products[-1])
        # now multiply from right to left with cumulative from original
        right = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products
```

