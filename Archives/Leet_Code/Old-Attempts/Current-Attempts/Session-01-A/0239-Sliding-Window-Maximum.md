# 239 Sliding Window Maximum

Maintain the sliding window in a queue. As we iterate on the given integers, we
remove from the queue so long as queue's values are less than new value
encountered since they cannot be the maximum once new element is added. Once
added, if the length of current sliding window exceeds the size k, then we
remove the first front element. So long as the sliding window size is met, we
can add to our result.

---

Python:

```python

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = list()

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
```
