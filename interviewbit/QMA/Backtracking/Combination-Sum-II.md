# Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
 All numbers (including target) will be positive integers.
 Elements in a combination (a1, a2, … , ak) must be in non-descending order.
 (ie, a1 ≤ a2 ≤ … ≤ ak).
 The solution set must not contain duplicate combinations.

---

Similar to previous Combination Sum I question but we now have to check and
exclude the already chosen candidate.

Again, we take a important note where the elements in the combinations must be
in ascending order; hence, we first sort the given candidates array. Then, as
we can choose the element once in our combination, when we backtrack and
consider our elements, we check that if the element is a duplicate, (same as
previous) then we skip the element.

---

Python:

```python

class Solution:

    def combinationSum(self, candidates, target):

        def helper(start, path, pathSum):
            if pathSum == 0:
                result.append(path)
            else:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i-1] == candidates[i]:
                        continue
                    if candidates[i] > pathSum:
                        break
                    helper(i, path + [candidates[i]], pathSum - candidates[i])

        candidates.sort()

        result = []

        helper(0, [], target)

        return result

```
