1477 Find Two Non-overlapping Subarrays Each With Target Sum
============================================================

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with sum equal
target. There can be multiple answers so you have to find an answer where the
sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return
-1 if you cannot find such two sub-arrays.

---

The idea here is to maintain a list of prefixSums. For example, if we have
a given array [x, y, z] then, we create [x, xy, xyz]. And for each of these
prefixes, we also record their indicies.

Then, as we iterate to examine each of the prefixSums, we can check whether we
can find the prefixSum + target and prefixSum - target. Each will represent the
sum of left and sum of right non-overlapping subarrays that has the target sum.
In other words, record[prefixSum[i] - target] will represent the previous
starting index of the left non-overlapping subarray and vice versa for right.

If they exist, we can update the left and right min sum values.

An example of how it should look like step by step:

```
A = [a, ab, c, a, b, c]; target = "abc"

prefixSums = [a, aab, aabc, aaabc, aaabbc, aaabbcc]

For first prefix "a", we do not have a left subarray, but right subarray exists
that is "a" + "abc" = "aabc"; length of right subarray is then 2 - 0 = 2. And
minSum does not change as left subarray has not been found yet.

prefix = "aab" does not have matching left subarray; but right subarray
"aaabbc" exists on index 4; current right length is 4 - 1 = 3, but it has no
matching left to update the minSum with.

prefix = "aabc" does have a matching left subarray at index 0. Length of left
adjusts to 2 - 0 = 2. Right also exists which is "aaabbcc", 5 - 2 = 3.
Since we now have two left and right candidates, add and update minSum to
2 + 3 = 5 (this represents two non-overlapping subarray [ab, c]  and [c, a, b]).

Notice that we are maintain the minimum of the left subarray.
```

Time complexity should be linear.

---

Python:

```python
class Solution:
    def minSumOfLengths(self, A, target):
        prefixSums = list()
        prefixSumToIndex = { 0:-1 }
        
        runningSum = 0 
        for i, num in enumerate(nums):
            runningSum += num
            prefixSum.append(runningSum)
            prefixSumToIndex[runningSum] = i

        minSum, left, right = float('inf'), float('inf'), float('inf')

        for i, prefixSum in enumerate(prefixSums):
            # left subarray with target sum exist?
            if prefixSum - target in prefixSumToIndex:
                # update left subarray sum
                prevStart = prefixSumToIndex[prefixSum - target]
                left = min(left, i - prevStart)
            
            # right subarray with target sum exist?
            if prefixSum + target in prefixSumToIndex:
                # update right subarray sum
                nextEnd = prefixSumToIndex[prefixSum + target]
                right = nextEnd - i # notice we do not maintain minimum
                # update minSum found thus far
                minSum = min(minSum, left + right)

        return res if res != float('inf') else - 1
```
