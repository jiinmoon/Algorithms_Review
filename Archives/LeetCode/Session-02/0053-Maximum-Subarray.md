# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

---

Naive approach to this problem would involve exploring all possible subarray
and their sum to find the largest amongst them.

We can improve upon this by utilizing the sliding window idea - we record the
current on-going contiguous subarray. As there are negative values present, we
see that if by adding the new element to current subarray would reduce the size
of the sum, then we start to create a new subarray starting from the new
element. This can achieve O(n) in time complexity.

---

Python:

```python

class Solution53:

    def maxSubarray(self, nums):

        maxSum, currSum = float('-inf'), 0

        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)

        return maxSum
```
