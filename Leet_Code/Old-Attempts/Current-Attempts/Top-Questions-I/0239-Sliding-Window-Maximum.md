# 239 Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size
k which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.

---

We approach this problem by maintainging the index of current maximum values in 
the queue. So, as we iterate on the given array of integers, we consider each
index as the end poing of our sliding window. To do so, we first check our top
of queue to maintain maximum value of current sliding window. If we find that
our starting point in the queue is less than the size, we update the queue by
removing the first starting element.

---

Python:

```python

class Solution:
    def maxSlidingWindow(self, nums):
        q = collections.deque()
        res = list()

        for i, num in enumerate(nums):
            # update queue to only include maximum values upto current index
            while q and nums[q[-1]] < num:
                q.pop()
            # include the last value of the sliding window
            q.append(i)
            # update size of the window; remove first
            if q[0] <= i - k:
                q.popleft()
            # add to result if size is reached
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
```

