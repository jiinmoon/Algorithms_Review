# 727 Minimum Window Subsequence

class Solution:
    def minWindowSubseq(self, S, T):
        nextInS = [[-1 for _ in range(26)] for _ in range(len(S))]
        for i in range(len(S)-1, -1, -1):
            nextInS[i][ord(S[i]) - ord('a')] = i

        windows = [ (i,i) for i, c in enumerate(S) if c == T[0] ]
        if not windows:
            return ""

        for char in T[1:]:
            temp = list()
            for start, end in windows:
                newEnd = nextInS[end][ord(char) - ord('a')]
                if newEnd >= 0:
                    temp.append(start, newEnd)
            if not temp:
                return ""
            windows = temp

        start, end = min(windows, key=lambda w: w[1] - w[0])
        return S[start:end]
