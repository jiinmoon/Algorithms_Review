516 Longest Palindromic Subsequence
===================================

Given a string s, find the longest palindromic subsequence's length in s.

---

We may use the dynamic programming here - the idea here is to iterate over the
s and maintain subsequences of len(s) - 1 and len(s) - 2 for each on the
indexes as the starting point in the s. In other words, we will mantain the
previous palindromic subsequences starting at each index which are current
length of -1 and -2.

Then, we examine all possible subsequence lengths from 2 to n + 1. For each
length, we have starting index - and when the starting index char is same as
ending char, we know that max length is the 2 + length without the ending
character (prev).

---

Python:

```python

class Solution:
    def longestPlaindromeSubseq(self, s):
        if not s or s == s[::-1]:
            return len(s)

        m = len(s)
        # dp - lengths of previous iterations.
        # each for subseq length - 1 and length - 2.
        prevSub = [1] * m
        prevPrevSub = [0] * m

        # expand for each length
        for currLength in range(2, m + 1):
            # current subsequences
            currSub = list()
            # examine each starting index
            for i in range(n - currLength + 1):
                # new starting index is same as ending char
                if s[i] == s[i + currLength - 1]:
                    # new length is 2 + previous of previous length
                    currSub.append(2 + prevPrevSub[i+1])
                else:
                    # if not, carry over from prev length
                    currSub.append(max(prevSub[i], prevSub[i+1]))

            prevPrevSub = prevSub
            prevSub = currSub

        return currSub[0]
```

