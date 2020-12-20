# Generate all Parentheses II

    Given n pairs of parentheses, write a function to generate all combinations of
    well-formed parentheses of length 2*n.

---

## Approach:

Use backtrack to discover while keep tracking the number of open and closed
parentheses added to current path. So long as we have few open parentheses
added than target n, we add "("; also, if we have more open parentheses than
the closing ones, we add ")" and recurse.

O(2^n) in time complexity as we have choice of adding parentheses or not at
every step.

---

Python:

```python

class Solution:

    def generateParen(self, n):

        def helper(open, closed, path):

            if len(path) == 2 * n:
                result.append(path)
                return

            if open < n:
                helper(open + 1, closed, path + "(")

            if closed < open:
                helper(open, closed + 1, path + ")")

        result = []

        helper(0, 0, "")
        
        return result
```
