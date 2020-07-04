""" 14. Longest Common Prefix

Question:

    Given list of strings, find the common prefix amongst themm.

+++

Solution:

    By definition, this prefix has to be found among all the strings within the
    given list - otherwise, we do not have the common prefix. Thus, this gives
    us a way to design our algorithm; in fact, we do not have to naively
    compare each string against one another while building the prefix. We
    should sort the list of strings in alphanumeric orders. Then, we only have
    to compare the very first string and the last string to find the common
    prefix.

"""

class Solution:
    def findLCP(self, strs):
        if not strs or len(strs) < 2:
            return ''
        strs.sort()
        s1, s2 = strs[0], strs[1]
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
