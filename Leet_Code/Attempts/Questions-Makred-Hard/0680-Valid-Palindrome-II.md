# 680. Valid Palindrome

Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

---

Notice here that we can make at most a single deletion to correct this. Rather
than naive approach of considering every deletion point to check for
correctness of the palindrome, all we have to do is find the first discrepency,
and fix that particular point instead. This will reduce the time complexity
down to O(n).

---

Python:

```python

class Solution:
    def validPalindrome(self, s):
        m = len(s)
        i = 0

        while i < m // 2:
            if s[i] != s[m-i-1]:
                removeFront = s[i+1:m-i]
                removeBack = s[i:m-i-1]
                return removeFront == removeFront[::-1] or removeBack == removeBack[::-1]
            i += 1

        return True
```
