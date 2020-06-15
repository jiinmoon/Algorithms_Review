""" 205. Isomorphic Strings """

class Solution:
    def isIsomorphic(self, s, t):
        if not s or not t:
            return True
        charMap = {}
        for i in range(len(t)):
            if s[i] in charMap:
                # have we seen s[i] before?
                if charMap[s[i]] != t[i]:
                    # if we did, but is not mapped correctly.
                    return False
            else:
                # t[i] should have not been mapped to any other char in s;
                # hence, it should not be in the charMap's values.
                if t[i] in charMap.values():
                    return False
                else:
                    charMap[s[i]] = t[i]
        return True
