# 53 Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

---

The problem is that negative integers will cause our algorithms to fail if we
are to approach this as simply finding maximum continuous value. Hence, we
maintain another variable that computes the current sum when encountered with
a new value. This is a current subarray sum that will reset itself once it
founds that newly encountered value is greater than sum of itself and the
current value. This will effectively break the continous subarray.

Time complexity should be O(n).

---

Python:

```python

class Solution:
    def maximumSubarray(self, nums):
        currSum, maxSum = 0, float('-inf')
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum if maxSum != float('-inf') else 0
```
