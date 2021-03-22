# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

---

We can generate n pairs of parentheses using backtracking to build our paths
down to end goal where we have all possible combinations of the well-formed
parentheses.

To generate, we have to consider what must occur at each of the depths. At each
depth, we should be building our parentheses out - by either appending a new
open or closing bracket.

As every open bracket should have a matching bracket, we should have a variable
to track the number of open brackets currently in the path; also, we need to
track how many pairs have been added to our path so far such that we know when
to terminate.

---

Python:

```python

class Solution22:

    def generateParen(self, n):

        def backtrack(path, open, closed):
            
            # end condition
            if not open and not closed:
                result.append(path)
                return
            
            # open backet should have matching closing braket
            if open:
                backtrack(path + ")", open - 1, closed)
            
            # more pairs to add
            if closed:
                backtrack(path + "(", open + 1, closed - 1)
        
        result = []
        backtrack("", 0, n)

        return result
```

