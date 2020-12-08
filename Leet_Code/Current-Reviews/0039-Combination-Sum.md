# 39. Combination Sum

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

It is guaranteed that the number of unique combinations that sum up to target
is less than 150 combinations for the given input.

---

We can use backtracking to explore all possible candidates sum to target value.
Base case of our recursion would be when the pathSum has finally reached the
target value; in which case, we can add current path to our result. Otherwise,
we continue to consider every combination while updating our path and pathSum.

Time complexity would be O(n ^ k) where n is the number of candidates and k are
the number of paths where we have to explore (current path sum has not yet to
reach target value).

---

Python:

```python

class Solution39:

    def combinationSum(self, candidates, target):

        def helper(start, path, pathSum):
            if pathSum == 0:
                result.append(path)
            else:
                for i in range(start, len(candidates)):
                    helper(i, path + [candidates[i]], pathSum - candidates[i])

        result = list()

        helper(0, [], target)

        return result
```
