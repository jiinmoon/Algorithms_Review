# Sliding Window Maximum

    Given an array of integers A. There is a sliding window of size B which
    is moving from the very left of the array to the very right.
    You can only see the w numbers in the window. Each time the sliding window
    moves rightwards by one position. You have to find the maximum for each window.

---

## Approach:

Use queue to maintain the current window of size B; for each new character, we
check against the last value of the queue and only maintain the maximum values
within the queue. If we find that queue size exceeds, we remove from the front.

O(n) in both time and space complexity.

---

Python:

```python

from collections import deque

class Solution:

    def slidingWindowMaximum(self, A, B):

        queue = deque()
        result = list()

        for i, num in enumerate(A):

            while queue and A[queue[-1]] < num:
                queue.pop()

            queue.append(i)

            if q[0] <= i - k:
                queue.popleft()

            if i >= k - 1:
                result.append(queue[0])

        return result
```
