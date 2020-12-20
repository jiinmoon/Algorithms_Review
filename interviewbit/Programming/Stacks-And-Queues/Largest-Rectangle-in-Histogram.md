# Largest Rectangle in Histogram

    Given an array of integers A of size N. A represents a histogram i.e A[i]
    denotes height of the ith histogram’s bar. Width of each bar is 1.

---

## Approach:

Use stack to maintain the indicies of the heights visited. For each new height
encountered, we check against the stack; so long as previous indicies on top of
our stack and extend (or greater than current height), we can move back and
compute the area of the largest rectangle.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def largestRectangle(self, hist):

        hist.append(0)
        stack = [0]
        maxThusFar = 0

        for i, height in enumerate(hist):
            while stack and hist[stack[-1]] >= height:
                height = hist[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxThusFar = max(maxThusFar, height * width)
            stack.append(i)

        return maxThusFar

```
