# Longest Increasing Subsequence

Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence’s elements
are in strictly increasing order, and in which the subsequence is as long as
possible.

This subsequence is not necessarily contiguous, or unique.

In this case, we only care about the length of the longest increasing
subsequence.

---

We can try to build the longest increasing subsequence by looking at each
value, and compare against the last value of our subsequence. If the new value
is greater, it extends the current subsequence. Otherwise, we have to look
behind to find the insertion point where we should replace it. Implementing it
naively will be O(n^2) in time complexity, as we have to do linear search on
our subsequence; but we can use binary search to reduce the overall time
complexity to O(n * log(n)).

---

Python:

```python

from bisect import bisect_left

class Solution:

    def lis(self, A):
        
        result = [ A[0] ]

        for num in A[1:]:
            # extends
            if result[-1] < num:
                result.append(num)
            # otherwise replace
            else:
                ins = bisect_left(result, num)
                result[ins] = num

        return len(result)
```
