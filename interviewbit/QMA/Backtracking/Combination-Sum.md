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

We have to pay attention to the particular details about the note here.

Firstable, the elements must be in ascending order. This means that we have to
sort the given candidate array first. Also, solution set must not contain any
duplciate combinations but we can choose the same candidate unlimited number of
times. Hence, we have to either avoid choosing duplicate at the same level, or
remove the duplicates from the candidates and use index pointer to denote which
element that we should start searching from.

O(n ^ (T/m)) in both time and space complexity as there are n candidates to
choose from; and amongst them, we have to consider at least the min candidate
that is less than the target value T.

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
                    # early exit; candidates are sorted
                    if pathSum < candidates[i]:
                        break
                    helper(i, path + [candidates[i]], pathSum - candidates[i])
        
        # ascending order and non-duplicate sets
        candidates.sort()
        i = 1
        while i < len(candidates):
            if candidates[i-1] == candidates[i]:
                candidates.pop(i)
            i += 1

        result = []
        helper(0, [], target)

        return result
```
