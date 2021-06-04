# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

Naive solution would be to consider every substring starting from size 2 and
check for whether the substring is a palindrome whilst recording the longest
palindromic substring that we have seen thus far. This involves nested loop
that at minimum would be O(n^3) in time complexity.

We can improve upon this by considering each of the position in the given
string as a "centre" point of the palindromic substring. Hence, we only have to
expand to left and right on each of the centre point so long as it is
a palindrome, so our time complexity is vastly improved for average case.
However, in worst case, the time complexity would be O(n^2).

The edge case here to watch out for would be to check for even and odd length
palindrome.

---

Python: Naive brute force approach.

```python

# times out in leetcode

class Solution5:

    def longestPalindromicSubstring(self, s):

        if not s or len(s) < 2:
            return ""

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    longest = max([longest, substr], key=len)

        return longest
```

Python: Centre expansion approach.

```python

class Solution5:

    def longestPalindromicSubstring(self, s):

        if not s or len(s) < 2:
            return ""

        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]

        longest = ""

        for i in range(len(s)):
            # odd and even case
            s1 = expand(i, i)
            s2 = expand(i, i + 1)
            longest = max([longest, s1, s2], key=len)

        return longest
```
