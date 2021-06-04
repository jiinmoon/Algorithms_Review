# 84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

---

We can use stack here to "look-behind" as far out as possible so long as
previous bar's height is larger than current - so that it will form the largest
rectangle possible. This will be O(n) in time complexity.

---

Python:

```python

class Solution84:

    def largestRectangle(self, hist):

        maxArea = 0
        stk = []
        # 0 is added to compute very last bar
        hist += [0]

        for i, bar in enumerate(hist[1:], 1):
            while stk and hist[stk[-1]] > bar:
                height = hist[stk.pop()]
                width = i - stk[-1] - 1 if stk else i
                maxArea = max(maxArea, height * width)
            stk.append(i)

        return maxArea
```

