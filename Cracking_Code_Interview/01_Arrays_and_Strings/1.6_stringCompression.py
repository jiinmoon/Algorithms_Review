""" 1.6 String Compression

Question:

    Implement a method to perform basic string compression using the counts of
    repated characters. For example, the string aabcccccaaa would become
    a2b1c5a3. If the compressed string would not become smaller than the
    original string, your method should return the original string.

    You can assume the string has only uppercase and lowercase letters.

---

There is a very similar and popular question which is called 'Counter-and-Say';
simply put, we make the compressed string and compare its length against the
original string.

"""

class Solution:

    def compressString(self, s):
        if not s: return s
        compStr = []
        currPtr = 0
        while currPtr < len(s) - 1:
            currChar = s[currPtr]
            count = 1
            scanPtr = currPtr + 1
            while currChar == s[scanPtr]:
                counter += 1
                scanPtr += 1
            compStr.append(curChar, str(count))
            currPtr += scanPtr
        compStr = ''.join(compStr)
        return compStr if len(compStr) < len(s) else s

