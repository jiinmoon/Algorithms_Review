""" 1.9 String Rotation

Question:

    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a
    rotation of s1 using only one call to isSubstring.

---

This is a bit of a brain teaser. The naive approach would be of course generate
all the possible rotation to check whether s2 is a rotation of s1. But this
would not require a call to isSubstring method; and the question specifically
asks you to use it and use it only once. This is the important point.

Notice the following; when you concatenate the two strings together, you
discover that the original string must be within the concatenate string
somewhere regardless of its rotation.

"""

class Solution:

    def stringRotation(self, s1, s2):
        return s1 in s2 + s2
