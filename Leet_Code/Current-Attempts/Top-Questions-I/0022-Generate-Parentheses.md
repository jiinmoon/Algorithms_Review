# 22 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

---

We may use DFS to explore all possible combinations of well-formed parentheses.
To do so, we need to maintain at each depth the current number of open
parentheses and remaining parentheses to form.

---

Python:

```python

class Solution:
    def generateParentheses(self, n):
        def helper(openCount, pairCount, path):
            if openCount == pairCount == 0:
                result.append(path)
                return
            if openCount:
                helper(openCount - 1, pairCount, path + ")")
            if pairCount:
                helper(openCount + 1, pairCount - 1, path + "(")
        
        result = list()
        helper(0, n, "")
        return result
```
