""" 139. Word Break

Question:

    Given a non-empty string s and a dictionary wordDict containing a list of
    non-empty words, determine if s can be segmented in a space-separated
    sequence of one or more dictionary words.

"""

class Solution:
    def wordBreak(self, s, wordDict):
        m = len(s)
        DP = [0] * (m + 1)
        DP[0] = 1
        for i in range(1, m+1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word:
                    DP[i] |= DP[i - len(word)]
        return DP[m]
