""" 3. Longest Substring Without Repeating Characters

Question:

    Given a string, find the length of the longeset substring without repeating
    characters.

+++

Solution:

    We try to build the substring as we iterate along the given string. Once we
    encounter repeat, we know that we have an candidate and record its length.
    Then, new substring begins from where the repeat char has been found.

"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        currS = []
        longestThusFar = 0
        for char in s:
            if char not in currS:
                currS += [char]
            else:
                currS = currS[currS.index(char)+1:] + [char]
            longestThusFar = max(len(currS), longestThusFar)
        return longestThusFar
