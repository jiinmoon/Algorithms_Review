# Subsets II

    Given a collection of integers that might contain duplicates, S, return all
    possible subsets.

    Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
    The subsets must be sorted lexicographically.

---

## Approach:

Because of the duplicates, we can create duplicate subsets while backtracking.
Hence, we use hashmap or set data structure to check whether we have already
seen the path that we are building exists in the result already; if so, we
return. Otherwise, we continue to add the path to our result and recursively
add all numbers to the path. As noted, we should sort the given nums.

---

Python:

```python

class Solution:

    def subsets(self, nums):

        def helper(start, path):

            if tuple(path) in result:
                return

            result.add(tuple(path))

            for i in range(start, len(nums)):
                helper(i + 1, path + [nums[i]])

        result = set()

        nums.sort()

        helper(0, [])

        return sorted(list(result))
```
