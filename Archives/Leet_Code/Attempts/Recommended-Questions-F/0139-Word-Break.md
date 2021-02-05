# 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.

You may assume the dictionary does not contain duplicate words.

---

To determine whether the given string s is composed of the words that can be
found within the dictionary, we break down the problem into subproblem where
the prefix upto j-th position has been identified as a composable, and if the
suffix of substring s[j:i] in the dictionary, both marks the next position in
upto s[:i] as composable. The time complexity of this algorithm is O(n^3) since
we need to consider every substring.

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
