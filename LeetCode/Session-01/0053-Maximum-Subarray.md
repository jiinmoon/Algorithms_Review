# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

---

To find the subarray within the given integer array which has largest sum, we
can try to compute the contiguous subarray sum so long as we can create
a larger sum. This is done so by maintaining current subarray sum as we iterate
forward. The current subarray sum can either increase by adding the new
element, or it could be actually made smaller by including it. If it becomes
smaller, we start a new subarray. Amongst all subarray sum found this way, we
find the maximum. This can be done in linear time complexity.

---

Python:

```python

class Solution53:

    def maxSubarray(self, nums):

        currSum, maxSum = 0, float('-inf')

        for num in nums:
            # currSum either increases by including current val or start new
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)

        return maxSum
```
