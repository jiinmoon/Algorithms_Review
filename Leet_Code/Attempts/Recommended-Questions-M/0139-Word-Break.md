# 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.

---

We can breakdown the main problem into a several subproblems which can be
combined to give us a result. For this, we can use dynamic programming
approach. For each index, we check to see whether previous characters upto that
ending index has been identified as possible segementation of the dictionary
words. This would require O(n) in both space and time complexity.

---

Python:

```python

class Solution:
    def isBreakable(self, words, s):
        words = set(words)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
```
