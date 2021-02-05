# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

---

Python: Bottom Up recursion.

```python

class Solution46:

    def permute(self, nums):
        
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        
        result = []
        for i in range(len(nums)):
            for path in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + path)

        return result
```

Python: Top Down recursion.

```python

class Solution46:

    def permute(self, nums):

        def helper(candidates, path):
            if not candidates:
                result.append(path)
            else:
                for i in range(len(candidates)):
                    helper(candidates[:i] + candidates[i+1:], path + [candidates[i]])

        result = []

        helper(nums, [])

        return result
```
