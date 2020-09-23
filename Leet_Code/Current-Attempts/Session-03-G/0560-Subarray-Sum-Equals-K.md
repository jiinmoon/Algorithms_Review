# 560 Subarray Sum Equals K

Maintain the prefix sum of elements from left to right. As we iterate, find the
cumulative sum to check whether we have subarray sum that can equal to k by
looking up the prefix sums.

---

```python

class Solution:
    def subarraySumEqualsK(self, nums, K):
        prefixSums = collections.defaultdict(int)
        runningSum, total = 0, 0
        for num in nums:
            runningSum += num
            total += runningSum == K
            total += prefixSums[runningSum - K]
            prefixSums[runningSum] += 1
        
        return total
```
