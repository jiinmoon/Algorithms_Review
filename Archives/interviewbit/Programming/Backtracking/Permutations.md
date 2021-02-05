# Permutations

    Given a collection of numbers, return all possible permutations.

---

## Approach:

Use backtracking to discover all possible permutations; at each recursion
depth, we choose the every possible choice of candidate, and reduce the
possible candidates without the chosen candidate to recurse.

O(2^n) in time complexity due to having to explore all possible permutations.

---

Python:

```python

class Solution:

    def permute(self, A):
        
        if len(A) == 1:
            return [A]

        result = []

        for i in range(len(A)):
            permutations = self.permute(A[:i] + A[i+1:]
            for p in permutations:
                result.append(p + [A[i]])

        return result
```


