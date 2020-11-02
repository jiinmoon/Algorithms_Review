# 46 Permutations

Given a collection of distinct integers, return all possible permutations.

---

Using recursion, we explore all possible ways that we can select the values
from the given set of integers.

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

