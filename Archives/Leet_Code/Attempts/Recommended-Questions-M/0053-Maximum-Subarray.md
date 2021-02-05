# 53 Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.

---

To find the contiguous subarray which has the largest sum, we could use naive
approach to consider every possible contiguous subarray.

We can improve upon this further to acheive O(n) in time complexity by
maintaining the current contiguous subarray sum and the total maximum found
thus far. As there can be negative value, when we iterate and consier new value
to add to our contiguous subarray, we first check whether adding this value
will increase the previous subarray sum. If it doesn't, we break the subarray
and update the current subarray sum as the current value to start the new
subarray sum. Amongst these, we find the maximum.

---

Python:

```python

class Solution:
    def maximumSubarraySum(self, nums):
        currSum, maxSum = float('-inf'), 0
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum
```
