# 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.

---

To determine whether the given string s can be broken down as a list of words
containing in the given wordDict, we may use dynamic programming to identify.
Whether a given substring is thus far fit the criteria is determined by the dp
array upto that index j where s[j:i] is the current substring considered.

---

Python:

```python

class Solution:
    def wordBreak(self, s, words):
        words = set(words)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
```
