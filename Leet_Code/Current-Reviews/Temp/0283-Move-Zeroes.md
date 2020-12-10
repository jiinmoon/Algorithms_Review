# 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

---

Maintain a pointer where last zero was. So long as value is non-zero, we
continuously swap with the last zero pointer. This takes in-place and O(n) in
time complexity.

---

Python:

```python

class Solution283:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ins = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[ins], nums[i] = nums[i], nums[ins]
                ins += 1

```
