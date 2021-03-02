# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

---

Since we have to generate all possible permutations, the time complexity would
be of O(n!) where in first position we have n possibilities, and our next
choices will decrease by one. `(n)(n-1)(n-2)...(1)`.

To generate, we can use backtracking algorithm. Our base case would be when our
candidates have been all exhausted, in which case we can return empty array.
Otherwise, for every position, we select the candidate and update the next
possible candidates by extracting the chosen candidate to avoid selecting
duplicate.

---

Python:

```python

class Solution46:

    def permute(self, nums):
        
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        result = []
        for i in range(len(nums)):
            # for every possible candidate chosen
            # we recursively build our path
            # returned paths will be expanded with chosen candidate bottom-up
            for path in self.permute(nums[:i] + nums[i+1:]):
                result.append([nums[i]] + path)

        return result
```
