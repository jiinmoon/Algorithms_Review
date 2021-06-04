# 66. Plus One

Given a non-empty array of decimal digits representing a non-negative integer,
increment one to the integer.

The digits are stored such that the most significant digit is at the head of
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

---

Simplest method to add one to the array of integers representing digits would
be to try to add the one to each digits starting from least significant digit
(starting from left). If the current digit is not 9, then there is no need to
continue as we can simply add one to current digit and return our result.
Otherwise, if the current value is 9, then we have to set the current digit to
0 and continue upwards. If we have set all the values to 0, then 1 carry over
is added to most significant digit.

---

Python:

```python

class Solution66:

    def plusOne(self, nums):
        
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        return [1] + digits
```

