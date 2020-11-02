# 239 Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size
k which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.

---

To find the maximum values within all the sliding windows, we simply try to
maintain the indicies of the maximum values in a queue. As we iterate on the
given integers array, we check against our queue where we maintain our indicies
of the maximum values - so long as the newly encountered value is greater than
the top of the queue, we can remove the values from the queue since it is
simply unnecessary (we are only interested in the maximum). Once we updated the
queue, then we need to check to see whether adding the current value has
exceeded the size K. This is done by examining the first (start of the sliding
window) element in the queue to see whether it is less than the currently added
element's index minus the size K. Then, if the current sliding window size has
reached the K, we may start to append the maximum (first element) to the
result.

---

Python:

```python

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k:
            return []

        result = list()
        q = deque()

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(num)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                result.append(num[q[0]])

        return result
```

