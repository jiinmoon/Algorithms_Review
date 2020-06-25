""" 1.3 URLify

Question:

    Write a method to replace all spaces in a string with '%20'. Assume that the
    string has sufficient space at the end to hold the additional characters,
    and that you are given the true length of the string.

---

An excercise of how fluent the one is with the particular languages string
manipulation method. The langauges such as C or Java will have to jump through
more difficult loops to edit the strings (given that we cannot use the already
exisiting APIs).

"""

class Solution:

    def URLify_1(self, s, n):
        """ using inherent string functionality """
        if not s: return s
        return s.strip().replace(' ', '%20')

    def URLify_2(self, s, n):
        """ modifying without using the functionalty """
        if not s: return s
        """ we know that insert pointer since we assume that the string already
        has computed the correct number of extra space. if this is not the case,
        then we will first have to scan the string for number of empty spaces
        and compute the correct insert position"""
        scanPtr, insPtr = n, len(s)-1
        s = list(s) # string itself is immutable; convert to list
        while scanPtr > 0:
            currChar = s[scanPtr]
            if currChar == " ":
                s[insPtr] = "0"
                s[insPtr-1] = "2"
                s[insPtr-2] = "%"
                insPtr -= 3
            else:
                s[insPtr] = currChar
                insPtr -= 1
            scanPtr -= 1
        return ''.join(s)
