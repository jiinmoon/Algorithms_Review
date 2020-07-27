39 Combination Sum
==================

Question:
---------

Given a set of candidates (without duplicates) and a target number, find all
unique combinations of canididates such that they add up to target.

Solutions:
----------

We may use a backtracking algorithm to build a path that selects candidates at
each step, and checks whether the current path sum equates to the target.

Codes:
------

Python:

```python
class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, pathSum, path):
            if pathSum < 0:
                return
            if pathSum == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= pathSum:
                    backtrack(i, pathSum - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result
```

Go:

```go
func combinationSum(candidates []int, target int) [][]int {
    result := new([][]int, 0)
    for i, val := range candidates {
        if val == target {
            result = append(result, []int{val})
            continue
        }
        if val < target {
            for _, subresult := range combinationSum(candidates[i:], target - val) {
                result = append(result, append(subresult, val))
            }
        }
    }
    return result
}
```

---

**Source:**

LeetCode: [Combination-Sum](https://leetcode.com/problems/combination-sum/)
