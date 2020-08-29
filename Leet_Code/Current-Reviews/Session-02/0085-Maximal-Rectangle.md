85 Maximal Rectangle
====================

Given a 2D matrix filled with '0's and '1's, find the largest rectangle
containing only '1's and return its area.

---

The brute force approach would be to for every coord that we find '1', we start
to expand right and down to compute the max area.

Better approach utilizes a histogram - we maintain the culmulative sum of each
row one from next. Then, we have two options available to us:

(1) use stack as an indicator of where consecutive ones start and end such that
we can find the width of the current rectangle being considered.

(2) we maintain also the left and right consecutive ones indicator - each array
index indicates the furthest left and furthest right for the given column.

---

Python: combine with #84 approach.

```python
class Solution:
    def findLargestRectInHist(self, hist):
        if not hist:
            return 0
        hist = [0] + hist + [0]
        stk = [0]
        maxArea = 0
        for i, bar in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > bar:
                height = hist[stk.pop()]
                width = i - [stk[-1]] - 1
                maxArea = max(maxArea, height * width)
            stk.append(i)
        return maxArea
    
    def findMaximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        hist = [0 for _ in range(n)]
        totalArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    hist[j] += 1
                else:
                    hist[j] = 0
                totalArea = max(totalArea, findLargestRectInHist(hist))
        return totalArea
```

Python: maintaining left and right pointers to compute width at each col.

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # starts at leftmost col
        leftMost = [0 for _ in range(n)]
        # starts at rightmost col
        rightMost = [n for _ in range(n)]
        hist = [0 for _ in range(n)]
        maxAreaThusFar = 0

        for row in range(m):
            l, r = 0, n
            # update histogram from prev row
            hist = [hist[col]+1 if matrix[row][col] == '1' else 0 for col in range(n)]
            # iterate from left to right - update each with leftmost consecutive 1s
            for col in range(n):
                if matrix[row][col] == '1':
                    leftMost[col] = max(l, leftMost[col]) 
                else:
                    # consecutive 1s is broken
                    leftMost[col] = 0
                    l = col + 1
            # interate from right to left
            for col in range(n-1, -1, -1):
                if matrix[row][col] == '1':
                    rightMost[col] = min(r, rightMost[col])
                else:
                    rightMost[col] = n
                    r = col
            # compute area
            for col in range(n):
                maxAreaThusFar = max(
                    maxAreaThusFar,
                    hist[col] * (rightMost[col] - leftMost[col])
                )
        return maxAreaThusFar
```
