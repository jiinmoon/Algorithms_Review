560 Subarray Sum Equals K
=========================

Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

---

Two general ideas:

(1) Maintain a subarray where we will continuously add the current element
encountered and if its sum equals to k then we increment the count. If its sum
is greater, then we remove the last element from the array. This has a problem
with the negative integers and performing sum opeartion for each of the
subarray is going to cost us overall O(n^2) in time complexity.

(2) We can improve by identifying the repeated work - let us instead record the
previous contiguous of sum thus far. So that, we can easily check whether we
have a subarray equals to K by looking up the (current contiguous sum - K) in
the record.

---

Python:

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        # record of count of previous contiguous sums before current num    
        prevSums = defaultdict(int)
        currentSum = 0
        total = 0
        for num in nums:
            currentSum += num
            # is current contiguous sum == k?
            total += (currentSum == k)
            # can we take away prev sums to have subarray == k?
            total += prevSums[currentSum - k]
            prevSums[currentSum] += 1
        return total
``` 

