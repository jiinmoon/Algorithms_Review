# 139 Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

---

To determine whether the s can be broken into the words, we can use dynamic
programming to determine whether the prefix upto a certain point exist in the
words.

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
                # previous prefix upto s[:j] is in words
                # as well as current substr s[j:i] is in words
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
```
