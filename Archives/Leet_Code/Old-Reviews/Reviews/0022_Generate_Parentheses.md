22 Generate Parentheses
=======================

Question:
---------

Given n pairs of parentheses, write a function to generate all posible
combinations of well-formed parentheses.

Solutions:
---------

We may use a backtracking algorithm to explore all possible paths that leads to
building our well-formed parentheses one-by-one. To do so, we need to know when
to terminate, and when to append more "open" or "closed" parentheses. In order
to keep track of these, our recursive backtracking function should take it in
its arguments its current number of "open" parentheses and the remaining number
of pair of parentheses to append to the path. Since each recursive call will
create two more, the resulting time complexity would be O(2^n).

Codes:
------

Python:

```python
class Solution:
    def generateParentheses(self, n):
        result = []

        def backtrack(pairCount, openCount, path):
            if not pairCount and not openCount:
                result.append(path)
                return
            if openCount:
                backtrack(pairCount, openCount-1, path + ')')
            if pairCount:
                backtrack(pairCount-1, openCount+1, path + '(')

        backtrack(n, 0, '')
        return result
```

---

**Source:**

LeetCode:
[Generate-Parentheses](https://leetcode.com/problems/generate-parentheses)
