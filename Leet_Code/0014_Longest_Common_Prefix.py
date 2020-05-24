""" 14. Longest Common Prefix

Question:

    Write a function to find the longest common prefix string amongst an array
    of strings. If there is none, return an empty string.

"""

class Solution:
    def findLCA(self, strs):
        if not strs:
            return ''
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        return first[:i]
