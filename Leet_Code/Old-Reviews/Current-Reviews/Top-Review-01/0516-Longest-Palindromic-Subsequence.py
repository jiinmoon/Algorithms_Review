# 516 Longest Palindromic Subsequence
#
# Prepare a set of previous lengths of longest palindromic subsequences begin
# at each index (length-1, and length-2).
#
# For each possible subsequence length, we expand out.

class Solution:
    def longestPalindromicSubseuqnece(self, s):
        m = len(s)
        if s == s[::-1]:
            return m

        prevPrevSub = [0] * m
        prevSub = [1] * m

        for length in range(2, n + 1):
            currSub = list()
            for i in range(n - length + 1):
                if s[i] == s[i+length-1]:
                    currSub.append(2 + prevPrevSub[i-1])
                else:
                    currSub.append(max(prevSub[i], prevSub[i+1]))

            prevPrevSub = prevSub
            prevSub = currSub

        return currSub[0]

