# 5 Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

---

Naive approach of considering every possible substring to check for the
palindrome is O(n^3) in time complexity.

We can instead change our approach to where we consider each element of the
string as a "centre" point of the substring, where we can expand-out as far
aout as possible. This is O(n^2) in time complexity.

---

Python:

```python

class Solution:
    def expand(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start += 1
            end -= 1
        return s[start+1:end]

    def longestPalindromicSubstr(self, s):
        longest = ""
        for i, char in enumerate(s):
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i+1)
            longest = max([longest, s1, s2])
        return longest
```
