# 91 Decode Ways

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1 ... 'Z' -> 26

Given a non-empty string containing only digits, determine the total number of
ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

---

We can approach this problem with a dynamic programming - that is, at each
index, we compute the number of ways that s[:i] can be decoded by checking the
s[:i-1] and s[:i-2].

---

Python:

```python

class Solution:
    def numDecodings(self, s):
        if not s: return 0
        
        # set dp and initial condition
        # account for case s starting with '10'
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if dp[0] != '0':
            dp[1] = 1

        for i in range(1, len(s)):
            # 1) current char is not 0; ignore current char
            if s[i] != '0':
                dp[i+1] += dp[i]
            # 2) last two chars makes a possible two digit (10 ~ 26)
            # ignore last two chars
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]

        return dp[-1]
```
