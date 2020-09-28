# 560 Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

---

We can simply approach this problem by recording the count of prefix sum
- continuous sum from left to right. Hence, if we discover that current running
sum minus the k exists within the record, we know that there is a continuous
subarray that sum equals to k.

Time complexity should be of O(n).

---

Python:

```python

class Solution:
    def subarraySum(self, nums, k):
        prefixSums = collections.defaultdict(int)
        runningSum, total = 0, 0
        for num in nums:
            runningSum += num
            total += (runningSum == k)
            total += (prefixSums[runningSum - k])
            prefixSums[runningSum] += 1
        return total
```
