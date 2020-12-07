# 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

---

### (1) Brute Force.

A simple method would be to generate all possible substrings - check all
substrings from size 2 to length of s, then continuously check for longest
palindromic substring. It takes O(n^2) to consider substrings and for each
substring, it would take additional O(n) to check for palindrome. Hence, time
complexity would be O(n^3) but space would be O(1).

### (2) Iteratively expand about mid-point.

Instead of considering every possible substring, we just try to expand from
every index that we consider. Here, we have to be careful to include both even
and odd length of palindromes. Since there are O(n) mid-points to consider and
O(n) time to expand from these points, total time complexity would be O(n^2).
Space complexity would be constant.

---

Python: expand about mid-point.

```python

class Solution5:

    def longestPalindrome(self, s):

        if not s or len(s) < 2:
            return s

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        longest = ""

        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i+1)
            longest = max([longest, s1, s2], key=len)

        return longest
```

Python: brute-force (times-out).

```python

class Solution5:

    def longestPalindrome(self, s):
        
        if not s or len(s) < 2:
            return s

        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    longest = max(longest, s[i:j], key=len)

        return longest
```
