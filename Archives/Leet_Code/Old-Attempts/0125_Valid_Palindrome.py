""" 125. Valid Palindrome

Question:

    Given a string, determine if it is a palindrome, considering only
    alphanumeric characters and ignoring cases.

"""

class Solution:
    def isPalindrome(self, s):
        # we can clean up the original string; but we will assume that we do not
        # wish to modify the given string.
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
