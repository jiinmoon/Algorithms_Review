# 26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

---

We can remove the duplicates in a single pass through the array by having two
pointers; one pointer will denote the insertion position and other will scan
forward to find the new non-duplicate element. Another possible approach would
be to use a hashset to record the elements but this would require O(n) extra
memory.

---

Python:

```python

class Solution26:

    def removeDups(self, nums):

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```
