# 670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

---

The naive approach would be to consider every possible swapped value which
there are n^3 of them.

Better approach would be either iterate from the beginning or end to find the
index of the maximum value that we have seen thus far that can be swapped with
the index of most significant digit. This would be O(n) in time complexity.

---

Python:

```python

class Solution:
    def maximumSwap(self, num):
        # convert into list of integer digits
        s = list(map(int, str(num)))
        
        # max swap value found thus far and its index from least significant digit
        maxSwapVal, swapIdx = float('-inf'), float('-inf')
        # swapTo = most significant digit whose value is less than maxSwapVal
        # swapFrom = swapIdx found previously
        swapTo, swapFrom = float('-inf'), float('-inf')

        for i in range(len(s)-1, -1, -1):
            currVal = s[i]
            # maxSwapVal has been found previously
            # and it is greater than current digit which is found later; able
            # to swap to create better value
            if maxSwapVal > currVal:
                swapTo, swapFrom = i, swapIdx
            # else, it is potentially maxSwapValue for down the road
            elif currVal > maxSwapVal:
                maxSwapVal, swapIdx = currVal, i

        # no maxSwapVal found; num is great as is
        if swapTo == float('-inf'):
            return num

        # else, perform swap and build the new result
        s[swapTo], s[swapFrom] = s[swapFrom], s[swapTo]
        result = 0
        for num in s:
            result = result * 10 + num
        return result
```


