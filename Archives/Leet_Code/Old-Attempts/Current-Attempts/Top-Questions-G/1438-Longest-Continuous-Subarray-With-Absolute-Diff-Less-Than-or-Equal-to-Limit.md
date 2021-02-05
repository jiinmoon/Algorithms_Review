# 1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the
longest non-empty subarray such that the absolute difference between any two
elements of this subarray is less than or equal to limit.

---

To find the longest continuous subarray, we maintain the index of this subarray
that we are exaimining. But since we want to find the abs difference between
max and min, we should maintain them separately in order to avoid having to
search for this values every time new element is examined and subarray is
updated. To support this fast update, we can use doubly-linked list for
updating not only the first and last element.

---

Python:

```python

from collections import deque

class Solution:
    def longestSubarray(self, nums, lim):
        maxQ, minQ = deque(), deque()
        l, r, longest = 0, 0, 0

        while r < len(nums):
            rval = nums[r]
            while maxQ and maxQ[-1] < rval: maxQ.pop()
            while minQ and minQ[-1] > rval: minQ.pop()
            maxQ.append(rval)
            minQ.append(rval)

            absDiff = maxQ[0] - minQ[0]
            if absDiff > lim:
                lval = nums[l]
                if maxQ[0] == lval:
                    maxQ.popleft()
                if minQ[0] == lval:
                    minQ.popleft()
                l += 1

            r += 1
            longest = max(longest, r - l)
        return longest
```

