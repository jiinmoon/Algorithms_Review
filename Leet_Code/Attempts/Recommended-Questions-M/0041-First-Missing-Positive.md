# 41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive
integer.

Follow up: Could you implement an algorithm that runs in O(n) time and uses
constant extra space.?

---

Simple approach would be to first sort the given array to identify the smallest
missing positive integer; but this would be bounded by O(n * log(n)) in time
complexity due to sorting algorithm involved.

Here, we can utilize the fact that if the smallest missing positive is present,
it must be bounded by the length of the given array. Thus, we can use the array
and the index to mark the elements present. And when we iterate on the second
time, the missing element should be the unmarked index. This algorithm is O(n)
in time complexity.

---

Python:

```python

class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) <= 1:
            return len(nums)
        # avoid zero index issue
        nums.append(0)
        for i, num in enuemrate(nums):
            while num != "#" and 0 < num < len(nums):
                nums[num], num = "#", nums[num]

        for i, num in enumerate(nums[1:], 1):
            if num != "#":
                return i

        return len(nums)
```
