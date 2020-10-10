# 5 Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Naive approach would be to consider every possible substring to check for
whether the string is palindrome or not. Better solution would be to iterate on
the string s, and consider each character as a "centre" point of the
paldinrome. Thus, all we need to do is expand as far out as possible to find
the longest palindrome that can be formed from this centre.

---

Python:

```python

class Solution:
    def expand(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]

    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            longest = max([longest, s1, s2], key=len)
        return longest
```
