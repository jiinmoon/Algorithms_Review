# 1239 Max Length of a Concatenated String with Unique Characters
#
# Order does not matter - what is important here is the number of unique
# characters; use Set structure to our advantage.

class Solution:
    def maxLength(self, A):
        charToSets = [set(s) for s in A if len(set(s)) == len(s)]
        DP = [ set() ]
        for currSet in charToSets:
            for prevSet in DP.copy():
                newSet = prevSet | currSet
                if len(newSet) == len(prevSet) + len(currSet):
                    DP.append(newSet)

        return len(max(DP, key=len))
