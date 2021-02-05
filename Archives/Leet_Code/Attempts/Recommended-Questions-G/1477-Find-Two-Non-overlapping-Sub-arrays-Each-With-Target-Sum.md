# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal
target. There can be multiple answers so you have to find an answer where the
sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return
-1 if you cannot find such two sub-arrays.

---

One method for approaching this problem would be to maintain the min sum of the
lengths of the two subarrays. Also, maintain the left and right subarrays found
thus far as well. To do this, we first create the prefix sum count - cumulative
prefix sum mapped to its ending indicies.

Then, iterate on the create mapped prefix sum indicies. We can easily find out
whether the subarrays have reached their desired target sum by checking for the
current prefixSum - target or prefixSum + target values. If they are found,
then the length of the left and right subarray sum values are updated. We can
update the min length once we have found the right subarray sum since both
subarrays sums are required to be equal to the target sum.

---

Python:

```python

class Solution:
    def minSumOfLengths(self, nums, target):
        record = { 0 : -1 }
        prefixSums = list()

        temp = 0
        for i, num in enumerate(nums):
            temp += num
            record[temp] = i
            prefixSums.append(temp)

        minLen, leftMinLen, rightMinLen = float('-inf'), float('-inf'), float('-inf')
        for i, prefixSum in enumerate(prefixSums):
            if prefixSum - target in record:
                leftMinLen = min(leftMinLen, i - record[prefixSum - target])
            if prefixSum + target in record:
                rightMinLen = min(rightMinLen, i - record[prefixSum + target])
                minLen = min(minLen, leftMinLen + rightMinLen)

        return minLen if minLen != float('-inf') else -1
```
