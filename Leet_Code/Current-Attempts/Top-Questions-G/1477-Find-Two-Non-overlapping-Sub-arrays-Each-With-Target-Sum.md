# 1477 Find Two Non-overlapping Sub-arrays Each With Target Sum

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal
target. There can be multiple answers so you have to find an answer where the
sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return
-1 if you cannot find such two sub-arrays.

---

Here, the problem is that we may have negative and positive values.

To find all the subarrays that have target sum, simplest method would be to
firstable, create a list of running cumulative sum; while doing so, we also
create a hashmap to map the index of each cumulative sum so that we can find
the length between the values.

Thus, as we iterate on the prefix, we check for two condition : if target sum
exists, then it must lie within prefix plus target and prefix minus target. So,
we maintain the overall minimum of all these.

---

Python:

```python

class Solution:
    def minSumOfLengths(self, arr, target):
        prefixSum = list()
        prefixIndex = { 0 : -1 }
        runningSum = 0

        for i, num in enumerate(arr):
            runningSum += num
            prefixSum.append(runningSum)
            prefixIndex[runningSum] = i

        minThusFar, lSum, rSum = float('inf'), float('inf'), float('inf')

        for i, prefix in enumerate(prefixSum):
            if prefix - target in prefixIndex:
                lSum = min(lSum, i - prefixIndex[prefix])
            if prefix + target in prefixIndex:
                rSum = min(rSum, prefixIndex[prefix] - i)
                minThusFar = min(minThusFar, lSum + rSum)

        return minThusFar if minThusFar 1= float('inf') else -1
```
