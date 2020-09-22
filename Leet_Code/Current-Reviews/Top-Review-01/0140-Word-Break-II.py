# 140 Word Break II
#
# We use dynamic programming to determine whether the given string is
# decomposable into the given set of words. Then, we examine every prefix and
# suffix of the string to find all words.

class Solution:
    def isBreakable(self, S, words):
        m = len(S)
        dp = [False] * (m + 1)
        dp[0] = True

        for i in range(1, m+1):
            for j in range(i-1, -1, -1):
                if dp[j] and S[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]

    def breakStr(self, S, words, left, memo):
        if left >= len(S):
            return [[]]
        if left in memo:
            return memo[left]
        res = []
        for i in range(left+1, len(S)+1):
            prefix = S[left:i]
            suffixes = self.breakStr(S, words, i, memo)
            if prefix in words and suffixes:
                for suffix in suffixes:
                    res.append([prefix] + suffix)
        memo[left] = res
        return res

    def wordBreak(self, S, words):
        words = set(words)
        if not self.isBreakable(S, words):
            return []
        res = self.breakStr(S, words)
        return ["".join(r) for r in res]


