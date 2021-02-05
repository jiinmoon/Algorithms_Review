# Combinations

    Given two integers n and k, return all possible combinations of k numbers out
    of 1 2 3 ... n.

    Make sure the combinations are sorted.

    To elaborate,

    Within every entry, elements should be sorted. [1, 4] is a valid entry while
    [4, 1] is not.

    Entries should be sorted within themselves.

---

## Approach:

We use backtrack to build our combinations down to the base case where we have
all candidates. For each recursive depth, we consider every candidate starting
from previous where the candidate has been chosen.

Time complexity is bounded by O(combinations(n choose k)) which is ((n!)/(k!)(n-k)!).

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
                    helper(i + 1, path + [i])

        result = []

        helper(0, [])

        return result
```


