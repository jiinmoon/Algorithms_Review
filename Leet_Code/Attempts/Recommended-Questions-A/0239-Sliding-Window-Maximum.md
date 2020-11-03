# 239. Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size
k which is moving from the very left of the array to the very right. You can
only see the k numbers in the window. Each time the sliding window moves right
by one position.

Return the max sliding window.

---

We use deque data structure to maintain the maximum values for the current
sliding window. The sliding window is maintained by its indicies.

---

Python:

```python

class Solution:
    def maxSlidingWindow(self, nums, k):
        window = collections.deque()
        result = list()
        for i, num in enumerate(nums):
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            # adding new element exceeds the size
            if window[0] <= i - k:
                window.popleft()
            # once window reaches the correct size
            if i >= k - 1:
                result.append(window[0])
        return result
```

