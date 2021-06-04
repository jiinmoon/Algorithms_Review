# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

---

Simple approach to generate all possible permutations from the given set of
candidates would be to use backtrack to explore. At each depth, we choose the
candidate the add to our path. The end condition would be when we have
exhausted the candidates in which case we can add the path to our result. The
time and space complexity is equal to number of permutations as per permutation
formula.

---

Python:

```python

class Solution46:

    def permute(self, candidates):

        def backtrack(path, candidates):

            if not candidates:
                result.append(path)
            else:
                for i in range(len(candidates)):
                    backtrack(path + [candidates[i]], candidates[:i] + candidates[i+1:])

        result = []
        backtrack([], candidates)

        return result
```
