# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

---

We can create a well form parentheses using recursion to build the path at each
step based on how many open parentheses were added previously and how many more
pairs of parentheses are to be added.

Note on the time complexity; at each depth, two more recursive calls can be
generated. Hence, this is O(2^n) in both time and space complexity.

---

Python:

```python

class Solution:
    def generateParentheses(self, n):
        def helper(path, open, pairs):
            if open == pairs == 0:
                result.append(path)
                return
            if open:
                helper(path + ")", open - 1, pairs)
            if pairs:
                helper(path + "(", open + 1, pairs - 1)

        result = list()
        helper("", 0, n)

        return result
```
