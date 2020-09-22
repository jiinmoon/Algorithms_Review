41 First Missing Positive
=========================

Given an unsorted integer array, find the smallest missing positive integer.

---

By its definition, the smallest positive integer has to be bounded by the range
of the array - it is between 1 <= x < len(array). If so, then we can find the
missing positive by marking the indicies of the elements that are appearing
within the array. When we iterate for the second time, any index that is not
marked is the missing positive elements.

Time complexity should be O(n).

---

Python:

```python
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        
        # avoid zero-indexing issues
        nums.append(0)
        for i, num in enumerate(nums):
            # mark indicies indicated by the elements appearing in the array
            while num != '#' and num > 0 and num < len(nums):
                nums[num], num = '#', nums[num]

        for i, num in enumerate(nums[1:], 1):
            if num != '#':
                return i

        return len(nums)
```
