# 53 Maximum Subarray

Problem is with the negative integers encountered; to deal with this, maintain
another current sum that checks whether current sum will be smaller by adding
the new element. If so, then disregard.

---

Python:

```python

class Solution:
    def maxSubarray(self, nums):
        currSum, maxSum = 0, float('-inf')
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum , currSum)
        return maxSum
```
