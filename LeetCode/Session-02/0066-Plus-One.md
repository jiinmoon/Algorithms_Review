# 66. Plus One

Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

---

Here, we can simply check from least significant digit to see whether current
digit is 9 or not - as we only carry over iff the current digit is 9. So long
as it is not 9, we can just simply add one to the digit and return the array.
Otherwise, we continue to check while setting the current digit to 0. If we run
out of the array, then we need a bigger array size + 1.

---

Python:

```python

class Solution66:

    def plusOne(self, nums):

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 9:
                nums[i] += 1
                return nums
            else:
                nums[i] = 0

        return [1] + nums
```
