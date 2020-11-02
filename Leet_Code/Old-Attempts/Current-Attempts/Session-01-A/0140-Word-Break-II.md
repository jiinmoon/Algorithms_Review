# 140 Word Break II

We recursively divide the given string into prefix and suffixes. So long as
prefix can be found in the words, we can add to our result. Since repeated
works are possible, we use memoization to save recomputing works.

---

Python:

```python

class Solution:
    def isBreakable(self, s, words):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(words)):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak(self, s, words):
        words = set(words)
        if not self.isBreakable(s, words):
            return []
        res = self.breakStr(s, words, 0, {})
        return ["".join(r) for r in res]

    def breakStr(self, s, words, left, memo):
        if left >= len(s): return [[]]
        if left in memo: return memo[left]

        res = list()
        for i in range(1, len(words)):
            prefix = word[:i]
            suffixes = self.breakStr(s, words, i, memo)
            if prefix in words and suffixes:
                for suffix in suffixes:
                    res.append([prefix] + suffix)

        memo[left] = res
        return res
```
