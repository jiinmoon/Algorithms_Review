# 1438 Lognest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Maintain the subarray by it's maximum and minimums so that we can easily detect
when our subarray has exceeded the limit and adjust it. Use deque to support
O(1) operations on either end of the list.

---

Python:

```python

from collections import deque

class Solution:
    def longestSubarray(self, nums, lim):
        mx, mn = deque(), deque()
        l, r, longest = 0, 0, 0
        while r < len(nums):
            rval = nums[r]
            while mx and mx[-1] < rval: mx.pop()
            while mn and mn[-1] > rval: mn.pop()
            mx.append(rval)
            mn.append(rval)

            diff = mx[0] - mn[0]
            if diff > lim:
                lval = nums[l]
                if mx[0] == lval: mx.popleft()
                if mn[0] == lval: mn.popleft()
                l += 1
            r += 1
            longest = max(longest, r - l)

        return longest
```
