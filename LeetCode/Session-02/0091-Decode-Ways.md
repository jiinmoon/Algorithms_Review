# 91. Decode Ways

A message containing letters from A-Z can be encoded into numbers using the
following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above (there may be multiple
ways). For example, "11106" can be mapped into:

```
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
```

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode
it.

The answer is guaranteed to fit in a 32-bit integer.

---

Here, we are interested in total number of ways to decode the given digits. For
every digit, we can iterpret it as a "single" case which is from "1" to "9" and
"double" case which spans from "11" to "26".

Hence, we can use backtracking algorithm to explore all possibilities so long
as we can start from each depth - each index position, we try to add the number
of ways we can decode by combining single and double cases whilst checking
whether single and double cases falls within the range (i.e. single case cannot
be zero, and double case must be within range 11 ~ 26).

As there will be duplicated works possible and for each position, max number of
ways to decode is fixed, we can use memoization technique to reduce the time
complexity down.

---

Python:

```python

from functools import lru_cache

class Solution91:

    def numDecodings(self, s):

        @lru_cache(None)
        def backtrack(i):
            # check for end and single case
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i == len(s) - 1:
                return 1

            result = backtrack(i+1) + (backtrack(i+2) if int(s[i:i+2]) <= 26 else 0)

            return result

        if not s:
            return 0

        return backtrack(0)
```
