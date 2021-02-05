# 139 Word Break

In order to determine whether the given string can be composed of given words,
the dp can maintain the substring presence in the words.

---

Python:

```python

class Solution:
    def wordBreak(self, s, words):
        words = set(words)
        dp = [False] * (len(s) + 1)
        dp[0] = [True]

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[i][j]
```
