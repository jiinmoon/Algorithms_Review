""" 3. Longest Substring Without Repeating Characters

Question:

    Given a string, find the length of the longest substring without repeating
    characters.

+++

Solution:

    We simply try to build the longest substring without the repeating
    characters. When we are building substring and encounter a repeat, then we
    know that this is the one possible candiddate for our longest substring
    without a repeat. Hence, we record its length, and adjust our substring by
    deleting the prefix upto the where rpeat has been found and continue with
    our search.

"""

class Solution:
    def findLongestSubstringWithoutRepeat(self, s):
        if not s:
            return 0
        longestThusFar = 0
        currS = []
        for char in s:
            if char in currS:
                currS = currS[currS.index(char)+1:] + [char]
            else:
                currS += [char]
            longestThusFar = max(longestThusFar, len(currS))
        return longestThusFar

