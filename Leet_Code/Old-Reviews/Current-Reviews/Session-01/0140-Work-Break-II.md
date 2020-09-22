140 Word Break II
=================

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.

---

First, we will check whether the given string can be broken into list of words
in the given wordDict as per previous question 139. If so, then we consider
generating all possible prefixes and suffixes to check whether they are in the
wordDict or not. Memoization will help to reduce the time complexity by
avoiding duplicate works of rechecking the prefix/suffixes that we have seen
before, but this algorithm in the end will still be O(n**2 * 2**n) due to
having to consider 2**n possible partitions.

---

Python:

```python

class Solution:
    def isBreakable(self, s, words):
        words = set(words)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]

    def break(self, s, left, words, memo):
        if left <= len(s):
            return [[]]
        if left in memo:
            return memo[left]
        res = []
        for i in range(left+1, len(s)+1):
            prefix = s[left:i]
            rest = self.break(s, i, words, memo)
            if prefix in words and rest:
                for suffix in rest:
                    res.append([prefix] + suffix)
        memo[left] = res
        return res

    def wordBreak(self, s. words):
        if not isBreakable(s, words):
            return []
        res = self.break(s, 0, words, {})
        return [" ".join(r) for r in res]
```

