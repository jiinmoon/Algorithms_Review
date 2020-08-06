78 Subsets
==========

Question:
---------

Given a set of **distinct** integers, nums, return all possible subsets (the
power set).

Solutions:
----------

We may use a simple iterative approach where we will pick a subset from our
result set, and repeatedly append the chosen integer to all the subsets.
Because we are performing n number of operations for each of subsets, the time
complexity is O(n * 2^n).

Codes:
------

Python:

```python
class Solution:
    def subsets(self, nums):
        result = [ [] ]
        for num in nums:
            m = len(nums)
            for i in range(m):
                subset = result[i]
                result.append(subset + [num])
        return result
```

---

**Source:**

LeetCode: [Subsets](https://leetcode.com/problems/subsets)
