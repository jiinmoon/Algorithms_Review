# 1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated
number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.

---

Finding the maximum score from the given row of cards, we can approach this
problem in inverse - that is find the "minimum" contiguous window sum of card
points. Then, we can find the max score by subtracting minimum sum from the total
sum of card points.

---

Python:

```python

class Solution:
    def maxScore(self, cardPoints, k):
        winSize = len(cardPoints) - k
        minWinSum = sum(cardPoints[:winSize])
        # current window sum
        temp = minWinSum
        for i in range(1, len(cardPoints) - winSize + 1):
            # take away start and add in end to current window
            temp = temp - cardPoints[i - 1] + cardPoints[i + windSize - 1]
            minWinSum = min(minWinSum, temp)
        return sum(cardPoints) - minWinSum
```

