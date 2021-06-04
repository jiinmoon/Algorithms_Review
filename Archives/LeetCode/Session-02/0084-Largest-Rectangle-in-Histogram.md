# 84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

---

One way to determine the largest area occupied by the heights in the given
histogram is that for each height, we look behind as far out as possible so
long as the heights can extend behind to determine the width. But we can reduce
the amount of work here as we can look behind so long as the heights of the
bars can only extend iff the heights are "greater" than the height of the
current bar being considered.

Hence, instead of extending from each position which costs us O(n^2) in time
complexity, we can reduce the time complexity to O(n) by utilizing stack to
push in the previous indicies of the bars. And for each new bar that we visit,
we compare against the top of the stack and pop so long as we can extend.
Compute the area for each bar that we visit and update the largest area when we
can.

---

Python:

```python

class Solution84:

    def largestRectangle(self, hist):

        maxArea = 0
        stack = []
        hist += [0]

        for i, currHeight in enumerate(hist):
            while stack and hist[stack[-1]] > currHeight:
                height = hist[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)
        
        return maxArea
```

