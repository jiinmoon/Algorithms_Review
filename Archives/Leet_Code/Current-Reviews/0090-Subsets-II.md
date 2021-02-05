# 90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

---

Use backtracking to discover all power set of given candidates. Since it may
have duplicate, we avoid selecting the duplicate by making our result
collection a set.

---

```python

class Solution90:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start, path):
            if tuple(path) not in result:
                result.add(tuple(path))
                for i in range(start, len(nums)):
                    backtrack(i + 1, path + [nums[i]])
                
        nums.sort()

        result = set()
        backtrack(0, [])

        return result
```
