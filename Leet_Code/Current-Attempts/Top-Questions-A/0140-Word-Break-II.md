# 140 Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.

---

Once we check that the string s can be indeed decomposable into the words using
the dynamic programming method from #139, we may use recursion to explore the
given string. To be precise, we continuously divide the given string into
several prefix and suffixes at every possible locations - and since there will
be duplicated works, we may also imploy memoization technique to reduce further
time complexity down.

---

Python:

```python

class Solution:
    def isDecomposable(self, s, words):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

    def wordBreak(self, s, words):
        words = set(words)
        if not self.isDecomposable(s, words):
            return []
        res = self.decompose(s, words, 0, {})
        return ["".join(r) for r in res]

    def decompose(self, s, words, left, memo):
        if left >= len(s):
            return [[]]
        if left in memo:
            return memo[left]
        res = []
        for i in range(left+1, len(s)+1):
            prefix = s[:i]
            suffixes = self.decompose(s, words, i, memo)
            if prefix in words and suffixes:
                for suffix in suffixes:
                    res.append([prefix] + suffix)
        memo[left] = res
        return res
```
