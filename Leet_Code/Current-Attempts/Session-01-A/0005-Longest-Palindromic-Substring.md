# 5 Longest Palindromic Substring

Instead of the naive approach of exaimning all possible substrings - O(n^3), we
treat each of the index as a centre of the palindrome and expand out as far out
as possible.

---

Python:

```python

class Solution:
    def expand(self, S, start, end):
        while start >= 0 and end < len(S) and S[start] == S[end]:
            start += 1
            end -= 1
        return S[start+1:end]

    def longestPalinSubstr(self, S):
        longest = ""
        for i in range(len(S)-1):
            s1 = self.expand(S, i, i)
            s2 = self.expand(S, i, i+1)
            longest = max([longest, s1, s2])

        return longest
```
