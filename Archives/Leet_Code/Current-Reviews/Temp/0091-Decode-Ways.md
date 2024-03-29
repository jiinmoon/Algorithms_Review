# 91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of
ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

---

### (1) Dynamic Programming.

We define our dp array as follows:

    Let dp at i-th index to be maximum number of ways to decode s upto i-th.
    Then, we have two cases as we iterate on the string:

    (1) Current char at i is NOT '0'.

        If current char at i is not '0', we can form a decoding map by itself
        in single digit case; hence, we move over the previous value.

            DP[i + 1] = DP[i]

    (2) Last two characters can form number between 10 and 26.

        In this case, we have another way to decode our string. Hence, we move
        over the maximum values from two previous cases ago.

            DP[i + 1] += DP[i - 1]

In this case, we can complete the algorithm in O(n) time complexity and
requires O(n) space for our dp array.

### (2) Dynamic Programming improved.

We can still improve on our space complexity down to O(1) since when we look at
our dp definition, `dp[i + 1]` ever depends upon two previous cases. Hence,
instead of entire dp array, we only have to store two previous variables.

### (3) Backtracking with memoization.

We can use backtracking algorithm to try out all different possible ways to
decode the string. At every index, we try to check for single and two digit
cases. Since there can be duplicate solutions exist and we can arrive at same
indicies while exploring all possible ways, we can record solutions to the
subproblems to reduce time complexity. This would be O(n) in both time and
space compleixty.

---

Python: DP with O(1) space.

```python

class Solution91:

    def numDecoding(self, s):

        if not s:
            return 0

        prevPrev = 1
        # include the case where s starts with '10'
        prev = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):

            temp = 0

            if s[i-1] != '0':
                temp = prev
            if 10 <= int(s[i-2:i]) <= 26:
                temp += prevPrev

            prevPrev = prev
            prev = temp

        return prev
```

Python: DP with O(n) space.

```python

class Solution91:

    def numDecodings(self, s: str) -> int:

        if not s: 
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        # case s = '10'
        if s[0] != '0':
            dp[1] = 1
        
        for i in range(1, len(s)):
            if s[i] != '0':
                # ignore current char and move over previous
                dp[i+1] = dp[i]
            if 10 <= int(s[i-1:i+1]) <= 26:
                # if last two chars can form num between 10, 26
                # ignore last two chars
                dp[i+1] += dp[i-1]
        
        return dp[-1]
```

Python: Backtracking with memoization.

```python

from functools import lru_cache

class Solution91:

    def numDecodings(self, s):

        if not s:
            return 0
        
        @lru_cache(None)
        def helper(i):
            # base cases:
            # 1. reached the end of string
            # 2. current char is '0'; is not mapped to any decodings
            # 3. cannot extend further to try for two digits

            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s)-1:
                return 1
            
            result = helper(i+1)                # single digit case
            if 10 <= int(s[i:i+2]) <= 26:
                result += helper(i+2)           # double digit case

            return result

        return helper(0)
```
