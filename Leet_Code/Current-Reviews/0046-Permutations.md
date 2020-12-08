# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

---

We can use backtracking to explore all possible n! permutations. Base case is
when we have our path length == candidates or no more candidates left to
consider. At every depth, we remove the the candidate and add to the path.

Time and space complexity would be O(n!) due to number of permutations to
explore.

---

Python:

```python

class Solution46:

    def permute(self, nums):

        def helper(candidates, path):
            if not candidates:
                result.append(path)
            else:
                for i in range(len(candidates)):
                    helper(candidates[:i] + candidates[i+1:], path + [candidates[i]])

        result = list()

        helper(nums, []

        return result
```
