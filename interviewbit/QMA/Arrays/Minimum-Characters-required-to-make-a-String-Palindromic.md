# Minimum Characters required to make a String Plaindromic

Given an string A. The only operation allowed is to insert characters in the
beginning of the string.

Find how many minimum characters are needed to be inserted to make the string
a palindrome string.

---

### (1) Reverse and concat prefix of reverse vs suffix of original.

Reverse the given string. Then we can check to see whether

    reverse[:i] + original == original[:i] + reverse

is true. If so, we return i.

### (2) Longest Proper Prefix/Suffix array.

By using LPS array of KMP; we can find the proper prefix of the concatenated
string of orignal + reverse. The amount that differs from length of original to
last value of lps or properly matching prefix count will be the difference
required to make it palindrome.

---

Python: Reverse and concat.

```python

class Solution:

    def solve(self, A):
        
        reversed = A.reverse()

        if A == reversed:
            return 0

        for i in range(1, len(A)):
            if reversed[:i] + A == A[:i] + reversed:
                return i
        return 0

```

Python: LPS.

```python

class Solution:

    def solve(self, A):

        concat = A + "." + A[::-1]
        lps = [0] * len(concat)
        i, length = 1, 0

        while i < len(concat):
            if concat[i] == concat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return len(A) - lps[-1]

```
