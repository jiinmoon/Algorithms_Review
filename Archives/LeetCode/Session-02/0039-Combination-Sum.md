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

The question is about finding the different arrangement of candidates from the
given pool as long as the sum of the candidates can reach or within the target
integer. Hence, the basic algorithm would be to use backtrack where at each
depth, we would choose the candidate so long as we do not over exceed the
current sum of the path that we are building - and once we have reached the
target integer, we can report the path as one of our result.

---

Python:

```python

class Solution39:

    def combinationSum(self, candidates, target):

        def backtrack(path, pathSum, start):
            # goal condition where we have reached the target path sum
            if pathSum == 0:
                result.append(path)
            else:
                # we can select same element unlimited number of times.
                # however, should be all unique combinations.
                for i in range(start, len(candidates)):
                    if candidates[i] <= pathSum:
                        backtrack(
                            path + [candidates[i]],
                            pathSum - candidates[i],
                            i
                        )

        result = []

        backtrack([], target, 0)

        return result

```
