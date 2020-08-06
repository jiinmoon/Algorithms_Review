75 Sort Colors
==============

Question:
---------

Given an array of integers where 0, 1, 2 represents red, white, blue
respectively, sort it such that it is in red, white and blue order.

Solutions:
----------

Simply we will use a chain of logic to help ordering the values.

We will first assume that every element we encounter is a blue. Save the
current value and mark it as blue. But we could have been wrong, so we check to
see whether it is non-blue. If it is non blue, then we assume it is white. If
it was not blue nor white, then we know it is red.

Codes:
------

Python:

```python
class Solution:
    def sortColors(self, nums):
        redPtr, whitePtr = 0, 0
        for i in range(len(nums)):
            temp = nums[i]
            # assume current is blue
            nums[i] = 2

            # but the current was non-blue, then assume white
            if temp < 2:
                nums[whitePtr] = 1
                whitePtr += 1
            # it was non-blue, non-white; has to be red
            if not temp:
                nums[redPtr] = 1
                redPtr += 1
```

---

**Source:**

LeetCode: [Sort-Colors](https://leetcode.com/problems/sort-colors/)
