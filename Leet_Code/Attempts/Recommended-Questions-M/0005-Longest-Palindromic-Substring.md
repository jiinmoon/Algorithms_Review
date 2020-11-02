# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Naive approach to this problem would be to first identify all possible
substrings of various lengths, and then check for the maximum possible
palindromic substrings amongst them. This would be a exhaustive search
algorithm that requires nested loops.

Better approach that can achieve the goal in O(n^2) time complexity would be to
realize the fact that we can treat each of the character in the given string
can be considered as a "centre" point of the palindromic substring; thus, we
simply iterate forward while expanding to left and right to find the maximum.

---

Python:

```python

class Solution:
    def longestPalindromicSubstring(self, s):
        longest = ""
        for i in range(len(s)):
            # take care of the case of even and odd length substrings
            s1 = self.expand(s, i, i)
            s2 = self.expand(s, i, i + 1)
            longest = max([longest, s1, s2], key=len)
        return longest

    def expand(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
```
