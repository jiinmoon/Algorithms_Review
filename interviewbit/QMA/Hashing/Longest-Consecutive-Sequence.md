# Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
4.

Your algorithm should run in O(n) complexity.

---

Convert the given array into a set of integers. For each num, we try to build
consecutive sequence out as far out as possible (so long as num + 1 exist).

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def longestConsecutive(self, A):

        A, longest = set(A), 0

        for num in A:
            # no need to compute; already included in previous sequence
            if num - 1 in A:
                continue

            count = 0
            while num in A:
                num += 1
                count += 1

            longest = max(longest, count)

        return longest
```
