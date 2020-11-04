# 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.

---

We can check for the valid palindrome by using two pointer method and comparing
the first and last characters each time. This can complete the process in O(n)
time complexity.

---

Python:

```python

class Solution:
    def isValidPalindrome(self, s):
        lo, hi = 0, len(s) - 1
        # ignore cases
        s.lower()
        while lo < hi:
            # ignore non-alphanumeric characters
            while lo < hi and not s[lo].isalnum:
                lo += 1
            while lo < hi and not s[hi].isalnum:
                hi -= 1
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
```
