# 1423 Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated
number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the
row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score
you can obtain.

---

Let's think this problem inverted. The problem wants us to find the maximum
points obtainable by taking from either end of the given array of integers.
This means that we can take K cards from the beginning, or from the end, or any
combination. To find this and try out all combination is an exhaustive search.

Better method is inverted method - instead of finding max points obtainable, we
find the "minimum" of the points obtainable from the consecutive array that has
the size of length of array minus the given size K. Thus, we use sliding window
approach - at each step, we take out the front and append on end. Then, record
the minimum points thus far. The result would be the sum of the entire array
minus the minimum points found by exaiming all the consecutive cards.

---

Python:

```python

class Solution:
    def maxScore(self, cardPoints, k):
        size = len(cardPoints) - k
        currMin = sum(cardPoints[:size])
        minThusFar = currMin

        for i in range(1, len(cardPoints) - size +1):
            currMin += cardPoints[i + size - 1] - cardPoints[i-1] 
            minThusFar = min(currMin, minThusFar)

        return sum(cardPoints) - minThusFar
```
