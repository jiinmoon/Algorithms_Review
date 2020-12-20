# Combination Sum

    Given a set of candidate numbers (C) and a target number (T), find all unique
    combinations in C where the candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:
    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order.
    (ie, a1 ≤ a2 ≤ … ≤ ak).
    The combinations themselves must be sorted in ascending order.
    CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1
    = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
    The solution set must not contain duplicate combinations.

---

## Approach:

Use backtrack to build the combinations so long as we can get closer to the
target number. As noted, the elements should be sorted and combinations must be
composed of non-duplicate elements. Hence, we will first sort the candidates
and remove the duplicate elements prior to backtrack.

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
                    if A[i] > pathSum:
                        break
                    helper(i, path + [nums[i]], pathSum - A[i])

        nums.sort()
        
        i = 1
        while i < len(A):
            
            if A[i-1] == A[i]:
                A.pop(i)
            else:
                i += 1

        result = []

        helper(0, [], target)

        return result
```
