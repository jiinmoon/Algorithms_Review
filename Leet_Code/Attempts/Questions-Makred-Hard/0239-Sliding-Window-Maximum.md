# 239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size
k which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.

---

One approach to this problem is maintaining the sliding window of given size k,
and as we update this window, we can constantly iterate to find the maximum
each time. This is O(n^2) which is highly inefficient.

Improvement can be made if we do not maintain the entire sliding window - but
only consider maximum values that we are encountering thus far. Consider window
as a queue. In this queue, we update with each value encountered. But for each
value, we remove all the values that are less than current value to maintain
only the maximum values. Hence, at any given moment, the start of the queue
will only contain the current maximum for the window.

The window size is computed by checking the first value (starting index). If it
is greater than the size k, we remove it. And once we find that current window
size is of size k, we can safely add to our result.

This is O(n) in time complexity and space complexity.

---

Python:

```python

class Solution:
    def slidingWindowMaximum(self, nums):
        q = collections.deque()
        result = list()

        for i, num in enumerate(nums):
            # update to remove values less than current
            while q and nums[q[-1]] < num:
                q.pop()
            # add last val
            q.append(i)
            # remove first val if size violated
            if q[0] <= i - k:
                q.popleft()
            # add to result if current window size == k
            if i >= k - 1:
                result.append(q[0])

        return result
```
