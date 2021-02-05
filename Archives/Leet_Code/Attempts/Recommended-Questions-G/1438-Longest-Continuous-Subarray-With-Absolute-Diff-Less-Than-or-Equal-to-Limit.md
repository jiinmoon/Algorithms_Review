# 1468. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the
longest non-empty subarray such that the absolute difference between any two
elements of this subarray is less than or equal to limit.

---

To find the longest continuous subarray, we iterate on the given list. Mark the
start and end pointers to denote the current subarray. As we iterate on the
given list of integers, we update our queue of max elements and min elements
- this will allow for easier update of finding the absolute differences. This
  is done so by on max queue we pop from behind until new element is the
  maximum found in the max queue; and likewise for the min queue.

Once we found that the current absolute difference (computed by the abs
difference of the first two elements in our queue) is greater than the limit,
then we have a potential longest continuous subarray. We need to decrease our
size of the subarray from the beginning - so increase the start pointer while
updating our queues as well. Then, record the size of the longest continuous
subarry for current.

---

Python:

```python

from collections import deque

class Solution:
    def longestContinousSubarray(self, nums, lim):
        l, r, longest = 0, 0, 0
        maxQueue, minQueue = deque(), deque()

        while r < len(nums):
            rVal = nums[r]
            while maxQueue and maxQueue[-1] < rVal: maxQueue.pop()
            while minQueue and minQueue[-1] > rVal: minQueue.pop()
            maxQueue.append(rVal)
            minQueue.append(rVal)
            diff = maxQueue[0] - minQueue[0]
            if diff > lim:
                lVal = nums[l]
                if maxQueue[0] == lVal: maxQueue.popleft()
                if minQueue[0] == lVal: minQueue.popleft()
                l += 1
            longest = max(longest, r - l + 1)
            r += 1

        return longest
```
