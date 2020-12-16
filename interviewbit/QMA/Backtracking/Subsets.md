# Subsets

Given a set of distinct integers, S, return all possible subsets.

 Note:
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
 Also, the subsets should be sorted in ascending ( lexicographic ) order.
 The list is not necessarily sorted.

---

Non-duplicates to worry about - hence we do not have to use set to check for
added subsets. We take note where subset has to be in ascending order as well
as subsets have to be sorted. Hence, we first sort the given set of integers
S and also sort the result.

---

Python:

```python

class Solution:

    def subsets(self, S):

        result = [[]]]

        for num in sorted(S):
            m = len(result)
            for i in range(m):
                result.append(result[i] + [num])

        return sorted(result)

```
