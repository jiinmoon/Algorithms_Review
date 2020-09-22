1423 Maximum Points You Can Obtain from Cards
=============================================

There are several cards arranged in a row, and each card has an associated
number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.

---

The important point here is that we can take from either beginning or the end
- and repeat this K times.

Then, the problem is about finding the window within the given array where its
size is len(A) - k that has minimum sum such that maximizes the elements
outside of its bound (which has K elements outside).

For example: Given `A = [100, 40, 17, 9, 73, 75]`, we start from the leftmost
window from `A[:len(A)-k]` which would be `[100, 40, 17]`. Then, we iterate on
right, adding a new element and taking out the last element. The next step
would add `9` and subtract `100`. Among these, we wish to find the "minimum"
sum such that maximizes the outside value.

---

Python: sliding window approach.

```python
class Solution:
    def maxScore(self, cardPoints, k):
        if not cardPoints or not k: return
        m = len(cardPoints)

        # starting window (same as picking all k from right)
        temp = sum(cardPoints[:m - k])
        # we want minmum of all windows examined
        minWindowSum = temp

        for i in range(1, m - k + 1):
            # add new val on end; subtract val from start
            temp = temp + cardPoints[i+m-k-1] - cardPoints[i-1]
            minWindowSum = min(minWindowSum, temp)

        # take away minimum sum of window found
        return sum(cardPoints) - minWindowSum
```

