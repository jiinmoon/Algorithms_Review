# 53 Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

---

The problem with determining the maximum subarray is that there are negative
values present - which we need to know where the subarray starts and ends.

To do so, we maintain a separte current sum value that computes the current
subarray sum by adding the current num. If the adding current num increases the
current sum, we can keep it. However, if it is smaller than the num itself,
then this breaks the subarray and we should start anew.

---

Python:

```python

class Solution:
    def maximumSubarray(self, nums):
        currSum, maxSum = 0, float('inf')
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum
```
