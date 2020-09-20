239 Sliding Window Maximum
==========================

Given an array of integers, there is a sliding window of size k which is moving
from the left to right. You can only see the k numbers in the window, Each time
the sliding window moves by one position.

Return the max sliding window.

---

For efficiency, we use a deque to maintain our sliding window such that we can
easily add and remove new integers as we slide the window from left to right
- and deque will support operations at either end of the list in constant time.

As we enumerate on the array, new element and its index will be appended - but
before appending we can pop from the queue the previous indicies where it
points to the numbers less than new element since it is a waste of space. Then,
we update the front of the queue as well if the total length of our window
exceeds the given size k. And when we have enough elements, we can update our
result list where we maintain our current max window elements.

This should be O(n) in time complexity. Since we are only maintaining the size
upto K, space is bounded by O(k).

---

Python:

```python

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 1:
            return nums

        q = collections.deque()
        res = list()

        for i, num in enumerate(nums):
            # update q to remove previous elements that are less than current
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            # update front if exceeds size
            # front of the queue is the beginning of the sliding window
            if q[0] <= i - k:
                q.popleft()
            
            # if current window is of size, update res
            # since we have removed all previous elements that are smaller than
            # current, the max has to be the front
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
```
