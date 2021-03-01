# 41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive
integer.

---

One naive method would be to sort the given array, and look for first positive
value that is missing. This would be O(n * log(n)) in time complexity.

We can improve the time complexity down to O(n) by realizing that the smallest
missing positive number present within the array has to be bounded by the
length of the array. This indicates that we can use the array index itself as
the indicator as to whether the value is present or not. So, first missing
smallest positive value is the first index that is not indicated.

---

Python:

```python

class Solution41:

    def firstMissingPositive(self, nums):
        
        if not nums:
            return 1
        
        # avoid zero-index issue
        nums.append(0)

        for num in nums:
            # so long as value is within the bound of length of array
            # mark it present by its index position; swap with whichever
            # value that was present before to avoid loss of information
            while isinstance(num, int) and 0 < num < len(nums):
                nums[num], num = "#", nums[num]

        # first missing positive if first index not marked "#"
        for i, num in enumerate(nums[1:], 1):
            if num != "#":
                return i

        return len(nums)
```
