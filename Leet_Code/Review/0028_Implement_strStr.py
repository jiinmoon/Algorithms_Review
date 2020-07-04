""" 28. Implement strStr()

Question:

    Implement strStr().

+++

Solution:

    Finding needle in a haystack has a variety of algorithms that has been
    studied extensively: KMP, Rolling-Hash, and so on.

    For this, we will use a simple matching - iterate on the given haystack,
    and compare each chunck of same length as needle.

"""

class Solution:
    def strStr(self, needle, haystack):
        lenHay, lenNee = len(haystack), len(needle)
        if not lenHay or not lenNee:
            return
        for i in range(lenHay - lenNee + 1):
            curr = haystack[i:i+lenNee]
            if curr == needle:
                return i
        return -1
            
            
