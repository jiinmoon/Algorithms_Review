# 46. Permutations

Given a collection of distinct integers, return all possible permutations.

---

To create all possible permuations from a given collection of distinct
integers, we use DFS to explore all the permutations at every possible
positions. For given n number of integers, there would be n! different
permutations; thus, the time complexity is O(n! * n^2).

---

Python:

```python

class Solution:
    def permute(self, nums):
        def helper(candidates, path):
            if not candidates:
                result.append(path)
                return
            for i in range(len(candidates)):
                helper(candidates[:i] + candidates[i+1:], path + [candidates[i]])

        result = list()
        helper(nums, list())

        return result
```
