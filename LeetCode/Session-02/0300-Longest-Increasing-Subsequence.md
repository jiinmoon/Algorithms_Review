# 300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements. For
example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

---

Naive implementation of the algorithm would be to for each starting point in
the given array, we iterate far out as possible to determine the length of the
longest increasing subsequence - which implies O(n^2) in time complexity.

Instead, we can reduce the complexity down to O(n * log(n)) by using binary
search method. As we iterate on the given array, we try to build the longest
increasing subsequence.

For each element encountered, we try to find its insertion point in our
on-going longest increasing subsequence via binary search method.

---

Python:

```python

from bisect import bisect_left

class Solution300:

    def longestIncreasingSubsequence(self, nums):

        result = []

        for num in nums:
            # if current num is greater than last element in window
            if not result or result[-1] < num:
                # append to grow our ongoing subsequence window
                result.append(num)
            # otherwise, we find the insertion point and replace
            else:
                i = bisect_left(result, num)
                result[i] = num

        return len(result)
```

