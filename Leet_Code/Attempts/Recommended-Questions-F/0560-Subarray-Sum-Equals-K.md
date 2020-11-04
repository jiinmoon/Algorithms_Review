# 560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of
continuous subarrays whose sum equals to k.

---

To find the count of the continuous subarrays sum to k, we maintain the mapping
of cumulative prefix sum to its counts. By dosing so, we can easily find number
of the total by looking up for current cumulative sum - k. This algorithm can
complete in O(n) time complexity.

---

Python:

```python

class Solution:
    def subarraySum(self, nums, k):
        prefixSums = collections.defaultdict(int)
        total, prefixSum = 0, 0
        for num in nums:
            prefixSum += num
            total += (prefixSum == k)
            total += prefixSums[prefixSum - k]
            prefixSums[prefixSum] += 1
        return total
```
