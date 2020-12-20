# Subset

    Given a set of distinct integers, S, return all possible subsets.

    Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
    Also, the subsets should be sorted in ascending ( lexicographic ) order.
    The list is not necessarily sorted.


---

## Approach:

We should first sort the given list if integers as noted. Then, for every
element, we repeatedly add the new value unto the previous result.

O(2^S) in both time and space complexity as it is bounded by the number of
power sets that we can generate.

---

Python:

```python

class Solution:

    def powerSet(self, nums):

        nums.sort()

        result = [[]]

        for num in nums:
            m = len(result)
            for i in range(m):
                result.append(result[i] + [num])

        return sorted(result)
```
