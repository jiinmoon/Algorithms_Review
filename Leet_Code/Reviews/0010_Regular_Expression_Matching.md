10 Regular Expression Matching
==============================

Question:
---------

Implement regular expression matching with support for wildcard characters '.'
and '\*'.

    '.' matches any single character.
    '*' matches zero or more of preceding element.

Solutions:
---------

For this problem, we may use dynamic programming. For given text and pattern,
we define our 2-D dp table at (i, j) to be a match so long as previous cases
has been a match (i.e. text[:i] matches the pattern[:j]).

The issue is with the wildcard characters. In the case of '.', this is
a non-issue since we can match any char to '.'; thus, this is simply an
automatic pass and `dp[i][j]` would be a match if the previous iteration
`dp[i-1][j-1]` has been a match.

In the case if '\*', it requires a bit more thought. Here, we have two
conditions that we need to check for: (1) zero matching case; and (2) text
matches the pattern's preceding star'd character. Hence, we either check for
whether `dp[i][j-2]` was a match or `dp[i-1][j]` was a match. Also, it is
entirely possible that preceding element of star was '.', so it must be
considered as well.

In short, the cases are as follows:

```
    if pattern[j-1] == '.':
        dp[i][j] = (i > 0 and dp[i-1][j-1])
    elif pattern[j-1] == '*':
        star_element = pattern[j-2]
        dp[i][j] = dp[i][j-2] or \
                    (i > 0 and dp[i-1][j] and \
                        (star_element == text[i-1] or \
                            star_element == '.'))
    else:
        dp[i][j] = i > 0 and dp[i-1][j-1] and text[i-1] == pattern[j-1]
```

This would be O(n * m) in both time and space complexity where n and m are
length of the text and patterns.

Codes:
------

```python
class Solution:
    def isMatch(self, text, pattern):
        m, n = len(text), len(pattern)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
    
        for i in range(m+1):
            for j in range(1, n+1):
                curr = pattern[j-1]
                if curr == '.':
                    dp[i][j] = (i > 0 and dp[i-1][j])
                elif curr == '*':
                    star_element = pattern[j-2]
                    dp[i][j] = (i > 0 and dp[i-1][j]) and \
                        (star_element == text[i-1] or \
                         star_element == '.')
                else:
                    dp[i][j] = (i > 0 and dp[i-1][j-1]) and curr == text[i-1]
        return dp[-1][-1]
```




---


**Source:**

LeetCode: [Regular-Expression-Matching](https://leetcode.com/problems/regular-expression-matching/)
