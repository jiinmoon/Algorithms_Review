# Combinations

Given two integers n and k, return all possible combinations of k numbers out
of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while
[4, 1] is not.

Entries should be sorted within themselves.

---

Backtrack to discover k possibilities as we iterate from 1 to n.

Time complexity is as much as discovering k combinations from 1 to n (k * C) as
well as space complexity is same to retain all combinations discovered.

---

Python:

```python

class Solution:

    def combinations(self, n, k):

        def helper(start, path):

            if len(path) == k:
                result.append(path)
            else:
                for i in range(start, n + 1):
                    helper(i+1, path + [i])

        result = []
        helper(1, [])

        return result
```
