# Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

---

Starting from behind, we remove as many of whitespace characters. Then, so long
as we see alphabets, we count. O(n) in time complexity.

---

Python:

```python

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        
        i = len(A) - 1
        
        while i >= 0 and A[i] == " ":
            i -= 1
        
        result = 0
        
        while i >= 0 and A[i].isalpha():
            result += 1
            i -= 1
        
        return result

```
