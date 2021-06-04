# 26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each
element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification
to the input array will be known to the caller as well.

---

We can do this in a single pass without extra memory as all we require is to
check the neighbours as this array is in sorted order. Hence, we maintain
a insertion pointer where we will place the new "non-duplicate" element as we
iterate on the given array.

---

Python:

```python

class Solution26:

    def removeDups(self, nums):

        ins = 0
        for i in range(1, len(nums)):
            # new element is non-duplicate of previous element
            if nums[ins] != nums[i]:
                ins += 1
                # insert new element in its insertion place
                nums[ins] = nums[i]
        return ins + 1
```
