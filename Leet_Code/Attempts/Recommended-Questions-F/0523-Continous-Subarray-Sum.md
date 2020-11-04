# 523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function
to check if the array has a continuous subarray of size at least 2 that sums up
to a multiple of k, that is, sums up to n*k where n is also an integer.

---

For finding the continuous subarrays that sum to multiple of target k, we can
confirm this by creating the continous (cumulative) prefix sum record - here,
we will record the prefix summation of the integers thus far and its index.
Thus, for every cumulative sum we are generating as we iterate on the given
list, we check to see whether it is multiple of target by first taking a modulo
with k, then check in the record to see whether we have previous encountered
this sum value and its ending index which should be the starting index for
current. Time complexity should be of O(n).

---

Python:

```python

class Solution:
    def checkSubarraySum(self, nums, k):
        currSum = 0
        prefixSums = { 0: -1 }
        for i, num in enumerate(nums):
            currSum += num
            if k != 0:
                currSum = currSum % k
            # current subarray sum is multiple of k
            # if this value exists in record, compute the length
            if currSum in prefixSums:
                if i - prefixSums[currSum] >= 2:
                    return True
            else:
                prefixSums[currSum] = i
        
        return False
```
