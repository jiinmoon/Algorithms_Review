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

## Approach:

While similar to previous question, we have an imposed condition where
same candidate can only every be chosen once. Hence, we add in an explict check
to see whether the chosen candidate is same as the previous value while
building our combinations. As per note, we should also sort to build our result
in sorted order.

---

Python:

```python

class Solution:

    def combinationSum(self, nums, target):

        def helper(start, path, pathSum):

            if not pathSum:
                result.append(path)

            else:
                for i in range(start, len(nums)):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    if nums[i] > pathSum:
                        break
                    helper(i + 1, path + [nums[i]], pathSum - nums[i])
        
        nums.sort()

        result = []

        helper(0, [], target)

        return result
```
