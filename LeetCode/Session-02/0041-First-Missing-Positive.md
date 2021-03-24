# 41. First Missing Positive

Given an unsorted integer array nums, find the smallest missing positive
integer.

---

Here, the trick is in realizing that the smallest missing positive value must
be within the bounds of the length of the unsorted integer array. In other
words, if there exists missing positive integer that is bounded by the length
of the array, it must be present. Hence, we can use this fact to use the array
index as a marker to record which values that we have seen thus far. For each
value we examine, we visit its index if it is in bound and swap/mark the index
present. On the second pass, we can find the missing positive integer by
checking to see which index has not been marked yet.

---

Python:

```python

class Solution41:

    def firstMissingPositive(self, nums):

        if not nums:
            return 1
        
        nums.append(0)

        for num in nums:
            while num != "#" and 0 < num < len(nums):
                nums[num], num = "#", nums[num]

        for i, num in enumerate(nums[1:], 1):
            if num != "#":
                return i

        return len(nums)
```

