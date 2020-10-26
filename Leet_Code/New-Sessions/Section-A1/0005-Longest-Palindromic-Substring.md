# 5 Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Naively, we may consider substring of every size from 2 to length of the given
string to check whether the substring is a palindromic substring or not; and
find the longest one amongst thus far. This is an exhaustive search involving
nested loop that much can be improved.

One way to improve time complexity of this algorithm is that we may consider
each of the character as a centre of the substring - and expand out to left and
right until it is a palindrome.

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
            s2 = self.expand(s, i, i + 1)
            longest = max([longest, s1, s2], key=len)
        return longest
```
