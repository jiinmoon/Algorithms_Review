# 1423 Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints, k):
        size = len(cardPoints) - k
        currSum = sum(cardPoints[:size])
        minSum = currSum
        for i in range(1, len(cardPoints) - size + 1):
            currSum += cardPoints[i+size-1] - cardPoints[i-1]
            minSum = min(minSum, currSum)
        return sum(cardPoints) - minSum
