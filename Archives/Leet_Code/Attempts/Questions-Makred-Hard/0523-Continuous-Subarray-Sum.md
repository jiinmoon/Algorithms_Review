# 523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function
to check if the array has a continuous subarray of size at least 2 that sums up
to a multiple of k, that is, sums up to n*k where n is also an integer.

---

Here, we are to find the continuous subarray whose sum is evenly divisible by
k.

We can approach this problem as a sliding window where we record the previous
prefix sums and starting indicies. Then, we can iterate forward consider adding
each encountered values to our current subarray sum. On these prefix sums, we
record its modulo k result to index where it will mark its start. Hence,
whenever we can find current prefix sum modulo k already within the record,
this is potential subarray where we can check their index to determine the
size.

The time complexity should be O(n).

---

Python:

```python

class Solution:
    def continuousSubarraySum(self, nums, k):
        record = {0 : -1}
        prefixSum = 0

        for i, num in enumerate(nums):
            prefixSum += num
            # edge case where k is 0
            prefixSum = prefixSum % k if k else prefixSum
            # current subarray sum evenly divisible by k
            if prefixSum in record:
                # check length
                if i - record[prefixSum] >= 2:
                    return True
            record[prefixSum] = i

        return False
```
